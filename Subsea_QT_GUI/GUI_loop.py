import math
from ast import arguments
import multiprocessing
from typing import Type
import vlc
#from tkinter import Widget
from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtMultimedia
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QCheckBox, QLabel, QFileDialog, QApplication, QWidget, QVBoxLayout, QSizeGrip, QFrame, QMessageBox, QStyleFactory, QSizeGrip, QGraphicsDropShadowEffect, QPushButton, QComboBox, QDesktopWidget
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.Qt import *
from PyQt5.QtGui import QColor, QIcon, QCursor, QFont
from PyQt5.QtCore import Qt, QtMsgType, QTimer, QEvent
from multiprocessing import Pipe, Value
from Threadwatch import Threadwatcher
import sys
import threading
import json
import os
import Subsea_QT_GUI.SUBSEAGUI as SUBSEAGUI
from Subsea_QT_GUI.custom_grips import CustomGrip, Widgets
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
import matplotlib
import time
from Subsea_QT_GUI.py_toggle import PyToggle

# QApplication.setAttribute(Qt.AA_UseDesktopOpenGL)
QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)  # enable highdpi scaling
QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)  # use highdpi icons
#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
#QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%


# GLOBALS:
# ///////////////////////////////////////////////////////////////

GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, port, threadwatcher: Threadwatcher, id, ):
        super().__init__()
        self.threadwatcher = threadwatcher
        self.id = id
        self.label = QLabel("Another Window")
        # self.conn = conn

        self.setWindowTitle(f"{'havbunnskamera' if port-6888 == 0 else 'frontkamera'}")
        self.setWindowIcon(QtGui.QIcon('Subsea_QT_GUI/images/camera.png'))

        self.url = f"http://10.0.0.2:{port}/cam.html"
        # self.url = f"https://nrk.no"
        self.stream1:QWebEngineView = QWebEngineView(self)
        self.stream1.setFixedWidth(1920)
        self.stream1.setFixedHeight(1080)
        self.stream1.load(QtCore.QUrl(self.url))

        def __init__(self, aleft: int, atop: int, awidth: int, aheight: int) -> None: ...
        
        # label_tilt = QLabel(text="test--sa-ds-ad-sad-ad-asd-sa")
        # self.stream1.layout().addWidget(label_tilt)
        # label_tilt.setGeometry(-100,-100,100,20)
        # # label_tilt.raise_()
        # label_tilt.setStyleSheet("QLabel { color: rgba(255, 255, 255, 200); background-color: rgba(179, 32, 36, 200); font-size: 24pt;}")
        # self.layout.addWidget(QLabel(text="test--sa-ds-ad-sad-ad-asd-sa"), alignment=QtCore.Qt.AlignRight)


        if len(QtWidgets.QApplication.screens())>2:
            monitor = QDesktopWidget().screenGeometry(int(f"{port-6887}"))
            self.move(monitor.left(), monitor.top())
            self.showMaximized()
            # self.showFullScreen()
        else:
            self.showMaximized()
            # self.showFullScreen()

PROFILE_UPDATE_ID = 2
COMMAND_TO_ROV_ID = 3


