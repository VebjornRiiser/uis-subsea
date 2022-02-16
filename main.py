from getopt import getopt
import multiprocessing
from pickletools import uint8
from socket import socket
from logger import logging
from Subsea_QT_GUI import GUI_loop
from multiprocessing import Pipe, Process, connection
from Subsea_QT_GUI import *
from Threadwatch import Threadwatcher
from network_handler import Network
import controller
import threading
import random
import time
import json
import sys
import datetime

# takes a python object and prepares it for sending over network
def network_format(data) -> bytes:
    packet_seperator = json.dumps("*")
    return bytes(packet_seperator+json.dumps(data)+packet_seperator, "utf-8")


    #################### is probably replaced by "send_data_to_rov" #######################################
def relay_data_from_controller(connection_controller, t_watch: Threadwatcher, id, relay=True):
    # thread = threading.current_thread()
    # while getattr(thread, "run", True):
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
        conn.recv()
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
        delta = random.randint(-1,1)
        try:
            sensordata = create_test_sensordata(delta, sensordata)
            # print(f"sending data from main to gui: {sensordata}")
            conn.send(sensordata)
            time.sleep(0.2)
        except KeyboardInterrupt:
            t_watch.stop_thread(id)

def send_data_to_rov(network_handler: Network, t_watch: Threadwatcher, id: int, pipe=None):
    camera_toggle_wait_counter = 0
    right_joystick_toggle_wait_counter = 0
    camera_tilt = [0.0, 0.0]
    if pipe is None:
        while t_watch.should_run(id):
            pass
            # network_handler.send(bytes("Hei","utf-8"))
    else:
        camera_toggle = True
        right_joystick_move_camera = True
        while t_watch.should_run(id):
            if camera_toggle_wait_counter > 0:
                camera_toggle_wait_counter -= 1
            if right_joystick_toggle_wait_counter > 0:
                right_joystick_toggle_wait_counter -= 1
            data = pipe.recv()
            camera_command = None
            if data["buttons"][2] and camera_toggle_wait_counter == 0:
                    # camera_command = [[200, {"on": True, "bildebehandlingsmodus": 0}]]
                    camera_toggle_wait_counter = 7
                    camera_command = [[200, {"on": camera_toggle}]]
                    camera_toggle = not camera_toggle
            if data["buttons"][9] and right_joystick_toggle_wait_counter == 0:
                right_joystick_toggle_wait_counter = 5
                right_joystick_move_camera = not right_joystick_move_camera
                print("changed right joystick function")
            # print(data["buttons"][9])
            formated_data, camera_tilt = handle_controller_data(data, camera_tilt, right_joystick_move_camera, camera_commands=camera_command)
            if network_handler is not None:
                network_handler.send(network_format(formated_data))
            else:
                print(formated_data)
                pass

ID = 0

X_axis = 1
Y_axis = 0
Z_axis = 6
ROTATION_axis = 2

Left_Button = 4
Right_Button = 5

def handle_controller_data(controller_values: dict, camera_tilt, joystick_moves_camera, camera_commands: list = None) -> list:
    packets_to_send = []
    ################  X,Y,Z, rotasjon, m.teleskop, m.vri, m.klype + uint8 throttle  #####################
    styredata = []
    styredata.append(controller_values["joysticks"][X_axis])
    styredata.append(controller_values["joysticks"][Y_axis])
    styredata.append(controller_values["joysticks"][Z_axis])
    if not joystick_moves_camera:
        styredata.append(controller_values["joysticks"][ROTATION_axis])
    else:
        styredata.append(0)
    styredata.append(build_manipulator_byte(list(controller_values["dpad"]), controller_values["buttons"]))
    styredata.append(0)
    styredata.append(0)
    styredata.append(0)

    # camera_packet = [500, {}]
    if joystick_moves_camera:
        camera_tilt, change = update_camera_tilt(controller_values["camera_to_control"], controller_values["camera_movement"], controller_values["time_between_updates"], camera_tilt   )
        if change != -1:
            packets_to_send.append([200 + controller_values["camera_to_control"], {"tilt": camera_tilt[change]}])

    packets_to_send.append([70, styredata])

    # adds the command to the existing packet if it exists and then removes it from the list.
    if camera_commands != None:
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


