from concurrent.futures import thread
from getopt import getopt
import multiprocessing
# import multiprocessing
from logger import Logger
from os import pipe
from Subsea_QT_GUI import GUI_loop
from multiprocessing import Pipe, Process, Queue
from Subsea_QT_GUI import *
from Threadwatch import Threadwatcher
from network_handler import Network
import Controller_handler as controller
import threading
import random
import time
import json
import sys
import os


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
        if conn.poll():
            print(f" Inside recieve_commands_from_gui {conn.recv() = }")
        # print("recieve commands from gui")
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
BUTTON_RELEASE = 4
BUTTON_GRAB = 5

class Rov_state:
    def __init__(self, queue, network_handler, gui_pipe, t_watch: Threadwatcher) -> None:
        self.t_watch: Threadwatcher = t_watch
        self.logger = Logger()
        self.data:dict = {}
        self.virtual_buttons: list[int] = []
        self.position = [0, 0, 0]
        # prevents the camera from toggling back again immediately if we hold the button down
        self.camera_toggle_wait_counter: int = 0
        # prevents the tilt toggle from toggling back again immediately if we hold the button down
        self.right_joystick_toggle_wait_counter: int = 0
        # prevents the manipulator toggle from toggling back again immediately if we hold the button down
        self.manipulator_toggle_wait_counter: int = 0
        # prevents the image processing toggle from toggling back again immediately if we hold the button down
        self.image_processing_mode_wait_counter: int = 0
        # Tilt in degrees of the camera servo motors
        self.camera_tilt: list[float] = [0, 0]
        # turn of the ability to change camera tilt, when camera processing is happening on the camera
        self.camera_tilt_allowed = [True, True]  #[cam 0, cam 1]
        # Toggles between controlling rotation or camera tilt on rigth joystick
        self.camera_tilt_control_active = False
        # queue for getting commands from gui and controller
        self.queue: multiprocessing.Queue = queue
        #Pipe to send sensordata back to the gui
        self.gui_pipe = gui_pipe
        # Network handler that sends data to rov (and recieves)
        self.network_handler:Network = network_handler
        # self.cam_is_enabled = [True, True]
        # list of functions that can be triggered by buttons. # need a function to tell it to grip and release and not do it by button like we do in build manipulator byte
        # theese functions need to line up their indexes with the line in button_config.txt
        self.button_function_list = [self.skip, self.toggle_active_camera, self.toggle_between_rotation_and_camera_tilt, self.toggle_manipulator_enabled, self.manipulator_release, self.manipulator_grip, self.update_bildebehandlingsmodus_controller, self.skip]
        #maps a button to a index in button_function_list Can be changed from gui
        self.button_to_function_map = [0, 6, 0, 1, 4, 5, 0, 0, 3, 2]
        self.camera_is_on = [True, True]
        self.camera_command: list[list[int, dict]] = None
        self.joystick_moves_camera = False
        self.image_processing_mode:list[int, int] = [0, 0]
        self.camera_modes = [0,1,2,3,4,5]
        # determines which camera is controlled
        self.active_camera = 0
        self.packets_to_send = []
        self.start_time = time.time() 

        self.valid_gui_commands = ["lekk_temp", "thrust", "accel", "gyro", "time", "manipulator", "power_consumption", "manipulator_toggled"]

        self.manipulator_active = True
        self.regulator_active: list[bool] = [True, True, True]
        self.video_recording_active = [False, False]
        self.light_intensity_forward = 100
        self.ligth_forward_is_on = True
        self.regulering_state = {"rull": True, "stamp": True, "hiv": True}
        self.thruster_struping = 0

        self.light_intensity_down = 100
        self.ligth_down_is_on = True

        self.send_startup_commands()

    def send_startup_commands(self):
        self.packets_to_send.append([200, {"tilt": self.camera_tilt[0]}])
        self.packets_to_send.append([201, {"tilt": self.camera_tilt[1]}])
        self.packets_to_send.append([64,  []])
        self.packets_to_send.append([96,  []])
        self.packets_to_send.append([71,  [11, 0.7]])

        # self.packets_to_send.append([128, []])
        
        self.set_depth_zeroing()


    def skip(self, button_index):
        pass
        # print("pass was called")

    # bit hacky since we overwrite the actual value of the button
    # Need to clear the button that sets this value so that the original function does not altso trigger
    def manipulator_grip(self, button_index):
        self.data["buttons"][BUTTON_GRAB] = 1

    # bit hacky since we overwrite the actual value of the button
    def manipulator_release(self, button_index):
        self.data["buttons"][BUTTON_RELEASE] = 1


    def toggle_manipulator_enabled(self, button_index = None, state = None):
        
        if state is not None and button_index is None:
            # print(f"{state=}, {button_index=}")
            self.manipulator_active = state
            # print(f"{self.manipulator_active = }")
            return

        if self.manipulator_toggle_wait_counter == 0:    
            self.manipulator_active = not self.manipulator_active
            print(f"{self.manipulator_active = }")
            self.manipulator_toggle_wait_counter = 7

        self.send_sensordata_to_gui({"manipulator_toggled": [self.manipulator_active]})
    

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
                self.button_function_list[self.button_to_function_map[index]](index)
                # print(f"button with {index = } is pressed")

    
    def toggle_active_camera(self, button_index):
        """Toggles which camera should get the commands from the controller"""
        if self.camera_toggle_wait_counter == 0:
            self.active_camera = (self.active_camera+1)%2  # Changes camera id betwen 0 and 1
            print(f"Changed active camera to {self.active_camera}")
            self.camera_toggle_wait_counter = 6

    def reset_fuse_on_power_supply(self, fuse_number):
        """reset_fuse_on_power_supply creates and adds
        packets for reseting a fuse on the ROV"""
        fuse_reset_signal = [False]*3
        fuse_reset_signal[fuse_number] = True
        
        for item in self.regulator_active :
            fuse_reset_signal.append(item)

        self.packets_to_send.append([139, fuse_reset_signal])

    def switch_power_supply_regulator(self, regulator_number: int, switch_on: bool):
        """switch_power_supply_regulator creates and adds packets
        for switching the regulator on the rov of or on depending
        on the state of the switch_on variable"""
        fuse_reset_signal = [False]*3
        self.regulator_active[regulator_number] = switch_on        
        for item in self.regulator_active:
            fuse_reset_signal.append(item)

        self.packets_to_send.append([139, fuse_reset_signal])

    def get_from_queue(self):
        """Takes data from the queue and sends it to the correct handler"""
        id, packet = self.queue.get()
        if id == 1: # controller data update
            self.data = packet
        elif id == GUI_loop.PROFILE_UPDATE_ID:
            # print("Updated profile")
            # print(id, packet)
            self.button_to_function_map = packet
        elif id == GUI_loop.COMMAND_TO_ROV_ID:
            commands = {"update_light_value": self.update_light_value,"reset_depth": self.set_depth_zeroing,
            "update_bildebehandling": self.update_bildebehandlingsmodus, "take_pic": self.take_pic,
            "manipulator_toggle": self.toggle_manipulator_enabled, "reset_sikring": self.reset_fuse_on_power_supply,
            "toggle_regulator": self.switch_power_supply_regulator, "thruster_struping": self.set_thruster_struping,
            "STOP": self.shutdown, "video_toggle": self.video_toggle,
            "regulering": self.toggle_regulering}

            if packet[0] not in commands:
                print(f"Got unrecognized command from gui {packet}")
                return
            commands[packet[0]](*packet[1:]) # * unpacks list
            

    def toggle_regulering(self, sensordata):
        sensordata.append(1)
        self.packets_to_send.append([71, sensordata])

    def video_toggle(self, data):
        # print(f"{data=}")
        self.packets_to_send.append([200+data[1], {"video_recording": data[0]}])
    
    def shutdown(self):
        print("recieved shutdown from gui")
        self.t_watch.stop_all_threads()
        exit(0)

    def set_thruster_struping(self, sensordata):
        self.thruster_struping = sensordata

    def set_depth_zeroing(self, sensordata=None):
        self.packets_to_send.append([129, []])
        # self.packets_to_send.append([96,  []])


    def get_rotation_input(self):
        # rotate_input = input("Rotate theta degrees around x,y,z axis")
        # rotation = [int(item.strip()) for item in rotate_input.split(",")]
        # if len(rotation) != 4:
        #     rotation = [0]*4
        # sensordata = {"rotate": [rotation[0], rotation[1], rotation[2], rotation[3]]}

        rotate_input = input()
        try:
            rotation = [float(item.strip()) for item in rotate_input.split(",")]
        except Exception:
            print("wrong input")
            return
        if len(rotation) != 2:
            rotation = [0, 0]
        sensordata = {"gyro": [rotation[0], rotation[1], 0]}

        # self.send_sensordata_to_gui(sensordata)




    def craft_packet(self, t_watch: Threadwatcher, id):
        while t_watch.should_run(id):
            userinput = input("Packet: [parameter_id of type int, value of type float or int]: ")
            var = []
            try:
                var = json.loads(userinput)
                if not isinstance(var[0], int):
                    print("Error: parameter id was not an int! try again.")
                    continue
                # if not isinstance(var[1], int) or not isinstance(var[1], float):
                #     print("Error: parameter id was not an int or float! try again.")
                #     continue
                if len(var) != 2:
                    print("Error: list was not length 2")
                    continue
            except Exception as e:
                print(f"Error when parsing input\n {e}")
                continue

            self.packets_to_send.append([71, var])

    def send_packets(self):
        """Sends the created network packets and clears it"""

        for packet in self.packets_to_send:
            if packet[0] != 70:
                pass
                print(f"{packet = }")
        self.logger.sensor_logger.info(self.packets_to_send)
        if self.network_handler is None:
            self.packets_to_send = []
            return
        self.network_handler.send(network_format(self.packets_to_send))
        self.packets_to_send = []
        

    def toggle_between_rotation_and_camera_tilt(self, button_index):
        if self.right_joystick_toggle_wait_counter == 0:
            self.camera_tilt_control_active = not self.camera_tilt_control_active
            print(f"{self.camera_tilt_control_active = }")
            self.right_joystick_toggle_wait_counter = 7

    def update_light_value(self, light_intensity_forward: int, ligth_forward_is_on: bool, light_intensity_down: int, ligth_down_is_on: bool):
        self.light_intensity_forward = light_intensity_forward
        self.ligth_forward_is_on = ligth_forward_is_on
        
        self.light_intensity_down = light_intensity_down
        self.ligth_down_is_on = ligth_down_is_on

        ligth_down = self.light_intensity_down * self.ligth_down_is_on
        ligth_forward = self.light_intensity_forward * self.ligth_forward_is_on
        # print(f"Lys oppdatert. verdien vi sender er {[142, ligth_forward, ligth_down]}")
        self.packets_to_send.append([142, [ligth_forward, ligth_down]])

    def update_camera_tilt(self):
        # print("camera tilt update func")
        if self.camera_tilt_control_active and self.camera_tilt_allowed[self.active_camera]:
            camera_movement = self.data.get('camera_movement')
            if camera_movement is None:
                return
            if abs(camera_movement) > 0:
                old_tilt = self.camera_tilt[self.active_camera]
                tilt_time_sec = 2  # time in seconds for the camera to move from one side to the other
                total_degrees = 80
                tilt_per_ms = total_degrees/(tilt_time_sec*1000)
                self.camera_tilt[self.active_camera] += (camera_movement/100)*self.data["time_between_updates"]*tilt_per_ms
                if self.camera_tilt[self.active_camera] > total_degrees/2:
                    self.camera_tilt[self.active_camera] = total_degrees//2

                elif self.camera_tilt[self.active_camera] < -total_degrees/2:
                    self.camera_tilt[self.active_camera] = -total_degrees//2

                self.camera_tilt[self.active_camera] = round(self.camera_tilt[self.active_camera])

                if old_tilt != self.camera_tilt[self.active_camera]:
                    self.packets_to_send.append([200 + self.active_camera, {"tilt": int(self.camera_tilt[self.active_camera])}])
                    # [[200/201, {"video_recording": True, "take_pic": True}]]

    def build_styredata(self):
        #  X, Y, Z, rotasjon, (m.teleskop, m.vri, m.klype, enable), fri, regulering_av_på,  throttle  ##########
        if self.data == {}:
            return
        styredata = []
        styredata.append(self.data["joysticks"][X_axis])
        styredata.append(self.data["joysticks"][Y_axis])
        styredata.append(-self.data["joysticks"][Z_axis]) # positive direction is downwards
        if not self.camera_tilt_control_active:
            styredata.append(self.data["joysticks"][ROTATION_axis])
        else:
            styredata.append(0)
        styredata.append(self.build_manipulator_byte())
        styredata.append(0)
        styredata.append(0)
        styredata.append(self.thruster_struping)
        self.packets_to_send.append([70, styredata])

    def build_regulering_byte(self):
        values = list(self.regulering_state.values())
        sum = 0
        for i in range(3):
            # Multiplies the each bit with the bolean value controlling the regulator
            sum += 2**i*list(self.regulering_state.values())[i]
        return sum

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
        # print(f"sending data from main to gui: {data =}")
        self.gui_pipe.send(data)

    def toggle_video_recording(self, camera_id):
        """toggle_video_recording turns of video recording on the rov and changes the state topside"""
        self.video_recording_active[camera_id] = not self.video_recording_active[camera_id]
        self.packets_to_send.append([200+camera_id, {"video_recording": self.video_recording_active[camera_id]}])

    def take_pic(self, camera_id):
        """sends a command to the rov to take a picture. Which camera the picture is taken on depends on the id"""
        self.packets_to_send.append([200+camera_id, {"take_pic": True}])

    def update_bildebehandlingsmodus(self, camera_id: int, mode: int):
        # print(f"{camera_id=}, {mode=}")
        self.image_processing_mode[camera_id] = self.camera_modes.index(mode)
        self.packets_to_send.append([200+camera_id, {"bildebehandlingsmodus": mode}])
        if self.image_processing_mode[camera_id] == 0 or self.image_processing_mode[camera_id] == 1:
            self.camera_tilt_allowed[camera_id] = True
        else:
            self.camera_tilt_allowed[camera_id] = False
        print(f"{self.image_processing_mode = }")


    def update_bildebehandlingsmodus_controller(self, button_index, camera_id: int = None, mode: int = None):
        if self.image_processing_mode_wait_counter == 0:
            if camera_id is None:
                camera_id = self.active_camera
            if mode is None:
                self.image_processing_mode[camera_id] = (self.image_processing_mode[camera_id]+1)%len(self.camera_modes)
            else:
                self.image_processing_mode[camera_id] = mode

            self.packets_to_send.append([200+camera_id, {"bildebehandlingsmodus": self.camera_modes[self.image_processing_mode[camera_id]]}])

            if self.image_processing_mode[camera_id] == 0 or self.image_processing_mode[camera_id] == 1:
                self.camera_tilt_allowed[camera_id] = True
            else:
                self.camera_tilt_allowed[camera_id] = False
            print(f"{self.image_processing_mode = }")
            self.image_processing_mode_wait_counter = 7

    def send_local_sensordata(self):
        buttons = self.data.get("buttons", [0]*10)
        dpad = self.data.get("dpad", (0, 0))
        time_since_start = time.time()-self.start_time
        rotation = dpad[0] * 100
        in_out = dpad[1] * 100
        grip_percent = 0
        if buttons[BUTTON_GRAB] == 1:
            grip_percent = 100
        elif buttons[BUTTON_RELEASE] == 1:
            grip_percent = -100
        if run_send_fake_sensordata:
            self.position[0] += self.data.get("joysticks", [0]*8)[Y_axis]*(3/100)
            self.position[1] += self.data.get("joysticks", [0]*8)[X_axis]*(3/100)
            self.position[2] += self.data.get("joysticks", [0]*8)[Z_axis]*(3/100)
        

        if manual_input_rotation:
            self.send_sensordata_to_gui({"time": [time_since_start], "manipulator": [grip_percent, in_out, rotation, self.manipulator_active]})
        else:
            self.send_sensordata_to_gui({"time": [time_since_start], "manipulator": [grip_percent, in_out, rotation, self.manipulator_active]})


    def recieve_data_from_rov(self, network: Network, t_watch: Threadwatcher, id: int):
        while t_watch.should_run(id):
            try:
                data = network.receive()
                # print(data)
                if data is None:
                    continue
                decoded = decode_packets(data)
                if decoded == []:
                    continue

                for message in decoded:
                    # print(message)
                    self.handle_data_from_rov(message)


                    
                    # Rov_state.send_sensordata_to_gui(Rov_state, message)

            except json.JSONDecodeError as e:
                print(f"{data = }, {e = }")
                pass


    def handle_data_from_rov(self, message: dict):
        self.logger.sensor_logger.info(message)
        # print(message)
        if "ERROR" in message:
            # print(message)
            return
        try:
            message_name = list(message.keys())[0]
        except Exception as e:
            print(e)
            return
        if message_name in self.valid_gui_commands:
            # if message_name == "thrust":
                # print(f"motatt data i main: {message}")
                # print(f"hhf, hhb, hvb, hvf, vhf, vhb, vvb, vvf")
            self.send_sensordata_to_gui(message)
        else:
            pass
            # print(f"\n\nMESSAGE NOT RECOGNISED AS VALID GUI COMMAND\n{message}\n")


    def handle_gyro(self, sensordata):
        print(f"gyro {sensordata = }")
        self.position = sensordata
        self.send_sensordata_to_gui({"gyro": self.position})


