    import multiprocessing
from socket import socket
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
import logging



def controllerdata_to_json(controll_data: dict) -> str:

    return json.dumps(controll_data)
    pass



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
    if pipe is None:
        while t_watch.should_run(id):
            pass
            # network_handler.send(bytes("Hei","utf-8"))
    else:
        while t_watch.should_run(id):
            data = pipe.recv()
            network_handler.send(packet_seperator+handle_controller_data(data)+packet_seperator)
            # print(handle_controller_data(data))
            # network_handler.send(bytes(json.dumps(data),"utf-8"))
            # print("sent data")
ID = 0

X_axis = 1
Y_axis = 0
Z_axis = 6
packet_seperator = bytes("*", "utf-8")

Left_Button = 4
Right_Button = 5

camera_tilt = 0 # degrees

def handle_controller_data(controller_values: dict) -> list:

    packets_to_send = []
    ################  X,Y,Z, rotasjon, m.teleskop, m.vri, m.klype + uint8 throttle  #####################
    styredata = []
    styredata.append(controller_values["joysticks"][X_axis])
    styredata.append(controller_values["joysticks"][Y_axis])
    styredata.append(controller_values["joysticks"][Z_axis])
    build_manipulator_byte(controller_values["dpad"], controller_values["buttons"])
    styredata.append(controller_values["dpad"][1])
    # for value in controller_values["joysticks"][2:-2]:
    #     joy_list.append(value)
    packets_to_send.append([70, styredata])

    packets_to_send.append([160 + controller_values["camera_to_control"], controller_values["camera_movement"]])


    return bytes(json.dumps(packets_to_send), "utf-8")
    
MANIPULATOR_IN_OUT_DPAD = 1
def build_manipulator_byte(dpad_data: list, button_data: list):
    # Inn, Ut, roter med klokka, roter mot klokka, lukk klo, åpne klo, tom, tom
    # byte_arr = [0]*8
    data_to_hex = {"in": 1, "out": 2}
    dpad_data[MANIPULATOR_IN_OUT_DPAD]
    return


def decode_packets(tcp_data: bytes) -> list:
    json_strings = bytes.decode(tcp_data, "utf-8")
    json_list = json_strings.split(json.dumps("*"))
    # print(f"{json_list.count('') = } ")

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
            print(decode_packets(data))
        except json.JSONDecodeError as e:
            print(f"{data = }, {e = }")


if __name__ == "__main__":
    global start_time_sec
    start_time_sec = time.time()
    print("starting")
    # with open("config.txt", 'r') as config:
    #     print(config.read()[1])

    t_watch = Threadwatcher()
    # [[0,76]]

    # id = t_watch.add_thread()
    # gui_parent_pipe, gui_child_pipe = Pipe() # starts the gui program. gui_parent_pipe should get the sensor data
    # gui_loop = Process(target=GUI_loop.run, args=(gui_child_pipe, t_watch, id)) # and should recieve commands from the gui
    # gui_loop.start()

    id = t_watch.add_thread()
    parent_conn_controller, child_conn_controller = Pipe() # takes in controller data and sends it into child_conn
    controller_process = Process(target=controller.run, args=(child_conn_controller, t_watch, id,True, False,), daemon=True)
    controller_process.start()


    # id = t_watch.add_thread()
    # recv_from_gui = threading.Thread(target=recieve_commands_from_gui, args=(gui_parent_pipe, t_watch, id),daemon=True)
    # recv_from_gui.start()

    # id = t_watch.add_thread()
    # send_to_gui = threading.Thread(target=send_sensordata_to_gui, args=(gui_parent_pipe, t_watch, id), daemon=True)
    # send_to_gui.start()

    # id = t_watch.add_thread()
    # recv_frm_cnt = threading.Thread(target=relay_data_from_controller, args=(parent_conn_controller, t_watch, id, True), daemon=True)
    # recv_frm_cnt.start()
    # print("starting network")
    
    # Network is blocking

    # network = Network(is_server=False, bind_addr="0.0.0.0", connect_addr="10.0.0.2", port=6900)
    network = Network(is_server=False, port=6900, connect_addr="10.0.0.2")
    print("network started")

    id = t_watch.add_thread()
    snd_data_to_rov = threading.Thread(target=send_data_to_rov, args=(network, t_watch, id, parent_conn_controller), daemon=True)
    snd_data_to_rov.start()

    recieve_data_from_rov = threading.Thread(target=recieve_data_from_rov, args=(network, t_watch, id), daemon=True)
    recieve_data_from_rov.start()
    try:
        while True:
            time.sleep(0.3)
            # print("...")
    except KeyboardInterrupt:
        t_watch.stop_all_threads()
        print("stopped all threads")