def update_camera_tilt(camera_to_update, move_speed, time_delta, camera_tilt):
    if move_speed==0: # no change
       return camera_tilt, -1 # -1 means no camera has changed

    tilt_time_sec = 2 # time in seconds for the camera to move from one side to the other
    # tilt_time_sec = 2 # time in seconds for the camera to move from one side to the other
    total_degrees = 80
    tilt_per_ms = total_degrees/(tilt_time_sec*1000)

    camera_tilt[camera_to_update] += (move_speed/100) * time_delta * tilt_per_ms
    if camera_tilt[camera_to_update]>total_degrees/2:
        camera_tilt[camera_to_update] = total_degrees/2
        return camera_tilt, -1 # -1 means no camera has changed

    elif camera_tilt[camera_to_update] < -total_degrees/2:
        camera_tilt[camera_to_update] = -total_degrees/2
        return camera_tilt, -1 # -1 means no camera has changed

    camera_tilt[camera_to_update] = round(camera_tilt[camera_to_update])

    return camera_tilt, camera_to_update

MANIPULATOR_IN_OUT = 1
MANIPULATOR_ROTATE = 0
BUTTON_GRAB = 4
BUTTON_RELEASE = 5

def build_manipulator_byte(dpad_data: list, button_data: list):
    data = dpad_data
    data.append(button_data[BUTTON_GRAB])
    data.append(button_data[BUTTON_RELEASE])
    # print(data)
    # Inn, Ut, roter med klokka, roter mot klokka, lukk klo, åpne klo, tom, tom
    # byte_arr = [0]*8
    # dpad_to_values = [{-1: "rotate ccw", 0: "no rotation", 1: "rotate ccw"}, {-1: "manipulator in", 0: "manipulator is still", 1: "manipulator out"}]
    data_to_values = [{-1: 0b0000_1000, 0: 0b0, 1: 0b0000_0100}, {-1: 0b0000_0001, 0: 0b0, 1: 0b0000_0010}, {1: 0b0001_0000, 0: 0b0}, {1: 0b0010_0000, 0: 0b0}]

    # print(button_data[BUTTON_GRAB], button_data[BUTTON_RELEASE])
    byte_val = 0
    for index, axis_val in enumerate(data):
        byte_val = byte_val | data_to_values[index][axis_val] # or's all the bitwise values. 

    # dpad_data[MANIPULATOR_IN_OUT]
    return byte_val


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
            print(decoded)
        except json.JSONDecodeError as e:
            print(f"{data = }, {e = }")

def get_args():
    pass
    print(getopt(sys.argv, "n:g:c:", "network=gui=controller="))

if __name__ == "__main__":
    # get_args()
    global start_time_sec
    start_time_sec = time.time()
    run_gui = False
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
        parent_conn_controller, child_conn_controller = Pipe() # takes in controller data and sends it into child_conn
        controller_process = Process(target=controller.run, args=(child_conn_controller, t_watch, id,True, False,), daemon=True)
        controller_process.start()



    #################### is probably replaced by "send_data_to_rov" #######################################
    # id = t_watch.add_thread()
    # recv_frm_cnt = threading.Thread(target=relay_data_from_controller, args=(parent_conn_controller, t_watch, id, True), daemon=True)
    # recv_frm_cnt.start()
    # print("starting network")
    
    # Network is blocking
    if run_network:
    # network = Network(is_server=False, bind_addr="0.0.0.0", connect_addr="10.0.0.2", port=6900)
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
            time.sleep(0.3)
            # print("...")
    except KeyboardInterrupt:
        t_watch.stop_all_threads()
        print("stopped all threads")