def run(network_handler: Network, t_watch: Threadwatcher, id: int, queue_for_rov: multiprocessing.Queue, gui_pipe):
    print(f"{network_handler = }")
    rov_state = Rov_state(queue_for_rov, network_handler, gui_pipe, t_watch)
    if network_handler != None:
        id = t_watch.add_thread()
        threading.Thread(target=rov_state.recieve_data_from_rov, args=(network_handler, t_watch, id), daemon=True).start()
    if run_craft_packet:
        id = t_watch.add_thread()
        threading.Thread(target=rov_state.craft_packet, args=(t_watch, id), daemon=True).start()

    while t_watch.should_run(id):
        rov_state.tick()

        if manual_input_rotation:
            rov_state.get_rotation_input()

        rov_state.get_from_queue()
        rov_state.send_local_sensordata()
        if run_get_controllerdata and rov_state.data != {}:
            rov_state.check_controls()
        rov_state.send_packets()
        rov_state.data = {}

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
def decode_packets(tcp_data: bytes, ) -> list:
    start_not_complete_packet = ""
    end_not_complete_packet = ""
    try:
        json_strings = bytes.decode(tcp_data, "utf-8")
        if not json_strings.startswith('"*"'): # pakken er ikke hel
            start_not_complete_packet = json_strings[:json_strings.index("*")-1]
            json_strings = json_strings[json_strings.index("*")+2:]
        if not json_strings.endswith('"*"'): # pakken er ikke hel
            end_not_complete_packet = json_strings[json_strings.rfind("*")-1:]
            json_strings = json_strings[:json_strings.rfind("*")+2] # til, men ikke med indexen


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
            try:
                item = json.loads(item)
            except Exception as e:
                print(f"{e = }\n {item = }, {tcp_data = }")
                with open("errors.txt", 'ab') as f:
                    f.write(tcp_data)
                
                # exit(0)
            decoded_items.append(item)
    return decoded_items, start_not_complete_packet, end_not_complete_packet




