from Subsea_QT_GUI import GUI_loop
import controller
import threading
import socket
from multiprocessing import Pipe, Process
from Subsea_QT_GUI import *


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
        # print(str(controller_data)[1:-1], end="    \r")
        print(controller_data["joysticks"])

        # sys.stdout.write(f"{controller_data}"+"\r")
        # sys.stdout.flush()
        if relay:
            pass


if __name__ == "__main__":
    print("starting")
    # with open("config.txt", 'r') as config:
        # print(config.read()[1])

    
    parent_conn, child_conn = Pipe() # takes in controller data and sends it into child_conn
    controller_process = Process(target=controller.run, args=(child_conn, True,))
    controller_process.start()

    gui_parent_pipe, gui_child_pipe = Pipe()

    gui_loop = Process(target=GUI_loop.run, args=(gui_child_pipe,))
    gui_loop.start()

    recv_frm_cnt = threading.Thread(target=relay_data_from_controller, daemon=True, args=(parent_conn, True))
    recv_frm_cnt.start()
