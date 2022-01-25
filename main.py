import json
from flask import Flask
import controller, nettverkskommunikasjon, requests, threading
from multiprocessing import Pipe, Process
import app


def controllerdata_to_json(controll_data):
    pass   
    can = {}
    # return json.dumps()

def run_webapp(connection):
    pass

def send_data_to_rov():
    pass

def receive_data_from_rov():
    pass

def relay_data_from_controller(connection_controller, relay=True):
    thread = threading.current_thread()
    # while getattr(thread, "run", True):
    while True:
        controller_data = connection_controller.recv()
        print(controller_data, end="                          \r")
        if relay:
            # requests.post("http://10.0.0.16:5000/update_data", json.dumps(controller_data))
            requests.post("http://127.0.0.1:5000/update_data", json.dumps(controller_data))



def send_data_to_rov():
    pass

if __name__ == "__main__":
    # with open("config.txt", 'r') as config:
        # print(config.read()[1])
    # flask_server = Process(target=app.app.run)
    # flask_server.start()
    # print(flask_server.is_alive())

    parent_conn, child_conn = Pipe()
    controll_process = Process(target=controller.run, args=(child_conn, True,))
    controll_process.start()
    recv_frm_cnt = threading.Thread(target=relay_data_from_controller, daemon=True, args=(parent_conn, False))
    recv_frm_cnt.start()
    # recv_frm_cnt.run = False
    # while True:
    #     controller_data = parent_conn.recv()
    #     print(controller_data, end="                          \r")
        # controll_process.join()