def get_args():
    pass
    print(getopt(sys.argv, "n:g:c:", "network=gui=controller="))




if __name__ == "__main__":        
    os.system("pyuic5 -x ./Subsea_QT_GUI/SUBSEAGUI.ui -o ./Subsea_QT_GUI/SUBSEAGUI.py")
    # get_args()
    # exit(0)
    try:
        global time_since_start
        global start_time_sec
        global run_gui
        global manual_input_rotation
        global run_network
        global run_craft_packet
        start_time_sec = time.time()
        run_gui = True
        run_get_controllerdata = True
        run_network = True
        run_craft_packet = False
        run_send_fake_sensordata = False
        manual_input_rotation = False
        
        queue_for_rov = multiprocessing.Queue()

        t_watch = Threadwatcher()

        gui_parent_pipe, gui_child_pipe = Pipe() # starts the gui program. gui_parent_pipe should get the sensor data
        if run_gui:
            id = t_watch.add_thread()
            gui_loop = Process(target=GUI_loop.run, args=(gui_child_pipe, queue_for_rov, t_watch, id), daemon=True) # and should recieve commands from the gui
            gui_loop.start()


        if run_get_controllerdata:
            id = t_watch.add_thread()
            # takes in controller data and sends it into child_conn
            controller_process = Process(target=controller.run, args=(queue_for_rov, t_watch, id,True, False,), daemon=True)
            controller_process.start()

        # Network is blocking
        network = None
        if run_network:
            network = Network(is_server=False, port=6900, connect_addr="10.0.0.2")
            print("network started")

        print("starting send to rov")
        id = t_watch.add_thread()
        main_driver_loop = threading.Thread(target=run, args=(network, t_watch, id, queue_for_rov, gui_parent_pipe), daemon=True)
        main_driver_loop.start()


        sensordata = {"lekk_temp": [False,  False, False, -1, -1, -1]}
        gui_parent_pipe.send(sensordata)


        if run_send_fake_sensordata:
            thrust_list = [num for num in range(-100,101)]
            power_list = [num for num in range(0, 101)]
            count = -1
            sensordata = {}
            while t_watch.should_run(0):
                time_since_start = round(time.time()-start_time_sec)
                count += 1
                sensordata["lekk_temp"] = [True, True, True, (25+count)%99, (37+count)%99, (61+count)%99]
                sensordata["thrust"] = [thrust_list[(0+count)%201], thrust_list[(13+count)%201], thrust_list[(25+count)%201], thrust_list[(38+count)%201], thrust_list[(37+count)%201], thrust_list[(50+count)%201], thrust_list[(63+count)%201], thrust_list[(75+count)%201], thrust_list[(88+count)%201], thrust_list[(107+count)%201]]
                sensordata["power_consumption"] = [power_list[count%101]*13, power_list[count%101]*2.4, power_list[count%101]*0.65]
                sensordata["gyro"] = [(time_since_start*2)%60, time_since_start%90, time_since_start%90]
                sensordata["time"] = [time_since_start]
                gui_parent_pipe.send(sensordata)
                time.sleep(1)

        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        gui_loop.kill()
        t_watch.stop_all_threads()
        print("stopped all threads")