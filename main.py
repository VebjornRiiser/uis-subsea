from Subsea_QT_GUI import GUI_loop
from multiprocessing import Pipe, Process
from Subsea_QT_GUI import *
import controller
import threading
import random
import time
import json

def controllerdata_to_json(controll_data):
    pass


def run_webapp(connection):
    pass


def send_data_to_rov():
    pass


def receive_data_from_rov():
    pass


def relay_data_from_controller(connection_controller, relay=True):
    # thread = threading.current_thread()
    # while getattr(thread, "run", True):
    while True:
        controller_data = connection_controller.recv()
        print(str(controller_data)[1:-1], end="    \r")
        # print(controller_data["joysticks"])

        # sys.stdout.write(f"{controller_data}"+"\r")
        # sys.stdout.flush()
        if relay:
            pass

def recieve_commands_from_gui(conn):
    while True:
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

def send_sensordata_to_gui(conn):
    sensordata = create_test_sensordata(1)
    while True:
        delta = random.randint(-1,1)
        try:
            sensordata = create_test_sensordata(delta, sensordata)
            # print(f"sending data from main to gui: {sensordata}")
            conn.send(sensordata)
            time.sleep(0.2)
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    global start_time_sec
    start_time_sec = time.time()
    print("starting")
    # with open("config.txt", 'r') as config:
        # print(config.read()[1])

    
    parent_conn, child_conn = Pipe() # takes in controller data and sends it into child_conn
    controller_process = Process(target=controller.run, args=(child_conn, True,))
    controller_process.start()

    gui_parent_pipe, gui_child_pipe = Pipe() # starts the gui program. gui_parent_pipe should get the sensor data
    gui_loop = Process(target=GUI_loop.run, args=(gui_child_pipe,)) # and should recieve commands from the gui
    # gui_loop.should_stop = False
    gui_loop.start()

    recv_from_gui = threading.Thread(target=lambda: recieve_commands_from_gui(gui_parent_pipe))
    recv_from_gui.start()

    send_to_gui = threading.Thread(target=lambda:send_sensordata_to_gui(gui_parent_pipe))
    send_to_gui.start()

    recv_frm_cnt = threading.Thread(target=relay_data_from_controller, daemon=True, args=(parent_conn, True))
    recv_frm_cnt.start()
    controller_process.join()