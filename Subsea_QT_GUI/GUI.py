__author__ = 'Christoffer Næss'

import os

os.system('pyuic5 -x nyttvindu.ui -o vindu.py')
import queue
import sys
import time
import threading
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, )
from PyQt5.QtWidgets import QApplication
from vindu import Ui_MainWindow as Ui_Dialog
from main_aks_xyz_loggar import seriekomm
import matplotlib
import matplotlib.pyplot as plt
import struct
import serial.tools.list_ports
import pyqtgraph
from shutil import copyfile
from datetime import datetime
import pandas
import yaml

matplotlib.use("Qt5Agg")
dataSendLoop_v = False
QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons
pyqtgraph.setConfigOptions(antialias=True)


# -----------------externe funksjoner----------------------#
def date_parser(date_):
    """Date parser, parses datestrings in ISO format to datetime object"""
    # date_ = date_[:date_.find('.')]
    date_time_obj = datetime.fromisoformat(date_)
    return date_time_obj


class Window(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Bol flags
        self.kjor = False
        self.connected = False
        self.kjor_plott_flag = False
        self.flag_servo_running = False
        self.first_loop = True

        # Setup GUI
        self.setupUi(self)
        self.logg_name = f'loggfil'

        # Setup menu
        with open(f'config.yaml') as config:
            config_data = yaml.load(config, Loader=yaml.FullLoader)
        self.config_data = config_data
        self.app = QApplication(sys.argv)
        self.app.setStyle(config_data['style'])
        self.actionSave_plot.triggered.connect(self.save_plot)
        self.setPalette(choose_palette(config_data['color_mode']))
        self.actionFalse.triggered.connect(lambda: self.setPalette(choose_palette()))
        self.actionTrue.triggered.connect(lambda: self.setPalette(choose_palette('darkmode')))
        self.actionFusion.triggered.connect(lambda: self.app.setStyle('Fusion'))
        self.actionWindows_Vista.triggered.connect(lambda: self.app.setStyle('Windows vista'))
        self.actionWindows.triggered.connect(lambda: self.app.setStyle('Windows'))
        self.actionQuit.triggered.connect(self.close_program)

        # Setup Plot
        self.plottet = pyqtgraph.PlotWidget()
        self.plot_grid.addWidget(self.plottet)

        # Line editor
        self.lineEdit_2.textEdited.connect(self.line_editor)
        self.line_index = -1
        self.line_editor()

        # Empty lists
        self.ports_listed = []
        self.com = []
        self.uC_meldinger = []
        self.list_x_aks = []
        self.list_y_aks = []
        self.list_z_aks = []
        self.list_dist = []
        self.time_axis = []
        self.ports_list = []
        self.create_portlist()

        # Communication variables
        self.brukerkommandoer = queue.Queue()
        self.port = 'COM6'
        self.baud = 115200

        # Button binds
        self.pushButton.clicked.connect(self.start_stop_servo)
        self.pushButton_2.clicked.connect(self.connect_controlhub)
        self.pushButton_6.clicked.connect(self.close_program)
        self.radio_plot.clicked.connect(self.kjorplott)
        self.button_parameters.clicked.connect(self.send_newparameters)
        self.button_save_parameters.clicked.connect(lambda: self.send_command('update_parameters'))
        self.radio_fir.clicked.connect(lambda: self.change_filter_type(1))
        self.radio_iir.clicked.connect(lambda: self.change_filter_type(0))
        self.radio_PonE.clicked.connect(lambda: self.change_paramters('regulator_type', 0))
        self.radio_PonM.clicked.connect(lambda: self.change_paramters('regulator_type', 1))

        # Sliders
        self.slider_distance.actionTriggered.connect(
            lambda: self.change_value(self.slider_distance, self.spin_distance, 'des_distance'))
        self.slider_p.actionTriggered.connect(lambda: self.change_value(self.slider_p, self.spin_p, 'p_mag', 2))
        self.slider_i.actionTriggered.connect(lambda: self.change_value(self.slider_i, self.spin_i, 'i_mag', 2))
        self.slider_d.actionTriggered.connect(lambda: self.change_value(self.slider_d, self.spin_d, 'd_mag', 2))
        self.slider_response.actionTriggered.connect(
            lambda: self.change_value(self.slider_response, self.spin_response, 'response', 2))
        self.slider_iir_a.actionTriggered.connect(
            lambda: self.change_value([self.slider_iir_a, self.slider_iir_b], [self.spin_iir_a, self.spin_iir_b], 'iir',
                                      2, 'alpha'))
        self.slider_iir_b.actionTriggered.connect(
            lambda: self.change_value([self.slider_iir_b, self.slider_iir_a], [self.spin_iir_b, self.spin_iir_a], 'iir',
                                      2, 'beta'))
        self.slider_iir_aks_a.actionTriggered.connect(
            lambda: self.change_value([self.slider_iir_aks_a, self.slider_iir_aks_b],
                                      [self.spin_iir_aks_a, self.spin_iir_aks_b], 'iir_aks', 2, 'alpha'))
        self.slider_iir_aks_b.actionTriggered.connect(
            lambda: self.change_value([self.slider_iir_aks_b, self.slider_iir_aks_a],
                                      [self.spin_iir_aks_b, self.spin_iir_aks_a], 'iir_aks', 2, 'alpha'))
        self.slider_fir.actionTriggered.connect(lambda: self.change_value(self.slider_fir, self.spin_fir, 'fir', 0))

        # Spinboxes
        self.spin_distance.valueChanged.connect(
            lambda: self.change_value_spin(self.spin_distance, self.slider_distance, 'des_distance', 0))
        self.spin_p.valueChanged.connect(lambda: self.change_value_spin(self.spin_p, self.slider_p, 'p_mag', 2))
        self.spin_i.valueChanged.connect(lambda: self.change_value_spin(self.spin_i, self.slider_i, 'i_mag', 2))
        self.spin_d.valueChanged.connect(lambda: self.change_value_spin(self.spin_d, self.slider_d, 'd_mag', 2))
        self.spin_response.valueChanged.connect(
            lambda: self.change_value_spin(self.spin_response, self.slider_response, 'response', 2))
        self.spin_iir_a.valueChanged.connect(
            lambda: self.change_value_spin([self.spin_iir_a, self.spin_iir_b], [self.slider_iir_a, self.slider_iir_b],
                                           'iir', 2, 'alpha'))
        self.spin_iir_b.valueChanged.connect(
            lambda: self.change_value_spin([self.spin_iir_b, self.spin_iir_a], [self.slider_iir_b, self.slider_iir_a],
                                           'iir', 2, 'beta'))
        self.spin_iir_aks_a.valueChanged.connect(
            lambda: self.change_value_spin([self.spin_iir_aks_a, self.spin_iir_aks_b],
                                           [self.slider_iir_aks_a, self.slider_iir_aks_b], 'iir_aks', 2, 'alpha'))
        self.spin_iir_aks_b.valueChanged.connect(
            lambda: self.change_value_spin([self.spin_iir_aks_b, self.spin_iir_aks_a],
                                           [self.slider_iir_aks_b, self.slider_iir_aks_a], 'iir_aks', 2, 'beta'))
        self.spin_fir.valueChanged.connect(lambda: self.change_value_spin(self.spin_fir, self.slider_fir, 'fir', 0))

        # Lists and dictionarys
        self.datadict = {
            'avstand': 0,
            'gyro_x': 0,
            'gyro_y': 0,
            'gyro_z': 0,
        }
        self.parameters = {
            'des_distance': ['change_distance', self.config_data['des_distance'], self.config_data['des_distance']],
            'p_mag': ['change_p', self.config_data['p_mag'], self.config_data['p_mag']],
            'i_mag': ['change_i', self.config_data['i_mag'], self.config_data['i_mag']],
            'd_mag': ['change_d', self.config_data['d_mag'], self.config_data['d_mag']],
            'response': ['change_response', self.config_data['response'], self.config_data['response']],
            'regulator_type': ['change_regulator', self.config_data['regulator_type'], self.config_data['regulator_type']],
            'filtertype': ['change_filter_type', self.config_data['filtertype'], self.config_data['filtertype'],
                           ['IIR', 'FIR']],
            'iir_aks': ['change_iir', self.config_data['iir_aks'], self.config_data['iir_aks']],
            'iir': ['change_iir', self.config_data['iir'], self.config_data['iir']],
            'fir': ['change_fir', self.config_data['fir'], self.config_data['fir']],
        }
        self.commandlist = {
            'start': 40,                # Starter kommunikasjon
            'stop': 42,                 # Stopper kommunikasjon
            'stop_servo': 46,           # Stopper servo
            'start_servo': 44,          # Starter servo
            'change_distance': 50,      # Endrer ønsket avstand fra object
            'change_p': 60,             # Endrer P verdi for regulator
            'change_i': 62,             # Endrer i verdi for regulator
            'change_d': 64,             # Ender d verdi for regulator
            'change_response': 66,      # Endrer respons til regulator
            'change_regulator': 68,      # Endrer regulator type
            'change_filter_type': 70,   # Endrer filter type
            'change_iir_aks_a': 72,     # Endrer filterverdi til akselerometer
            'change_iir_a': 74,         # Endrer iir verdi til avstandsensor
            'change_fir': 80,           # Endrer fir verdi til avstandsesnor
            'update_parameters': 82,    # Lagrer paramtererverdier i flash på uC
            'end_transmit': 3,          # Stopp byte
            'begin_transmit': 2,        # Start byte
            '0': 0,                     # Padding
        }
        self.param_commands = {
            '--node1': 55,  # 37
            '--disp': 57,  # 39
            '--read': 59  # 3B
        }
        self.bin_param = {
            '--node1': 0b00000001,
            '--disp': 0b00000010,
            '--read': 0b00000100,
            '--store': 0b00001000
        }
        self.colors = {
            'red': QtGui.QColor(135, 18, 18, 150).name(),
            'blue': QtGui.QColor(25, 18, 135, 150).name(),
            'green': QtGui.QColor(18, 134, 18, 150).name(),
            'bkgrey': QtGui.QColor(174, 174, 174, 150).name(),
            'desgrey': QtGui.QColor(53, 53, 53, 150).name(),
            'orange': QtGui.QColor(255, 136, 0, 150).name()
        }
        self.log_data = {
            'timer': [],
            'x_aks': [],
            'y_aks': [],
            'z_aks': [],
            'dist': [],
            'dist_filtrert': [],
        }

        # Almost done
        self.change_defaults()

    def create_portlist(self):
        a = 0
        self.menuPort.clear()
        self.com.clear()
        self.ports_listed.clear()
        self.ports_list = serial.tools.list_ports.comports()
        for port, desc, asd in sorted(self.ports_list):
            self.ports_listed.append([port, desc])
            self.com.append(QtWidgets.QAction(self))
            self.com[a].setObjectName(f"{port}")
            self.menuPort.addAction(self.com[a])
            self.com[a].setText(f"{desc}")
            self.com[a].triggered.connect(self.com_port_select)
            a += 1
        self.com.append(QtWidgets.QAction(self))
        self.com[a].setObjectName(f"update_ports")
        self.menuPort.addAction(self.com[a])
        self.com[a].setText(f'Update ports')
        self.com[a].triggered.connect(self.create_portlist)

    def addData_callbackFunc(self, value):  # Plot loop
        for counter, key in enumerate(self.log_data):
            if key == 'timer':
                self.log_data['timer'].append(value[0])
            else:
                self.log_data[key].append(int(value[counter]))
        if self.log_data['timer'][-1] >= 1000:
            for key in self.log_data:
                self.log_data[key].pop(0)
            self.plottet.setXRange(self.log_data['timer'][-1] - 10, self.log_data['timer'][-1])
        elif self.log_data['timer'][-1] > 10:
            self.plottet.setXRange(self.log_data['timer'][-1] - 10, self.log_data['timer'][-1])
        self.plottet.clear()
        self.plottet.addLegend()
        self.lcdNumber.display(self.log_data['dist'][-1])
        self.plottet.plot(self.log_data['timer'], self.log_data['x_aks'], pen='r', name="Accelerometer X-Axis")
        self.plottet.plot(self.log_data['timer'], self.log_data['y_aks'], pen='b', name='Accelerometer y-Axis')
        self.plottet.plot(self.log_data['timer'], self.log_data['z_aks'], pen='g', name='Accelerometer z-Axis')
        self.plottet.plot(self.log_data['timer'], self.log_data['dist'], pen='y', name='Distance from target')
        global data_measurments
        data_measurments = self.uC_meldinger

    def com_port_select(self):  # Changes com port to connect with
        self.port = self.sender().objectName()
        self.status_handler(f'Com port set to:{self.port}', 'info', 1)

    def start_stop_servo(self):  # Start/Stop servo control
        if self.connected:
            if self.kjor:
                self.serieport.write(self.data_pack_builder('stop_servo', send_lenght=8))
                self.status_handler('Servo has been stopped', 'info', 1)
                self.frame_2.setStyleSheet("QWidget { background-color: %s }" % self.colors['desgrey'])
                self.pushButton.setText('Start')
                self.kjor = False
            else:
                self.serieport.write(self.data_pack_builder('start_servo', send_lenght=8))
                self.send_command('start_servo')
                self.status_handler('Servo started', 'info', 1)
                self.frame_2.setStyleSheet("QWidget { background-color: %s }" % self.colors['green'])
                self.kjor = True
                self.pushButton.setText('Stop')
            return
        else:
            self.status_handler('No connection to uC<br>Cant start servo!', 'info', 2)
            self.frame_2.setStyleSheet("QWidget { background-color: %s }" % self.colors['orange'])
            self.graphicsView.setStyleSheet("QWidget { background-color: %s }" % self.colors['orange'])

    def connect_controlhub(self):  # Connect to card/start logging
        try:
            self.connected ^= True
            if self.connected:
                self.serieport = serial.Serial(self.port, self.baud, timeout=1)
                self.serie_traad = threading.Thread(target=seriekomm, daemon=True, args=(
                self.serieport, self.brukerkommandoer, self.uC_meldinger, self.parameters, self.logg_name))
                self.status_handler('Communication started', 'info', 1)
                self.graphicsView.setStyleSheet("QWidget { background-color: %s }" % self.colors['green'])
                self.pushButton_2.setText('Disconnect')
                self.frame_3.setStyleSheet("QWidget { background-color: %s }" % self.colors['green'])
                self.graphicsView.setStyleSheet("QWidget { background-color: %s }" % self.colors['blue'])
                if self.serieport.isOpen():
                    self.status_handler(f'{self.serieport.name} is open', 'info', 1)
                else:
                    self.serieport.open()
                self.serie_traad.start()
                self.brukerkommandoer.put('k')
                self.serieport.write(self.data_pack_builder('start', send_lenght=8))
                time.sleep(0.2)
                self.change_defaults()
            else:
                if self.kjor_plott_flag:
                    self.radio_plot.toggle()
                    global dataSendLoop_v
                    dataSendLoop_v = False
                    self.kjor_plott_flag = False
                self.status_handler('Disconnected', 'info', 1)
                self.serieport.write(self.data_pack_builder('stop', send_lenght=8))
                self.frame_3.setStyleSheet("QWidget { background-color: %s }" % self.colors['desgrey'])
                self.pushButton_2.setText('Connect')
                self.graphicsView.setStyleSheet("QWidget { background-color: %s }" % self.colors['bkgrey'])
                time.sleep(0.1)
                self.brukerkommandoer.put('s')
        except OSError as temp:
            print(temp)
            self.connected = False
            if str(temp) == f"could not open port '{self.port}': FileNotFoundError(2, 'The system cannot find the file specified.', None, 2)":
                self.status_handler(f'Could not find{self.port}', 'info', 2)
            else:
                self.status_handler(f'{self.port} already in use!', 'info', 2)
            self.frame_3.setStyleSheet("QWidget { background-color: %s }" % self.colors['red'])
            self.graphicsView.setStyleSheet("QWidget { background-color: %s }" % self.colors['red'])
        except Exception as temp:
            print(temp)
            self.connected = False
            self.frame_3.setStyleSheet("QWidget { background-color: %s }" % self.colors['red'])
            self.graphicsView.setStyleSheet("QWidget { background-color: %s }" % self.colors['red'])

    def close_program(self):  # Quit program, disconnect and shutdown servo
        if self.connected:
            if self.kjor:
                self.start_stop_servo()  # STOPS SERVO IF RUNNING
                self.ErrorMessage.append('Servo stopped')
            if self.kjor_plott_flag:
                self.kjorplott()  # Stops plot if running
            self.connect_controlhub()  # STOPS CONNECTION IF CONNECTED
        self.update_config()
        quit()  # Closes GUI

    def kjorplott(self):
        if self.connected:
            global dataSendLoop_v
            self.kjor_plott_flag ^= True
            if self.kjor_plott_flag:
                if self.first_loop:
                    dataSendLoop_v = True
                    self.myDataLoop = threading.Thread(name='myDataLoop', target=DataSend, daemon=True,
                                                       args=(self.addData_callbackFunc,))
                    self.first_loop = False
                    self.myDataLoop.start()
                else:
                    self.myDataLoop = threading.Thread(name='myDataLoop', target=DataSend, daemon=True,
                                                       args=(self.addData_callbackFunc,))
                    self.myDataLoop.start()
                    dataSendLoop_v = True
            else:
                dataSendLoop_v = False
        else:
            self.radio_plot.toggle()
            self.status_handler('No connection to uC<br>Cant  plot graph', 'info', 2)

    def change_value(self, slider, spin, index, div=0, name=None):
        div = 10 ** div
        if name is None:
            if div == 1:
                self.parameters[index][1] = slider.sliderPosition()
            else:
                self.parameters[index][1] = slider.sliderPosition() / div
            spin.setValue(self.parameters[index][1])
        else:
            temp = slider[0].sliderPosition()
            if name == 'alpha':
                self.parameters[index][1] = temp / div
            else:
                self.parameters[index][1] = temp / div - 1
            slider[1].setSliderPosition(100 - temp)
            spin[1].setValue(1 - temp / div)
            spin[0].setValue(temp / div)

    def change_value_spin(self, spin, slider, index, mult=0, name=None):
        mult = 10 ** mult
        if name is not None:
            temp = spin[0].value()
            if name == 'alpha':
                self.parameters[index][1] = temp
            else:
                self.parameters[index][1] = 1 - temp
            slider[0].setSliderPosition(int(temp * mult))
        else:
            self.parameters[index][1] = spin.value()
            if mult == 1:
                slider.setSliderPosition(int(self.parameters[index][1]))
            else:
                slider.setSliderPosition(int(self.parameters[index][1] * mult))

    def change_filter_type(self, filtertype):
        if filtertype == 0:
            self.radio_fir.setChecked(False)
            self.radio_iir.setChecked(True)
        elif filtertype == 1:
            self.radio_iir.setChecked(False)
            self.radio_fir.setChecked(True)
        self.parameters['filtertype'][1] = filtertype

    def send_newparameters(self):
        if self.connected:
            for key in self.parameters:
                if self.parameters[key][1] != self.parameters[key][2]:
                    self.serieport.write(
                        self.data_pack_builder(f'{self.parameters[key][0]} {self.parameters[key][1]}', send_lenght=8))
                    self.parameters[key][2] = self.parameters[key][1]
                    if key == 'filtertype':
                        self.status_handler(f'{key} has been set to {self.parameters[key][3][self.parameters[key][1]]}',
                                            'info', 1)
                    else:
                        self.status_handler(f'{key} has been set to:{self.parameters[key][1]}', 'info', 1)
                    time.sleep(0.1)
        else:
            self.status_handler(f'Not connected <br> Cant change parameters', 'info', 2)

    def data_pack_builder(self, input_string, send_lenght=None, padding_var=0, binary_param=True, debug=False):
        string_list = input_string.split(" ")
        out_list = []
        param_bin_variabel = 0b00000000
        out_list.append(self.commandlist['begin_transmit'])
        for i, command in enumerate(string_list):
            try:
                if command[0:2] == '--':
                    if binary_param:
                        # Setter sammen en bit mask for parameter hvis aktiv
                        param_bin_variabel |= self.bin_param[command]
                    else:
                        out_list.append(self.param_commands[command])
                elif command[0] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '-'):
                    [out_list.append(i) for i in struct.pack('<f', float(command))]
                else:
                    out_list.append(self.commandlist[command])
            except KeyError as e:
                print(e)
                return None

        # Regner ut padding
        if send_lenght is not None:
            padding = (send_lenght) - len(out_list) - 2
            if padding < 0:
                self.ErrorMessage.append('Not a valid command or syntax')
                self.graphicsView.setStyleSheet("QWidget { background-color: %s }" % self.colors['orange'])
                return None
            [out_list.append(padding_var) for _ in range(padding)]

        # appender param byte hvis aktiv
        if binary_param:
            out_list.append(param_bin_variabel)
        out_list.append(self.commandlist['end_transmit'])

        # Returnerer en bytearray som enkelt kan sendes over serial
        if debug:
            print(out_list)
        return bytearray(out_list)

    def line_editor(self):
        self.linetext = self.lineEdit_2.text()

    def keyPressEvent(self, event):
        if self.connected:
            if event.key() in (Qt.Key_Enter, Qt.Key_Return):
                test = self.data_pack_builder(self.linetext, send_lenght=8)
                if test == None:
                    self.ErrorMessage.append('Not a valid input')
                    self.graphicsView.setStyleSheet("QWidget { background-color: %s }" % self.colors['orange'])
                else:
                    self.serieport.write(test)
                self.lineEdit_2.clear()
            elif event.key() == Qt.Key_Up and self.line_hist != []:
                self.lineEdit_2.setText(self.line_hist[self.line_index])
                self.line_index += 1
        else:
            self.ErrorMessage.append(f'Not connected')

    def status_handler(self, payload, errorSeverity: str, preset=None, value=None):
        """ved bruk av preset 4 tar value= en liste med tre verdier [bool,str (True),str (False)"""
        # TODO Print ut payload til en error lable eller lignende, håndterer ikke newlines lengre
        if preset == 1:
            rich_tekst = "<span style=\" color:#2b8a06;\" >"
            rich_tekst += "success"
            rich_tekst += "</span>"
            payload = rich_tekst + ": " + payload
        elif preset == 2:
            rich_tekst = "<span style=\" color:#b53f04;\" >"
            rich_tekst += "warning"
            rich_tekst += "</span>"
            payload = rich_tekst + ": " + payload
        elif preset == 3:
            rich_tekst = "<span style=\" color:#800303;\" >"
            rich_tekst += "warning"
            rich_tekst += "</span>"
            payload = rich_tekst + ": " + payload
        elif preset == 4:  # bools preset, forventer en liste
            if len(value) != 3:
                value = [value[0], 'PÃ¥', 'Av']
            if value[0]:
                rich_tekst = "<span style=\" color:#06868a;\" >"
                rich_tekst += value[1]
                rich_tekst += "</span>"
                payload = rich_tekst + ": " + payload
            else:
                rich_tekst = "<span style=\" color:#8a0641;\" >"
                rich_tekst += value[2]
                rich_tekst += "</span>"
                payload = rich_tekst + ": " + payload
        if errorSeverity == "error":
            color = QtGui.QColor(200, 0, 0)
            self.ErrorMessage.setTextColor(color)
            self.ErrorMessage.append(payload)
        elif errorSeverity == "debug":
            color = QtGui.QColor(0, 200, 0)
            self.ErrorMessage.setTextColor(color)
            self.ErrorMessage.append(payload)
        elif errorSeverity == "info":
            color = QtGui.QColor(255, 255, 255)
            self.ErrorMessage.setTextColor(color)
            self.ErrorMessage.append(payload)
        elif errorSeverity == "":
            self.ErrorMessage.append(payload)

    def save_plot(self):
        if not self.connected:
            plot_path = QFileDialog.getSaveFileName(self, 'Save File', 'logg',
                                                    'csv (*.csv);;pdf (*.pdf);;jpg bilde (*.jpg);;png bilde (*.png);;Bitmap (*.bmp);;txt (*.txt)')
            if '.txt' in plot_path[0] or 'csv' in plot_path[0]:
                copyfile(f'{self.logg_name}.csv', plot_path[0])
            else:
                with open(f'{self.logg_name}.csv') as loggfil:
                    plotdata = pandas.read_csv(loggfil)
                    plotdata['Realtime'] = plotdata['Realtime'].map(date_parser)
                    # Mulig denne også fungerer fint. skal i teorien vært samme funksjonen
                    # plotdata['Realtime'] = plotdata['Realtime'].map(dt.datetime.fromisoformat)
                    fig, ax = plt.subplots()
                    ax.plot_date(plotdata['Realtime'], plotdata['X-Acceleration'])
                    ax.plot_date(plotdata['Realtime'], plotdata['Y-Acceleration'])
                    ax.plot_date(plotdata['Realtime'], plotdata['Z-Acceleration'])
                    ax.plot_date(plotdata['Realtime'], plotdata['Distance_from_object'])
                    fig.savefig(f'{plot_path[0]}')

    def update_config(self):    # Overwrites config file
        if self.palette() == choose_palette('darkmode'):
            self.config_data['color_mode'] = 'darkmode'
        else:
            self.config_data['color_mode'] = 'standard'
        self.config_data['style'] = self.app.style().objectName()
        config_string = f'style: "{self.config_data["style"]}"\n' \
                        f'color_mode: "{self.config_data["color_mode"]}"\n'
        for index in self.parameters:
            config_string += f'{index}: {self.parameters[index][1]}\n'
        with open(f'config.yaml', 'w') as config:
            config.write(config_string)

    def change_defaults(self):
        self.spin_distance.setValue(int(self.parameters['des_distance'][1]))
        self.spin_p.setValue(self.parameters['p_mag'][1])
        self.spin_i.setValue(self.parameters['i_mag'][1])
        self.spin_d.setValue(self.parameters['d_mag'][1])
        self.spin_response.setValue(self.parameters['response'][1])
        self.spin_iir_aks_a.setValue(self.parameters['iir_aks'][1])
        self.spin_iir_a.setValue(self.parameters['iir'][1])
        self.spin_fir.setValue(int(self.parameters['fir'][1]))
        if self.parameters['regulator_type'][1]:
            self.radio_PonM.setChecked(True)
        else:
            self.radio_PonE.setChecked(True)
        self.update_config()

    def send_command(self, command): #Send command to uC
        if self.connected:
            self.serieport.write(self.data_pack_builder(command, send_lenght=8))
        else:
            self.status_handler(f'Not connected <br> Cant send commands', 'info', 2)

    def change_paramters(self, index, value):
        self.parameters[index][1] = value

