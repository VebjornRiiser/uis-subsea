# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nyttvindu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(956, 834)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setFocusPolicy(Qt.TabFocus)
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionSave_plot = QAction(MainWindow)
        self.actionSave_plot.setObjectName(u"actionSave_plot")
        self.actionCom_1 = QAction(MainWindow)
        self.actionCom_1.setObjectName(u"actionCom_1")
        self.actionCom_2 = QAction(MainWindow)
        self.actionCom_2.setObjectName(u"actionCom_2")
        self.actionWindows = QAction(MainWindow)
        self.actionWindows.setObjectName(u"actionWindows")
        self.actionFusion = QAction(MainWindow)
        self.actionFusion.setObjectName(u"actionFusion")
        self.actionWindows_Vista = QAction(MainWindow)
        self.actionWindows_Vista.setObjectName(u"actionWindows_Vista")
        self.actionTrue = QAction(MainWindow)
        self.actionTrue.setObjectName(u"actionTrue")
        self.actionFalse = QAction(MainWindow)
        self.actionFalse.setObjectName(u"actionFalse")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setFocusPolicy(Qt.StrongFocus)
        self.centralwidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setMinimumSize(QSize(220, 749))
        self.groupBox.setMaximumSize(QSize(220, 16777215))
        self.groupBox.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.graphicsView = QGraphicsView(self.groupBox)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QRect(8, 339, 201, 301))
        self.graphicsView.setAutoFillBackground(True)
        brush = QBrush(QColor(85, 0, 255, 255))
        brush.setStyle(Qt.NoBrush)
        self.graphicsView.setBackgroundBrush(brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        self.graphicsView.setForegroundBrush(brush1)
        self.graphicsView.setInteractive(True)
        self.radio_plot = QRadioButton(self.groupBox)
        self.radio_plot.setObjectName(u"radio_plot")
        self.radio_plot.setGeometry(QRect(40, 300, 141, 41))
        font = QFont()
        font.setPointSize(14)
        self.radio_plot.setFont(font)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(20, 110, 181, 61))
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)
        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 100, 201, 81))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(18, 220, 181, 81))
        font1 = QFont()
        font1.setPointSize(20)
        self.lcdNumber.setFont(font1)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(18, 190, 181, 21))
        self.label.setFont(font)
        self.ErrorMessage = QTextEdit(self.groupBox)
        self.ErrorMessage.setObjectName(u"ErrorMessage")
        self.ErrorMessage.setGeometry(QRect(20, 350, 181, 281))
        self.ErrorMessage.setReadOnly(True)
        self.ErrorMessage.setOverwriteMode(False)
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 20, 201, 81))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_5 = QFrame(self.groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 640, 201, 91))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 650, 181, 71))
        self.pushButton_6.setFont(font)
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(20, 30, 181, 61))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setToolTipDuration(-1)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(False)
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.graphicsView.raise_()
        self.radio_plot.raise_()
        self.pushButton.raise_()
        self.lcdNumber.raise_()
        self.label.raise_()
        self.ErrorMessage.raise_()
        self.frame_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_2.raise_()

        self.gridLayout.addWidget(self.groupBox, 1, 1, 2, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tabWidget.setToolTipDuration(5)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setFocusPolicy(Qt.NoFocus)
        self.tab.setContextMenuPolicy(Qt.NoContextMenu)
        self.plot_grid = QGridLayout(self.tab)
        self.plot_grid.setObjectName(u"plot_grid")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.button_parameters = QPushButton(self.tab_2)
        self.button_parameters.setObjectName(u"button_parameters")
        self.button_parameters.setGeometry(QRect(10, 480, 181, 71))
        self.button_parameters.setFont(font)
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 0, 209, 50))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 390, 291, 71))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(11)
        self.label_2.setFont(font2)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.spin_distance = QSpinBox(self.gridLayoutWidget)
        self.spin_distance.setObjectName(u"spin_distance")
        self.spin_distance.setMinimum(20)
        self.spin_distance.setMaximum(150)

        self.gridLayout_2.addWidget(self.spin_distance, 1, 1, 1, 1)

        self.slider_distance = QSlider(self.gridLayoutWidget)
        self.slider_distance.setObjectName(u"slider_distance")
        self.slider_distance.setMinimumSize(QSize(150, 0))
        self.slider_distance.setMinimum(20)
        self.slider_distance.setMaximum(150)
        self.slider_distance.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.slider_distance, 1, 0, 1, 1)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 10, 121, 31))
        self.label_3.setFont(font2)
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(280, 40, 281, 341))
        self.tabWidget_2.setTabPosition(QTabWidget.North)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 10, 271, 161))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.slider_iir_b = QSlider(self.gridLayoutWidget_3)
        self.slider_iir_b.setObjectName(u"slider_iir_b")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slider_iir_b.sizePolicy().hasHeightForWidth())
        self.slider_iir_b.setSizePolicy(sizePolicy2)
        self.slider_iir_b.setMinimumSize(QSize(150, 0))
        self.slider_iir_b.setMaximum(100)
        self.slider_iir_b.setValue(50)
        self.slider_iir_b.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.slider_iir_b, 3, 0, 1, 1)

        self.spin_iir_a = QDoubleSpinBox(self.gridLayoutWidget_3)
        self.spin_iir_a.setObjectName(u"spin_iir_a")
        self.spin_iir_a.setMaximum(1.000000000000000)
        self.spin_iir_a.setSingleStep(0.010000000000000)
        self.spin_iir_a.setValue(0.500000000000000)

        self.gridLayout_4.addWidget(self.spin_iir_a, 1, 1, 1, 1)

        self.slider_iir_a = QSlider(self.gridLayoutWidget_3)
        self.slider_iir_a.setObjectName(u"slider_iir_a")
        sizePolicy2.setHeightForWidth(self.slider_iir_a.sizePolicy().hasHeightForWidth())
        self.slider_iir_a.setSizePolicy(sizePolicy2)
        self.slider_iir_a.setMinimumSize(QSize(150, 0))
        self.slider_iir_a.setMaximum(100)
        self.slider_iir_a.setValue(50)
        self.slider_iir_a.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.slider_iir_a, 1, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.spin_iir_b = QDoubleSpinBox(self.gridLayoutWidget_3)
        self.spin_iir_b.setObjectName(u"spin_iir_b")
        self.spin_iir_b.setDecimals(2)
        self.spin_iir_b.setMaximum(1.000000000000000)
        self.spin_iir_b.setSingleStep(0.010000000000000)
        self.spin_iir_b.setValue(0.500000000000000)

        self.gridLayout_4.addWidget(self.spin_iir_b, 3, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 1)

        self.radio_iir = QRadioButton(self.gridLayoutWidget_3)
        self.radio_iir.setObjectName(u"radio_iir")

        self.gridLayout_4.addWidget(self.radio_iir, 4, 0, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 10, 271, 71))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.gridLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_16, 0, 0, 1, 1)

        self.slider_fir = QSlider(self.gridLayoutWidget_4)
        self.slider_fir.setObjectName(u"slider_fir")
        sizePolicy2.setHeightForWidth(self.slider_fir.sizePolicy().hasHeightForWidth())
        self.slider_fir.setSizePolicy(sizePolicy2)
        self.slider_fir.setMinimumSize(QSize(150, 0))
        self.slider_fir.setMinimum(2)
        self.slider_fir.setMaximum(50)
        self.slider_fir.setOrientation(Qt.Horizontal)

        self.gridLayout_5.addWidget(self.slider_fir, 1, 0, 1, 1)

        self.radio_fir = QRadioButton(self.gridLayoutWidget_4)
        self.radio_fir.setObjectName(u"radio_fir")

        self.gridLayout_5.addWidget(self.radio_fir, 2, 0, 1, 1)

        self.spin_fir = QSpinBox(self.gridLayoutWidget_4)
        self.spin_fir.setObjectName(u"spin_fir")

        self.gridLayout_5.addWidget(self.spin_fir, 1, 1, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_5 = QWidget(self.tab_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 10, 271, 141))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.gridLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_18, 2, 0, 1, 1)

        self.spin_iir_aks_b = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.spin_iir_aks_b.setObjectName(u"spin_iir_aks_b")
        self.spin_iir_aks_b.setMaximum(1.000000000000000)
        self.spin_iir_aks_b.setSingleStep(0.010000000000000)
        self.spin_iir_aks_b.setValue(0.500000000000000)

        self.gridLayout_6.addWidget(self.spin_iir_aks_b, 3, 1, 1, 1)

        self.spin_iir_aks_a = QDoubleSpinBox(self.gridLayoutWidget_5)
        self.spin_iir_aks_a.setObjectName(u"spin_iir_aks_a")
        self.spin_iir_aks_a.setMaximum(1.000000000000000)
        self.spin_iir_aks_a.setSingleStep(0.010000000000000)
        self.spin_iir_aks_a.setValue(0.500000000000000)

        self.gridLayout_6.addWidget(self.spin_iir_aks_a, 1, 1, 1, 1)

        self.slider_iir_aks_b = QSlider(self.gridLayoutWidget_5)
        self.slider_iir_aks_b.setObjectName(u"slider_iir_aks_b")
        sizePolicy2.setHeightForWidth(self.slider_iir_aks_b.sizePolicy().hasHeightForWidth())
        self.slider_iir_aks_b.setSizePolicy(sizePolicy2)
        self.slider_iir_aks_b.setMinimumSize(QSize(150, 0))
        self.slider_iir_aks_b.setMaximum(100)
        self.slider_iir_aks_b.setValue(50)
        self.slider_iir_aks_b.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.slider_iir_aks_b, 3, 0, 1, 1)

        self.slider_iir_aks_a = QSlider(self.gridLayoutWidget_5)
        self.slider_iir_aks_a.setObjectName(u"slider_iir_aks_a")
        sizePolicy2.setHeightForWidth(self.slider_iir_aks_a.sizePolicy().hasHeightForWidth())
        self.slider_iir_aks_a.setSizePolicy(sizePolicy2)
        self.slider_iir_aks_a.setMinimumSize(QSize(150, 0))
        self.slider_iir_aks_a.setMaximum(100)
        self.slider_iir_aks_a.setValue(50)
        self.slider_iir_aks_a.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.slider_iir_aks_a, 1, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 40, 271, 251))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.slider_response = QSlider(self.gridLayoutWidget_2)
        self.slider_response.setObjectName(u"slider_response")
        sizePolicy2.setHeightForWidth(self.slider_response.sizePolicy().hasHeightForWidth())
        self.slider_response.setSizePolicy(sizePolicy2)
        self.slider_response.setMinimumSize(QSize(150, 0))
        self.slider_response.setMaximum(200)
        self.slider_response.setValue(100)
        self.slider_response.setOrientation(Qt.Horizontal)
        self.slider_response.setTickPosition(QSlider.TicksAbove)
        self.slider_response.setTickInterval(100)

        self.gridLayout_3.addWidget(self.slider_response, 1, 0, 1, 1)

        self.spin_response = QDoubleSpinBox(self.gridLayoutWidget_2)
        self.spin_response.setObjectName(u"spin_response")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spin_response.sizePolicy().hasHeightForWidth())
        self.spin_response.setSizePolicy(sizePolicy3)
        self.spin_response.setMaximum(2.000000000000000)
        self.spin_response.setSingleStep(0.050000000000000)
        self.spin_response.setValue(1.000000000000000)

        self.gridLayout_3.addWidget(self.spin_response, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)

        self.slider_i = QSlider(self.gridLayoutWidget_2)
        self.slider_i.setObjectName(u"slider_i")
        self.slider_i.setMinimumSize(QSize(150, 0))
        self.slider_i.setMaximum(10000)
        self.slider_i.setOrientation(Qt.Horizontal)
        self.slider_i.setTickPosition(QSlider.TicksAbove)
        self.slider_i.setTickInterval(10)

        self.gridLayout_3.addWidget(self.slider_i, 5, 0, 1, 1)

        self.slider_p = QSlider(self.gridLayoutWidget_2)
        self.slider_p.setObjectName(u"slider_p")
        self.slider_p.setMinimumSize(QSize(150, 0))
        self.slider_p.setMaximum(10000)
        self.slider_p.setOrientation(Qt.Horizontal)
        self.slider_p.setTickPosition(QSlider.TicksAbove)
        self.slider_p.setTickInterval(10)

        self.gridLayout_3.addWidget(self.slider_p, 3, 0, 1, 1)

        self.spin_p = QDoubleSpinBox(self.gridLayoutWidget_2)
        self.spin_p.setObjectName(u"spin_p")
        self.spin_p.setMaximum(100.000000000000000)
        self.spin_p.setSingleStep(0.010000000000000)

        self.gridLayout_3.addWidget(self.spin_p, 3, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)

        self.spin_i = QDoubleSpinBox(self.gridLayoutWidget_2)
        self.spin_i.setObjectName(u"spin_i")
        self.spin_i.setMaximum(100.000000000000000)
        self.spin_i.setSingleStep(0.010000000000000)

        self.gridLayout_3.addWidget(self.spin_i, 5, 1, 1, 1)

        self.slider_d = QSlider(self.gridLayoutWidget_2)
        self.slider_d.setObjectName(u"slider_d")
        self.slider_d.setMinimumSize(QSize(150, 0))
        self.slider_d.setMaximum(10000)
        self.slider_d.setOrientation(Qt.Horizontal)
        self.slider_d.setTickPosition(QSlider.TicksAbove)
        self.slider_d.setTickInterval(10)

        self.gridLayout_3.addWidget(self.slider_d, 7, 0, 1, 1)

        self.spin_d = QDoubleSpinBox(self.gridLayoutWidget_2)
        self.spin_d.setObjectName(u"spin_d")
        self.spin_d.setMaximum(100.000000000000000)
        self.spin_d.setSingleStep(0.010000000000000)

        self.gridLayout_3.addWidget(self.spin_d, 7, 1, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.radio_PonM = QRadioButton(self.tab_2)
        self.radio_PonM.setObjectName(u"radio_PonM")
        self.radio_PonM.setGeometry(QRect(20, 340, 61, 21))
        self.radio_PonE = QRadioButton(self.tab_2)
        self.radio_PonE.setObjectName(u"radio_PonE")
        self.radio_PonE.setGeometry(QRect(110, 340, 61, 21))
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 310, 171, 25))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.button_save_parameters = QPushButton(self.tab_2)
        self.button_save_parameters.setObjectName(u"button_save_parameters")
        self.button_save_parameters.setGeometry(QRect(210, 480, 181, 71))
        self.button_save_parameters.setFont(font)
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.lineEdit_2.raise_()
        self.groupBox.raise_()
        self.tabWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 956, 21))
        self.menuhallo = QMenu(self.menubar)
        self.menuhallo.setObjectName(u"menuhallo")
        self.menuPort = QMenu(self.menuhallo)
        self.menuPort.setObjectName(u"menuPort")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuStyle = QMenu(self.menuWindow)
        self.menuStyle.setObjectName(u"menuStyle")
        self.menuDarkmode = QMenu(self.menuWindow)
        self.menuDarkmode.setObjectName(u"menuDarkmode")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuhallo.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuhallo.addAction(self.actionSave_plot)
        self.menuhallo.addAction(self.menuPort.menuAction())
        self.menuhallo.addAction(self.actionQuit)
        self.menuWindow.addAction(self.menuStyle.menuAction())
        self.menuWindow.addAction(self.menuDarkmode.menuAction())
        self.menuStyle.addAction(self.actionWindows)
        self.menuStyle.addAction(self.actionWindows_Vista)
        self.menuStyle.addAction(self.actionFusion)
        self.menuDarkmode.addAction(self.actionTrue)
        self.menuDarkmode.addAction(self.actionFalse)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(True)
        self.pushButton_6.setDefault(True)
        self.pushButton_2.setDefault(True)
        self.tabWidget.setCurrentIndex(1)
        self.button_parameters.setDefault(True)
        self.tabWidget_2.setCurrentIndex(0)
        self.button_save_parameters.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ELE 340 SCADA", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionSave_plot.setText(QCoreApplication.translate("MainWindow", u"Save plot as", None))
        self.actionCom_1.setText(QCoreApplication.translate("MainWindow", u"Com 1", None))
        self.actionCom_2.setText(QCoreApplication.translate("MainWindow", u"Com 2", None))
        self.actionWindows.setText(QCoreApplication.translate("MainWindow", u"Windows", None))
        self.actionFusion.setText(QCoreApplication.translate("MainWindow", u"Fusion", None))
        self.actionWindows_Vista.setText(QCoreApplication.translate("MainWindow", u"Windows Vista", None))
        self.actionTrue.setText(QCoreApplication.translate("MainWindow", u"True", None))
        self.actionFalse.setText(QCoreApplication.translate("MainWindow", u"False", None))
