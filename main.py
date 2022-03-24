from getopt import getopt
import multiprocessing
# import multiprocessing
# from logger import logging
from os import pipe
from Subsea_QT_GUI import GUI_loop
from multiprocessing import Pipe, Process, Queue
from Subsea_QT_GUI import *
from Threadwatch import Threadwatcher
from network_handler import Network
import controller
import threading
import random
import time
import json
import sys


# takes a python object and prepares it for sending over network
def network_format(data) -> bytes:
    """Formats the data for sending to network handler"""
    packet_seperator = json.dumps("*")
    return bytes(packet_seperator+json.dumps(data)+packet_seperator, "utf-8")


# is probably replaced by "send_data_to_rov" #############################
def relay_data_from_controller(connection_controller, t_watch: Threadwatcher, id, relay=True):
    while t_watch.should_run(id):
        controller_data = connection_controller.recv()
        print("taking controller data")
        # print(str(controller_data)[1:-1], end="                                                      \r")
        # print(controller_data["joysticks"])

        sys.stdout.write(f"{controller_data}"+"         \r")
        sys.stdout.flush()
        if relay:
            # print(controllerdata_to_json(controller_data), end="            \r")
            # print(controllerdata_to_json(controller_data))
            pass


def recieve_commands_from_gui(conn, t_watch: Threadwatcher, id):
    #Probably deprecated
    while t_watch.should_run(id):
        print(conn.recv())
    print("t_watch is false")


def create_test_sensordata(delta, old_sensordata=None):
    # test function
    sensordata = {}
    if old_sensordata is None:
        sensordata = {"tid": int(time.time()-start_time_sec), "dybde": -2500.0, "spenning": 48.0, "temp_rov": 26.0}
    else:
        sensordata["tid"] = int(time.time()-start_time_sec)
        sensordata["dybde"] = old_sensordata["dybde"] + 10*delta
        sensordata["spenning"] = old_sensordata["spenning"] + 0.4*delta
        sensordata["temp_rov"] = old_sensordata["temp_rov"] + 0.3*delta
    return sensordata



MANIPULATOR_IN_OUT = 1
MANIPULATOR_ROTATE = 0
BUTTON_GRAB = 4
BUTTON_RELEASE = 5

