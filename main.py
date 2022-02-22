from getopt import getopt
# import multiprocessing
# from logger import logging
from os import pipe
from Subsea_QT_GUI import GUI_loop
from multiprocessing import Pipe, Process
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
    while t_watch.should_run(id):
        print(conn.recv())
    print("t_watch is false")


def create_test_sensordata(delta, old_sensordata=None):
    sensordata = {}
    if old_sensordata is None:
        sensordata = {"tid": int(time.time()-start_time_sec), "dybde": -2500.0, "spenning": 48.0, "temp_vann": 26.0}
    else:
        sensordata["tid"] = int(time.time()-start_time_sec)
        sensordata["dybde"] = old_sensordata["dybde"] + 10*delta
        sensordata["spenning"] = old_sensordata["spenning"] + 0.4*delta
        sensordata["temp_vann"] = old_sensordata["temp_vann"] + 0.3*delta
    return sensordata


def send_sensordata_to_gui(conn, t_watch: Threadwatcher, id):
    sensordata = create_test_sensordata(1)
    while t_watch.should_run(id):
        delta = random.randint(-1, 1)
        try:
            sensordata = create_test_sensordata(delta, sensordata)
            # print(f"sending data from main to gui: {sensordata}")
            conn.send(sensordata)
            time.sleep(0.2)
        except KeyboardInterrupt:
            t_watch.stop_thread(id)

class Rov_state:
    def __init__(self) -> None:
        self.data:dict = {}
        self.camera_toggle_wait_counter: int = 0
        self.right_joystick_toggle_wait_counter: int = 0
        self.camera_tilt: list[float] = [0.0, 0.0]
        self.camera_tilt_control_active = True
        self.cam_is_enabled = [True, True]
        self.camera_tilt_allowed = [True, True]  #[cam 0, cam 1]
        self.button_function_list = [self.skip, self.toggle_camera, self.skip, self.toggle_camera]
        self.camera_toggle = True
        self.camera_command: list[list[int, dict]] = None


    def skip(self):
        pass

    
    def toggle_camera(self):
        self.camera_toggle = not self.camera_toggle

    def tick(self):
        self.camera_command = None
        if self.camera_toggle_wait_counter > 0:
            self.camera_toggle_wait_counter -= 1
        if self.right_joystick_toggle_wait_counter > 0:
            self.right_joystick_toggle_wait_counter -= 1



def send_data_to_rov(network_handler: Network, t_watch: Threadwatcher, id: int, controller_pipe=None):

    rov_state = Rov_state()

    # prevents the camera from toggling back again immediately if we hold the button down
    camera_toggle_wait_counter: int = 0

    # prevents the tilt toggle from toggling back again immediately if we hold the button down
    right_joystick_toggle_wait_counter: int = 0

    camera_tilt = [0.0, 0.0]  # tilt in degrees on the camera motors

    if controller_pipe is None:
        while t_watch.should_run(id):
            pass
            # network_handler.send(bytes("Hei","utf-8"))
    else:
        camera_toggle = True
        right_joystick_move_camera = True  # locks
        camera_tilt_lock = [False, False]  # locks the camera tilt if the rov is processing images
        while t_watch.should_run(id):

            rov_state.tick()

            
            if camera_toggle_wait_counter > 0:
                camera_toggle_wait_counter -= 1
            if right_joystick_toggle_wait_counter > 0:
                right_joystick_toggle_wait_counter -= 1

            rov_state.data = controller_pipe.recv()
            camera_command: list[list[int, dict]] = None
            if data["buttons"][2] and camera_toggle_wait_counter == 0:
                # gui_selct_list[id_fra_gui]()
                # camera_command = [[200, {"on": True, "bildebehandlingsmodus": 0}]]
                camera_toggle_wait_counter = 7
                # camera_command = [[200+data["camera_to_control"], {"on": camera_toggle}], [200, {"on": True, "bildebehandlingsmodus": 0}]]
                camera_command = [[200+data["camera_to_control"], {"on": camera_toggle, "bildebehandlingsmodus": 1}]]
                # print(camera_command)
                camera_toggle = not camera_toggle
            if data["buttons"][9] and right_joystick_toggle_wait_counter == 0:
                right_joystick_toggle_wait_counter = 5
                right_joystick_move_camera = not right_joystick_move_camera
                print("changed right joystick function")

            if camera_command is not None:
                camera_tilt_lock = check_camera_command(camera_command)

            formated_data, camera_tilt = handle_controller_data(data, camera_tilt, right_joystick_move_camera, camera_tilt_lock, camera_commands=camera_command)
            if network_handler is not None:
                network_handler.send(network_format(formated_data))
            else:
                # print(formated_data)
                pass


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


