from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QSizeGrip
from multiprocessing import Pipe, Value
from Threadwatch import Threadwatcher
import random
import time
import sys
import threading
import json
import os
import Subsea_QT_GUI.SUBSEAGUI as SUBSEAGUI
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGraphicsDropShadowEffect, QPushButton, QApplication, QComboBox
from PyQt5.QtCore import Qt


os.system('pyuic5 -x NYGUI.ui -o SUBSEAGUI.py')
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

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
        # self.stream1.setMinimumWidth(640)
        # self.stream1.setMinimumHeight(480)
        self.stream1.load(QUrl(self.url))
        # self.stream2 = QWebEngineView(self)
        # self.stream2.load(QUrl("http://10.0.0.2:6888/cam.html"))
        layout.addWidget(self.stream1.setMinimumWidth(1000))
        # layout.addWidget(motor_widget)
        # layout.addWidget(self.stream2)
        self.setLayout(layout)
        # self.  .resize(1920,1080)
    

class Window(QMainWindow, SUBSEAGUI.Ui_MainWindow):
    def __init__(self, conn, t_watch: Threadwatcher, id: int, parent=None):
        super().__init__(parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.thread = threading.current_thread()
        self.conn = conn
        os.chdir("Subsea_QT_GUI")
        self.setupUi(self)
        os.chdir("..")
        self.t_watch = t_watch
        self.id = id
        # self.stream1 = QWebEngineView(self)
        # self.stream1.load(QUrl("http://10.0.0.2:6889/cam.html"))
        # self.stream2 = QWebEngineView(self)
        # self.stream2.load(QUrl("http://10.0.0.2:6888/cam.html"))
        # # self.stream1.resize(1920,1080)
        # self.horizontalLayout_6.addWidget(self.stream1)
        # self.horizontalLayout_6.addWidget(self.stream2)

        self.manuell_btn.clicked.connect(self.button_test)
        self.kontroller_btn.clicked.connect(lambda: self.change_current_widget(2))
        self.informasjon_btn.clicked.connect(lambda: self.change_current_widget(1))

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.bgApp.setGraphicsEffect(self.shadow)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setContentsMargins(0, 0, 0, 0)


        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.closeAppBtn.clicked.connect(lambda: self.close())

        # APPLY VALUES TO PROGREESBAR
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.VHF_percentage, self.VHF, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.HVF_percentage, self.HVF, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.VVF_percentage, self.VVF, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.HHF_percentage, self.HHF, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.HVF_percentage, self.HVF, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.VVB_percentage, self.VVB, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.HVB_percentage, self.HVB, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.HVB_percentage, self.HVB, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.VHB_percentage, self.VHB, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.HHB_percentage, self.HHB, "rgba(85, 170, 255, 255)"))

        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.mani_percentage_1, self.mani_1, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.mani_percentage_2, self.mani_2, "rgba(85, 170, 255, 255)"))
        self.slider.valueChanged.connect(lambda: self.setValue(self.slider, self.mani_percentage_3, self.mani_3, "rgba(85, 170, 255, 255)"))

        self.lys_slider.valueChanged.connect(lambda: self.setValue(self.lys_slider, self.lys_percentage, self.lys, "rgba(85, 170, 255, 255)"))

        self.recieve = threading.Thread(target=self.recieve_and_set_text, daemon=True, args=(self.conn,))
        self.recieve.start()
        # print(f"type of self.widget: {type(self.widget)}")
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
        while self.t_watch.should_run(self.id):
            # print("trying to take out of pipe")
            sensordata = conn.recv()
            # print(sensordata)
            self.update_gui(sensordata)
        print("recieved close thread. trying to close")
        self.close()
        

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
        htmlText = """<p align="center"><span style=" font-size:9pt;">{VALUE}</span><span style=" font-size:9pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))

        # CALL DEF progressBarValue
        self.progressBarValue(sliderValue, progressBarName, color)

    ## DEF PROGRESS BAR VALUE
    def progressBarValue(self, value, widget, color):
        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0
        if value >= 0:
            # PROGRESSBAR STYLESHEET BASE
            styleSheet = """
            QFrame{
                border-radius: 30px;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
            }
            """
            # GET NEW VALUES
            stop_1 = str(progress - 0.001)
            stop_2 = str(progress)
        else:
            # PROGRESSBAR STYLESHEET BASE
            styleSheet = """
            QFrame{
                border-radius: 30px;
                background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgb(226, 47, 53));
            }
            """
            
            # GET NEW VALUES
            stop_1 = str(progress - 1)
            stop_2 = str(progress - 0.001 -1)

        # FIX MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # APPLY STYLESHEET WITH NEW VALUES
        widget.setStyleSheet(newStylesheet)

def run(conn, t_watch: Threadwatcher, id):
    app = QtWidgets.QApplication(sys.argv)
    
    win = Window(conn, t_watch, id)
    win.setWindowTitle("UiS Subsea")
    win.showMaximized() # for windows
    #win.showFullScreen() # for mac
    win.show()
    # win.close()
    sys.exit(app.exec())    

if __name__ == "__main__":
    import SUBSEAGUI
    run()