class Rov_state:
    def __init__(self, queue, network_handler, gui_pipe) -> None:
        self.data:dict = {}
        # prevents the camera from toggling back again immediately if we hold the button down
        self.camera_toggle_wait_counter: int = 0
        # prevents the tilt toggle from toggling back again immediately if we hold the button down
        self.right_joystick_toggle_wait_counter: int = 0
        # prevents the manipulator toggle from toggling back again immediately if we hold the button down
        self.manipulator_toggle_wait_counter: int = 0
        # prevents the image processing toggle from toggling back again immediately if we hold the button down
        self.image_processing_mode_wait_counter: int = 0
        # Tilt in degrees of the camera servo motors
        self.camera_tilt: list[float] = [0.0, 0.0]
        # turn of the ability to change camera tilt, when camera processing is happening on the camera
        self.camera_tilt_allowed = [True, True]  #[cam 0, cam 1]
        # Toggles between controlling rotation or camera tilt on rigth joystick
        self.camera_tilt_control_active = True
        # queue for getting commands from gui and controller
        self.queue: multiprocessing.Queue = queue
        #Pipe to send sensordata back to the gui
        self.gui_pipe = gui_pipe
        # Network handler that sends data to rov (and recieves)
        self.network_handler:Network = network_handler
        # self.cam_is_enabled = [True, True]
        # list of functions that can be triggered by buttons. # need a function to tell it to grip and release and not do it by button like we do in build manipulator byte
        # theese functions need to line up their indexes with the line in button_config.txt
        self.button_function_list = [self.skip, self.toggle_active_camera, self.toggle_between_rotation_and_camera_tilt, self.toggle_manipulator_enabled, self.manipulator_grip, self.manipulator_release, self.update_bildebehandlingsmodus, self.skip]
        #maps a button to a index in button_function_list Can be changed from gui
        self.button_to_function_map = [0, 6, 0, 1, 4, 5, 0, 0, 3, 2]
        self.camera_is_on = [True, True]
        self.camera_command: list[list[int, dict]] = None
        self.joystick_moves_camera = False
        self.image_processing_mode:list[int, int] = [0, 0]
        # determines which camera is controlled
        self.active_camera = 0
        self.packets_to_send = []

        self.manipulator_active = True

        self.light_intensity_forward = 100
        self.ligth_forward_is_on = True

        self.light_intensity_down = 100
        self.ligth_down_is_on = True


    def skip(self):
        pass
        # print("pass was called")

    # bit hacky since we overwrite the actual value of the button
    def manipulator_grip(self):
        self.data["buttons"][BUTTON_GRAB] = 1
        print("grip")


    # bit hacky since we overwrite the actual value of the button
    def manipulator_release(self):
        self.data["buttons"][BUTTON_RELEASE] = 1
        print("release")


    def toggle_manipulator_enabled(self):
        # print("")
        if self.manipulator_toggle_wait_counter == 0:    
            self.manipulator_active = not self.manipulator_active
            print(f"{self.manipulator_active = }")
            self.manipulator_toggle_wait_counter = 7
    

    def toggle_camera_on_or_off(self, id=None):
        if id is None:
            id = self.active_camera
        print(f"toggle camera was called")
        self.camera_is_on[id] = not self.camera_is_on[id]
        self.packets_to_send.append([200+id, {"on": self.camera_is_on}])


    # updates variables that needs to be done each tick
    def tick(self):
        self.camera_command = None

        if self.camera_toggle_wait_counter > 0:
            self.camera_toggle_wait_counter -= 1

        if self.right_joystick_toggle_wait_counter > 0:
            self.right_joystick_toggle_wait_counter -= 1

        if self.manipulator_toggle_wait_counter > 0:
            self.manipulator_toggle_wait_counter -= 1
            
        if self.image_processing_mode_wait_counter > 0:
            self.image_processing_mode_wait_counter -= 1



    #checks which buttons were pressed and calls the appropiate function
    def check_controls(self):
        self.button_handling()
        self.update_camera_tilt()
        self.build_styredata()


    def button_handling(self):
        buttons = self.data.get("buttons")
        if buttons is None:
            return
        for index, button in enumerate(buttons):
            if button: # is pressed
                self.button_function_list[self.button_to_function_map[index]]()
                # print(f"button with {index = } is pressed")

    
    def toggle_active_camera(self):
        """Toggles which camera should get the commands from the controller"""
        if self.camera_toggle_wait_counter == 0:
            self.active_camera = (self.active_camera+1)%2  # Changes camera id betwen 0 and 1
            print(f"Changed active camera to {self.active_camera}")
            self.camera_toggle_wait_counter = 6


    def get_from_queue(self):
        """Takes data from the queue and sends it to the correct handler"""
        id, packet = self.queue.get()
        if id == 1: # controller data update
            self.data = packet
        elif id == GUI_loop.PROFILE_UPDATE_ID:
            # print("Updated profile")
            print(id, packet)
            self.button_to_function_map = packet
        elif id == GUI_loop.COMMAND_TO_ROV_ID:
            commands = {"update_light_value": self.update_light_value}
            print("got command")
            print(id, packet)
            if packet.split(":")[0] not in commands:
                print(f"Got unrecognized command from gui {packet}")
                return
            commands[packet[0]]()


    def send_packets(self):
        """Sends the created network packets and clears it"""
        if self.network_handler is None:
            # print(self.packets_to_send)
            # print(self.data["buttons"])
            self.packets_to_send = []
            return
        print(self.packets_to_send)
        self.network_handler.send(network_format(self.packets_to_send))
        self.packets_to_send = []

    def toggle_between_rotation_and_camera_tilt(self):
        if self.right_joystick_toggle_wait_counter == 0:
            self.camera_tilt_control_active = not self.camera_tilt_control_active
            print(f"{self.camera_tilt_control_active = }")
            self.right_joystick_toggle_wait_counter = 7

    def update_light_value(self):
        self.light_intensity_forward = 100
        self.ligth_forward_is_on = True
        
        self.light_intensity_down = 100
        self.ligth_down_is_on = True

        ligth_down = self.light_intensity_down * self.ligth_down_is_on
        ligth_forward = self.light_intensity_forward * self.ligth_forward_is_on
        self.packets_to_send.append([142, ligth_forward, ligth_down])

    def update_camera_tilt(self):
        # print("camera tilt update func")
        if self.camera_tilt_control_active and self.camera_tilt_allowed[self.active_camera]:
            camera_movement = self.data.get('camera_movement')
            if camera_movement is None:
                return
            if abs(camera_movement) > 0:
                old_tilt = self.camera_tilt[self.active_camera]
                # print(f"{self.data.get('camera_movement')}")
                tilt_time_sec = 2  # time in seconds for the camera to move from one side to the other
                total_degrees = 80
                tilt_per_ms = total_degrees/(tilt_time_sec*1000)
                self.camera_tilt[self.active_camera] += (camera_movement/100)*self.data["time_between_updates"]*tilt_per_ms
                if self.camera_tilt[self.active_camera] > total_degrees/2:
                    self.camera_tilt[self.active_camera] = total_degrees/2

                elif self.camera_tilt[self.active_camera] < -total_degrees/2:
                    self.camera_tilt[self.active_camera] = -total_degrees/2

                self.camera_tilt[self.active_camera] = round(self.camera_tilt[self.active_camera])

                if old_tilt != self.camera_tilt[self.active_camera]:
                    self.packets_to_send.append([200 + self.active_camera, {"tilt": self.camera_tilt[self.active_camera]}])

    def build_styredata(self):
        #  X,Y,Z, rotasjon, m.teleskop, m.vri, m.klype + uint8 throttle  ##########
        styredata = []
        styredata.append(self.data["joysticks"][X_axis])
        styredata.append(self.data["joysticks"][Y_axis])
        styredata.append(self.data["joysticks"][Z_axis])
        if not self.camera_tilt_control_active:
            styredata.append(self.data["joysticks"][ROTATION_axis])
        else:
            styredata.append(0)
        styredata.append(self.build_manipulator_byte())
        styredata.append(0)
        styredata.append(0)
        styredata.append(0)
        self.packets_to_send.append([70, styredata])


    def build_manipulator_byte(self):
        data = list(self.data["dpad"])
        data.append(self.data["buttons"][BUTTON_GRAB])
        data.append(self.data["buttons"][BUTTON_RELEASE])
        # print(f"{data = }")
        # Inn: 1, Ut: 2, roter med klokka: 4, roter mot klokka: 8, lukk klo: 16,
        # åpne klo: 32, enable: 64, ingen funksjon
        data_to_values = [{-1: 0b0000_1000, 0: 0b0, 1: 0b0000_0100},
                        {-1: 0b0000_0001, 0: 0b0, 1: 0b0000_0010},
                        {1: 0b0001_0000, 0: 0b0},
                        {1: 0b0010_0000, 0: 0b0}]

        data_to_values = [{-1: 0b0000_1000, 0: 0b0, 1: 0b0000_0100},
                {-1: 1, 0: 0b0, 1: 2},
                {1: 16, 0: 0},
                {1: 32, 0: 0}]

        byte_val = 0
        for index, axis_val in enumerate(data):  # bitwise or's all the values
            byte_val = byte_val | data_to_values[index][axis_val]
        if self.manipulator_active:
            byte_val = byte_val | 64  # enables manipulator

        return byte_val

    def send_sensordata_to_gui(self, data):
        print(f"sending data from main to gui: {data =}")
        self.gui_pipe.send(data)

    def  update_bildebehandlingsmodus(self, camera_id: int = None, mode: int = None):
        camera_modes = [0,1,5,6]
        if self.image_processing_mode_wait_counter == 0:
            if camera_id is None and mode is None:
                camera_id = self.active_camera
                self.image_processing_mode[camera_id] = (self.image_processing_mode[camera_id]+1)%3
            self.packets_to_send.append([200+camera_id, {"bildebehandlingsmodus": camera_modes[self.image_processing_mode[camera_id]]}])
            # print([200+camera_id, {"bildebehandlingsmodus": camera_modes[self.image_processing_mode[camera_id]]}])
            if self.image_processing_mode[camera_id] == 0 or self.image_processing_mode[camera_id] == 1:
                self.camera_tilt_allowed[camera_id] = True
            else:
                self.camera_tilt_allowed[camera_id] = False
            # print(f"{self.image_processing_mode = }")
            self.image_processing_mode_wait_counter = 7