def handle_controller_data(controller_values: dict, camera_tilt, joystick_moves_camera, tilt_lock, camera_commands: list = None) -> list:
    """Takes inn all the controller data and produces the list of commands
    to send to the rov"""

    packets_to_send = []
    #  X,Y,Z, rotasjon, m.teleskop, m.vri, m.klype + uint8 throttle  ##########
    styredata = []
    styredata.append(controller_values["joysticks"][X_axis])
    styredata.append(controller_values["joysticks"][Y_axis])
    styredata.append(controller_values["joysticks"][Z_axis])
    if not joystick_moves_camera:
        styredata.append(controller_values["joysticks"][ROTATION_axis])
    else:
        styredata.append(0)
    styredata.append(build_manipulator_byte(list(controller_values["dpad"]), controller_values["buttons"], True))
    styredata.append(0)
    styredata.append(0)
    styredata.append(0)

    # camera_packet = [500, {}]
    if joystick_moves_camera:
        camera_tilt, change = update_camera_tilt(controller_values["camera_to_control"], controller_values["camera_movement"], controller_values["time_between_updates"], camera_tilt, tilt_lock)
        if change != -1:
            packets_to_send.append([200 + controller_values["camera_to_control"], {"tilt": camera_tilt[change]}])

    packets_to_send.append([70, styredata])

    # adds the command to the existing packet if it exists and then removes it from the list.
    if camera_commands is not None:
        # print(f"{len(camera_commands)}")
        for index, camera in enumerate(camera_commands):
            for packet in packets_to_send:
                if packet[ID] == camera[ID]:
                    for item in camera[1]:
                        packet[1][item] = camera[1][item]
                    camera_commands.pop(index)

        if len(camera_commands) > 0:
            for command in camera_commands:
                packets_to_send.append(command)

    return packets_to_send, camera_tilt


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


MANIPULATOR_IN_OUT = 1
MANIPULATOR_ROTATE = 0
BUTTON_GRAB = 4
BUTTON_RELEASE = 5


# Creates the byte that describes how the manipulator should move
def build_manipulator_byte(dpad_data: list, button_data: list, enabled):
    data = list(dpad_data)
    data.append(button_data[BUTTON_GRAB])
    data.append(button_data[BUTTON_RELEASE])
    # Inn: 1, Ut: 2, roter med klokka: 4, roter mot klokka: 8, lukk klo: 16,
    # åpne klo: 32, enable: 64, ingen funksjon
    data_to_values = [{-1: 0b0000_1000, 0: 0b0, 1: 0b0000_0100},
                      {-1: 0b0000_0001, 0: 0b0, 1: 0b0000_0010},
                      {1: 0b0001_0000, 0: 0b0},
                      {1: 0b0010_0000, 0: 0b0}]

    byte_val = 0
    for index, axis_val in enumerate(data):  # bitwise or's all the values
        byte_val = byte_val | data_to_values[index][axis_val]
    if enabled:
        byte_val = byte_val | 64  # enables manipulator

    return byte_val


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
            # if len(decoded)>0:
            #     print(decoded[0]["sensor1"])
            if decoded == []:
                continue
            # print(decoded)
        except json.JSONDecodeError as e:
            print(f"{data = }, {e = }")


def get_args():
    pass
    print(getopt(sys.argv, "n:g:c:", "network=gui=controller="))




if __name__ == "__main__":
    # print(check_camera_command([[201, {"on": True, "bildebehandlingsmodus": 1}], [70, [0, 0, 0, 0, 0, 0, 0, 0]]]))
    # exit(0)
    global start_time_sec
    start_time_sec = time.time()
    run_gui = True
    run_get_controllerdata = True
    run_network = False

    t_watch = Threadwatcher()
    if run_gui:
        id = t_watch.add_thread()
        gui_parent_pipe, gui_child_pipe = Pipe() # starts the gui program. gui_parent_pipe should get the sensor data
        gui_loop = Process(target=GUI_loop.run, args=(gui_child_pipe, t_watch, id)) # and should recieve commands from the gui
        gui_loop.start()

        id = t_watch.add_thread()
        recv_from_gui = threading.Thread(target=recieve_commands_from_gui, args=(gui_parent_pipe, t_watch, id),daemon=True)
        recv_from_gui.start()

        id = t_watch.add_thread()
        send_to_gui = threading.Thread(target=send_sensordata_to_gui, args=(gui_parent_pipe, t_watch, id), daemon=True)
        send_to_gui.start()

    if run_get_controllerdata:
        id = t_watch.add_thread()
        # takes in controller data and sends it into child_conn
        parent_conn_controller, child_conn_controller = Pipe()
        controller_process = Process(target=controller.run, args=(child_conn_controller, t_watch, id,True, False,), daemon=True)
        controller_process.start()

    # Network is blocking
    if run_network:
        network = Network(is_server=False, port=6900, connect_addr="10.0.0.2")
        print("network started")

        id = t_watch.add_thread()
        snd_data_to_rov = threading.Thread(target=send_data_to_rov, args=(network, t_watch, id, parent_conn_controller), daemon=True)
        # snd_data_to_rov = threading.Thread(target=send_data_to_rov, args=(None, t_watch, id, parent_conn_controller), daemon=True)
        snd_data_to_rov.start()

        recieve_data_from_rov = threading.Thread(target=recieve_data_from_rov, args=(network, t_watch, id), daemon=True)
        recieve_data_from_rov.start()

    elif run_get_controllerdata:
        print("starting send to rov")
        snd_data_to_rov = threading.Thread(target=send_data_to_rov, args=(None, t_watch, id, parent_conn_controller), daemon=True)
        snd_data_to_rov.start()

    try:
        while True:
            time.sleep(1)
            # print("...")
    except KeyboardInterrupt:
        t_watch.stop_all_threads()
        print("stopped all threads")