#if QT_CONFIG(accessibility)
        self.groupBox.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.groupBox.setTitle("")
        self.radio_plot.setText(QCoreApplication.translate("MainWindow", u"View Graphs", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("MainWindow", u"Start servo regulator", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
#if QT_CONFIG(tooltip)
        self.lcdNumber.setToolTip(QCoreApplication.translate("MainWindow", u"Distance measured from object", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Distance from object", None))
        self.ErrorMessage.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Close and quit program", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"QUIT", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"Connect to uC", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Graph", None))
#if QT_CONFIG(tooltip)
        self.button_parameters.setToolTip(QCoreApplication.translate("MainWindow", u"Sends new parameters to uC", None))
#endif // QT_CONFIG(tooltip)
        self.button_parameters.setText(QCoreApplication.translate("MainWindow", u"Update parameters", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Regulator parameters", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Change distance from object[cm]", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Filter Parameters", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Alpha value", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Beta Value", None))
        self.radio_iir.setText(QCoreApplication.translate("MainWindow", u"Enable IIR Filter", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"IIR filter", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sample size", None))
        self.radio_fir.setText(QCoreApplication.translate("MainWindow", u"Enable FIR filter", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"FIR filter", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Beta Value", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Alpha value", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"IIR Accelerometer", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Response", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"P Magnitude", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"I Magnitude", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"D Magnitude", None))
        self.radio_PonM.setText(QCoreApplication.translate("MainWindow", u"PonM", None))
        self.radio_PonE.setText(QCoreApplication.translate("MainWindow", u"PonE", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Regulator type", None))
#if QT_CONFIG(tooltip)
        self.button_save_parameters.setToolTip(QCoreApplication.translate("MainWindow", u"Store parameters to uC", None))
#endif // QT_CONFIG(tooltip)
        self.button_save_parameters.setText(QCoreApplication.translate("MainWindow", u"Save parameters", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.menuhallo.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuPort.setTitle(QCoreApplication.translate("MainWindow", u"Port", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuStyle.setTitle(QCoreApplication.translate("MainWindow", u"Style", None))
        self.menuDarkmode.setTitle(QCoreApplication.translate("MainWindow", u"Darkmode", None))
    # retranslateUi