def run(network_handler: Network, t_watch: Threadwatcher, id: int, queue_for_rov: multiprocessing.Queue, gui_pipe):
    print(f"{network_handler = }")
    rov_state = Rov_state(queue_for_rov, network_handler, gui_pipe)
    camera_tilt_lock = [False, False]  # locks the camera tilt if the rov is processing images
    while t_watch.should_run(id):

        rov_state.tick()

        rov_state.get_from_queue()
        if rov_state.data == {}:
            continue
        rov_state.check_controls()
        print(rov_state.packets_to_send)
        rov_state.send_packets()

ID = 0

X_axis = 1
Y_axis = 0
Z_axis = 6
ROTATION_axis = 2

Left_Button = 4
Right_Button = 5


def check_camera_command(camera_command):
    """Checks if the we are turning on image proccesing and locks the camera
    if needed"""
    lock = [False, False]
    for command in camera_command:
        if "bildebehandlingsmodus" in command[1]:
            if command[1]["bildebehandlingsmodus"] != 0:
                lock[command[0]-200] = True
    # return lock
    return lock


# Handles the update of tilting of the camera motor
def update_camera_tilt(camera_to_update: int, move_speed: int, time_delta: int, camera_tilt: list[float], tilt_lock: list[bool]):
    if move_speed == 0:  # no change
        return camera_tilt, -1  # -1 means no camera has changed

    tilt_time_sec = 2  # time in seconds for the camera to move from one side to the other
    # tilt_time_sec = 2 # time in seconds for the camera to move from one side to the other
    total_degrees = 80
    tilt_per_ms = total_degrees/(tilt_time_sec*1000)

    camera_tilt[camera_to_update] += (move_speed/100) * time_delta * tilt_per_ms
    if camera_tilt[camera_to_update] > total_degrees/2:
        camera_tilt[camera_to_update] = total_degrees/2
        return camera_tilt, -1  # -1 means no camera has changed

    elif camera_tilt[camera_to_update] < -total_degrees/2:
        camera_tilt[camera_to_update] = -total_degrees/2
        return camera_tilt, -1  # -1 means no camera has changed

    camera_tilt[camera_to_update] = round(camera_tilt[camera_to_update])

    return camera_tilt, camera_to_update





