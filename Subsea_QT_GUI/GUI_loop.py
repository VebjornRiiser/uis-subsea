from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QTextBrowser
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
        # self.stackedWidget.addWidget(self.informasjon)
        # self.stackedWidget.addWidget(self.kontroller)

        print(os.path.dirname(os.path.realpath(__file__)))
        self.thread = threading.current_thread()
        self.conn = conn
        super().__init__(parent)
        self.setupUi(self)
        self.btn_manuell.clicked.connect(self.button_test)
        self.pushButton_5.clicked.connect(lambda: self.change_current_widget(0))
        self.recieve = threading.Thread(target=lambda: self.recieve_and_set_text(self.conn), daemon=True)
        self.recieve.start()
        self.change_current_widget(0)

    def recieve_and_set_text(self, conn):
        # while not self.thread.should_stop:
        while True:
            # print("trying to take out of pipe")
            sensordata = conn.recv()
            # print(sensordata)
            self.update_gui(sensordata)

    def update_gui(self, data):
        self.dybde.setText(str(round(data["dybde"],4)))
        self.tid.setText(str(data["tid"]))
        self.spenning.setText(str(round(data["spenning"],4)))
        self.temp_vann.setText(str(round(data["temp_vann"],4)))


    def button_test(self):
        print("Clicked on button")

    def change_current_widget(self, index):
        print(f"should change to widget {index}")
        self.stackedWidget.setCurrentIndex(index)


def run(conn=None):
    if conn is None:
        send_to_GUI, receive_from_GUI = Pipe()
        conn = send_to_GUI
        data_thread = threading.Thread(target=generate_data, args=(receive_from_GUI,), daemon=True)
        data_thread.start()

    app = QtWidgets.QApplication(sys.argv)
    win = Window(conn)
    win.show()
    sys.exit(app.exec())


def generate_data(conn):
    while True:
        try:
            time.sleep(1)
            # print("tring to send on pipe")
            conn.send((random.randrange(65,97)))
        except KeyboardInterrupt:
            exit(0)

if __name__ == "__main__":
    run()
