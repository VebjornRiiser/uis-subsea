from Subsea_QT_GUI import GUI_loop
from multiprocessing import Pipe, Process, connection
from Subsea_QT_GUI import *
from Threadwatch import Threadwatcher
import controller
import threading
import random
import time
import json
import sys


def controllerdata_to_json(controll_data: dict) -> str:

    return json.dumps(controll_data)
    pass


def send_data_to_rov():
    pass


def receive_data_from_rov():
    pass


def relay_data_from_controller(connection_controller, t_watch: Threadwatcher, id, relay=True):
    # thread = threading.current_thread()
    # while getattr(thread, "run", True):
    while t_watch.should_run(id):
        controller_data = connection_controller.recv()
        # print(str(controller_data)[1:-1], end="                                                      \r")
        # print(controller_data["joysticks"])

        sys.stdout.write(f"{controller_data}"+"         \r")
        sys.stdout.flush()
        if relay:
            # print(controllerdata_to_json(controller_data), end="            \r")
            # print(controllerdata_to_json(controller_data))
            pass

def recieve_commands_from_gui(conn, t_watch: Threadwatcher, id):
    while t_watch.should_run:
        try:
            conn.recv()
        except KeyboardInterrupt:
            return

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

if __name__ == "__main__":
    global start_time_sec
    start_time_sec = time.time()
    print("starting")
    # with open("config.txt", 'r') as config:
    #     print(config.read()[1])

    t_watch = Threadwatcher()

    


    id = t_watch.add_thread()
    parent_conn, child_conn = Pipe() # takes in controller data and sends it into child_conn
    controller_process = Process(target=controller.run, args=(child_conn, True, False, t_watch, id), daemon=True)
    controller_process.start()

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

    id = t_watch.add_thread()
    recv_frm_cnt = threading.Thread(target=relay_data_from_controller, args=(parent_conn, t_watch, id, True), daemon=True)
    recv_frm_cnt.start()

    gui_loop.join()