# Decodes the tcp packet/s recieved from the rov
def decode_packets(tcp_data: bytes) -> list:
    try:
        json_strings = bytes.decode(tcp_data, "utf-8")
        json_list = json_strings.split(json.dumps("*"))
    except Exception as e:
        print(f"{tcp_data = } Got error {e}")
        return []
    decoded_items = []

    for item in json_list:

        if item == '' or item == json.dumps("heartbeat"):
            # print(f"{item = }")
            continue

        else:
            # print(f"{item = }")
            item = json.loads(item)
            decoded_items.append(item)
    return decoded_items


def recieve_data_from_rov(network: Network, t_watch: Threadwatcher, id: int):
    while t_watch.should_run(id):
        try:
            data = network.receive()
            if data is None:
                continue
            # print(f"recieve data from from {data = }")
            decoded = decode_packets(data)
            if decoded == []:
                continue
            # if len(decoded)>0:
                # print(decoded)
            # print(decoded)
        except json.JSONDecodeError as e:
            print(f"{data = }, {e = }")


def get_args():
    pass
    print(getopt(sys.argv, "n:g:c:", "network=gui=controller="))




if __name__ == "__main__":
    # print(check_camera_command([[201, {"on": True, "bildebehandlingsmodus": 1}], [70, [0, 0, 0, 0, 0, 0, 0, 0]]]))
    # exit(0)
    try:

        global start_time_sec
        global run_gui
        start_time_sec = time.time()
        run_gui = True
        run_get_controllerdata = True
        run_network = True
        run_send_fake_sensordata = False
        
        queue_for_rov = multiprocessing.Queue()

        t_watch = Threadwatcher()

        gui_parent_pipe, gui_child_pipe = Pipe() # starts the gui program. gui_parent_pipe should get the sensor data
        if run_gui:
            id = t_watch.add_thread()
            gui_loop = Process(target=GUI_loop.run, args=(gui_child_pipe, queue_for_rov, t_watch, id)) # and should recieve commands from the gui
            gui_loop.start()

            id = t_watch.add_thread()
            recv_from_gui = threading.Thread(target=recieve_commands_from_gui, args=(gui_child_pipe, t_watch, id),daemon=True)
            recv_from_gui.start()

        if run_send_fake_sensordata:
            while True:
                sensordata = {"lekk_temp": [0, 21.2, 27.0, 99.0]}
                gui_parent_pipe.send(sensordata)
                time.sleep(2)


        if run_get_controllerdata:
            id = t_watch.add_thread()
            # takes in controller data and sends it into child_conn
            controller_process = Process(target=controller.run, args=(queue_for_rov, t_watch, id,True, False,), daemon=True)
            controller_process.start()

        # Network is blocking
        if run_network:
            network = Network(is_server=False, port=6900, connect_addr="10.0.0.2")
            print("network started")

            id = t_watch.add_thread()
            snd_data_to_rov = threading.Thread(target=run, args=(network, t_watch, id, queue_for_rov, gui_parent_pipe), daemon=True)
            # snd_data_to_rov = threading.Thread(target=send_data_to_rov, args=(None, t_watch, id, parent_conn_controller), daemon=True)
            snd_data_to_rov.start()

            recieve_data_from_rov = threading.Thread(target=recieve_data_from_rov, args=(network, t_watch, id), daemon=True)
            recieve_data_from_rov.start()

        elif run_get_controllerdata:
            print("starting send to rov")
            snd_data_to_rov = threading.Thread(target=run, args=(None, t_watch, id, queue_for_rov, gui_parent_pipe), daemon=True)
            snd_data_to_rov.start()

            while True:
                time.sleep(1)
    except KeyboardInterrupt:
        t_watch.stop_all_threads()
        print("stopped all threads")