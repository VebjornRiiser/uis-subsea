from multiprocessing import Pipe, Process
import multiprocessing
import controller

def controllerdata_to_json(controll_data):
    pass
    # dictionary
    # return json.dumps()


if __name__ == "__main__":
    # with open("config.txt", 'r') as config:
        # print(config.read()[1])
    parent_conn, child_conn = Pipe()
    controll_process = multiprocessing.Process(target=controller.run, args=(child_conn, True,))
    controll_process.start()
    while True:
        controller_data = parent_conn.recv()
        print(controller_data, end="                          \r")
        # controll_process.join()
    