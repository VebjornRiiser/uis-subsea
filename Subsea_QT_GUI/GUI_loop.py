from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from multiprocessing import Pipe
import random
import time
import sys
import threading
import json
import os
import Subsea_QT_GUI.SUBSEAGUI as SUBSEAGUI

class Window(QMainWindow, SUBSEAGUI.Ui_MainWindow):
    def __init__(self, conn, parent=None):
        print(os.path.dirname(os.path.realpath(__file__)))
        self.thread = threading.current_thread()
        super().__init__(parent)
        self.setupUi(self)
        self.btn_manuell.clicked.connect(self.button_test)
        threading.Thread(target=lambda: self.recieve_and_set_text(conn)).start()

    def recieve_and_set_text(self, conn):
        print("trying to take out of pipe")
        # while not self.thread.should_stop:
        while True:
            data = conn.recv()
            data = json.loads(str(data))
            print(data)
            # self.dybde.setText(str(data["dybde"]))


    def button_test(self):
        print("Clicked on button")


def run(conn=None):

    send_to_GUI, receive_from_GUI = Pipe()
    conn = send_to_GUI
    data_thread = threading.Thread(target=generate_data, args=(receive_from_GUI,))
    data_thread.start()

    app = QtWidgets.QApplication(sys.argv)
    win = Window(conn)
    win.show()
    sys.exit(app.exec())


def generate_data(conn):
    while True:
        try:
            time.sleep(1)
            print("tring to send on pipe")
            conn.send((random.randrange(65,97)))
        except KeyboardInterrupt:
            exit(0)

if __name__ == "__main__":
    import SUBSEAGUI

    run()