class Communicate(QtCore.QObject):
    data_signal = QtCore.pyqtSignal(list)


class DataSend:  # Sends new data to plot
    def __init__(self, addData_callbrackFunc=None):
        self.myconnect = Communicate()
        self.myconnect.data_signal.connect(addData_callbrackFunc)
        old_step = 2138213
        timer = 0
        global dataSendLoop_v
        dataSendLoop_v = True
        global data_measurments
        data_measurments = [[10, 20, 30, 40, 50, 60]]
        while dataSendLoop_v:
            time.sleep(0.01)
            timer += 0.01
            if len(data_measurments[0]) > 1:
                if old_step != data_measurments[0][0]:
                    old_step = data_measurments[0][0]
                    self.myconnect.data_signal.emit(
                        [timer, data_measurments[0][1], data_measurments[0][2], data_measurments[0][3],
                         data_measurments[0][4], data_measurments[0][4]])


def choose_palette(choice=None):  # Creates a palette, only darkmode supported for now
    if choice == 'darkmode':
        QPalette = QtGui.QPalette
        QColor = QtGui.QColor
        dark_palette = QPalette()
        dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        # dark_palette.setColor(QPalette.BrightText, Qt.red)
        # dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        return dark_palette
    else:
        QPalette = QtGui.QPalette
        standard_palette = QPalette()
        return standard_palette


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())