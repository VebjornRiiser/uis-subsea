from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel
from PyQt5.QtWebEngineWidgets import *
from PyQt5.Qt import *
from multiprocessing import Pipe, Value
from Threadwatch import Threadwatcher
import random
import time
import sys
import threading
import json
import os
import Subsea_QT_GUI.SUBSEAGUI as SUBSEAGUI

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, port):
        super().__init__()
        layout = QHBoxLayout()
        self.label = QLabel("Another Window")
        self.setWindowTitle("Camera 1")

        self.url = f"http://10.0.0.2:{port}/cam.html"
        self.stream1 = QWebEngineView(self)
        self.stream1.load(QUrl(self.url))
        # self.stream2 = QWebEngineView(self)
        # self.stream2.load(QUrl("http://10.0.0.2:6888/cam.html"))

        layout.addWidget(self.stream1)
        # layout.addWidget(self.stream2)
        self.setLayout(layout)
        # self.  .resize(1920,1080)


class Window(QMainWindow, SUBSEAGUI.Ui_MainWindow):
    def __init__(self, conn, parent=None):
        super().__init__(parent)

        self.thread = threading.current_thread()
        self.conn = conn
        os.chdir("Subsea_QT_GUI")
        self.setupUi(self)
        os.chdir("..")
        # self.stream1 = QWebEngineView(self)
        # self.stream1.load(QUrl("http://10.0.0.2:6889/cam.html"))
        # self.stream2 = QWebEngineView(self)
        # self.stream2.load(QUrl("http://10.0.0.2:6888/cam.html"))
        # # self.stream1.resize(1920,1080)
        # self.horizontalLayout_6.addWidget(self.stream1)
        # self.horizontalLayout_6.addWidget(self.stream2)

        self.btn_manuell.clicked.connect(self.button_test)
        self.pushButton_5.clicked.connect(lambda: self.change_current_widget(0))
        self.pushButton_6.clicked.connect(lambda: self.change_current_widget(1))

        # APPLY VALUES TO PROGREESBAR
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.labelPercentage, self.circularProgress, "rgba(85, 170, 255, 255)"))

        self.recieve = threading.Thread(target=lambda: self.recieve_and_set_text(self.conn), daemon=True)
        self.recieve.start()
        self.w1 = AnotherWindow(6888)
        self.w1.show()
        self.w2 = AnotherWindow(6889)
        self.w2.show()
        
    def update_gui(self, data):
        self.dybde.setText(str(round(data["dybde"],4)))
        self.tid.setText(str(data["tid"]))
        self.spenning.setText(str(round(data["spenning"],4)))
        self.temp_vann.setText(str(round(data["temp_vann"],4)))

    def recieve_and_set_text(self, conn):
        # while not self.thread.should_stop:
        while True:
            # print("trying to take out of pipe")
            sensordata = conn.recv()
            # print(sensordata)
            self.update_gui(sensordata)

    def button_test(self):
        # print("Clicked on button")
        self.w1.stream1.load(Qurl("http://vg.no"))
        self.w2.stream1.load(Qurl("http://vg.no"))

    def change_current_widget(self, index):
        print(f"should change to widget {index}")
        self.stackedWidget.setCurrentIndex(index)


    ## SET VALUES TO DEF progressBarValue
    def setValue(self, slider, labelPercentage, progressBarName, color):
        # GET SLIDER VALUE
        value = slider.value()
        # CONVERT VALUE TO INT
        sliderValue = int(value)
        # HTML TEXT PERCENTAGE
        htmlText = """<p align="center"><span style=" font-size:14pt;">{VALUE}</span><span style=" font-size:14pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

        # CALL DEF progressBarValue
        self.progressBarValue(sliderValue, progressBarName, color)

    ## DEF PROGRESS BAR VALUE
    def progressBarValue(self, value, widget, color):
        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 30px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """
        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0
        if value >= 0:
            # GET NEW VALUES
            stop_1 = str(progress - 0.001)
            stop_2 = str(progress)
        else:
            # GET NEW VALUES
            stop_1 = str(progress - 1)
            stop_2 = str(progress - 0.001 -1)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)

def run(conn, t_watch: Threadwatcher, id):
    app = QtWidgets.QApplication(sys.argv)
    win = Window(conn)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    import SUBSEAGUI

    run()
