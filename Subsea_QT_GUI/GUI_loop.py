import random, time
import Subsea_QT_GUI.SUBSEAGUI, sys, threading
from PyQt5 import QtCore, QtGui, QtWidgets
from multiprocessing import Pipe

from PyQt5.QtWidgets import QMainWindow

import Subsea_QT_GUI.SUBSEAGUI as SUBSEAGUI

class Window(QMainWindow, SUBSEAGUI.Ui_MainWindow):
    def __init__(self, conn, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btn_paa_5.clicked.connect(self.button_test)
        threading.Thread(target=lambda: self.recieve_and_set_text(conn)).start()

    def recieve_and_set_text(self, conn):
        print("trying to take out of pipe")
        while True:
            data = conn.recv()
            self.dybde.setText(str(data))


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
        time.sleep(1)
        print("tring to send on pipe")
        conn.send((random.randrange(65,97)))

if __name__ == "__main__":
    run()