class Window(QMainWindow, SUBSEAGUI.Ui_MainWindow):
    def __init__(self, pipe_conn_only_rcv, queue: multiprocessing.Queue, t_watch: Threadwatcher, id: int, parent=None):
        super().__init__(parent)
        self.lekkasje_varsel_is_running = False

        self.setWindowIcon(QtGui.QIcon('Subsea_QT_GUI/images/logo.png'))
        self.queue = queue
        self.pipe_conn_only_rcv = pipe_conn_only_rcv
        self.t_watch = t_watch
        self.id = id
        self.rov_3d_coordinates = [0, 0, 0]
        self.rotation_counter = 0
        self.last_rotation = [0, 0]

        # Remove frame around window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setup_gui_with_folder_change()

        # Set the stylesheet of the application
        #self.set_style(self, self.auto_btn)
        #self.styleSheet.setStyleSheet(s)


        # STL viewer for ROV 3D model
        self.view_STL()
       
        button = QtGui.QPushButton()
        button.setText('Rotate')
        xyz = [0, 360, 0]
        button.clicked.connect(lambda: self.update(xyz))
        #self.layout.addWidget(button)

        '''
        def set_plotdata(self, name, points, color, width):
                self.traces[name].setData(pos=points, color=color, width=width)
        '''

        # GUI buttons clicked
        
        # KJØREMODUS

        # Toggle buttons 
        # https://www.youtube.com/watch?v=NnJFi285s3M&ab_channel=Wanderson
        self.make_toggle_btns()

        # BILDEBEHANDLING
        #self.beregn_strl_btn(self.beregn_strl)
        #self.fotomoasaikk_btn(self.fotomoasaikk)

        # VIDEO
        #self.start_video_btn(self.start_video)
        #self.stopp_video_btn(self.stop_video)

        # KAMERA
        #self.ta_bilde_frontkamera_btn(self.ta_bilde_frontkamera)
        #self.ta_bilde_havbunn_btn(self.ta_bilde_havbunnskamera)
        #self.slett_bilde_btn(self.slett_siste_bilde)

        # Vis siste bildet:
        #self.show_image
        
        # Menu button clicked
        # self.btn_toggle.clicked.connect(lambda: self.change_current_widget(0))
        self.btn_kontroller.clicked.connect(lambda: self.change_current_widget(2))
        self.btn_informasjon.clicked.connect(lambda: self.change_current_widget(1))

        # Kjøremodus
        self.btn_manuell.clicked.connect(lambda: self.set_bildebehandlingsmodus(0, -1, "Manuell kjøring"))
        self.btn_finn_fisk.clicked.connect(lambda: self.set_bildebehandlingsmodus(1, 0, "Finn fisk"))
        self.btn_autonom_merd.clicked.connect(lambda: self.set_bildebehandlingsmodus(2, 0, "Autonom merd"))
        self.btn_bildemoasaikk.clicked.connect(lambda: self.set_bildebehandlingsmodus(0, 3, "Bildemosaikk"))
        self.btn_autonom_parkering.clicked.connect(lambda: self.set_bildebehandlingsmodus(4, 0, "Autonom parkering"))

        # Reset sikring
        self.btn_reset_sikring_elektronikk.clicked.connect(lambda: self.reset_sikring(0))
        self.btn_reset_sikring_manipulator.clicked.connect(lambda: self.reset_sikring(1))
        self.btn_reset_sikring_thrustere.clicked.connect(lambda: self.reset_sikring(2))

        # Reset nullpunkt
        self.btn_reset_nullpunkt.clicked.connect(self.set_start_point_depth_sensor)

        # Start video
        self.btn_start_video_frontkamera.clicked.connect(lambda: self.video_toggle(self.btn_start_video_frontkamera, 0))
        self.btn_start_video_havbunn.clicked.connect(lambda: self.video_toggle(self.btn_start_video_havbunn, 1))

        # Av/På-effektforbruk
        self.btn_regulator_elektronikk.clicked.connect(lambda: self.toggle_regulator(0, self.btn_regulator_elektronikk))
        self.btn_regulator_manipulator.clicked.connect(lambda: self.toggle_regulator(1, self.btn_regulator_manipulator))
        self.btn_regulator_thrustere.clicked.connect(lambda: self.toggle_regulator(2, self.btn_regulator_thrustere))

        # Ta bilde
        self.btn_ta_bilde_frontkamera.clicked.connect(lambda: self.ta_bilde(0))
        self.btn_ta_bilde_havbunn.clicked.connect(lambda: self.ta_bilde(1))
        
        # self.slider_lys_down.setValue(100)
        # self.slider_lys_forward.setValue(100)

        
        # Struping-slider
        self.slider_struping_thrustere.valueChanged.connect(self.send_thruster_struping)

        self.send_current_ligth_intensity()


        # CONTROLLER PAGE:
        # "Lag ny profil"-button clicked
        self.btn_make_new_profile.clicked.connect(self.make_new_profile)
        #self.make_new_profile_btn.clicked.connect(self.make_new_profile)

        # "Reset"-button clicked
        self.btn_reset.clicked.connect(self.reset_profile)

        # "Lagre"-button clicked
        self.btn_save_profile.clicked.connect(lambda: self.save_profile())
        self.btn_save_profile.setEnabled(False)

        # -----------------------------------
        # LEGGES INN I EN ANNEN FIL:
        #self.init_drop_shadow()

        self.titleRightInfo.mouseDoubleClickEvent = self.dobleClickMaximizeRestore
        self.maximizeRestoreAppBtn.mouseDoubleClickEvent = self.dobleClickMaximizeRestore

        self.titleRightInfo.mouseMoveEvent = self.moveWindow

        # STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)

        # CUSTOM GRIPS
        self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
        self.right_grip = CustomGrip(self, Qt.RightEdge, True)
        self.top_grip = CustomGrip(self, Qt.TopEdge, True)
        self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.minimizeAppBtn.clicked.connect(self.minimize)
        
        # MAXIMIZE/RESTORE
        self.maximizeRestoreAppBtn.clicked.connect(self.maximize_restore)

        # CLOSE APPLICATION
        self.closeAppBtn.clicked.connect(self.shutdown)
        
        self.connect_sliders_to_gui()

        #hest
        self.camera_windows_opened = False
        if self.camera_windows_opened:
            self.start_camera_windows()

        self.recieve = threading.Thread(target=self.recieve_sensordata, daemon=True, args=(self.pipe_conn_only_rcv,))
        self.recieve.start()
        
        # print(f"type of self.widget: {type(self.widget)}")
        # these need to match up with the indexes of the buttons on the controller
        self.btn_combobox_list:list[QComboBox] = [self.comboBox_A_btn, self.comboBox_B_btn, self.comboBox_X_btn, self.comboBox_Y_btn, self.comboBox_RB_btn, self.comboBox_LB_btn, self.comboBox_view_btn, self.comboBox_menu_btn, self.comboBox_left_stick_btn, self.comboBox_right_stick_btn]
        btn_command_list:list[str] = []
        with open("button_config.txt", 'r', encoding="utf-8") as btn_config:
            btn_command_list = [line.strip() for line in btn_config.readlines()]
        for btn in self.btn_combobox_list:
            btn:QComboBox
            btn.clear()  # removes the options already in the combobox
            btn.addItems(btn_command_list) # adds the possible commands
            btn.currentIndexChanged.connect(self.updated_profile_settings)
        self.btn_slett_bilde.clicked.connect(self.make_viewer_opts)


        self.set_default_profile()
        self.send_profile_to_main()

        self.combobox_styling()
        self.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_Y_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_velg_profil.currentIndexChanged.connect(self.load_selected_profile)
        self.toggle_frontlys.setChecked(True)
        self.toggle_havbunnslys.setChecked(True)
        self.send_current_ligth_intensity()
        self.set_bildebehandlingsmodus(-1, -1, "Manuell kjøring")
        # self.setTestValue(self.slider_lys_forward, self.label_percentage_lys_forward, self.frame_lys_forward, "rgba(85, 170, 255, 255)")
        # self.setTestValue(self.slider_lys_down, self.label_percentage_lys_down, self.frame_lys_down, "rgba(85, 170, 255, 255)")
        # self.setTestValue(self.slider_struping_thrustere, self.label_percentage_struping, self.frame_struping, "rgba(85, 170, 255, 255)")
        self.change_current_widget(1)
        self.maximize_restore()
        self.slider_lys_down.valueChanged.connect(self.send_current_ligth_intensity)
        self.slider_lys_forward.valueChanged.connect(self.send_current_ligth_intensity)

    def make_viewer_opts(self):
        print(self.viewer.opts)

    def make_toggle_btns(self):
        self.toggle_mani = PyToggle()
        self.toggle_hiv_regulering = PyToggle()
        self.toggle_stamp_regulering = PyToggle()
        self.toggle_rull_regulering = PyToggle()
        self.toggle_frontlys = PyToggle()
        self.toggle_havbunnslys = PyToggle()
        
        self.toggle_hiv_regulering.stateChanged.connect(lambda: self.update_regulering(3))
        self.toggle_rull_regulering.stateChanged.connect(lambda: self.update_regulering(4))
        self.toggle_stamp_regulering.stateChanged.connect(lambda: self.update_regulering(5))
        self.toggle_hiv_regulering.setChecked(True)
        self.toggle_rull_regulering.setChecked(True)
        self.toggle_stamp_regulering.setChecked(True)

        self.toggle_mani.setText("Manipulator")
        self.toggle_hiv_regulering.setText("Hiv-regulering")
        self.toggle_stamp_regulering.setText("Helning")
        self.toggle_frontlys.setText("Frontlys")
        self.toggle_havbunnslys.setText("Havbunnslys")

        self.toggle_mani.stateChanged.connect(self.toggle_manipulator_enable)
        self.toggle_mani.setChecked(True)

        self.toggle_frontlys.stateChanged.connect(self.send_current_ligth_intensity)
        self.toggle_havbunnslys.stateChanged.connect(self.send_current_ligth_intensity)

        self.toggle_layout.addWidget(self.toggle_mani, alignment=QtCore.Qt.AlignRight)
        self.toggle_layout.addWidget(self.toggle_hiv_regulering, alignment=QtCore.Qt.AlignRight)
        self.toggle_layout.addWidget(self.toggle_stamp_regulering, alignment=QtCore.Qt.AlignRight)
        self.toggle_layout.addWidget(self.toggle_rull_regulering, alignment=QtCore.Qt.AlignRight)
        self.toggle_layout.addWidget(self.toggle_frontlys, alignment=QtCore.Qt.AlignRight)
        self.toggle_layout.addWidget(self.toggle_havbunnslys, alignment=QtCore.Qt.AlignRight)


    # --------------------------------------------------------------------------------------
    def view_STL(self):
        self.viewer = gl.GLViewWidget()
        self.viewer.opts['distance'] = 579
        self.viewer.opts['elevation'] = 47
        self.viewer.opts['azimuth'] = 22
        self.traces = dict()


        gl.shaders.Shaders.append(gl.shaders.ShaderProgram('myShader', [
        gl.shaders.VertexShader("""
                varying vec3 normal;
                void main() {
                    // compute here for use in fragment shader
                    normal = normalize(gl_NormalMatrix * gl_Normal);
                    gl_FrontColor = gl_Color;
                    gl_BackColor = gl_Color;
                    gl_Position = ftransform();
                }
            """),
        gl.shaders.FragmentShader("""
                #ifdef GL_ES
                precision mediump float;
                #endif
                /* Color palette */
                #define BLACK           vec3(0.0, 0.0, 0.0)
                #define WHITE           vec3(1.0, 1.0, 1.0)
                #define RED             vec3(1.0, 0.0, 0.0)
                #define GREEN           vec3(0.0, 1.0, 0.0)
                #define BLUE            vec3(0.0, 0.0, 1.0)
                #define YELLOW          vec3(1.0, 1.0, 0.0)
                #define CYAN            vec3(0.0, 1.0, 1.0)
                #define MAGENTA         vec3(1.0, 0.0, 1.0)
                #define ORANGE          vec3(1.0, 0.5, 0.0)
                #define PURPLE          vec3(1.0, 0.0, 0.5)
                #define LIME            vec3(0.5, 1.0, 0.0)
                #define ACQUA           vec3(0.0, 1.0, 0.5)
                #define VIOLET          vec3(0.5, 0.0, 1.0)
                #define AZUR            vec3(0.0, 0.5, 1.0)
                #define PI 3.14159
                uniform vec2 u_resolution;
                uniform vec2 u_mouse;

                float ylargerthanxsquared(vec2 normalpos) {
                    //should be 1 when y is larger than x^2  
                    return step(pow(normalpos.x, 2.) ,normalpos.y) - 1.*step(2.,pow(normalpos.x,2.));
                    
                }

                void main() {
                    vec2 normal_pixel = ((gl_FragCoord.xy/u_resolution)-0.5);
                    // step(normal_pixel.x,0.)*step(normal_pixel.y,0.);
                    

                    // float stepresult = pow((normal_pixel[0]),2.0);

                    // gl_FragColor = vec4(stepresult),0.0,0.0,1.0);
                    // gl_FragColor = vec4(ylargerthanxsquared(normal_pixel),0.0,0.0,1.0);
                    gl_FragColor = vec4(abs(ylargerthanxsquared(normal_pixel*10.)*step(0.,normal_pixel.y)),0.0,0.0,1.0);
                    }
            """)
        ]))

        cwd = os.getcwd() # Current working directory
        self.stl_mesh = mesh.Mesh.from_file(f'{cwd}/ROV.STL') # Imported STL file
        shape = self.stl_mesh.points.shape
        points = self.stl_mesh.points.reshape(-1, 3)
        faces = np.arange(points.shape[0]).reshape(-1, 3)

        self.meshdata = gl.MeshData(vertexes=points, faces=faces)
        self.meshitem = gl.GLMeshItem(meshdata=self.meshdata, smooth=False, drawFaces=True, shader='viewNormalColor', glOptions='opaque', color=(0,0,0,0), drawEdges=False, edgeColor=(0,0,0,0))
        # self.meshitem = gl.GLMeshItem(meshdata=self.meshdata, smooth=False, drawFaces=True, shader='myShader', glOptions='opaque', color=(0,0,0,0), drawEdges=False, edgeColor=(0,0,0,0))
        self.viewer.addItem(self.meshitem)

        self.meshitem.rotate(0, 0, 0, 0)
        # self.meshitem.translate(0, 100, 100)
        self.layout = self.QVBoxLayout
        self.layout.addWidget(self.viewer, 1)
        self.viewer.setCameraPosition(distance=350)
        self.meshitem.translate(0,0, 60)
        # self.viewer.setCameraPosition(rotation=90)

        g = gl.GLGridItem()
        g.setSize(1000, 1000)
        g.setSpacing(100, 100)
        color = QColor("#ffffff")
        g.setColor(color)
        self.viewer.addItem(g)

        self.rotation = [0, 0, 0]

        self.viewer.show()  
        

    def update_regulering(self, id: int):
        self.send_command_to_rov(["regulering", [id]])

    def video_toggle(self, btn, id: int):
        self.send_command_to_rov(["video_toggle", [btn.isChecked(), id]])

    def send_thruster_struping(self):
        # print(self.viewer.opts)
        self.send_command_to_rov(["thruster_struping", self.slider_struping_thrustere.value()])

    def toggle_regulator(self, nr: int, btn: QPushButton):
        self.send_command_to_rov(["toggle_regulator", nr, not btn.isChecked()])

    def reset_sikring(self, nr: int):
        self.send_command_to_rov(["reset_sikring", nr])

    def toggle_manipulator_enable(self):
        if self.toggle_mani.checkState() != 0:
            self.send_command_to_rov(["manipulator_toggle", None, True])
        else:
            self.send_command_to_rov(["manipulator_toggle", None, False])


    def set_bildebehandlingsmodus(self, modus_kamera_1: int, modus_kamera_2: int, navn: str):
        # print(modus_kamera_1, modus_kamera_2)
        if modus_kamera_1 != -1:
            self.send_command_to_rov(["update_bildebehandling", 0, modus_kamera_1])
        if modus_kamera_2 != -1:
            self.send_command_to_rov(["update_bildebehandling", 1, modus_kamera_2])
        self.label_bildebehandlingsmodus.setText(str(navn))


    # HOME PAGE FUNCTIONS
    def check_btn_state(self, b):
        if b.text() == "Manipulator":
            if b.isChecked() == True:
                print(b.text()+" is selected")
            else:
                print(b.text()+" is deselected")
				
        if b.text() == "Dybde":
            if b.isChecked() == True:
                print(b.text()+" is selected")
            else:
                print(b.text()+" is deselected")

        if b.text() == "Helning":
            if b.isChecked() == True:
                print(b.text()+" is selected")
            else:
                print(b.text()+" is deselected")

        if b.text() == "Lys":
            if b.isChecked() == True:
                print(b.text()+" is selected")
            else:
                print(b.text()+" is deselected")


    def ta_bilde(self, kamera_id):
        self.send_command_to_rov(["take_pic", kamera_id])

    # KJØREMODUS
    def manuell_btn_clicked(self):
        print("manuell btn clicked")
        if self.btn_auto.isChecked():
            # Hvis automatisk kjøring knappen er 'checked', må den endres til 'unchecked'
            # kan ikke ha både manuell og automatisk kjøring samtidig
            pass
    
    def auto_btn_clicked(self):
        self.send_command_to_rov(["update_bildebehandling", [-1, ]])



    # CONTROLLER PAGE FUNCTIONS:


    def set_default_profile(self):
        """Sets the current profile back to the default one"""
        # profiledata = ""
        # with open("Standard profil.userprofile", 'r', encoding="utf-8") as standard_profile:
        #     profiledata = standard_profile.readlines()
        # if len(profiledata) == 0:
        #     raise Exception("Error! could not get default userprofile!")
        #     # [0, 0, 0, 1, 0, 3, 0, 2, 0, 0] default profile
        # options = json.loads(profiledata[0])

        options = self.get_profile_from_file("Standard profil.userprofile")

        for index, combobox in enumerate(self.btn_combobox_list):
            combobox.setCurrentIndex(options[index])
        self.btn_save_profile.setEnabled(False)
        self.set_active_profile_in_combobox("Standard profil")

    def load_selected_profile(self) -> None:
        """loads the settings from the current profile into the gui"""
        name = self.comboBox_velg_profil.currentText()
        print(f"Loading profile '{name}'")
        options = self.get_profile_from_file(f"{name}.userprofile")
        for index, combobox in enumerate(self.btn_combobox_list):
            combobox.setCurrentIndex(options[index])
        self.btn_save_profile.setEnabled(False)
        self.set_active_profile_in_combobox(name)


    def get_profile_from_file(self, filename: str) -> list[int]:
        """Reads the profile data from file and returns it. Filename should include the .userprofile extension"""
        profiledata = ""
        with open(filename, 'r', encoding="utf-8") as profile:
            profiledata = profile.readlines()
        if len(profiledata) == 0:
            raise Exception(f"Error! could not get the userprofile! {filename = } ")
            # [0, 0, 0, 1, 0, 3, 0, 2, 0, 0] default profile
        options = json.loads(profiledata[0])
        return options

    def set_active_profile_in_combobox(self, name):
        self.comboBox_velg_profil.setCurrentIndex(self.comboBox_velg_profil.findText(name))

    def send_command_to_rov(self, command):
        """Sends at command to the rov eg. turn on lights at 60% power"""
        self.send_data_to_main(command, COMMAND_TO_ROV_ID)

    def updated_profile_settings(self):
        self.btn_save_profile.setEnabled(True)
        self.send_profile_to_main()

    def send_profile_to_main(self):
        self.send_data_to_main([btn.currentIndex() for btn in self.btn_combobox_list], PROFILE_UPDATE_ID)    

    def make_new_profile(self):
        """Trykker på "Lag ny profil"
        Skal oppgi navn på profilen og lagre en fil med det som er valgt i comboboxen"""
        print("make new profile called")
        fname = QFileDialog.getSaveFileName(self, 'Open file', 'Custom-profile')
        if fname[0] != "":
            print("inside make new profile. fname "+ fname[0].split("/")[-1])
            self.save_profile(name=fname[0].split("/")[-1])
            self.update_current_profiles()
            self.set_active_profile_in_combobox(fname[0].split('/')[-1])
            self.btn_save_profile.setEnabled(False) # we have now saved so there is no need to save again before changes

        else:
            print(f"Fname[0] is empty: {fname[0]}")

    def reset_profile(self):
        standard_options = self.get_profile_from_file("Standard profil.userprofile")
        with open(self.comboBox_velg_profil.currentText()+".userprofile", 'w') as profile:
            profile.write(json.dumps(standard_options))
        self.load_selected_profile()

    def save_profile(self, name=None):
        """Det er allerede laget en fil.
        (ellers kan det komme opp: "Du har ikke gjort noen endring")
        Skal lagre endringene gjort i comboboxen til denne filen når man trykker på "Lagre"""
        self.comboBox_velg_profil: QComboBox
        print(f"at line 195. {self.comboBox_velg_profil.currentIndex() = }")
        if self.comboBox_velg_profil.currentIndex() == 0 and name is None: # Standard profile so we need to create a new one instead of changing it
            print("save profile calls make new profile")
            self.make_new_profile()
        else:
            print("Saving profile")
            if name is None:
                name = self.comboBox_velg_profil.currentText()
            print(f"{name = }")
            with open(name+".userprofile", 'w', encoding="utf-8") as profile:
                profile.write(json.dumps([btn.currentIndex() for btn in self.btn_combobox_list]))
        self.btn_save_profile.setEnabled(False)



    def browse_files(self):
        pass
        """Skal laste inn ny profil når man velger en egendefinert profil i comboboxen"""
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'Custom-profile')
        if len(fname):
            print(fname)
            with open(fname[0], 'r', encoding="utf-8") as profile:
                profile.readlines()
            self.filename.setText(str(fname)) # for å vise fram filepath
        self.save_profile()
    
    
    def update_current_profiles(self):
        file_list = os.listdir()
        self.comboBox_velg_profil.clear()
        self.comboBox_velg_profil.addItem("Standard profil")
        # print(file_list)
        # QFileDialog.selectedNameFilter()
        self.comboBox_velg_profil.addItems([file.split(".userprofile")[0] for file in file_list if file.endswith(".userprofile")])
        # self.comboBox_velg_profil:QComboBox
        # [self.comboBox_velg_profil.itemText(index))
        # print("updated profiles")

    def messagebox_popup(self):
        # Popup for reset-button
        msg = QMessageBox()
        msg.setWindowTitle("Melding")
        msg.setText("Profilen er satt til standard")
        msg.setIcon(QMessageBox.Warning)
        x = msg.exec_()
        
    def send_data_to_main(self, data, id):
        if self.queue is not None:
            self.queue.put([id, data])
        else:
            raise TypeError("self.queue does not exist inside send_data_to_main")

    def shutdown(self):
        print("shutdown ran")
        self.send_command_to_rov(["STOP"])
        self.t_watch.stop_all_threads()
        if self.camera_windows_opened:
            for window in self.child_window:
                window.close()
        self.close()
        exit(0)
    

    def button_works(self):
        print("function activated")

    def start_camera_windows(self):
        self.child_window: list[AnotherWindow] = []

        id = self.t_watch.add_thread()
        self.child_window.append(AnotherWindow(6888, self.t_watch, id))
        self.child_window[0].show()

        id = self.t_watch.add_thread()
        self.child_window.append(AnotherWindow(6889, self.t_watch, id))
        self.child_window[1].show()
    

    def setup_gui_with_folder_change(self):
        os.chdir("Subsea_QT_GUI")
        self.setupUi(self)
        os.chdir("..")
        self.update_current_profiles()

    #Updates the gui with new sensordata
    def update_gui(self, data):
        print(f"{data}")
        if self.t_watch.should_run(self.id):
            self.dybde.setText(str(round(data["dybde"],4)))
            self.tid.setText(str(data["tid"]))
            self.spenning.setText(str(round(data["spenning"],4)))
            self.label_temp_ROV_hovedkort.setText(str(round(data["temp_rov"],4)))

    def recieve_sensordata(self, conn):
        self.communicate = Communicate()
        self.communicate.data_signal.connect(self.decide_gui_update)
        while self.t_watch.should_run(self.id):
            # print("waiting for sensordata")
            data_is_ready = conn.poll()
            # print(self.viewer.cameraPosition())
            if data_is_ready:
                sensordata: dict = conn.recv()
                self.communicate.data_signal.emit(sensordata)
            else:
                time.sleep(0.15)
        print("recieved close thread. trying to close")
        # self.shutdown()
        exit(0)
        
    def decide_gui_update(self, sensordata):
        self.sensor_update_function = {
        "lekk_temp": self.gui_lekk_temp_update, 
        "thrust" : self.gui_thrust_update,
        "accel": self.gui_acceleration_update,
        "gyro": self.gui_gyro_update,
        "time": self.gui_time_update,
        "manipulator": self.gui_manipulator_update,
        "power_consumption": self.gui_watt_update,
        "manipulator_toggled": self.gui_manipulator_state_update}
        for key in sensordata.keys():
            if key in self.sensor_update_function:
                self.sensor_update_function[key](sensordata[key])

    def gui_manipulator_state_update(self, sensordata):
        self.toggle_mani.setChecked(sensordata[0])

    def gui_watt_update(self, sensordata):
        effekt_liste: list[QLabel] = [self.label_effekt_thrustere, self.label_effekt_manipulator, self.label_effekt_elektronikk]
        color_list = ["rgb(30, 33, 38);"]*3
        if sensordata[0] > 1000:
            color_list[0] = "#ff0000"
        if sensordata[1] > 200:
            color_list[1] = "#ff0000"
        if sensordata[2] > 40:
            color_list[2] = "#ff0000"

        for index, label in enumerate(effekt_liste):
            label.setText(str(round(sensordata[index])) + " W")
            label.setStyleSheet(f"background-color: {color_list[index]}; border-radius: 5px; border: 1px solid rgb(30, 30, 30);")

        # self.label_effekt_manipulator_2.setText(str(round(sensordata[1])) + " W")
        # self.label_effekt_elektronikk_2.setText(str(round(sensordata[2])) +" W")
        
    def gui_time_update(self, sensordata):
        tid = round(sensordata[0])
        hours = tid//3600
        tid -= hours*3600

        minutes = tid//60
        tid -= minutes*60
        seconds = tid

        tid_string = f"{'0'+str(hours) if len(str(hours)) == 1 else str(hours)}:{'0'+str(minutes) if len(str(minutes)) == 1 else str(minutes)}:{'0'+str(seconds) if len(str(seconds)) == 1 else str(seconds)}"

        self.label_tid.setText(tid_string)

    def gui_manipulator_update(self, sensordata):
        self.update_round_percent_visualizer(0, self.label_percentage_mani_1, self.frame_mani_1)
        self.update_round_percent_visualizer(0, self.label_percentage_mani_2, self.frame_mani_2)
        self.update_round_percent_visualizer(0, self.label_percentage_mani_3, self.frame_mani_3)
        if sensordata[3]:
            if sensordata[0] != 0: # åpne/lukke manipulator
                self.update_round_percent_visualizer(sensordata[0], self.label_percentage_mani_1, self.frame_mani_1)
            elif sensordata[2] != 0: # rotere manipulator
                self.update_round_percent_visualizer(sensordata[2], self.label_percentage_mani_2, self.frame_mani_2)
            elif sensordata[1] != 0: # inn ut med manipulator
                self.update_round_percent_visualizer(sensordata[1], self.label_percentage_mani_3, self.frame_mani_3)

    def gui_thrust_update(self, sensordata):
        # print(f"ran gui_thrust_update {sensordata = }")
        for i in range(len(sensordata)):
            if sensordata[i] > 100:
                sensordata[i] = 100
        self.update_round_percent_visualizer(sensordata[0], self.label_percentage_HHF, self.frame_HHF)
        self.update_round_percent_visualizer(sensordata[1], self.label_percentage_HHB, self.frame_HHB)
        self.update_round_percent_visualizer(sensordata[2], self.label_percentage_HVB, self.frame_HVB)
        self.update_round_percent_visualizer(sensordata[3], self.label_percentage_HVF, self.frame_HVF)
        self.update_round_percent_visualizer(sensordata[4], self.label_percentage_VHF, self.frame_VHF)
        self.update_round_percent_visualizer(sensordata[5], self.label_percentage_VHB, self.frame_VHB)
        self.update_round_percent_visualizer(sensordata[6], self.label_percentage_VVB, self.frame_VVB)
        self.update_round_percent_visualizer(sensordata[7], self.label_percentage_VVF, self.frame_VVF)

    def gui_lekk_temp_update(self, sensordata):
        # self.check_data_types(sensordata["lekk_temp"], (int, float, float, float))
        # print(f"ran gui_lekk_temp_update {sensordata = }")
        # print(f"{sensordata =}")
        temp_label_list:list[QLabel] = [self.label_temp_ROV_hovedkort, self.label_temp_ROV_kraftkort,
         self.label_temp_ROV_sensorkort, self.label_gjsnitt_temp_ROV]
        lekkasje_liste: list[bool] = [sensordata[0], sensordata[1], sensordata[2]]
        if not isinstance(lekkasje_liste[0], bool):
            raise TypeError(f"Lekkasje sensor 1 has wrong type. {type(lekkasje_liste[0]) = }, {lekkasje_liste[0]} ")
        average_temp =  round(sum((sensordata[3:6]))/3)
        sensordata.append(average_temp)
        for i in range(4):
            temp_label_list[i].setText(str(sensordata[i+3]))
            if sensordata[i+3] > 65:
                temp_label_list[i].setStyleSheet("background-color: #ff0000; border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
            else:
                temp_label_list[i].setStyleSheet("background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")

        id_with_lekkasje = []
        for lekkasje_nr, is_lekkasje in enumerate(lekkasje_liste):
            if not is_lekkasje:
                id_with_lekkasje.append(lekkasje_nr+1)
        if not self.lekkasje_varsel_is_running and len(id_with_lekkasje)>0:
            self.lekkasje_varsel_is_running = True
            threading.Thread(target=lambda: self.lekkasje_varsel(id_with_lekkasje)).start()
                
                # self.update_round_percent_visualizer(sensordata[0], self.label_percentage_HHB, self.frame_HHB)

    def lekkasje_varsel(self, sensor_nr_liste):
        self.label_lekkasje_varsel.raise_()
        sensor_nr_liste = [str(item) for item in sensor_nr_liste]
        text = f"Advarsel vannlekkasje oppdaget på sensor: {str(', '.join(sensor_nr_liste))}"
        self.label_lekkasje_varsel.setText(text)
        self.label_lekkasje_varsel.setStyleSheet("QLabel { color: rgba(255, 255, 255, 200); background-color: rgba(179, 32, 36, 200); font-size: 24pt;}")
        self.audio = vlc.MediaPlayer("file:///ække normalt.mp3")
        self.audio.play()            
        time.sleep(2)
        self.label_lekkasje_varsel.setStyleSheet("QLabel { color: rgba(255, 255, 255, 0); background-color: rgba(179, 32, 36, 0); font-size: 24pt;}")
        self.label_lekkasje_varsel.lower()
        self.audio = vlc.MediaPlayer("file:///synker.mp3")
        self.audio.play()
        time.sleep(1)
        self.lekkasje_varsel_is_running = False



    def update_round_percent_visualizer(self, value, text_label, round_frame):
        """This function will update the various circles with a progress bar around and percent in the middle"""
        blue = "rgba(85, 170, 255, 255)"
        red = "rgb(226, 47, 53)"
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        color = blue
        if value < 0:
            stop_1 = str(progress - 1)
            stop_2 = str(progress - 0.001 -1)
            color = red
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"
        htmlText = f"""<p align="center"><span style=" font-size:9pt;">{value}
        </span><span style=" font-size:9pt; vertical-align:super;">%</span></p>"""
        text_label.setText(htmlText)
        styleSheet = """QFrame{ border-radius: 30px; background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(77, 77, 127, 100), stop:{STOP_2} {COLOR}); }"""
        styleSheet = styleSheet.replace("{STOP_1}", str(stop_1)).replace("{STOP_2}", str(stop_2)).replace("{COLOR}", color)
        round_frame.setStyleSheet(styleSheet)

    def gui_acceleration_update(self, sensordata):
        pass
        # print(f"gui_acceleration_update {sensordata = }")

    def gui_gyro_update(self, sensordata):
        # Removes the previous rotation. We do not have yaw rotation
        # so it is not necesarry to reset or rotate it
        # print(f"{sensordata = }")
        # hiv, rull, stamp
        # print(f"gyro update inside gui = {sensordata = }")
        self.meshitem.rotate(self.rov_3d_coordinates[1], 1, 0, 0, local=True)
        self.meshitem.rotate(self.rov_3d_coordinates[2], 0, 1, 0, local=True)

        self.meshitem.rotate(-sensordata[2], 0, 1, 0, local=True)
        self.meshitem.rotate(-sensordata[1], 1, 0, 0, local=True)

        # height translation
        height_diff = sensordata[0]-self.rov_3d_coordinates[0]
        self.meshitem.translate(0,0, height_diff)

        self.rov_3d_coordinates = sensordata

        self.label_dybde.setText(str(round(self.rov_3d_coordinates[0]))+ " cm")

    def set_start_point_depth_sensor(self):
        self.send_command_to_rov(["reset_depth", []])
        # self.meshitem.translate()



    def check_data_types(self, values: tuple, data_types: tuple):
        """Takes in n arguments and n data types and checks that they are equal"""

        if len(values) != len(data_types):
            raise ValueError(f"Number of values does not equal number of data_types to match against")
        for index, value in enumerate(values):
            if not isinstance(value, data_types[index]):
                raise TypeError(f"{value = } is not of type {data_types[index]}")

    def send_current_ligth_intensity(self):
        frontlys_on: bool = False
        if self.toggle_frontlys.checkState() != 0:
            frontlys_on = True

        havbunnslys_on: bool = False
        if self.toggle_havbunnslys.checkState() != 0:
            havbunnslys_on = True

        self.send_command_to_rov(["update_light_value", self.slider_lys_forward.value(), frontlys_on, self.slider_lys_down.value(), havbunnslys_on])
        # print(f"sent command to rov. {frontlys_on = }, {havbunnslys_on = }")

    def button_test(self):
        print(f"function was called")
        # print(f"{self.comboBox_velg_profil.findText('Standard profil') = }")

        # self.w1.stream1.load(QtCore.QUrl("http://vg.no"))
        # self.w2.stream1.load(QtCore.QUrl("http://vg.no"))
    
    def change_current_widget(self, index):
        print(f"should change to widget {index}")
        self.stackedWidget.setCurrentIndex(index)
    
    
    # ///////////////////////////////////////////////////////////////
    # Open the qss styles file and read in the css-alike styling code
    '''def set_style(self, widget):
        with open('styles.qss', 'r') as f:
            style = f.read()
            self.widget.setStyleSheet(style)'''

    def combobox_styling(self):
        self.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_Y_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_X_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_A_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_B_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_directional_pad_leftright.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_directional_pad_updown.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_LB_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_left_stick_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_left_stick_x.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_left_stick_y.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_LT_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_menu_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_RB_btn.setStyle(QStyleFactory.create('Windows'))
        self.comboBox_right_stick_btn.setStyle(QStyleFactory.create('Windows'))
        
    def init_drop_shadow(self):
        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.bgApp.setGraphicsEffect(self.shadow)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.appMargins.setContentsMargins(10, 10, 10, 10)

    # Set test values (procent) to progressbar
    def setTestValue(self, slider, labelPercentage, progressBarName, color):
        value = slider.value()
        sliderValue = int(value)
        htmlText = """<p align="center"><span style=" font-size:9pt;">{VALUE}</span><span style=" font-size:9pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))
        self.progressBarValue(sliderValue, progressBarName, color)

    # Set widget percent
    def set_widget_percent(self, labelPercentage, value, progressBarName, color):
        sliderValue = int(value)
        htmlText = """<p align="center"><span style=" font-size:9pt;">{VALUE}</span><span style=" font-size:9pt; vertical-align:super;">%</span></p>"""
        labelPercentage.setText(htmlText.replace("{VALUE}", str(sliderValue)))
        self.progressBarValue(sliderValue, progressBarName, color)

    # ProgressBarValue
    def progressBarValue(self, value, widget, color):
        # Get progress bar value, convert to float and invert values
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0
        if value >= 0:
            styleSheet = """QFrame{ border-radius: 30px; background-color:qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(77, 77, 127, 100), stop:{STOP_2} {COLOR}); }"""
            # Get new values for gradient stop (0 to 100 %)
            stop_1 = str(progress - 0.001)
            stop_2 = str(progress)
        else:
            styleSheet = """QFrame{ border-radius: 30px; background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgb(226, 47, 53)); }"""
            # Get new values for gradient stop (0 to -100 %)
            stop_1 = str(progress - 1)
            stop_2 = str(progress - 0.001 -1)
        # Fix max values
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"
        # Set values to new stylesheet
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)
        # Apply stylesheet with new values
        widget.setStyleSheet(newStylesheet)

    def connect_sliders_to_gui(self):
        self.slider_lys_forward.valueChanged.connect(lambda: self.setTestValue(self.slider_lys_forward, self.label_percentage_lys_forward, self.frame_lys_forward, "rgba(85, 170, 255, 255)"))
        self.slider_lys_down.valueChanged.connect(lambda: self.setTestValue(self.slider_lys_down, self.label_percentage_lys_down, self.frame_lys_down, "rgba(85, 170, 255, 255)"))
        self.slider_struping_thrustere.valueChanged.connect(lambda: self.setTestValue(self.slider_struping_thrustere, self.label_percentage_struping, self.frame_struping, "rgba(85, 170, 255, 255)"))



    # ------------------------------
    # HA I EGEN FIL:

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def resizeEvent(self, event):
        # Update Size Grips
        self.resize_grips()

    def minimize(self):
        print("clicked minimized")
        if sys.platform == "darwin" or sys.platform.startswith("linux"):
            self.setWindowState(self.windowState() | self.showMinimized())
            self.hide()
        elif sys.platform == "win32":
            self.showMinimized()
        
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            if sys.platform == "darwin" or sys.platform.startswith("linux"):
                self.showFullScreen()
            elif sys.platform == "win32":
                self.showMaximized()
            GLOBAL_STATE = True
            self.appMargins.setContentsMargins(0, 0, 0, 0)
            self.maximizeRestoreAppBtn.setToolTip("Restore")
            self.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.appMargins.setContentsMargins(0, 0, 0, 0)
            self.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    def dobleClickMaximizeRestore(self, event):
        # IF DOUBLE CLICK CHANGE STATUS
        if event.type() == QEvent.MouseButtonDblClick:
            QTimer.singleShot(250, lambda: self.maximize_restore())

    def moveWindow(self, event):
        # print("MOVE WINDOW")
        # IF MAXIMIZED CHANGE TO NORMAL
        if self.returnStatus():
            self.maximize_restore()
        # MOVE WINDOW
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def resize_grips(self):
            ENABLE_CUSTOM_TITLE_BAR = True
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # RETURN STATUS
    def returnStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status




def suppress_qt_warnings():
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"

def run(conn, queue_for_rov, t_watch: Threadwatcher, id):
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)


    win = Window(conn, queue_for_rov, t_watch, id)
    win.setWindowTitle("UiS Subsea")

    GLOBAL_STATE = False

    #win.maximize_restore() # for windows
    #win.showFullScreen() # for mac
    #win.showMinimized()

    win.show()
    

    # win.close()
    sys.exit(app.exec())
  
class Communicate(QtCore.QObject):
    data_signal = QtCore.pyqtSignal(dict)

if __name__ == "__main__":
    #import SUBSEAGUI

    run()
    
