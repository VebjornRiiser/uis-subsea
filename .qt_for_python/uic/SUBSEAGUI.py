# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SUBSEAGUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1267, 966)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1250, 930))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"/* STYLE SHEET - DARK THEME */\n"
"\n"
"\n"
"#pagesContainer QFrame[frameStyle='outerCircle'] {\n"
"	border-radius: 30px;\n"
"	background-color: rgba(77, 77, 127, 100); \n"
"}\n"
"\n"
"#pagesContainer QFrame[frameStyle='innerCircle'] {\n"
"	border-radius: 25px;\n"
"	background-color: rgba(77, 77, 127, 255); \n"
"}\n"
"\n"
"\n"
"/* stackedWidget */\n"
"#informasjon, #home, #kontroller { background-color: transparent; }\n"
"\n"
"/* ScrollArea */\n"
"QScrollArea { background: transparent; }\n"
"QScrollArea > QWidget > QWidget { background: transparent; }\n"
"\n"
"QWidget { color: rgb(221, 221, 221); }\n"
"\n"
"QFrame#column1, #column2, #column3 { width: 100%; }\n"
"\n"
"/* Labels */\n"
"QLabel { padding: 1px; }\n"
"\n"
"QLabel[labelStyle='blackBg'] {\n"
"	background-color: rgb(30, 33, 38);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(30, 30, 30);\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QLabel[colorStyle='subTitle'] {\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"	paddin"
                        "g: 10px;\n"
"	margin: 1px;\n"
"}\n"
"\n"
"#pagesContainer QPushButton[btnStyle='redBtn'] {\n"
"	border-color: rgb(80, 36, 37);\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.495, y2:1, stop:0.00492611 rgba(211, 94, 94, 255), stop:1 rgba(96, 14, 14, 255));\n"
"}\n"
"\n"
"#pagesContainer QPushButton[btnStyle='redBtn']:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.495, y2:1, stop:0.00492611 rgba(255, 113, 113, 255), stop:0.995074 rgba(120, 18, 18, 255));\n"
"}\n"
"\n"
"#pagesContainer QPushButton[btnStyle='redBtn']:hover:pressed {\n"
"	background-color: rgb(95, 9, 15); \n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"	background-color:  rgba(45, 51, 63, 255);\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#pagesContainer QPushButton {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5"
                        "px;\n"
"}\n"
"\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));\n"
"}\n"
"\n"
"#pagesContainer QPushButton:hover:pressed {\n"
"	background-color: rgba(45, 51, 63, 255);\n"
"	border-color: rgb(33, 37, 46);\n"
"}\n"
"\n"
"#pagesContainer QPushButton:checked {\n"
"	background-color: rgb(35, 41, 54);\n"
"	border: 1px solid rgb(23, 27, 37);\n"
"}\n"
"\n"
"/* Tooltip */\n"
"QToolTip {\n"
"	padding: 5px;\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 240);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Bg App */\n"
"#bgApp {	\n"
"	background-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"/* Top Menu */\n"
"#topMenu .QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#topMenu .QPushButton:hover {\n"
"	backgrou"
                        "nd-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(74, 82, 91);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(31, 35, 41);\n"
"}\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/*ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"  "
                        "  margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(74, 82, 91);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(74, 82, "
                        "91);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"\n"
"/* ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	width: 5px;\n"
"}\n"
"QComboBox:disabled{\n"
"	background-color: rgb(52, 53, 58);\n"
"	color: rgba(255, 255, 255, 55);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgba(26, 27, 3"
                        "3, 55);\n"
"	padding-left: 10px;\n"
"	width: 5px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(74, 82, 91);	\n"
"	background-color: rgb(50, 50, 50);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 8px;\n"
"    height: 16px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(80, 85, 97);\n"
"}\n"
"QSlider::handle:"
                        "horizontal {\n"
"    background-color: rgb(206, 203, 230);\n"
"    border: none;\n"
"    height: 16px;\n"
"    width: 16px;\n"
"    margin: 0px;\n"
"	border-radius: 8px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(143, 141, 160);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 8px;\n"
"    width: 16px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(80, 85, 97);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(206, 203, 230);\n"
"	border: none;\n"
"    height: 16px;\n"
"    width: 16px;\n"
"    margin: 0px;\n"
"	border-radius: 8px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(143, 141, 160);\n"
"}\n"
"\n"
".QSlider {\n"
"    min-height: 68px;\n"
"    max-h"
                        "eight: 68px;\n"
"}\n"
"/*\n"
".QSlider::groove:horizontal {\n"
"    border: 1px solid #262626;\n"
"    height: 5px;\n"
"    background: #393939;\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:horizontal {\n"
"    background: #22B14C;\n"
"    border: 5px solid #B5E61D;\n"
"    width: 23px;\n"
"    height: 100px;\n"
"    margin: -24px -12px;\n"
"}*/\n"
"")
        self.verticalLayout_14 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFont(font)
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(16777215, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.leftMenuBg.setLineWidth(0)
        self.logo = QLabel(self.leftMenuBg)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(12, 5, 35, 35))
        self.logo.setMinimumSize(QSize(35, 35))
        self.logo.setMaximumSize(QSize(35, 35))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background-color: transparent;")
        self.logo.setPixmap(QPixmap(u":/images/images/nylogo2.png"))
        self.logo.setScaledContents(True)
        self.topMenu = QFrame(self.leftMenuBg)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setGeometry(QRect(0, 44, 60, 138))
        self.topMenu.setMouseTracking(True)
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Plain)
        self.topMenu.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 7, 0)
        self.btn_informasjon = QPushButton(self.topMenu)
        self.btn_informasjon.setObjectName(u"btn_informasjon")
        sizePolicy.setHeightForWidth(self.btn_informasjon.sizePolicy().hasHeightForWidth())
        self.btn_informasjon.setSizePolicy(sizePolicy)
        self.btn_informasjon.setMinimumSize(QSize(60, 30))
        self.btn_informasjon.setMaximumSize(QSize(16777215, 16777215))
        self.btn_informasjon.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_informasjon.setMouseTracking(True)
        self.btn_informasjon.setTabletTracking(False)
        self.btn_informasjon.setToolTipDuration(3)
        self.btn_informasjon.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_informasjon.setIcon(icon)
        self.btn_informasjon.setIconSize(QSize(60, 60))
        self.btn_informasjon.setCheckable(False)
        self.btn_informasjon.setAutoDefault(False)
        self.btn_informasjon.setFlat(False)

        self.verticalLayout_8.addWidget(self.btn_informasjon)

        self.btn_kontroller = QPushButton(self.topMenu)
        self.btn_kontroller.setObjectName(u"btn_kontroller")
        sizePolicy.setHeightForWidth(self.btn_kontroller.sizePolicy().hasHeightForWidth())
        self.btn_kontroller.setSizePolicy(sizePolicy)
        self.btn_kontroller.setMinimumSize(QSize(60, 30))
        self.btn_kontroller.setMaximumSize(QSize(16777215, 16777215))
        self.btn_kontroller.setFont(font1)
        self.btn_kontroller.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_kontroller.setLayoutDirection(Qt.LeftToRight)
        self.btn_kontroller.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-gamepad.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_kontroller.setIcon(icon1)
        self.btn_kontroller.setIconSize(QSize(60, 60))
#if QT_CONFIG(shortcut)
        self.btn_kontroller.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.btn_kontroller.setCheckable(False)
        self.btn_kontroller.setAutoDefault(False)
        self.btn_kontroller.setFlat(False)

        self.verticalLayout_8.addWidget(self.btn_kontroller)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 40))
        self.contentTopBg.setMaximumSize(QSize(16777215, 40))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.leftBox.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 40))
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setStyleSheet(u"")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.zoomBtns = QFrame(self.rightButtons)
        self.zoomBtns.setObjectName(u"zoomBtns")
        self.zoomBtns.setMinimumSize(QSize(50, 0))
        self.zoomBtns.setFrameShape(QFrame.NoFrame)
        self.zoomBtns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.zoomBtns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_zoom_in = QPushButton(self.zoomBtns)
        self.btn_zoom_in.setObjectName(u"btn_zoom_in")
        self.btn_zoom_in.setMinimumSize(QSize(28, 28))
        self.btn_zoom_in.setMaximumSize(QSize(50, 50))
        self.btn_zoom_in.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-zoom-in.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_zoom_in.setIcon(icon2)
        self.btn_zoom_in.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.btn_zoom_in)

        self.btn_zoom_out = QPushButton(self.zoomBtns)
        self.btn_zoom_out.setObjectName(u"btn_zoom_out")
        self.btn_zoom_out.setMinimumSize(QSize(28, 28))
        self.btn_zoom_out.setMaximumSize(QSize(50, 50))
        self.btn_zoom_out.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-zoom-out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_zoom_out.setIcon(icon3)
        self.btn_zoom_out.setIconSize(QSize(20, 20))

        self.horizontalLayout_10.addWidget(self.btn_zoom_out)

        self.btn_change_theme = QPushButton(self.zoomBtns)
        self.btn_change_theme.setObjectName(u"btn_change_theme")
        self.btn_change_theme.setMinimumSize(QSize(28, 28))
        self.btn_change_theme.setMaximumSize(QSize(50, 50))
        self.btn_change_theme.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-lightbulb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_change_theme.setIcon(icon4)
        self.btn_change_theme.setIconSize(QSize(20, 20))
        self.btn_change_theme.setCheckable(True)
        self.btn_change_theme.setChecked(False)

        self.horizontalLayout_10.addWidget(self.btn_change_theme)


        self.horizontalLayout_2.addWidget(self.zoomBtns)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon5)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon6)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon7)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setStyleSheet(u"")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pagesContainer.sizePolicy().hasHeightForWidth())
        self.pagesContainer.setSizePolicy(sizePolicy3)
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setAutoFillBackground(False)
        self.horizontalLayout_17 = QHBoxLayout(self.home)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stackedWidget.addWidget(self.home)
        self.informasjon = QWidget()
        self.informasjon.setObjectName(u"informasjon")
        self.informasjon.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.informasjon)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.row = QFrame(self.informasjon)
        self.row.setObjectName(u"row")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.row.sizePolicy().hasHeightForWidth())
        self.row.setSizePolicy(sizePolicy4)
        self.row.setMinimumSize(QSize(0, 0))
        self.row.setStyleSheet(u"")
        self.row.setFrameShape(QFrame.NoFrame)
        self.row.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.row)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.column1 = QFrame(self.row)
        self.column1.setObjectName(u"column1")
        sizePolicy.setHeightForWidth(self.column1.sizePolicy().hasHeightForWidth())
        self.column1.setSizePolicy(sizePolicy)
        self.column1.setMinimumSize(QSize(0, 0))
        self.column1.setMaximumSize(QSize(16777215, 16777215))
        self.column1.setSizeIncrement(QSize(0, 0))
        self.column1.setBaseSize(QSize(0, 0))
        self.column1.setFont(font)
        self.column1.setStyleSheet(u"")
        self.column1Layout = QVBoxLayout(self.column1)
        self.column1Layout.setSpacing(5)
        self.column1Layout.setObjectName(u"column1Layout")
        self.column1Layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.column1Layout.setContentsMargins(-1, -1, 12, -1)
        self.frame = QFrame(self.column1)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.kjoremodusLayout = QVBoxLayout(self.frame)
        self.kjoremodusLayout.setSpacing(5)
        self.kjoremodusLayout.setObjectName(u"kjoremodusLayout")
        self.kjoremodusLayout.setContentsMargins(0, 0, 0, 0)
        self.title_kjoremodus = QLabel(self.frame)
        self.title_kjoremodus.setObjectName(u"title_kjoremodus")
        self.title_kjoremodus.setMinimumSize(QSize(0, 0))
        self.title_kjoremodus.setMaximumSize(QSize(16777215, 16777215))
        self.title_kjoremodus.setFont(font1)
        self.title_kjoremodus.setStyleSheet(u"")

        self.kjoremodusLayout.addWidget(self.title_kjoremodus)

        self.text_kjoring = QLabel(self.frame)
        self.text_kjoring.setObjectName(u"text_kjoring")
        self.text_kjoring.setMinimumSize(QSize(0, 0))
        self.text_kjoring.setMaximumSize(QSize(16777215, 16777215))
        self.text_kjoring.setFont(font)
        self.text_kjoring.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_kjoring.setLineWidth(1)
        self.text_kjoring.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.kjoremodusLayout.addWidget(self.text_kjoring)

        self.btn_manuell = QPushButton(self.frame)
        self.btn_manuell.setObjectName(u"btn_manuell")
        sizePolicy.setHeightForWidth(self.btn_manuell.sizePolicy().hasHeightForWidth())
        self.btn_manuell.setSizePolicy(sizePolicy)
        self.btn_manuell.setMinimumSize(QSize(0, 0))
        self.btn_manuell.setMaximumSize(QSize(16777215, 16777215))
        self.btn_manuell.setFont(font1)
        self.btn_manuell.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manuell.setCheckable(False)
        self.btn_manuell.setChecked(False)
        self.btn_manuell.setAutoRepeat(False)

        self.kjoremodusLayout.addWidget(self.btn_manuell)

        self.btn_finn_fisk = QPushButton(self.frame)
        self.btn_finn_fisk.setObjectName(u"btn_finn_fisk")
        sizePolicy.setHeightForWidth(self.btn_finn_fisk.sizePolicy().hasHeightForWidth())
        self.btn_finn_fisk.setSizePolicy(sizePolicy)
        self.btn_finn_fisk.setMinimumSize(QSize(0, 0))
        self.btn_finn_fisk.setFont(font1)
        self.btn_finn_fisk.setCursor(QCursor(Qt.PointingHandCursor))

        self.kjoremodusLayout.addWidget(self.btn_finn_fisk)

        self.btn_autonom_merd = QPushButton(self.frame)
        self.btn_autonom_merd.setObjectName(u"btn_autonom_merd")
        sizePolicy.setHeightForWidth(self.btn_autonom_merd.sizePolicy().hasHeightForWidth())
        self.btn_autonom_merd.setSizePolicy(sizePolicy)
        self.btn_autonom_merd.setMinimumSize(QSize(200, 0))
        self.btn_autonom_merd.setFont(font1)
        self.btn_autonom_merd.setCursor(QCursor(Qt.PointingHandCursor))

        self.kjoremodusLayout.addWidget(self.btn_autonom_merd)

        self.btn_bildemoasaikk = QPushButton(self.frame)
        self.btn_bildemoasaikk.setObjectName(u"btn_bildemoasaikk")
        sizePolicy.setHeightForWidth(self.btn_bildemoasaikk.sizePolicy().hasHeightForWidth())
        self.btn_bildemoasaikk.setSizePolicy(sizePolicy)
        self.btn_bildemoasaikk.setMinimumSize(QSize(0, 0))
        self.btn_bildemoasaikk.setFont(font1)
        self.btn_bildemoasaikk.setCursor(QCursor(Qt.PointingHandCursor))

        self.kjoremodusLayout.addWidget(self.btn_bildemoasaikk)

        self.btn_autonom_parkering = QPushButton(self.frame)
        self.btn_autonom_parkering.setObjectName(u"btn_autonom_parkering")
        sizePolicy.setHeightForWidth(self.btn_autonom_parkering.sizePolicy().hasHeightForWidth())
        self.btn_autonom_parkering.setSizePolicy(sizePolicy)
        self.btn_autonom_parkering.setMinimumSize(QSize(0, 0))
        self.btn_autonom_parkering.setFont(font1)
        self.btn_autonom_parkering.setCursor(QCursor(Qt.PointingHandCursor))

        self.kjoremodusLayout.addWidget(self.btn_autonom_parkering)

        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        self.bildebehandlingLayout = QHBoxLayout(self.frame1)
        self.bildebehandlingLayout.setObjectName(u"bildebehandlingLayout")
        self.text_bildebehandlingsmodus = QLabel(self.frame1)
        self.text_bildebehandlingsmodus.setObjectName(u"text_bildebehandlingsmodus")
        self.text_bildebehandlingsmodus.setMinimumSize(QSize(0, 0))
        self.text_bildebehandlingsmodus.setMaximumSize(QSize(16777215, 16777215))
        self.text_bildebehandlingsmodus.setFont(font1)
        self.text_bildebehandlingsmodus.setStyleSheet(u"")

        self.bildebehandlingLayout.addWidget(self.text_bildebehandlingsmodus)

        self.label_bildebehandlingsmodus = QLabel(self.frame1)
        self.label_bildebehandlingsmodus.setObjectName(u"label_bildebehandlingsmodus")
        self.label_bildebehandlingsmodus.setMinimumSize(QSize(0, 0))
        self.label_bildebehandlingsmodus.setMaximumSize(QSize(16777215, 16777215))
        self.label_bildebehandlingsmodus.setFont(font1)
        self.label_bildebehandlingsmodus.setFrameShape(QFrame.NoFrame)
        self.label_bildebehandlingsmodus.setLineWidth(0)
        self.label_bildebehandlingsmodus.setMidLineWidth(0)
        self.label_bildebehandlingsmodus.setAlignment(Qt.AlignCenter)
        self.label_bildebehandlingsmodus.setMargin(0)

        self.bildebehandlingLayout.addWidget(self.label_bildebehandlingsmodus)


        self.kjoremodusLayout.addWidget(self.frame1)


        self.column1Layout.addWidget(self.frame)

        self.rovFrame = QFrame(self.column1)
        self.rovFrame.setObjectName(u"rovFrame")
        self.rovFrame.setMinimumSize(QSize(0, 0))
        self.rovFrame.setMaximumSize(QSize(16777215, 16777215))
        self.rovLayout = QHBoxLayout(self.rovFrame)
        self.rovLayout.setObjectName(u"rovLayout")
        self.ROVinfoFrame = QFrame(self.rovFrame)
        self.ROVinfoFrame.setObjectName(u"ROVinfoFrame")
        self.ROVinfoFrame.setMinimumSize(QSize(0, 0))
        self.ROVinfoFrame.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.ROVinfoFrame)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_effekt_manipulator = QLabel(self.ROVinfoFrame)
        self.label_effekt_manipulator.setObjectName(u"label_effekt_manipulator")
        self.label_effekt_manipulator.setMinimumSize(QSize(0, 0))
        self.label_effekt_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.label_effekt_manipulator.setFont(font1)
        self.label_effekt_manipulator.setFrameShape(QFrame.NoFrame)
        self.label_effekt_manipulator.setLineWidth(0)
        self.label_effekt_manipulator.setMidLineWidth(0)
        self.label_effekt_manipulator.setAlignment(Qt.AlignCenter)
        self.label_effekt_manipulator.setMargin(0)

        self.gridLayout_3.addWidget(self.label_effekt_manipulator, 6, 2, 1, 1)

        self.text_gjsnitttemp = QLabel(self.ROVinfoFrame)
        self.text_gjsnitttemp.setObjectName(u"text_gjsnitttemp")
        self.text_gjsnitttemp.setMinimumSize(QSize(0, 0))
        self.text_gjsnitttemp.setMaximumSize(QSize(16777215, 16777215))
        self.text_gjsnitttemp.setFont(font1)
        self.text_gjsnitttemp.setTextFormat(Qt.PlainText)
        self.text_gjsnitttemp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.text_gjsnitttemp, 10, 5, 1, 1)

        self.btn_regulator_elektronikk = QPushButton(self.ROVinfoFrame)
        self.btn_regulator_elektronikk.setObjectName(u"btn_regulator_elektronikk")
        sizePolicy.setHeightForWidth(self.btn_regulator_elektronikk.sizePolicy().hasHeightForWidth())
        self.btn_regulator_elektronikk.setSizePolicy(sizePolicy)
        self.btn_regulator_elektronikk.setMinimumSize(QSize(0, 0))
        self.btn_regulator_elektronikk.setMaximumSize(QSize(16777215, 16777215))
        self.btn_regulator_elektronikk.setFont(font1)
        self.btn_regulator_elektronikk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_regulator_elektronikk.setCheckable(True)
        self.btn_regulator_elektronikk.setChecked(False)
        self.btn_regulator_elektronikk.setAutoRepeat(False)
        self.btn_regulator_elektronikk.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_regulator_elektronikk, 4, 4, 1, 1)

        self.btn_regulator_manipulator = QPushButton(self.ROVinfoFrame)
        self.btn_regulator_manipulator.setObjectName(u"btn_regulator_manipulator")
        sizePolicy.setHeightForWidth(self.btn_regulator_manipulator.sizePolicy().hasHeightForWidth())
        self.btn_regulator_manipulator.setSizePolicy(sizePolicy)
        self.btn_regulator_manipulator.setMinimumSize(QSize(0, 0))
        self.btn_regulator_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.btn_regulator_manipulator.setFont(font1)
        self.btn_regulator_manipulator.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_regulator_manipulator.setCheckable(True)
        self.btn_regulator_manipulator.setChecked(False)
        self.btn_regulator_manipulator.setAutoRepeat(False)
        self.btn_regulator_manipulator.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_regulator_manipulator, 6, 4, 1, 1)

        self.btn_reset_sikring_manipulator = QPushButton(self.ROVinfoFrame)
        self.btn_reset_sikring_manipulator.setObjectName(u"btn_reset_sikring_manipulator")
        sizePolicy.setHeightForWidth(self.btn_reset_sikring_manipulator.sizePolicy().hasHeightForWidth())
        self.btn_reset_sikring_manipulator.setSizePolicy(sizePolicy)
        self.btn_reset_sikring_manipulator.setMinimumSize(QSize(0, 0))
        self.btn_reset_sikring_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_sikring_manipulator.setFont(font1)
        self.btn_reset_sikring_manipulator.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_sikring_manipulator.setCheckable(False)
        self.btn_reset_sikring_manipulator.setChecked(False)
        self.btn_reset_sikring_manipulator.setAutoRepeat(False)
        self.btn_reset_sikring_manipulator.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_reset_sikring_manipulator, 6, 5, 1, 1)

        self.text_effekt_thrustere = QLabel(self.ROVinfoFrame)
        self.text_effekt_thrustere.setObjectName(u"text_effekt_thrustere")
        self.text_effekt_thrustere.setMinimumSize(QSize(0, 0))
        self.text_effekt_thrustere.setMaximumSize(QSize(16777215, 16777215))
        self.text_effekt_thrustere.setFont(font1)
        self.text_effekt_thrustere.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.text_effekt_thrustere, 5, 0, 1, 1)

        self.btn_regulator_thrustere = QPushButton(self.ROVinfoFrame)
        self.btn_regulator_thrustere.setObjectName(u"btn_regulator_thrustere")
        sizePolicy.setHeightForWidth(self.btn_regulator_thrustere.sizePolicy().hasHeightForWidth())
        self.btn_regulator_thrustere.setSizePolicy(sizePolicy)
        self.btn_regulator_thrustere.setMinimumSize(QSize(0, 0))
        self.btn_regulator_thrustere.setMaximumSize(QSize(16777215, 16777215))
        self.btn_regulator_thrustere.setFont(font1)
        self.btn_regulator_thrustere.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_regulator_thrustere.setCheckable(True)
        self.btn_regulator_thrustere.setChecked(False)
        self.btn_regulator_thrustere.setAutoRepeat(False)
        self.btn_regulator_thrustere.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_regulator_thrustere, 5, 4, 1, 1)

        self.title_effektforbruk = QLabel(self.ROVinfoFrame)
        self.title_effektforbruk.setObjectName(u"title_effektforbruk")
        self.title_effektforbruk.setMinimumSize(QSize(0, 0))
        self.title_effektforbruk.setMaximumSize(QSize(16777215, 16777215))
        self.title_effektforbruk.setFont(font1)
        self.title_effektforbruk.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.title_effektforbruk, 3, 0, 1, 3)

        self.label_effekt_elektronikk = QLabel(self.ROVinfoFrame)
        self.label_effekt_elektronikk.setObjectName(u"label_effekt_elektronikk")
        self.label_effekt_elektronikk.setMinimumSize(QSize(0, 0))
        self.label_effekt_elektronikk.setMaximumSize(QSize(16777215, 16777215))
        self.label_effekt_elektronikk.setFont(font1)
        self.label_effekt_elektronikk.setFrameShape(QFrame.NoFrame)
        self.label_effekt_elektronikk.setLineWidth(0)
        self.label_effekt_elektronikk.setMidLineWidth(0)
        self.label_effekt_elektronikk.setAlignment(Qt.AlignCenter)
        self.label_effekt_elektronikk.setMargin(0)

        self.gridLayout_3.addWidget(self.label_effekt_elektronikk, 4, 2, 1, 1)

        self.text_dybde = QLabel(self.ROVinfoFrame)
        self.text_dybde.setObjectName(u"text_dybde")
        self.text_dybde.setMinimumSize(QSize(0, 0))
        self.text_dybde.setMaximumSize(QSize(16777215, 16777215))
        self.text_dybde.setFont(font1)
        self.text_dybde.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_dybde, 2, 0, 1, 1)

        self.text_effekt_manipulator = QLabel(self.ROVinfoFrame)
        self.text_effekt_manipulator.setObjectName(u"text_effekt_manipulator")
        self.text_effekt_manipulator.setMinimumSize(QSize(0, 0))
        self.text_effekt_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.text_effekt_manipulator.setFont(font1)
        self.text_effekt_manipulator.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_effekt_manipulator, 6, 0, 1, 1)

        self.btn_reset_sikring_thrustere = QPushButton(self.ROVinfoFrame)
        self.btn_reset_sikring_thrustere.setObjectName(u"btn_reset_sikring_thrustere")
        sizePolicy.setHeightForWidth(self.btn_reset_sikring_thrustere.sizePolicy().hasHeightForWidth())
        self.btn_reset_sikring_thrustere.setSizePolicy(sizePolicy)
        self.btn_reset_sikring_thrustere.setMinimumSize(QSize(0, 0))
        self.btn_reset_sikring_thrustere.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_sikring_thrustere.setFont(font1)
        self.btn_reset_sikring_thrustere.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_sikring_thrustere.setCheckable(False)
        self.btn_reset_sikring_thrustere.setChecked(False)
        self.btn_reset_sikring_thrustere.setAutoRepeat(False)
        self.btn_reset_sikring_thrustere.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_reset_sikring_thrustere, 5, 5, 1, 1)

        self.btn_reset_sikring_elektronikk = QPushButton(self.ROVinfoFrame)
        self.btn_reset_sikring_elektronikk.setObjectName(u"btn_reset_sikring_elektronikk")
        sizePolicy.setHeightForWidth(self.btn_reset_sikring_elektronikk.sizePolicy().hasHeightForWidth())
        self.btn_reset_sikring_elektronikk.setSizePolicy(sizePolicy)
        self.btn_reset_sikring_elektronikk.setMinimumSize(QSize(0, 0))
        self.btn_reset_sikring_elektronikk.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_sikring_elektronikk.setFont(font1)
        self.btn_reset_sikring_elektronikk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_sikring_elektronikk.setCheckable(False)
        self.btn_reset_sikring_elektronikk.setChecked(False)
        self.btn_reset_sikring_elektronikk.setAutoRepeat(False)
        self.btn_reset_sikring_elektronikk.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_reset_sikring_elektronikk, 4, 5, 1, 1)

        self.text_tidtaker = QLabel(self.ROVinfoFrame)
        self.text_tidtaker.setObjectName(u"text_tidtaker")
        self.text_tidtaker.setMinimumSize(QSize(0, 0))
        self.text_tidtaker.setFont(font1)
        self.text_tidtaker.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_tidtaker, 1, 0, 1, 1)

        self.label_temp_ROV_hovedkort = QLabel(self.ROVinfoFrame)
        self.label_temp_ROV_hovedkort.setObjectName(u"label_temp_ROV_hovedkort")
        self.label_temp_ROV_hovedkort.setMinimumSize(QSize(0, 0))
        self.label_temp_ROV_hovedkort.setMaximumSize(QSize(16777215, 16777215))
        self.label_temp_ROV_hovedkort.setFont(font1)
        self.label_temp_ROV_hovedkort.setFrameShape(QFrame.NoFrame)
        self.label_temp_ROV_hovedkort.setLineWidth(0)
        self.label_temp_ROV_hovedkort.setMidLineWidth(0)
        self.label_temp_ROV_hovedkort.setAlignment(Qt.AlignCenter)
        self.label_temp_ROV_hovedkort.setMargin(0)

        self.gridLayout_3.addWidget(self.label_temp_ROV_hovedkort, 9, 2, 1, 1)

        self.label_dybde = QLabel(self.ROVinfoFrame)
        self.label_dybde.setObjectName(u"label_dybde")
        self.label_dybde.setMinimumSize(QSize(0, 0))
        self.label_dybde.setMaximumSize(QSize(16777215, 16777215))
        self.label_dybde.setFont(font1)
        self.label_dybde.setFrameShape(QFrame.NoFrame)
        self.label_dybde.setLineWidth(0)
        self.label_dybde.setMidLineWidth(0)
        self.label_dybde.setAlignment(Qt.AlignCenter)
        self.label_dybde.setMargin(0)

        self.gridLayout_3.addWidget(self.label_dybde, 2, 2, 1, 1)

        self.label_temp_ROV_kraftkort = QLabel(self.ROVinfoFrame)
        self.label_temp_ROV_kraftkort.setObjectName(u"label_temp_ROV_kraftkort")
        self.label_temp_ROV_kraftkort.setMinimumSize(QSize(0, 0))
        self.label_temp_ROV_kraftkort.setMaximumSize(QSize(16777215, 16777215))
        self.label_temp_ROV_kraftkort.setFont(font1)
        self.label_temp_ROV_kraftkort.setFrameShape(QFrame.NoFrame)
        self.label_temp_ROV_kraftkort.setLineWidth(0)
        self.label_temp_ROV_kraftkort.setMidLineWidth(0)
        self.label_temp_ROV_kraftkort.setAlignment(Qt.AlignCenter)
        self.label_temp_ROV_kraftkort.setMargin(0)

        self.gridLayout_3.addWidget(self.label_temp_ROV_kraftkort, 10, 2, 1, 1)

        self.label_gjsnitt_temp_ROV = QLabel(self.ROVinfoFrame)
        self.label_gjsnitt_temp_ROV.setObjectName(u"label_gjsnitt_temp_ROV")
        self.label_gjsnitt_temp_ROV.setMinimumSize(QSize(0, 0))
        self.label_gjsnitt_temp_ROV.setMaximumSize(QSize(16777215, 16777215))
        self.label_gjsnitt_temp_ROV.setFont(font1)
        self.label_gjsnitt_temp_ROV.setFrameShape(QFrame.NoFrame)
        self.label_gjsnitt_temp_ROV.setLineWidth(0)
        self.label_gjsnitt_temp_ROV.setMidLineWidth(0)
        self.label_gjsnitt_temp_ROV.setAlignment(Qt.AlignCenter)
        self.label_gjsnitt_temp_ROV.setMargin(0)

        self.gridLayout_3.addWidget(self.label_gjsnitt_temp_ROV, 11, 5, 1, 1)

        self.label_temp_ROV_sensorkort = QLabel(self.ROVinfoFrame)
        self.label_temp_ROV_sensorkort.setObjectName(u"label_temp_ROV_sensorkort")
        self.label_temp_ROV_sensorkort.setMinimumSize(QSize(0, 0))
        self.label_temp_ROV_sensorkort.setMaximumSize(QSize(16777215, 16777215))
        self.label_temp_ROV_sensorkort.setFont(font1)
        self.label_temp_ROV_sensorkort.setFrameShape(QFrame.NoFrame)
        self.label_temp_ROV_sensorkort.setLineWidth(0)
        self.label_temp_ROV_sensorkort.setMidLineWidth(0)
        self.label_temp_ROV_sensorkort.setAlignment(Qt.AlignCenter)
        self.label_temp_ROV_sensorkort.setMargin(0)

        self.gridLayout_3.addWidget(self.label_temp_ROV_sensorkort, 11, 2, 1, 1)

        self.text_hovedkort = QLabel(self.ROVinfoFrame)
        self.text_hovedkort.setObjectName(u"text_hovedkort")
        self.text_hovedkort.setMinimumSize(QSize(0, 0))
        self.text_hovedkort.setMaximumSize(QSize(16777215, 16777215))
        self.text_hovedkort.setFont(font1)
        self.text_hovedkort.setTextFormat(Qt.PlainText)
        self.text_hovedkort.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.text_hovedkort, 9, 0, 1, 1)

        self.title_temp_ROV = QLabel(self.ROVinfoFrame)
        self.title_temp_ROV.setObjectName(u"title_temp_ROV")
        self.title_temp_ROV.setMaximumSize(QSize(16777215, 16777215))
        self.title_temp_ROV.setFont(font1)
        self.title_temp_ROV.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.title_temp_ROV, 8, 0, 1, 1)

        self.text_effekt_elektronikk = QLabel(self.ROVinfoFrame)
        self.text_effekt_elektronikk.setObjectName(u"text_effekt_elektronikk")
        self.text_effekt_elektronikk.setMinimumSize(QSize(0, 0))
        self.text_effekt_elektronikk.setMaximumSize(QSize(16777215, 16777215))
        self.text_effekt_elektronikk.setFont(font1)
        self.text_effekt_elektronikk.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_effekt_elektronikk, 4, 0, 1, 1)

        self.text_kraftkort = QLabel(self.ROVinfoFrame)
        self.text_kraftkort.setObjectName(u"text_kraftkort")
        self.text_kraftkort.setMinimumSize(QSize(0, 0))
        self.text_kraftkort.setFont(font1)
        self.text_kraftkort.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_kraftkort, 10, 0, 1, 1)

        self.label_effekt_thrustere = QLabel(self.ROVinfoFrame)
        self.label_effekt_thrustere.setObjectName(u"label_effekt_thrustere")
        self.label_effekt_thrustere.setMinimumSize(QSize(0, 0))
        self.label_effekt_thrustere.setMaximumSize(QSize(16777215, 16777215))
        self.label_effekt_thrustere.setFont(font1)
        self.label_effekt_thrustere.setFrameShape(QFrame.NoFrame)
        self.label_effekt_thrustere.setLineWidth(0)
        self.label_effekt_thrustere.setMidLineWidth(0)
        self.label_effekt_thrustere.setAlignment(Qt.AlignCenter)
        self.label_effekt_thrustere.setMargin(0)

        self.gridLayout_3.addWidget(self.label_effekt_thrustere, 5, 2, 1, 1)

        self.text_sensorkort = QLabel(self.ROVinfoFrame)
        self.text_sensorkort.setObjectName(u"text_sensorkort")
        self.text_sensorkort.setMinimumSize(QSize(0, 0))
        self.text_sensorkort.setFont(font1)
        self.text_sensorkort.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_sensorkort, 11, 0, 1, 1)

        self.label_tid = QLabel(self.ROVinfoFrame)
        self.label_tid.setObjectName(u"label_tid")
        self.label_tid.setMinimumSize(QSize(0, 0))
        self.label_tid.setMaximumSize(QSize(16777215, 16777215))
        self.label_tid.setFont(font1)
        self.label_tid.setFrameShape(QFrame.NoFrame)
        self.label_tid.setLineWidth(0)
        self.label_tid.setMidLineWidth(0)
        self.label_tid.setAlignment(Qt.AlignCenter)
        self.label_tid.setMargin(0)

        self.gridLayout_3.addWidget(self.label_tid, 0, 2, 1, 1)

        self.btn_reset_nullpunkt = QPushButton(self.ROVinfoFrame)
        self.btn_reset_nullpunkt.setObjectName(u"btn_reset_nullpunkt")
        sizePolicy.setHeightForWidth(self.btn_reset_nullpunkt.sizePolicy().hasHeightForWidth())
        self.btn_reset_nullpunkt.setSizePolicy(sizePolicy)
        self.btn_reset_nullpunkt.setMinimumSize(QSize(0, 0))
        self.btn_reset_nullpunkt.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_nullpunkt.setFont(font1)
        self.btn_reset_nullpunkt.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_nullpunkt.setCheckable(False)
        self.btn_reset_nullpunkt.setChecked(False)
        self.btn_reset_nullpunkt.setAutoRepeat(False)
        self.btn_reset_nullpunkt.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_reset_nullpunkt, 2, 4, 1, 1)

        self.text_tid = QLabel(self.ROVinfoFrame)
        self.text_tid.setObjectName(u"text_tid")
        self.text_tid.setMinimumSize(QSize(0, 0))
        self.text_tid.setFont(font1)
        self.text_tid.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_tid, 0, 0, 1, 1)

        self.btn_reset_tidtaker = QPushButton(self.ROVinfoFrame)
        self.btn_reset_tidtaker.setObjectName(u"btn_reset_tidtaker")
        sizePolicy.setHeightForWidth(self.btn_reset_tidtaker.sizePolicy().hasHeightForWidth())
        self.btn_reset_tidtaker.setSizePolicy(sizePolicy)
        self.btn_reset_tidtaker.setMinimumSize(QSize(0, 0))
        self.btn_reset_tidtaker.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_tidtaker.setFont(font1)
        self.btn_reset_tidtaker.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_tidtaker.setCheckable(False)
        self.btn_reset_tidtaker.setChecked(False)
        self.btn_reset_tidtaker.setAutoRepeat(False)
        self.btn_reset_tidtaker.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_reset_tidtaker, 1, 5, 1, 1)

        self.btn_start_tidtaker = QPushButton(self.ROVinfoFrame)
        self.btn_start_tidtaker.setObjectName(u"btn_start_tidtaker")
        sizePolicy.setHeightForWidth(self.btn_start_tidtaker.sizePolicy().hasHeightForWidth())
        self.btn_start_tidtaker.setSizePolicy(sizePolicy)
        self.btn_start_tidtaker.setMinimumSize(QSize(0, 0))
        self.btn_start_tidtaker.setMaximumSize(QSize(16777215, 16777215))
        self.btn_start_tidtaker.setFont(font1)
        self.btn_start_tidtaker.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_tidtaker.setCheckable(True)
        self.btn_start_tidtaker.setChecked(False)
        self.btn_start_tidtaker.setAutoRepeat(False)
        self.btn_start_tidtaker.setFlat(False)

        self.gridLayout_3.addWidget(self.btn_start_tidtaker, 1, 4, 1, 1)

        self.label_tidtaker = QLabel(self.ROVinfoFrame)
        self.label_tidtaker.setObjectName(u"label_tidtaker")
        self.label_tidtaker.setMinimumSize(QSize(0, 0))
        self.label_tidtaker.setMaximumSize(QSize(16777215, 16777215))
        self.label_tidtaker.setFont(font1)
        self.label_tidtaker.setFrameShape(QFrame.NoFrame)
        self.label_tidtaker.setLineWidth(0)
        self.label_tidtaker.setMidLineWidth(0)
        self.label_tidtaker.setAlignment(Qt.AlignCenter)
        self.label_tidtaker.setMargin(0)

        self.gridLayout_3.addWidget(self.label_tidtaker, 1, 2, 1, 1)


        self.rovLayout.addWidget(self.ROVinfoFrame)


        self.column1Layout.addWidget(self.rovFrame)


        self.horizontalLayout_6.addWidget(self.column1)

        self.label_lekkasje_varsel = QLabel(self.row)
        self.label_lekkasje_varsel.setObjectName(u"label_lekkasje_varsel")
        self.label_lekkasje_varsel.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label_lekkasje_varsel.sizePolicy().hasHeightForWidth())
        self.label_lekkasje_varsel.setSizePolicy(sizePolicy)
        self.label_lekkasje_varsel.setMinimumSize(QSize(0, 0))
        self.label_lekkasje_varsel.setMaximumSize(QSize(0, 0))
        self.label_lekkasje_varsel.setStyleSheet(u"QLabel { color: rgba(255, 255, 255, 0); background-color: rgba(179, 32, 36, 0); }")
        self.label_lekkasje_varsel.setAlignment(Qt.AlignCenter)
        self.label_lekkasje_varsel.setWordWrap(True)
        self.label_lekkasje_varsel.setMargin(0)
        self.label_lekkasje_varsel.setIndent(0)

        self.horizontalLayout_6.addWidget(self.label_lekkasje_varsel)

        self.column2 = QFrame(self.row)
        self.column2.setObjectName(u"column2")
        sizePolicy.setHeightForWidth(self.column2.sizePolicy().hasHeightForWidth())
        self.column2.setSizePolicy(sizePolicy)
        self.column2.setMinimumSize(QSize(400, 0))
        self.column2.setMaximumSize(QSize(16777215, 16777215))
        self.column2.setFont(font)
        self.column2.setStyleSheet(u"")
        self.column2Layout = QVBoxLayout(self.column2)
        self.column2Layout.setSpacing(5)
        self.column2Layout.setObjectName(u"column2Layout")
        self.column2Layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.title_motor = QLabel(self.column2)
        self.title_motor.setObjectName(u"title_motor")
        self.title_motor.setFont(font1)

        self.column2Layout.addWidget(self.title_motor)

        self.motorOuterContainer = QFrame(self.column2)
        self.motorOuterContainer.setObjectName(u"motorOuterContainer")
        sizePolicy.setHeightForWidth(self.motorOuterContainer.sizePolicy().hasHeightForWidth())
        self.motorOuterContainer.setSizePolicy(sizePolicy)
        self.motorOuterContainer.setMinimumSize(QSize(0, 350))
        self.motorOuterContainer.setMaximumSize(QSize(16777215, 16777215))
        self.motorOuterContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.motorOuterContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.motorContainter = QFrame(self.motorOuterContainer)
        self.motorContainter.setObjectName(u"motorContainter")
        self.motorContainter.setMinimumSize(QSize(350, 450))
        self.motorContainter.setMaximumSize(QSize(16777215, 16777215))
        self.motorContainter.setAutoFillBackground(False)
        self.motorContainter.setStyleSheet(u"")
        self.motorContainter.setFrameShape(QFrame.NoFrame)
        self.motorContainter.setFrameShadow(QFrame.Raised)
        self.img_manipulator_2 = QLabel(self.motorContainter)
        self.img_manipulator_2.setObjectName(u"img_manipulator_2")
        self.img_manipulator_2.setGeometry(QRect(22, 10, 280, 330))
        sizePolicy.setHeightForWidth(self.img_manipulator_2.sizePolicy().hasHeightForWidth())
        self.img_manipulator_2.setSizePolicy(sizePolicy)
        self.img_manipulator_2.setMinimumSize(QSize(0, 0))
        self.img_manipulator_2.setMaximumSize(QSize(16777215, 16777215))
        self.img_manipulator_2.setSizeIncrement(QSize(0, 0))
        self.img_manipulator_2.setAutoFillBackground(False)
        self.img_manipulator_2.setStyleSheet(u"")
        self.img_manipulator_2.setPixmap(QPixmap(u":/images/images/motorpaadrag.png"))
        self.img_manipulator_2.setScaledContents(True)
        self.img_manipulator_2.setAlignment(Qt.AlignCenter)
        self.img_manipulator_2.setMargin(0)
        self.frame_VHB = QFrame(self.motorContainter)
        self.frame_VHB.setObjectName(u"frame_VHB")
        self.frame_VHB.setGeometry(QRect(249, 250, 61, 60))
        self.frame_VHB.setAutoFillBackground(False)
        self.frame_VHB.setFrameShape(QFrame.NoFrame)
        self.frame_VHB.setFrameShadow(QFrame.Raised)
        self.frame_VHB_circle = QFrame(self.frame_VHB)
        self.frame_VHB_circle.setObjectName(u"frame_VHB_circle")
        self.frame_VHB_circle.setGeometry(QRect(5, 5, 50, 50))
        self.frame_VHB_circle.setAutoFillBackground(False)
        self.frame_VHB_circle.setStyleSheet(u"")
        self.frame_VHB_circle.setFrameShape(QFrame.NoFrame)
        self.frame_VHB_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_VHB = QLabel(self.frame_VHB_circle)
        self.label_percentage_VHB.setObjectName(u"label_percentage_VHB")
        self.label_percentage_VHB.setGeometry(QRect(0, 10, 50, 30))
        font2 = QFont()
        font2.setPointSize(9)
        self.label_percentage_VHB.setFont(font2)
        self.label_percentage_VHB.setAutoFillBackground(False)
        self.label_percentage_VHB.setStyleSheet(u"background: transparent;")
        self.label_percentage_VHB.setScaledContents(False)
        self.label_percentage_VHB.setAlignment(Qt.AlignCenter)
        self.label_percentage_VHB.setWordWrap(False)
        self.frame_HHB = QFrame(self.motorContainter)
        self.frame_HHB.setObjectName(u"frame_HHB")
        self.frame_HHB.setGeometry(QRect(193, 210, 60, 60))
        self.frame_HHB.setFrameShape(QFrame.NoFrame)
        self.frame_HHB.setFrameShadow(QFrame.Raised)
        self.frame_HHB_circle = QFrame(self.frame_HHB)
        self.frame_HHB_circle.setObjectName(u"frame_HHB_circle")
        self.frame_HHB_circle.setGeometry(QRect(5, 5, 50, 50))
        self.frame_HHB_circle.setFrameShape(QFrame.StyledPanel)
        self.frame_HHB_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_HHB = QLabel(self.frame_HHB_circle)
        self.label_percentage_HHB.setObjectName(u"label_percentage_HHB")
        self.label_percentage_HHB.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_HHB.setFont(font2)
        self.label_percentage_HHB.setAutoFillBackground(False)
        self.label_percentage_HHB.setStyleSheet(u"background: transparent;")
        self.label_percentage_HHB.setScaledContents(False)
        self.label_percentage_HHB.setAlignment(Qt.AlignCenter)
        self.label_percentage_HHB.setWordWrap(False)
        self.frame_VVB = QFrame(self.motorContainter)
        self.frame_VVB.setObjectName(u"frame_VVB")
        self.frame_VVB.setGeometry(QRect(9, 260, 60, 60))
        self.frame_VVB.setFrameShape(QFrame.NoFrame)
        self.frame_VVB.setFrameShadow(QFrame.Raised)
        self.frame_VVB_circle = QFrame(self.frame_VVB)
        self.frame_VVB_circle.setObjectName(u"frame_VVB_circle")
        self.frame_VVB_circle.setGeometry(QRect(5, 5, 50, 50))
        self.frame_VVB_circle.setFrameShape(QFrame.StyledPanel)
        self.frame_VVB_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_VVB = QLabel(self.frame_VVB_circle)
        self.label_percentage_VVB.setObjectName(u"label_percentage_VVB")
        self.label_percentage_VVB.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_VVB.setFont(font2)
        self.label_percentage_VVB.setAutoFillBackground(False)
        self.label_percentage_VVB.setStyleSheet(u"background: transparent;")
        self.label_percentage_VVB.setScaledContents(False)
        self.label_percentage_VVB.setAlignment(Qt.AlignCenter)
        self.label_percentage_VVB.setWordWrap(False)
        self.frame_VHF = QFrame(self.motorContainter)
        self.frame_VHF.setObjectName(u"frame_VHF")
        self.frame_VHF.setGeometry(QRect(249, 60, 60, 60))
        self.frame_VHF.setFrameShape(QFrame.NoFrame)
        self.frame_VHF.setFrameShadow(QFrame.Raised)
        self.frame_VHF_circle = QFrame(self.frame_VHF)
        self.frame_VHF_circle.setObjectName(u"frame_VHF_circle")
        self.frame_VHF_circle.setGeometry(QRect(5, 5, 50, 50))
        self.frame_VHF_circle.setFrameShape(QFrame.StyledPanel)
        self.frame_VHF_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_VHF = QLabel(self.frame_VHF_circle)
        self.label_percentage_VHF.setObjectName(u"label_percentage_VHF")
        self.label_percentage_VHF.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_VHF.setFont(font2)
        self.label_percentage_VHF.setAutoFillBackground(False)
        self.label_percentage_VHF.setStyleSheet(u"background: transparent;")
        self.label_percentage_VHF.setScaledContents(False)
        self.label_percentage_VHF.setAlignment(Qt.AlignCenter)
        self.label_percentage_VHF.setWordWrap(False)
        self.frame_HVF = QFrame(self.motorContainter)
        self.frame_HVF.setObjectName(u"frame_HVF")
        self.frame_HVF.setGeometry(QRect(72, 110, 60, 60))
        self.frame_HVF.setFrameShape(QFrame.NoFrame)
        self.frame_HVF.setFrameShadow(QFrame.Raised)
        self.frame_HVF_circle = QFrame(self.frame_HVF)
        self.frame_HVF_circle.setObjectName(u"frame_HVF_circle")
        self.frame_HVF_circle.setGeometry(QRect(5, 5, 50, 50))
        self.frame_HVF_circle.setFrameShape(QFrame.NoFrame)
        self.frame_HVF_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_HVF = QLabel(self.frame_HVF_circle)
        self.label_percentage_HVF.setObjectName(u"label_percentage_HVF")
        self.label_percentage_HVF.setGeometry(QRect(6, 10, 41, 30))
        self.label_percentage_HVF.setFont(font2)
        self.label_percentage_HVF.setAutoFillBackground(False)
        self.label_percentage_HVF.setScaledContents(False)
        self.label_percentage_HVF.setAlignment(Qt.AlignCenter)
        self.label_percentage_HVF.setWordWrap(False)
        self.frame_HHF = QFrame(self.motorContainter)
        self.frame_HHF.setObjectName(u"frame_HHF")
        self.frame_HHF.setGeometry(QRect(189, 110, 60, 60))
        self.frame_HHF.setFrameShape(QFrame.NoFrame)
        self.frame_HHF.setFrameShadow(QFrame.Raised)
        self.frame_HHF_circle = QFrame(self.frame_HHF)
        self.frame_HHF_circle.setObjectName(u"frame_HHF_circle")
        self.frame_HHF_circle.setGeometry(QRect(5, 5, 50, 50))
        self.frame_HHF_circle.setFrameShape(QFrame.NoFrame)
        self.frame_HHF_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_HHF = QLabel(self.frame_HHF_circle)
        self.label_percentage_HHF.setObjectName(u"label_percentage_HHF")
        self.label_percentage_HHF.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_HHF.setFont(font2)
        self.label_percentage_HHF.setAutoFillBackground(False)
        self.label_percentage_HHF.setStyleSheet(u"background: transparent;")
        self.label_percentage_HHF.setScaledContents(False)
        self.label_percentage_HHF.setAlignment(Qt.AlignCenter)
        self.label_percentage_HHF.setWordWrap(False)
        self.frame_VVF = QFrame(self.motorContainter)
        self.frame_VVF.setObjectName(u"frame_VVF")
        self.frame_VVF.setGeometry(QRect(9, 60, 60, 60))
        self.frame_VVF.setFrameShape(QFrame.NoFrame)
        self.frame_VVF.setFrameShadow(QFrame.Raised)
        self.frame_VVF_circle = QFrame(self.frame_VVF)
        self.frame_VVF_circle.setObjectName(u"frame_VVF_circle")
        self.frame_VVF_circle.setGeometry(QRect(5, 5, 50, 50))
        self.frame_VVF_circle.setFrameShape(QFrame.StyledPanel)
        self.frame_VVF_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_VVF = QLabel(self.frame_VVF_circle)
        self.label_percentage_VVF.setObjectName(u"label_percentage_VVF")
        self.label_percentage_VVF.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_VVF.setFont(font2)
        self.label_percentage_VVF.setAutoFillBackground(False)
        self.label_percentage_VVF.setStyleSheet(u"background: transparent;")
        self.label_percentage_VVF.setScaledContents(False)
        self.label_percentage_VVF.setAlignment(Qt.AlignCenter)
        self.label_percentage_VVF.setWordWrap(False)
        self.frame_HVB = QFrame(self.motorContainter)
        self.frame_HVB.setObjectName(u"frame_HVB")
        self.frame_HVB.setGeometry(QRect(72, 210, 60, 60))
        self.frame_HVB.setFrameShape(QFrame.NoFrame)
        self.frame_HVB.setFrameShadow(QFrame.Raised)
        self.frame_HVB_circle = QFrame(self.frame_HVB)
        self.frame_HVB_circle.setObjectName(u"frame_HVB_circle")
        self.frame_HVB_circle.setGeometry(QRect(5, 5, 50, 50))
        self.frame_HVB_circle.setFrameShape(QFrame.StyledPanel)
        self.frame_HVB_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_HVB = QLabel(self.frame_HVB_circle)
        self.label_percentage_HVB.setObjectName(u"label_percentage_HVB")
        self.label_percentage_HVB.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_HVB.setFont(font2)
        self.label_percentage_HVB.setAutoFillBackground(False)
        self.label_percentage_HVB.setStyleSheet(u"background: transparent;")
        self.label_percentage_HVB.setScaledContents(False)
        self.label_percentage_HVB.setAlignment(Qt.AlignCenter)
        self.label_percentage_HVB.setWordWrap(False)
        self.text_rov = QLabel(self.motorContainter)
        self.text_rov.setObjectName(u"text_rov")
        self.text_rov.setGeometry(QRect(0, 10, 357, 14))
        self.text_rov.setFont(font)
        self.text_rov.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_rov.setLineWidth(1)
        self.text_rov.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.motorContainter)


        self.column2Layout.addWidget(self.motorOuterContainer)

        self.strupingGrid = QGridLayout()
        self.strupingGrid.setSpacing(5)
        self.strupingGrid.setObjectName(u"strupingGrid")
        self.text_struping_thrustere = QLabel(self.column2)
        self.text_struping_thrustere.setObjectName(u"text_struping_thrustere")
        self.text_struping_thrustere.setMinimumSize(QSize(0, 0))
        self.text_struping_thrustere.setMaximumSize(QSize(16777215, 16777215))
        self.text_struping_thrustere.setFont(font1)
        self.text_struping_thrustere.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_struping_thrustere.setTextFormat(Qt.RichText)

        self.strupingGrid.addWidget(self.text_struping_thrustere, 0, 0, 1, 1)

        self.slider_struping_thrustere = QSlider(self.column2)
        self.slider_struping_thrustere.setObjectName(u"slider_struping_thrustere")
        sizePolicy.setHeightForWidth(self.slider_struping_thrustere.sizePolicy().hasHeightForWidth())
        self.slider_struping_thrustere.setSizePolicy(sizePolicy)
        self.slider_struping_thrustere.setMinimumSize(QSize(0, 68))
        self.slider_struping_thrustere.setMaximumSize(QSize(16777215, 68))
        self.slider_struping_thrustere.setFont(font1)
        self.slider_struping_thrustere.setStyleSheet(u"")
        self.slider_struping_thrustere.setMaximum(100)
        self.slider_struping_thrustere.setOrientation(Qt.Horizontal)
        self.slider_struping_thrustere.setInvertedAppearance(False)
        self.slider_struping_thrustere.setInvertedControls(False)
        self.slider_struping_thrustere.setTickPosition(QSlider.NoTicks)

        self.strupingGrid.addWidget(self.slider_struping_thrustere, 0, 1, 1, 1)

        self.strupingWidget = QWidget(self.column2)
        self.strupingWidget.setObjectName(u"strupingWidget")
        self.frame_struping = QFrame(self.strupingWidget)
        self.frame_struping.setObjectName(u"frame_struping")
        self.frame_struping.setGeometry(QRect(0, 0, 60, 60))
        self.frame_struping.setFrameShape(QFrame.NoFrame)
        self.frame_struping.setFrameShadow(QFrame.Raised)
        self.struping_circle = QFrame(self.frame_struping)
        self.struping_circle.setObjectName(u"struping_circle")
        self.struping_circle.setGeometry(QRect(5, 5, 50, 50))
        self.struping_circle.setFrameShape(QFrame.StyledPanel)
        self.struping_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_struping = QLabel(self.struping_circle)
        self.label_percentage_struping.setObjectName(u"label_percentage_struping")
        self.label_percentage_struping.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_struping.setFont(font2)
        self.label_percentage_struping.setAutoFillBackground(False)
        self.label_percentage_struping.setStyleSheet(u"background: transparent;")
        self.label_percentage_struping.setScaledContents(False)
        self.label_percentage_struping.setAlignment(Qt.AlignCenter)
        self.label_percentage_struping.setWordWrap(False)

        self.strupingGrid.addWidget(self.strupingWidget, 0, 3, 1, 1)

        self.btn_lav_struping = QPushButton(self.column2)
        self.btn_lav_struping.setObjectName(u"btn_lav_struping")
        sizePolicy.setHeightForWidth(self.btn_lav_struping.sizePolicy().hasHeightForWidth())
        self.btn_lav_struping.setSizePolicy(sizePolicy)
        self.btn_lav_struping.setMinimumSize(QSize(0, 0))
        self.btn_lav_struping.setMaximumSize(QSize(16777215, 16777215))
        self.btn_lav_struping.setFont(font1)
        self.btn_lav_struping.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_lav_struping.setCheckable(True)
        self.btn_lav_struping.setChecked(False)
        self.btn_lav_struping.setAutoRepeat(False)
        self.btn_lav_struping.setFlat(False)

        self.strupingGrid.addWidget(self.btn_lav_struping, 1, 0, 1, 1)


        self.column2Layout.addLayout(self.strupingGrid)

        self.maniOuterContainer = QFrame(self.column2)
        self.maniOuterContainer.setObjectName(u"maniOuterContainer")
        self.maniOuterContainer.setMinimumSize(QSize(360, 180))
        self.maniOuterContainer.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.maniOuterContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.maniContainer = QFrame(self.maniOuterContainer)
        self.maniContainer.setObjectName(u"maniContainer")
        self.maniContainer.setMinimumSize(QSize(0, 0))
        self.maniContainer.setMaximumSize(QSize(16777215, 16777215))
        self.maniContainer.setFrameShape(QFrame.NoFrame)
        self.maniContainer.setFrameShadow(QFrame.Raised)
        self.img_manipulator = QLabel(self.maniContainer)
        self.img_manipulator.setObjectName(u"img_manipulator")
        self.img_manipulator.setGeometry(QRect(-20, -8, 320, 161))
        self.img_manipulator.setMinimumSize(QSize(0, 0))
        self.img_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.img_manipulator.setSizeIncrement(QSize(0, 0))
        self.img_manipulator.setPixmap(QPixmap(u":/images/images/manipulator.png"))
        self.img_manipulator.setScaledContents(True)
        self.frame_mani_1 = QFrame(self.maniContainer)
        self.frame_mani_1.setObjectName(u"frame_mani_1")
        self.frame_mani_1.setGeometry(QRect(10, 37, 60, 60))
        self.frame_mani_1.setFrameShape(QFrame.NoFrame)
        self.frame_mani_1.setFrameShadow(QFrame.Raised)
        self.mani_circle_1 = QFrame(self.frame_mani_1)
        self.mani_circle_1.setObjectName(u"mani_circle_1")
        self.mani_circle_1.setGeometry(QRect(5, 5, 50, 50))
        self.mani_circle_1.setFrameShape(QFrame.NoFrame)
        self.mani_circle_1.setFrameShadow(QFrame.Raised)
        self.label_percentage_mani_1 = QLabel(self.mani_circle_1)
        self.label_percentage_mani_1.setObjectName(u"label_percentage_mani_1")
        self.label_percentage_mani_1.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_mani_1.setFont(font2)
        self.label_percentage_mani_1.setAutoFillBackground(False)
        self.label_percentage_mani_1.setStyleSheet(u"background: transparent;")
        self.label_percentage_mani_1.setScaledContents(False)
        self.label_percentage_mani_1.setAlignment(Qt.AlignCenter)
        self.label_percentage_mani_1.setWordWrap(False)
        self.frame_mani_3 = QFrame(self.maniContainer)
        self.frame_mani_3.setObjectName(u"frame_mani_3")
        self.frame_mani_3.setGeometry(QRect(150, 87, 60, 60))
        self.frame_mani_3.setFrameShape(QFrame.NoFrame)
        self.frame_mani_3.setFrameShadow(QFrame.Raised)
        self.mani_circle_3 = QFrame(self.frame_mani_3)
        self.mani_circle_3.setObjectName(u"mani_circle_3")
        self.mani_circle_3.setGeometry(QRect(5, 5, 50, 50))
        self.mani_circle_3.setFrameShape(QFrame.StyledPanel)
        self.mani_circle_3.setFrameShadow(QFrame.Raised)
        self.label_percentage_mani_3 = QLabel(self.mani_circle_3)
        self.label_percentage_mani_3.setObjectName(u"label_percentage_mani_3")
        self.label_percentage_mani_3.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_mani_3.setFont(font2)
        self.label_percentage_mani_3.setAutoFillBackground(False)
        self.label_percentage_mani_3.setStyleSheet(u"background: transparent;")
        self.label_percentage_mani_3.setScaledContents(False)
        self.label_percentage_mani_3.setAlignment(Qt.AlignCenter)
        self.label_percentage_mani_3.setWordWrap(False)
        self.frame_mani_2 = QFrame(self.maniContainer)
        self.frame_mani_2.setObjectName(u"frame_mani_2")
        self.frame_mani_2.setGeometry(QRect(250, 47, 60, 60))
        self.frame_mani_2.setFrameShape(QFrame.NoFrame)
        self.frame_mani_2.setFrameShadow(QFrame.Raised)
        self.mani_circle_2 = QFrame(self.frame_mani_2)
        self.mani_circle_2.setObjectName(u"mani_circle_2")
        self.mani_circle_2.setGeometry(QRect(5, 5, 50, 50))
        self.mani_circle_2.setFrameShape(QFrame.StyledPanel)
        self.mani_circle_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_mani_2 = QLabel(self.mani_circle_2)
        self.label_percentage_mani_2.setObjectName(u"label_percentage_mani_2")
        self.label_percentage_mani_2.setGeometry(QRect(10, 10, 31, 30))
        self.label_percentage_mani_2.setFont(font2)
        self.label_percentage_mani_2.setAutoFillBackground(False)
        self.label_percentage_mani_2.setStyleSheet(u"background: transparent;")
        self.label_percentage_mani_2.setScaledContents(False)
        self.label_percentage_mani_2.setAlignment(Qt.AlignCenter)
        self.label_percentage_mani_2.setWordWrap(False)
        self.text_manipulator = QLabel(self.maniContainer)
        self.text_manipulator.setObjectName(u"text_manipulator")
        self.text_manipulator.setGeometry(QRect(-10, -10, 376, 34))
        self.text_manipulator.setFont(font)
        self.text_manipulator.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_manipulator.setLineWidth(1)
        self.text_manipulator.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.text_manipulator.setMargin(10)

        self.verticalLayout_3.addWidget(self.maniContainer)


        self.column2Layout.addWidget(self.maniOuterContainer)

        self.lysGridLayout = QGridLayout()
        self.lysGridLayout.setSpacing(5)
        self.lysGridLayout.setObjectName(u"lysGridLayout")
        self.lysForwardWidget = QWidget(self.column2)
        self.lysForwardWidget.setObjectName(u"lysForwardWidget")
        self.frame_lys_forward = QFrame(self.lysForwardWidget)
        self.frame_lys_forward.setObjectName(u"frame_lys_forward")
        self.frame_lys_forward.setGeometry(QRect(0, 0, 60, 60))
        self.frame_lys_forward.setFrameShape(QFrame.NoFrame)
        self.frame_lys_forward.setFrameShadow(QFrame.Raised)
        self.lys_forward_circle = QFrame(self.frame_lys_forward)
        self.lys_forward_circle.setObjectName(u"lys_forward_circle")
        self.lys_forward_circle.setGeometry(QRect(5, 5, 50, 50))
        self.lys_forward_circle.setFrameShape(QFrame.StyledPanel)
        self.lys_forward_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_lys_forward = QLabel(self.lys_forward_circle)
        self.label_percentage_lys_forward.setObjectName(u"label_percentage_lys_forward")
        self.label_percentage_lys_forward.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_lys_forward.setFont(font2)
        self.label_percentage_lys_forward.setAutoFillBackground(False)
        self.label_percentage_lys_forward.setStyleSheet(u"background: transparent;")
        self.label_percentage_lys_forward.setScaledContents(False)
        self.label_percentage_lys_forward.setAlignment(Qt.AlignCenter)
        self.label_percentage_lys_forward.setWordWrap(False)

        self.lysGridLayout.addWidget(self.lysForwardWidget, 2, 2, 1, 1)

        self.lysDownWidget = QWidget(self.column2)
        self.lysDownWidget.setObjectName(u"lysDownWidget")
        self.frame_lys_down = QFrame(self.lysDownWidget)
        self.frame_lys_down.setObjectName(u"frame_lys_down")
        self.frame_lys_down.setGeometry(QRect(0, 0, 60, 60))
        self.frame_lys_down.setFrameShape(QFrame.NoFrame)
        self.frame_lys_down.setFrameShadow(QFrame.Raised)
        self.lys_down_circle = QFrame(self.frame_lys_down)
        self.lys_down_circle.setObjectName(u"lys_down_circle")
        self.lys_down_circle.setGeometry(QRect(5, 5, 50, 50))
        self.lys_down_circle.setFrameShape(QFrame.StyledPanel)
        self.lys_down_circle.setFrameShadow(QFrame.Raised)
        self.label_percentage_lys_down = QLabel(self.lys_down_circle)
        self.label_percentage_lys_down.setObjectName(u"label_percentage_lys_down")
        self.label_percentage_lys_down.setGeometry(QRect(0, 10, 50, 30))
        self.label_percentage_lys_down.setFont(font2)
        self.label_percentage_lys_down.setAutoFillBackground(False)
        self.label_percentage_lys_down.setStyleSheet(u"background: transparent;")
        self.label_percentage_lys_down.setScaledContents(False)
        self.label_percentage_lys_down.setAlignment(Qt.AlignCenter)
        self.label_percentage_lys_down.setWordWrap(False)

        self.lysGridLayout.addWidget(self.lysDownWidget, 3, 2, 1, 1)

        self.lys_title = QLabel(self.column2)
        self.lys_title.setObjectName(u"lys_title")
        self.lys_title.setMinimumSize(QSize(0, 0))
        self.lys_title.setMaximumSize(QSize(16777215, 16777215))
        self.lys_title.setFont(font1)
        self.lys_title.setTextFormat(Qt.PlainText)

        self.lysGridLayout.addWidget(self.lys_title, 1, 0, 1, 1)

        self.slider_lys_down = QSlider(self.column2)
        self.slider_lys_down.setObjectName(u"slider_lys_down")
        sizePolicy.setHeightForWidth(self.slider_lys_down.sizePolicy().hasHeightForWidth())
        self.slider_lys_down.setSizePolicy(sizePolicy)
        self.slider_lys_down.setMinimumSize(QSize(0, 68))
        self.slider_lys_down.setMaximumSize(QSize(16777215, 68))
        self.slider_lys_down.setFont(font1)
        self.slider_lys_down.setStyleSheet(u"")
        self.slider_lys_down.setMaximum(100)
        self.slider_lys_down.setOrientation(Qt.Horizontal)
        self.slider_lys_down.setInvertedAppearance(False)
        self.slider_lys_down.setInvertedControls(False)
        self.slider_lys_down.setTickPosition(QSlider.NoTicks)

        self.lysGridLayout.addWidget(self.slider_lys_down, 3, 1, 1, 1)

        self.text_lys_down = QLabel(self.column2)
        self.text_lys_down.setObjectName(u"text_lys_down")
        self.text_lys_down.setMinimumSize(QSize(0, 0))
        self.text_lys_down.setMaximumSize(QSize(16777215, 16777215))
        self.text_lys_down.setFont(font1)
        self.text_lys_down.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_lys_down.setTextFormat(Qt.RichText)

        self.lysGridLayout.addWidget(self.text_lys_down, 3, 0, 1, 1)

        self.slider_lys_forward = QSlider(self.column2)
        self.slider_lys_forward.setObjectName(u"slider_lys_forward")
        sizePolicy.setHeightForWidth(self.slider_lys_forward.sizePolicy().hasHeightForWidth())
        self.slider_lys_forward.setSizePolicy(sizePolicy)
        self.slider_lys_forward.setMinimumSize(QSize(0, 68))
        self.slider_lys_forward.setMaximumSize(QSize(16777215, 68))
        self.slider_lys_forward.setFont(font1)
        self.slider_lys_forward.setStyleSheet(u"")
        self.slider_lys_forward.setMaximum(100)
        self.slider_lys_forward.setOrientation(Qt.Horizontal)
        self.slider_lys_forward.setInvertedAppearance(False)
        self.slider_lys_forward.setInvertedControls(False)
        self.slider_lys_forward.setTickPosition(QSlider.TicksBothSides)
        self.slider_lys_forward.setTickInterval(10)

        self.lysGridLayout.addWidget(self.slider_lys_forward, 2, 1, 1, 1)

        self.text_lys_forward = QLabel(self.column2)
        self.text_lys_forward.setObjectName(u"text_lys_forward")
        self.text_lys_forward.setMinimumSize(QSize(0, 0))
        self.text_lys_forward.setMaximumSize(QSize(16777215, 16777215))
        self.text_lys_forward.setFont(font1)
        self.text_lys_forward.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_lys_forward.setTextFormat(Qt.RichText)

        self.lysGridLayout.addWidget(self.text_lys_forward, 2, 0, 1, 1)


        self.column2Layout.addLayout(self.lysGridLayout)


        self.horizontalLayout_6.addWidget(self.column2)

        self.column3 = QFrame(self.row)
        self.column3.setObjectName(u"column3")
        sizePolicy.setHeightForWidth(self.column3.sizePolicy().hasHeightForWidth())
        self.column3.setSizePolicy(sizePolicy)
        self.column3.setMinimumSize(QSize(0, 0))
        self.column3.setMaximumSize(QSize(16777215, 16777215))
        self.column3.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        self.column3.setFont(font3)
        self.column3.setStyleSheet(u"")
        self.column3Layout = QVBoxLayout(self.column3)
        self.column3Layout.setSpacing(5)
        self.column3Layout.setObjectName(u"column3Layout")
        self.column3Layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.QVBoxLayout_2 = QFrame(self.column3)
        self.QVBoxLayout_2.setObjectName(u"QVBoxLayout_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(8)
        sizePolicy5.setHeightForWidth(self.QVBoxLayout_2.sizePolicy().hasHeightForWidth())
        self.QVBoxLayout_2.setSizePolicy(sizePolicy5)
        self.QVBoxLayout_2.setMinimumSize(QSize(0, 280))
        self.QVBoxLayout_2.setMaximumSize(QSize(16777215, 16777215))
        self.QVBoxLayout_2.setStyleSheet(u"border: 1px solid rgb(23, 25, 30);")
        self.QVBoxLayout_2.setFrameShape(QFrame.NoFrame)
        self.QVBoxLayout = QVBoxLayout(self.QVBoxLayout_2)
        self.QVBoxLayout.setSpacing(0)
        self.QVBoxLayout.setObjectName(u"QVBoxLayout")
        self.QVBoxLayout.setContentsMargins(0, 0, 0, 0)

        self.column3Layout.addWidget(self.QVBoxLayout_2)

        self.title_video = QLabel(self.column3)
        self.title_video.setObjectName(u"title_video")
        self.title_video.setMaximumSize(QSize(16777215, 16777215))
        self.title_video.setFont(font1)
        self.title_video.setStyleSheet(u"")

        self.column3Layout.addWidget(self.title_video)

        self.tite_kamera = QLabel(self.column3)
        self.tite_kamera.setObjectName(u"tite_kamera")
        self.tite_kamera.setMaximumSize(QSize(16777215, 16777215))
        self.tite_kamera.setFont(font1)
        self.tite_kamera.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.column3Layout.addWidget(self.tite_kamera)

        self.kameraBtnFrame = QFrame(self.column3)
        self.kameraBtnFrame.setObjectName(u"kameraBtnFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.kameraBtnFrame.sizePolicy().hasHeightForWidth())
        self.kameraBtnFrame.setSizePolicy(sizePolicy6)
        self.kameraBtnFrame.setMinimumSize(QSize(0, 0))
        self.kameraBtnFrame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_13 = QVBoxLayout(self.kameraBtnFrame)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_ta_bilde_havbunn = QPushButton(self.kameraBtnFrame)
        self.btn_ta_bilde_havbunn.setObjectName(u"btn_ta_bilde_havbunn")
        sizePolicy.setHeightForWidth(self.btn_ta_bilde_havbunn.sizePolicy().hasHeightForWidth())
        self.btn_ta_bilde_havbunn.setSizePolicy(sizePolicy)
        self.btn_ta_bilde_havbunn.setMinimumSize(QSize(0, 0))
        self.btn_ta_bilde_havbunn.setFont(font1)
        self.btn_ta_bilde_havbunn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/images/images/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ta_bilde_havbunn.setIcon(icon8)

        self.verticalLayout_13.addWidget(self.btn_ta_bilde_havbunn)

        self.btn_ta_bilde_frontkamera = QPushButton(self.kameraBtnFrame)
        self.btn_ta_bilde_frontkamera.setObjectName(u"btn_ta_bilde_frontkamera")
        sizePolicy.setHeightForWidth(self.btn_ta_bilde_frontkamera.sizePolicy().hasHeightForWidth())
        self.btn_ta_bilde_frontkamera.setSizePolicy(sizePolicy)
        self.btn_ta_bilde_frontkamera.setMinimumSize(QSize(0, 0))
        self.btn_ta_bilde_frontkamera.setFont(font1)
        self.btn_ta_bilde_frontkamera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ta_bilde_frontkamera.setIcon(icon8)

        self.verticalLayout_13.addWidget(self.btn_ta_bilde_frontkamera)

        self.btn_slett_bilde = QPushButton(self.kameraBtnFrame)
        self.btn_slett_bilde.setObjectName(u"btn_slett_bilde")
        sizePolicy.setHeightForWidth(self.btn_slett_bilde.sizePolicy().hasHeightForWidth())
        self.btn_slett_bilde.setSizePolicy(sizePolicy)
        self.btn_slett_bilde.setMinimumSize(QSize(0, 0))
        self.btn_slett_bilde.setFont(font1)
        self.btn_slett_bilde.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/images/images/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_slett_bilde.setIcon(icon9)

        self.verticalLayout_13.addWidget(self.btn_slett_bilde)


        self.column3Layout.addWidget(self.kameraBtnFrame)

        self.videooptakFrame = QFrame(self.column3)
        self.videooptakFrame.setObjectName(u"videooptakFrame")
        sizePolicy.setHeightForWidth(self.videooptakFrame.sizePolicy().hasHeightForWidth())
        self.videooptakFrame.setSizePolicy(sizePolicy)
        self.videooptakFrame.setMinimumSize(QSize(0, 0))
        self.videooptakFrame.setMaximumSize(QSize(16777215, 16777215))
        self.kameraGrid = QGridLayout(self.videooptakFrame)
        self.kameraGrid.setSpacing(5)
        self.kameraGrid.setObjectName(u"kameraGrid")
        self.kameraGrid.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.btn_start_video_havbunn = QPushButton(self.videooptakFrame)
        self.btn_start_video_havbunn.setObjectName(u"btn_start_video_havbunn")
        sizePolicy6.setHeightForWidth(self.btn_start_video_havbunn.sizePolicy().hasHeightForWidth())
        self.btn_start_video_havbunn.setSizePolicy(sizePolicy6)
        self.btn_start_video_havbunn.setMinimumSize(QSize(0, 0))
        self.btn_start_video_havbunn.setMaximumSize(QSize(16777215, 16777215))
        self.btn_start_video_havbunn.setFont(font1)
        self.btn_start_video_havbunn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start_video_havbunn.setIcon(icon10)
        self.btn_start_video_havbunn.setCheckable(True)

        self.kameraGrid.addWidget(self.btn_start_video_havbunn, 4, 1, 1, 1)

        self.btn_start_video_frontkamera = QPushButton(self.videooptakFrame)
        self.btn_start_video_frontkamera.setObjectName(u"btn_start_video_frontkamera")
        sizePolicy6.setHeightForWidth(self.btn_start_video_frontkamera.sizePolicy().hasHeightForWidth())
        self.btn_start_video_frontkamera.setSizePolicy(sizePolicy6)
        self.btn_start_video_frontkamera.setMinimumSize(QSize(0, 0))
        self.btn_start_video_frontkamera.setMaximumSize(QSize(16777215, 16777215))
        self.btn_start_video_frontkamera.setFont(font1)
        self.btn_start_video_frontkamera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_video_frontkamera.setIcon(icon10)
        self.btn_start_video_frontkamera.setCheckable(True)

        self.kameraGrid.addWidget(self.btn_start_video_frontkamera, 1, 1, 1, 1)

        self.text_frontkamera = QLabel(self.videooptakFrame)
        self.text_frontkamera.setObjectName(u"text_frontkamera")
        self.text_frontkamera.setMaximumSize(QSize(16777215, 16777215))
        self.text_frontkamera.setFont(font1)
        self.text_frontkamera.setStyleSheet(u"")

        self.kameraGrid.addWidget(self.text_frontkamera, 1, 0, 1, 1)

        self.text_havbunnskamera = QLabel(self.videooptakFrame)
        self.text_havbunnskamera.setObjectName(u"text_havbunnskamera")
        self.text_havbunnskamera.setMaximumSize(QSize(16777215, 16777215))
        self.text_havbunnskamera.setFont(font1)
        self.text_havbunnskamera.setStyleSheet(u"")

        self.kameraGrid.addWidget(self.text_havbunnskamera, 4, 0, 1, 1)

        self.title_start_videoopptak = QLabel(self.videooptakFrame)
        self.title_start_videoopptak.setObjectName(u"title_start_videoopptak")
        self.title_start_videoopptak.setMaximumSize(QSize(16777215, 16777215))
        self.title_start_videoopptak.setFont(font1)
        self.title_start_videoopptak.setStyleSheet(u"color: rgb(113, 126, 149);")

        self.kameraGrid.addWidget(self.title_start_videoopptak, 0, 0, 1, 1)

        self.tiltFrameHavbunn = QFrame(self.videooptakFrame)
        self.tiltFrameHavbunn.setObjectName(u"tiltFrameHavbunn")
        self.tiltFrameHavbunn.setFrameShape(QFrame.NoFrame)
        self.tiltFrameHavbunn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.tiltFrameHavbunn)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_havbunn_tilt_opp = QPushButton(self.tiltFrameHavbunn)
        self.btn_havbunn_tilt_opp.setObjectName(u"btn_havbunn_tilt_opp")
        sizePolicy.setHeightForWidth(self.btn_havbunn_tilt_opp.sizePolicy().hasHeightForWidth())
        self.btn_havbunn_tilt_opp.setSizePolicy(sizePolicy)
        self.btn_havbunn_tilt_opp.setMinimumSize(QSize(0, 0))
        self.btn_havbunn_tilt_opp.setMaximumSize(QSize(16777215, 16777215))
        self.btn_havbunn_tilt_opp.setFont(font1)
        self.btn_havbunn_tilt_opp.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-arrow-top-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_havbunn_tilt_opp.setIcon(icon11)
        self.btn_havbunn_tilt_opp.setCheckable(False)
        self.btn_havbunn_tilt_opp.setChecked(False)
        self.btn_havbunn_tilt_opp.setAutoRepeat(False)
        self.btn_havbunn_tilt_opp.setFlat(False)

        self.verticalLayout_10.addWidget(self.btn_havbunn_tilt_opp)

        self.btn_havbunn_tilt_ned = QPushButton(self.tiltFrameHavbunn)
        self.btn_havbunn_tilt_ned.setObjectName(u"btn_havbunn_tilt_ned")
        sizePolicy.setHeightForWidth(self.btn_havbunn_tilt_ned.sizePolicy().hasHeightForWidth())
        self.btn_havbunn_tilt_ned.setSizePolicy(sizePolicy)
        self.btn_havbunn_tilt_ned.setMinimumSize(QSize(0, 0))
        self.btn_havbunn_tilt_ned.setMaximumSize(QSize(16777215, 16777215))
        self.btn_havbunn_tilt_ned.setFont(font1)
        self.btn_havbunn_tilt_ned.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-arrow-bottom-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_havbunn_tilt_ned.setIcon(icon12)
        self.btn_havbunn_tilt_ned.setCheckable(False)
        self.btn_havbunn_tilt_ned.setChecked(False)
        self.btn_havbunn_tilt_ned.setAutoRepeat(False)
        self.btn_havbunn_tilt_ned.setFlat(False)

        self.verticalLayout_10.addWidget(self.btn_havbunn_tilt_ned)


        self.kameraGrid.addWidget(self.tiltFrameHavbunn, 4, 2, 1, 1)

        self.tiltFrameFront = QFrame(self.videooptakFrame)
        self.tiltFrameFront.setObjectName(u"tiltFrameFront")
        self.tiltFrameFront.setFrameShape(QFrame.NoFrame)
        self.tiltFrameFront.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.tiltFrameFront)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_front_tilt_opp = QPushButton(self.tiltFrameFront)
        self.btn_front_tilt_opp.setObjectName(u"btn_front_tilt_opp")
        sizePolicy.setHeightForWidth(self.btn_front_tilt_opp.sizePolicy().hasHeightForWidth())
        self.btn_front_tilt_opp.setSizePolicy(sizePolicy)
        self.btn_front_tilt_opp.setMinimumSize(QSize(0, 0))
        self.btn_front_tilt_opp.setMaximumSize(QSize(16777215, 16777215))
        self.btn_front_tilt_opp.setFont(font1)
        self.btn_front_tilt_opp.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_front_tilt_opp.setIcon(icon11)
        self.btn_front_tilt_opp.setCheckable(False)
        self.btn_front_tilt_opp.setChecked(False)
        self.btn_front_tilt_opp.setAutoRepeat(False)
        self.btn_front_tilt_opp.setFlat(False)

        self.verticalLayout_11.addWidget(self.btn_front_tilt_opp)

        self.btn_front_tilt_ned = QPushButton(self.tiltFrameFront)
        self.btn_front_tilt_ned.setObjectName(u"btn_front_tilt_ned")
        sizePolicy.setHeightForWidth(self.btn_front_tilt_ned.sizePolicy().hasHeightForWidth())
        self.btn_front_tilt_ned.setSizePolicy(sizePolicy)
        self.btn_front_tilt_ned.setMinimumSize(QSize(0, 0))
        self.btn_front_tilt_ned.setMaximumSize(QSize(16777215, 16777215))
        self.btn_front_tilt_ned.setFont(font1)
        self.btn_front_tilt_ned.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_front_tilt_ned.setIcon(icon12)
        self.btn_front_tilt_ned.setCheckable(False)
        self.btn_front_tilt_ned.setChecked(False)
        self.btn_front_tilt_ned.setAutoRepeat(False)
        self.btn_front_tilt_ned.setFlat(False)

        self.verticalLayout_11.addWidget(self.btn_front_tilt_ned)


        self.kameraGrid.addWidget(self.tiltFrameFront, 1, 2, 1, 1)


        self.column3Layout.addWidget(self.videooptakFrame)

        self.toggleBtnFrame = QFrame(self.column3)
        self.toggleBtnFrame.setObjectName(u"toggleBtnFrame")
        sizePolicy6.setHeightForWidth(self.toggleBtnFrame.sizePolicy().hasHeightForWidth())
        self.toggleBtnFrame.setSizePolicy(sizePolicy6)
        self.toggleBtnFrame.setMaximumSize(QSize(16777215, 16777215))
        self.toggleBtnFrame.setStyleSheet(u"")
        self.toggleBtnFrame.setFrameShape(QFrame.NoFrame)
        self.toggleBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.toggleBtnFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.toggleBtnsFrame = QFrame(self.toggleBtnFrame)
        self.toggleBtnsFrame.setObjectName(u"toggleBtnsFrame")
        self.toggleBtnsFrame.setMinimumSize(QSize(0, 0))
        self.toggleBtnsFrame.setMaximumSize(QSize(16777215, 300))
        self.toggleBtnsFrame.setStyleSheet(u"")
        self.toggleBtnsFrame.setFrameShape(QFrame.NoFrame)
        self.toggleBtnsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.toggleBtnsFrame)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.toogleBtnContainer = QFrame(self.toggleBtnsFrame)
        self.toogleBtnContainer.setObjectName(u"toogleBtnContainer")
        self.toogleBtnContainer.setMinimumSize(QSize(100, 0))
        self.toogleBtnContainer.setFrameShape(QFrame.NoFrame)
        self.toogleBtnContainer.setFrameShadow(QFrame.Raised)
        self.toggle_layout = QVBoxLayout(self.toogleBtnContainer)
        self.toggle_layout.setObjectName(u"toggle_layout")
        self.toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_20.addWidget(self.toogleBtnContainer)

        self.toogleBtnLabels = QFrame(self.toggleBtnsFrame)
        self.toogleBtnLabels.setObjectName(u"toogleBtnLabels")
        self.toogleBtnLabels.setFrameShape(QFrame.NoFrame)
        self.toogleBtnLabels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.toogleBtnLabels)
        self.verticalLayout_32.setSpacing(15)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(10, 10, 10, 10)
        self.text_mani = QLabel(self.toogleBtnLabels)
        self.text_mani.setObjectName(u"text_mani")
        self.text_mani.setFont(font1)
        self.text_mani.setTextFormat(Qt.PlainText)

        self.verticalLayout_32.addWidget(self.text_mani)

        self.text_hiv_regulering = QLabel(self.toogleBtnLabels)
        self.text_hiv_regulering.setObjectName(u"text_hiv_regulering")
        self.text_hiv_regulering.setMinimumSize(QSize(0, 0))
        self.text_hiv_regulering.setFont(font1)
        self.text_hiv_regulering.setTextFormat(Qt.PlainText)

        self.verticalLayout_32.addWidget(self.text_hiv_regulering)

        self.text_stamp_regulering = QLabel(self.toogleBtnLabels)
        self.text_stamp_regulering.setObjectName(u"text_stamp_regulering")
        self.text_stamp_regulering.setMinimumSize(QSize(0, 0))
        self.text_stamp_regulering.setFont(font1)
        self.text_stamp_regulering.setTextFormat(Qt.PlainText)

        self.verticalLayout_32.addWidget(self.text_stamp_regulering)

        self.text_rull_regulering = QLabel(self.toogleBtnLabels)
        self.text_rull_regulering.setObjectName(u"text_rull_regulering")
        self.text_rull_regulering.setMinimumSize(QSize(0, 0))
        self.text_rull_regulering.setFont(font1)
        self.text_rull_regulering.setTextFormat(Qt.PlainText)

        self.verticalLayout_32.addWidget(self.text_rull_regulering)

        self.text_frontlys = QLabel(self.toogleBtnLabels)
        self.text_frontlys.setObjectName(u"text_frontlys")
        self.text_frontlys.setFont(font1)
        self.text_frontlys.setTextFormat(Qt.RichText)

        self.verticalLayout_32.addWidget(self.text_frontlys)

        self.text_havbunnslys = QLabel(self.toogleBtnLabels)
        self.text_havbunnslys.setObjectName(u"text_havbunnslys")
        self.text_havbunnslys.setFont(font1)
        self.text_havbunnslys.setTextFormat(Qt.RichText)

        self.verticalLayout_32.addWidget(self.text_havbunnslys)


        self.horizontalLayout_20.addWidget(self.toogleBtnLabels)


        self.horizontalLayout_7.addWidget(self.toggleBtnsFrame)

        self.sisteBildeFrame = QFrame(self.toggleBtnFrame)
        self.sisteBildeFrame.setObjectName(u"sisteBildeFrame")
        self.sisteBildeFrame.setMinimumSize(QSize(0, 0))
        self.sisteBildeFrame.setFrameShape(QFrame.NoFrame)
        self.sisteBildeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.sisteBildeFrame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.text_siste_bilde = QLabel(self.sisteBildeFrame)
        self.text_siste_bilde.setObjectName(u"text_siste_bilde")
        self.text_siste_bilde.setMaximumSize(QSize(16777215, 16777215))
        self.text_siste_bilde.setFont(font)
        self.text_siste_bilde.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_siste_bilde.setLineWidth(1)
        self.text_siste_bilde.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.text_siste_bilde)

        self.recent_img = QLabel(self.sisteBildeFrame)
        self.recent_img.setObjectName(u"recent_img")
        self.recent_img.setMinimumSize(QSize(0, 0))
        self.recent_img.setMaximumSize(QSize(300, 200))
        self.recent_img.setStyleSheet(u"border: 1px solid rgb(23, 25, 30);")
        self.recent_img.setPixmap(QPixmap(u":/images/images/underwater.png"))
        self.recent_img.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.recent_img)


        self.horizontalLayout_7.addWidget(self.sisteBildeFrame)


        self.column3Layout.addWidget(self.toggleBtnFrame)


        self.horizontalLayout_6.addWidget(self.column3)

        self.column1.raise_()
        self.column2.raise_()
        self.column3.raise_()
        self.label_lekkasje_varsel.raise_()

        self.verticalLayout.addWidget(self.row, 0, Qt.AlignVCenter)

        self.stackedWidget.addWidget(self.informasjon)
        self.kontroller = QWidget()
        self.kontroller.setObjectName(u"kontroller")
        self.kontroller.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.kontroller)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.hovedFrameColumn = QFrame(self.kontroller)
        self.hovedFrameColumn.setObjectName(u"hovedFrameColumn")
        self.hovedFrameColumn.setStyleSheet(u"")
        self.hovedFrameColumn.setFrameShape(QFrame.NoFrame)
        self.hovedFrameColumn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.hovedFrameColumn)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(12, 0, 12, -1)
        self.scrollArea = QScrollArea(self.hovedFrameColumn)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1133, 839))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.kontrollerContainer = QFrame(self.scrollAreaWidgetContents)
        self.kontrollerContainer.setObjectName(u"kontrollerContainer")
        self.kontrollerContainer.setFrameShape(QFrame.NoFrame)
        self.kontrollerContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.kontrollerContainer)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.kontrollerRows = QFrame(self.kontrollerContainer)
        self.kontrollerRows.setObjectName(u"kontrollerRows")
        self.kontrollerRows.setMaximumSize(QSize(16777215, 16777215))
        self.kontrollerRows.setStyleSheet(u"")
        self.kontrollerRows.setFrameShape(QFrame.NoFrame)
        self.kontrollerRows.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.kontrollerRows)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_kontroller_container = QFrame(self.kontrollerRows)
        self.btn_kontroller_container.setObjectName(u"btn_kontroller_container")
        self.btn_kontroller_container.setMaximumSize(QSize(16777214, 16777215))
        self.btn_kontroller_container.setStyleSheet(u"")
        self.btn_kontroller_container.setFrameShape(QFrame.NoFrame)
        self.btn_kontroller_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.btn_kontroller_container)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.kontrollerTextContainer = QFrame(self.btn_kontroller_container)
        self.kontrollerTextContainer.setObjectName(u"kontrollerTextContainer")
        self.kontrollerTextContainer.setFrameShape(QFrame.NoFrame)
        self.kontrollerTextContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.kontrollerTextContainer)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.title_kontroller = QLabel(self.kontrollerTextContainer)
        self.title_kontroller.setObjectName(u"title_kontroller")
        self.title_kontroller.setMinimumSize(QSize(0, 20))
        self.title_kontroller.setFont(font1)
        self.title_kontroller.setStyleSheet(u"color: #dddddd;")
        self.title_kontroller.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.title_kontroller)

        self.text_kontroller_description = QLabel(self.kontrollerTextContainer)
        self.text_kontroller_description.setObjectName(u"text_kontroller_description")
        self.text_kontroller_description.setFont(font)
        self.text_kontroller_description.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_kontroller_description.setLineWidth(1)
        self.text_kontroller_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.text_kontroller_description.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.text_kontroller_description)


        self.horizontalLayout_13.addWidget(self.kontrollerTextContainer)

        self.profileContainer = QFrame(self.btn_kontroller_container)
        self.profileContainer.setObjectName(u"profileContainer")
        self.profileContainer.setMinimumSize(QSize(0, 0))
        self.profileContainer.setMaximumSize(QSize(16777215, 16777215))
        self.profileContainer.setFrameShape(QFrame.NoFrame)
        self.profileContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.profileContainer)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.text_velg_profil = QLabel(self.profileContainer)
        self.text_velg_profil.setObjectName(u"text_velg_profil")
        self.text_velg_profil.setMinimumSize(QSize(0, 40))
        self.text_velg_profil.setMaximumSize(QSize(100, 40))
        self.text_velg_profil.setFont(font1)
        self.text_velg_profil.setStyleSheet(u"color: #dddddd;")

        self.horizontalLayout_11.addWidget(self.text_velg_profil)

        self.comboBox_velg_profil = QComboBox(self.profileContainer)
        self.comboBox_velg_profil.addItem("")
        self.comboBox_velg_profil.addItem("")
        self.comboBox_velg_profil.setObjectName(u"comboBox_velg_profil")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.comboBox_velg_profil.sizePolicy().hasHeightForWidth())
        self.comboBox_velg_profil.setSizePolicy(sizePolicy7)
        self.comboBox_velg_profil.setMinimumSize(QSize(0, 30))
        self.comboBox_velg_profil.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_velg_profil.setFont(font1)
        self.comboBox_velg_profil.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_velg_profil.setEditable(False)

        self.horizontalLayout_11.addWidget(self.comboBox_velg_profil)


        self.horizontalLayout_13.addWidget(self.profileContainer)

        self.profileBtnContainer = QFrame(self.btn_kontroller_container)
        self.profileBtnContainer.setObjectName(u"profileBtnContainer")
        self.profileBtnContainer.setMinimumSize(QSize(0, 120))
        self.profileBtnContainer.setFrameShape(QFrame.NoFrame)
        self.profileBtnContainer.setFrameShadow(QFrame.Raised)
        self.btn_reset = QPushButton(self.profileBtnContainer)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(40, 70, 201, 45))
        self.btn_reset.setMinimumSize(QSize(150, 45))
        self.btn_reset.setFont(font1)
        self.btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reset.setIcon(icon13)
        self.btn_make_new_profile = QPushButton(self.profileBtnContainer)
        self.btn_make_new_profile.setObjectName(u"btn_make_new_profile")
        self.btn_make_new_profile.setGeometry(QRect(40, 20, 201, 45))
        self.btn_make_new_profile.setMinimumSize(QSize(150, 45))
        self.btn_make_new_profile.setFont(font1)
        self.btn_make_new_profile.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_make_new_profile.setIcon(icon14)

        self.horizontalLayout_13.addWidget(self.profileBtnContainer)


        self.verticalLayout_19.addWidget(self.btn_kontroller_container)

        self.kontrollerImgContainer = QFrame(self.kontrollerRows)
        self.kontrollerImgContainer.setObjectName(u"kontrollerImgContainer")
        self.kontrollerImgContainer.setMinimumSize(QSize(0, 600))
        self.kontrollerImgContainer.setFont(font1)
        self.kontrollerImgContainer.setStyleSheet(u"")
        self.kontrollerImgContainer.setFrameShape(QFrame.NoFrame)
        self.kontrollerImgContainer.setFrameShadow(QFrame.Raised)
        self.xbox_image = QLabel(self.kontrollerImgContainer)
        self.xbox_image.setObjectName(u"xbox_image")
        self.xbox_image.setGeometry(QRect(140, -40, 801, 771))
        self.xbox_image.setPixmap(QPixmap(u":/images/images/xboxOne.png"))
        self.xbox_image.setScaledContents(True)
        self.comboBox_right_stick_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_right_stick_btn.addItem("")
        self.comboBox_right_stick_btn.setObjectName(u"comboBox_right_stick_btn")
        self.comboBox_right_stick_btn.setGeometry(QRect(790, 550, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_right_stick_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_right_stick_btn.setSizePolicy(sizePolicy7)
        self.comboBox_right_stick_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_right_stick_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_right_stick_btn.setFont(font1)
        self.comboBox_right_stick_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_directional_pad_leftright = QComboBox(self.kontrollerImgContainer)
        self.comboBox_directional_pad_leftright.addItem("")
        self.comboBox_directional_pad_leftright.setObjectName(u"comboBox_directional_pad_leftright")
        self.comboBox_directional_pad_leftright.setEnabled(False)
        self.comboBox_directional_pad_leftright.setGeometry(QRect(50, 336, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_directional_pad_leftright.sizePolicy().hasHeightForWidth())
        self.comboBox_directional_pad_leftright.setSizePolicy(sizePolicy7)
        self.comboBox_directional_pad_leftright.setMinimumSize(QSize(0, 30))
        self.comboBox_directional_pad_leftright.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_directional_pad_leftright.setFont(font1)
        self.comboBox_directional_pad_leftright.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_directional_pad_leftright.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_right_stick_x = QComboBox(self.kontrollerImgContainer)
        self.comboBox_right_stick_x.addItem("")
        self.comboBox_right_stick_x.setObjectName(u"comboBox_right_stick_x")
        self.comboBox_right_stick_x.setEnabled(False)
        self.comboBox_right_stick_x.setGeometry(QRect(867, 450, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_right_stick_x.sizePolicy().hasHeightForWidth())
        self.comboBox_right_stick_x.setSizePolicy(sizePolicy7)
        self.comboBox_right_stick_x.setMinimumSize(QSize(0, 30))
        self.comboBox_right_stick_x.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_right_stick_x.setFont(font1)
        self.comboBox_right_stick_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_x.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_RB_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_RB_btn.addItem("")
        self.comboBox_RB_btn.setObjectName(u"comboBox_RB_btn")
        self.comboBox_RB_btn.setGeometry(QRect(774, 140, 250, 30))
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.comboBox_RB_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_RB_btn.setSizePolicy(sizePolicy8)
        self.comboBox_RB_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_RB_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_RB_btn.setFont(font1)
        self.comboBox_RB_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_RB_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_left_stick_btn.addItem("")
        self.comboBox_left_stick_btn.setObjectName(u"comboBox_left_stick_btn")
        self.comboBox_left_stick_btn.setGeometry(QRect(60, 512, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_left_stick_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_left_stick_btn.setSizePolicy(sizePolicy7)
        self.comboBox_left_stick_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_left_stick_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_left_stick_btn.setFont(font1)
        self.comboBox_left_stick_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_RT_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_RT_btn.addItem("")
        self.comboBox_RT_btn.setObjectName(u"comboBox_RT_btn")
        self.comboBox_RT_btn.setEnabled(False)
        self.comboBox_RT_btn.setGeometry(QRect(780, 96, 250, 30))
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.comboBox_RT_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_RT_btn.setSizePolicy(sizePolicy9)
        self.comboBox_RT_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_RT_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_RT_btn.setFont(font1)
        self.comboBox_RT_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_RT_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_x = QComboBox(self.kontrollerImgContainer)
        self.comboBox_left_stick_x.addItem("")
        self.comboBox_left_stick_x.setObjectName(u"comboBox_left_stick_x")
        self.comboBox_left_stick_x.setEnabled(False)
        self.comboBox_left_stick_x.setGeometry(QRect(20, 260, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_left_stick_x.sizePolicy().hasHeightForWidth())
        self.comboBox_left_stick_x.setSizePolicy(sizePolicy7)
        self.comboBox_left_stick_x.setMinimumSize(QSize(0, 30))
        self.comboBox_left_stick_x.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_left_stick_x.setFont(font1)
        self.comboBox_left_stick_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_x.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_menu_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_menu_btn.setObjectName(u"comboBox_menu_btn")
        self.comboBox_menu_btn.setGeometry(QRect(560, 10, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_menu_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_menu_btn.setSizePolicy(sizePolicy7)
        self.comboBox_menu_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_menu_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_menu_btn.setFont(font1)
        self.comboBox_menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_menu_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_right_stick_y = QComboBox(self.kontrollerImgContainer)
        self.comboBox_right_stick_y.addItem("")
        self.comboBox_right_stick_y.setObjectName(u"comboBox_right_stick_y")
        self.comboBox_right_stick_y.setEnabled(False)
        self.comboBox_right_stick_y.setGeometry(QRect(530, 506, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_right_stick_y.sizePolicy().hasHeightForWidth())
        self.comboBox_right_stick_y.setSizePolicy(sizePolicy7)
        self.comboBox_right_stick_y.setMinimumSize(QSize(0, 30))
        self.comboBox_right_stick_y.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_right_stick_y.setFont(font1)
        self.comboBox_right_stick_y.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_y.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_view_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_view_btn.setObjectName(u"comboBox_view_btn")
        self.comboBox_view_btn.setGeometry(QRect(280, 8, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_view_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_view_btn.setSizePolicy(sizePolicy7)
        self.comboBox_view_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_view_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_view_btn.setFont(font1)
        self.comboBox_view_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_view_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_B_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_B_btn.setObjectName(u"comboBox_B_btn")
        self.comboBox_B_btn.setGeometry(QRect(810, 260, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_B_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_B_btn.setSizePolicy(sizePolicy7)
        self.comboBox_B_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_B_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_B_btn.setFont(font1)
        self.comboBox_B_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_B_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_X_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_X_btn.setObjectName(u"comboBox_X_btn")
        self.comboBox_X_btn.setGeometry(QRect(817, 319, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_X_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_X_btn.setSizePolicy(sizePolicy7)
        self.comboBox_X_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_X_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_X_btn.setFont(font1)
        self.comboBox_X_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_X_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_directional_pad_updown = QComboBox(self.kontrollerImgContainer)
        self.comboBox_directional_pad_updown.addItem("")
        self.comboBox_directional_pad_updown.setObjectName(u"comboBox_directional_pad_updown")
        self.comboBox_directional_pad_updown.setEnabled(False)
        self.comboBox_directional_pad_updown.setGeometry(QRect(310, 540, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_directional_pad_updown.sizePolicy().hasHeightForWidth())
        self.comboBox_directional_pad_updown.setSizePolicy(sizePolicy7)
        self.comboBox_directional_pad_updown.setMinimumSize(QSize(0, 30))
        self.comboBox_directional_pad_updown.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_directional_pad_updown.setFont(font1)
        self.comboBox_directional_pad_updown.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_directional_pad_updown.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_A_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_A_btn.setObjectName(u"comboBox_A_btn")
        self.comboBox_A_btn.setGeometry(QRect(836, 390, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_A_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_A_btn.setSizePolicy(sizePolicy7)
        self.comboBox_A_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_A_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_A_btn.setFont(font1)
        self.comboBox_A_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_A_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_y = QComboBox(self.kontrollerImgContainer)
        self.comboBox_left_stick_y.addItem("")
        self.comboBox_left_stick_y.setObjectName(u"comboBox_left_stick_y")
        self.comboBox_left_stick_y.setEnabled(False)
        self.comboBox_left_stick_y.setGeometry(QRect(0, 199, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_left_stick_y.sizePolicy().hasHeightForWidth())
        self.comboBox_left_stick_y.setSizePolicy(sizePolicy7)
        self.comboBox_left_stick_y.setMinimumSize(QSize(0, 30))
        self.comboBox_left_stick_y.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_left_stick_y.setFont(font1)
        self.comboBox_left_stick_y.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_y.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_LB_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_LB_btn.addItem("")
        self.comboBox_LB_btn.setObjectName(u"comboBox_LB_btn")
        self.comboBox_LB_btn.setGeometry(QRect(70, 144, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_LB_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_LB_btn.setSizePolicy(sizePolicy7)
        self.comboBox_LB_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_LB_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_LB_btn.setFont(font1)
        self.comboBox_LB_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_LB_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_Y_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_Y_btn.addItem("")
        self.comboBox_Y_btn.setObjectName(u"comboBox_Y_btn")
        self.comboBox_Y_btn.setGeometry(QRect(810, 200, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_Y_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_Y_btn.setSizePolicy(sizePolicy7)
        self.comboBox_Y_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_Y_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_Y_btn.setFont(font1)
        self.comboBox_Y_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_Y_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_LT_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_LT_btn.addItem("")
        self.comboBox_LT_btn.setObjectName(u"comboBox_LT_btn")
        self.comboBox_LT_btn.setEnabled(False)
        self.comboBox_LT_btn.setGeometry(QRect(100, 100, 250, 30))
        sizePolicy7.setHeightForWidth(self.comboBox_LT_btn.sizePolicy().hasHeightForWidth())
        self.comboBox_LT_btn.setSizePolicy(sizePolicy7)
        self.comboBox_LT_btn.setMinimumSize(QSize(0, 30))
        self.comboBox_LT_btn.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_LT_btn.setFont(font1)
        self.comboBox_LT_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_LT_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn_kontroller_info = QPushButton(self.kontrollerImgContainer)
        self.btn_kontroller_info.setObjectName(u"btn_kontroller_info")
        self.btn_kontroller_info.setGeometry(QRect(-20, 0, 191, 45))
        self.btn_kontroller_info.setMinimumSize(QSize(0, 0))
        self.btn_kontroller_info.setFont(font1)
        self.btn_kontroller_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_kontroller_info.setStyleSheet(u"QPushButton { background-color: transparent; border: 0px; } QToolTip { background-color: rgba(255, 255, 255, 240) } ")
        icon15 = QIcon()
        icon15.addFile(u":/images/images/infoicon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_kontroller_info.setIcon(icon15)

        self.verticalLayout_19.addWidget(self.kontrollerImgContainer)

        self.frame_4 = QFrame(self.kontrollerRows)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_save_profile = QPushButton(self.frame_4)
        self.btn_save_profile.setObjectName(u"btn_save_profile")
        self.btn_save_profile.setEnabled(False)
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.btn_save_profile.sizePolicy().hasHeightForWidth())
        self.btn_save_profile.setSizePolicy(sizePolicy10)
        self.btn_save_profile.setMinimumSize(QSize(150, 45))
        self.btn_save_profile.setFont(font1)
        self.btn_save_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_profile.setStyleSheet(u"QPushButton:disabled {\n"
"	background-color: rgb(52, 53, 58);\n"
"	color: rgba(255, 255, 255, 55);\n"
"	border: 2px solid rgba(26, 27, 33, 55);\n"
"	border-radius: 5px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_profile.setIcon(icon16)

        self.verticalLayout_9.addWidget(self.btn_save_profile, 0, Qt.AlignRight|Qt.AlignTop)

        self.text_ingen_endringer = QLabel(self.frame_4)
        self.text_ingen_endringer.setObjectName(u"text_ingen_endringer")
        self.text_ingen_endringer.setMinimumSize(QSize(0, 10))
        self.text_ingen_endringer.setBaseSize(QSize(0, 0))
        self.text_ingen_endringer.setFont(font)
        self.text_ingen_endringer.setStyleSheet(u"color: rgb(127, 127, 130); padding: 5px;")
        self.text_ingen_endringer.setLineWidth(1)
        self.text_ingen_endringer.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.text_ingen_endringer.setWordWrap(False)
        self.text_ingen_endringer.setIndent(0)

        self.verticalLayout_9.addWidget(self.text_ingen_endringer, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_19.addWidget(self.frame_4)


        self.horizontalLayout_9.addWidget(self.kontrollerRows)


        self.verticalLayout_18.addWidget(self.kontrollerContainer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_8.addWidget(self.scrollArea)


        self.verticalLayout_20.addWidget(self.hovedFrameColumn)

        self.stackedWidget.addWidget(self.kontroller)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(0, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)
        self.grip_icon = QLabel(self.frame_size_grip)
        self.grip_icon.setObjectName(u"grip_icon")
        self.grip_icon.setGeometry(QRect(-15, 0, 40, 20))
        self.grip_icon.setPixmap(QPixmap(u":/icons/images/icons/cil-size-grip.png"))
        self.grip_icon.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_14.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.btn_regulator_elektronikk.setDefault(False)
        self.btn_regulator_manipulator.setDefault(False)
        self.btn_reset_sikring_manipulator.setDefault(False)
        self.btn_regulator_thrustere.setDefault(False)
        self.btn_reset_sikring_thrustere.setDefault(False)
        self.btn_reset_sikring_elektronikk.setDefault(False)
        self.btn_reset_nullpunkt.setDefault(False)
        self.btn_reset_tidtaker.setDefault(False)
        self.btn_start_tidtaker.setDefault(False)
        self.btn_lav_struping.setDefault(False)
        self.btn_havbunn_tilt_opp.setDefault(False)
        self.btn_havbunn_tilt_ned.setDefault(False)
        self.btn_front_tilt_opp.setDefault(False)
        self.btn_front_tilt_ned.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.btn_informasjon.setText("")
#if QT_CONFIG(shortcut)
        self.btn_informasjon.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.btn_kontroller.setText("")
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"UiS Subsea", None))
#if QT_CONFIG(tooltip)
        self.btn_zoom_in.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_zoom_in.setText("")
#if QT_CONFIG(tooltip)
        self.btn_zoom_out.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_zoom_out.setText("")
#if QT_CONFIG(tooltip)
        self.btn_change_theme.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_change_theme.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.title_kjoremodus.setText(QCoreApplication.translate("MainWindow", u"KJ\u00d8REMODUS", None))
        self.text_kjoring.setText(QCoreApplication.translate("MainWindow", u"Velg kj\u00f8remodus", None))
        self.text_kjoring.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.btn_manuell.setText(QCoreApplication.translate("MainWindow", u"Manuell kj\u00f8ring", None))
        self.btn_finn_fisk.setText(QCoreApplication.translate("MainWindow", u"Finn fisk (og kalkul\u00e9r n\u00e6rmeste avstand)", None))
        self.btn_autonom_merd.setText(QCoreApplication.translate("MainWindow", u"Autonom merd", None))
        self.btn_bildemoasaikk.setText(QCoreApplication.translate("MainWindow", u"Bildemoasaikk", None))
        self.btn_autonom_parkering.setText(QCoreApplication.translate("MainWindow", u"Autonom parkering", None))
        self.text_bildebehandlingsmodus.setText(QCoreApplication.translate("MainWindow", u"Bildebehandling som kj\u00f8res:", None))
        self.label_bildebehandlingsmodus.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_bildebehandlingsmodus.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_bildebehandlingsmodus.setProperty("whiteBg", "")
        self.label_bildebehandlingsmodus.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.label_effekt_manipulator.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_effekt_manipulator.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_effekt_manipulator.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.text_gjsnitttemp.setText(QCoreApplication.translate("MainWindow", u"Gj.snitt:", None))
        self.text_gjsnitttemp.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
#if QT_CONFIG(tooltip)
        self.btn_regulator_elektronikk.setToolTip(QCoreApplication.translate("MainWindow", u"Skru av regulering.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_regulator_elektronikk.setText(QCoreApplication.translate("MainWindow", u"Av / P\u00e5", None))
#if QT_CONFIG(tooltip)
        self.btn_regulator_manipulator.setToolTip(QCoreApplication.translate("MainWindow", u"Skru av regulering.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_regulator_manipulator.setText(QCoreApplication.translate("MainWindow", u"Av / P\u00e5", None))
#if QT_CONFIG(tooltip)
        self.btn_reset_sikring_manipulator.setToolTip(QCoreApplication.translate("MainWindow", u"Reset regulering.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset_sikring_manipulator.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.text_effekt_thrustere.setText(QCoreApplication.translate("MainWindow", u"Thrustere:", None))
        self.text_effekt_thrustere.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
#if QT_CONFIG(tooltip)
        self.btn_regulator_thrustere.setToolTip(QCoreApplication.translate("MainWindow", u"Skru av regulering.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_regulator_thrustere.setText(QCoreApplication.translate("MainWindow", u"Av / P\u00e5", None))
        self.title_effektforbruk.setText(QCoreApplication.translate("MainWindow", u"EFFEKTFORBRUK", None))
        self.label_effekt_elektronikk.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_effekt_elektronikk.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_effekt_elektronikk.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.text_dybde.setText(QCoreApplication.translate("MainWindow", u"Dybde:", None))
        self.text_dybde.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.text_effekt_manipulator.setText(QCoreApplication.translate("MainWindow", u"Manipulator:", None))
        self.text_effekt_manipulator.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
#if QT_CONFIG(tooltip)
        self.btn_reset_sikring_thrustere.setToolTip(QCoreApplication.translate("MainWindow", u"Reset regulering.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset_sikring_thrustere.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.btn_reset_sikring_elektronikk.setToolTip(QCoreApplication.translate("MainWindow", u"Reset regulering.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset_sikring_elektronikk.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.text_tidtaker.setText(QCoreApplication.translate("MainWindow", u"Tidtaker:", None))
        self.text_tidtaker.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.label_temp_ROV_hovedkort.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_temp_ROV_hovedkort.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_temp_ROV_hovedkort.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.label_dybde.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_dybde.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_dybde.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.label_temp_ROV_kraftkort.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_temp_ROV_kraftkort.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_temp_ROV_kraftkort.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.label_gjsnitt_temp_ROV.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_gjsnitt_temp_ROV.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_gjsnitt_temp_ROV.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.label_temp_ROV_sensorkort.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_temp_ROV_sensorkort.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_temp_ROV_sensorkort.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.text_hovedkort.setText(QCoreApplication.translate("MainWindow", u"Hovedkort:", None))
        self.text_hovedkort.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.title_temp_ROV.setText(QCoreApplication.translate("MainWindow", u"TEMPERATUR I ROV", None))
        self.text_effekt_elektronikk.setText(QCoreApplication.translate("MainWindow", u"Elektronikk:", None))
        self.text_effekt_elektronikk.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.text_kraftkort.setText(QCoreApplication.translate("MainWindow", u"Kraftkort:", None))
        self.text_kraftkort.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.label_effekt_thrustere.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_effekt_thrustere.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_effekt_thrustere.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.text_sensorkort.setText(QCoreApplication.translate("MainWindow", u"Sensorkort:", None))
        self.text_sensorkort.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
#if QT_CONFIG(tooltip)
        self.label_tid.setToolTip(QCoreApplication.translate("MainWindow", u"Tid fra ROV-en starter.", None))
#endif // QT_CONFIG(tooltip)
        self.label_tid.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_tid.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_tid.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
#if QT_CONFIG(tooltip)
        self.btn_reset_nullpunkt.setToolTip(QCoreApplication.translate("MainWindow", u"Nullstill dybden, fra der ROV-en settes ut i vann.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset_nullpunkt.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.text_tid.setText(QCoreApplication.translate("MainWindow", u"Tid:", None))
        self.text_tid.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
#if QT_CONFIG(tooltip)
        self.btn_reset_tidtaker.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_reset_tidtaker.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.btn_start_tidtaker.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_start_tidtaker.setText(QCoreApplication.translate("MainWindow", u"Start / Stopp", None))
#if QT_CONFIG(tooltip)
        self.label_tidtaker.setToolTip(QCoreApplication.translate("MainWindow", u"Tiden til tidtakeren.", None))
#endif // QT_CONFIG(tooltip)
        self.label_tidtaker.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_tidtaker.setProperty("labelStyle", QCoreApplication.translate("MainWindow", u"blackBg", None))
        self.label_tidtaker.setProperty("labelStyle2", QCoreApplication.translate("MainWindow", u"whiteBg", None))
        self.label_lekkasje_varsel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">ADVARSEL:</span></p><p align=\"center\"><span style=\" font-size:24pt;\">VANNLEKKASJE I ROV</span></p></body></html>", None))
        self.title_motor.setText(QCoreApplication.translate("MainWindow", u"MOTORP\u00c5DRAG", None))
        self.img_manipulator_2.setText("")
        self.frame_VHB.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.frame_VHB_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_VHB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_HHB.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.frame_HHB_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_HHB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_VVB.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.frame_VVB_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_VVB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_VHF.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.frame_VHF_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_VHF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_HVF.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.frame_HVF_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_HVF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_HHF.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.frame_HHF_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_HHF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_VVF.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.frame_VVF_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_VVF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_HVB.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.frame_HVB_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_HVB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.text_rov.setText(QCoreApplication.translate("MainWindow", u"ROV", None))
        self.text_rov.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.text_struping_thrustere.setText(QCoreApplication.translate("MainWindow", u"Struping thrustere:", None))
        self.text_struping_thrustere.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.frame_struping.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.struping_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_struping.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_lav_struping.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_lav_struping.setText(QCoreApplication.translate("MainWindow", u"Lav struping", None))
        self.img_manipulator.setText("")
        self.frame_mani_1.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.mani_circle_1.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_mani_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_mani_3.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.mani_circle_3.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_mani_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_mani_2.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.mani_circle_2.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_mani_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.text_manipulator.setText(QCoreApplication.translate("MainWindow", u"MANIPULATOR", None))
        self.text_manipulator.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.frame_lys_forward.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.lys_forward_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_lys_forward.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.frame_lys_down.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"outerCircle", None))
        self.lys_down_circle.setProperty("frameStyle", QCoreApplication.translate("MainWindow", u"innerCircle", None))
        self.label_percentage_lys_down.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><span>0</span><span style=\"vertical-align:super;\">%</span></body></html>", None))
        self.lys_title.setText(QCoreApplication.translate("MainWindow", u"LYS", None))
        self.text_lys_down.setText(QCoreApplication.translate("MainWindow", u"Havbunnslys:", None))
        self.text_lys_down.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.text_lys_forward.setText(QCoreApplication.translate("MainWindow", u"Frontlys:", None))
        self.text_lys_forward.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.title_video.setText(QCoreApplication.translate("MainWindow", u"KAMERA", None))
        self.tite_kamera.setText(QCoreApplication.translate("MainWindow", u"Ta bilde", None))
        self.tite_kamera.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.btn_ta_bilde_havbunn.setText(QCoreApplication.translate("MainWindow", u" Havbunnskamera", None))
        self.btn_ta_bilde_frontkamera.setText(QCoreApplication.translate("MainWindow", u" Frontkamera", None))
        self.btn_slett_bilde.setText(QCoreApplication.translate("MainWindow", u" Slett det siste bildet", None))
        self.btn_slett_bilde.setProperty("btnStyle", QCoreApplication.translate("MainWindow", u"redBtn", None))
        self.btn_start_video_havbunn.setText("")
        self.btn_start_video_frontkamera.setText("")
        self.text_frontkamera.setText(QCoreApplication.translate("MainWindow", u"Frontkamera: ", None))
        self.text_havbunnskamera.setText(QCoreApplication.translate("MainWindow", u"Havbunnskamera: ", None))
        self.title_start_videoopptak.setText(QCoreApplication.translate("MainWindow", u"Start og stopp videoopptak", None))
        self.title_start_videoopptak.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
#if QT_CONFIG(tooltip)
        self.btn_havbunn_tilt_opp.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_havbunn_tilt_opp.setText("")
#if QT_CONFIG(tooltip)
        self.btn_havbunn_tilt_ned.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_havbunn_tilt_ned.setText("")
#if QT_CONFIG(tooltip)
        self.btn_front_tilt_opp.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_front_tilt_opp.setText("")
#if QT_CONFIG(tooltip)
        self.btn_front_tilt_ned.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_front_tilt_ned.setText("")
        self.text_mani.setText(QCoreApplication.translate("MainWindow", u"Manipulator", None))
        self.text_hiv_regulering.setText(QCoreApplication.translate("MainWindow", u"Hiv-regulering", None))
        self.text_stamp_regulering.setText(QCoreApplication.translate("MainWindow", u"Stamp-regulering", None))
        self.text_rull_regulering.setText(QCoreApplication.translate("MainWindow", u"Rull-regulering", None))
        self.text_frontlys.setText(QCoreApplication.translate("MainWindow", u"Frontlys", None))
        self.text_havbunnslys.setText(QCoreApplication.translate("MainWindow", u"Havbunnslys", None))
        self.text_siste_bilde.setText(QCoreApplication.translate("MainWindow", u"Siste bilde tatt vises her:", None))
        self.text_siste_bilde.setProperty("colorStyle", QCoreApplication.translate("MainWindow", u"subTitle", None))
        self.recent_img.setText("")
        self.title_kontroller.setText(QCoreApplication.translate("MainWindow", u"ENDRE KONTROLLER-KNAPPER", None))
        self.text_kontroller_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Her kan du endre funksjonene til knappene p\u00e5 Xbox-kontrolleren.</p><p>Lag en ny profil hvis du \u00f8nsker \u00e5 lagre endringene til senere.</p></body></html>", None))
        self.text_velg_profil.setText(QCoreApplication.translate("MainWindow", u"Valgt profil:", None))
        self.comboBox_velg_profil.setItemText(0, QCoreApplication.translate("MainWindow", u"Standard profil", None))
        self.comboBox_velg_profil.setItemText(1, QCoreApplication.translate("MainWindow", u"Egendefinert profil", None))

#if QT_CONFIG(tooltip)
        self.btn_reset.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/images/eksempelbilde.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u" Reset", None))
        self.btn_make_new_profile.setText(QCoreApplication.translate("MainWindow", u" Lag ny profil", None))
        self.xbox_image.setText("")
        self.comboBox_right_stick_btn.setItemText(0, QCoreApplication.translate("MainWindow", u"Bytt mellom rotasjon/gir og kamera-tilt", None))

        self.comboBox_directional_pad_leftright.setItemText(0, QCoreApplication.translate("MainWindow", u"Manipulator rotasjon", None))

        self.comboBox_right_stick_x.setItemText(0, QCoreApplication.translate("MainWindow", u"Rotasjon/gir", None))

        self.comboBox_RB_btn.setItemText(0, QCoreApplication.translate("MainWindow", u"Gripe manipulator", None))

        self.comboBox_left_stick_btn.setItemText(0, QCoreApplication.translate("MainWindow", u"Manipulator av/p\u00e5", None))

        self.comboBox_RT_btn.setItemText(0, QCoreApplication.translate("MainWindow", u"ROV opp/hiv", None))

        self.comboBox_left_stick_x.setItemText(0, QCoreApplication.translate("MainWindow", u"Svai/sideveis forskyvning", None))

        self.comboBox_right_stick_y.setItemText(0, QCoreApplication.translate("MainWindow", u"Kamera-tilt", None))

        self.comboBox_directional_pad_updown.setItemText(0, QCoreApplication.translate("MainWindow", u"Manipulator inn/ut", None))

        self.comboBox_left_stick_y.setItemText(0, QCoreApplication.translate("MainWindow", u"Jag fremover/bakover", None))

        self.comboBox_LB_btn.setItemText(0, QCoreApplication.translate("MainWindow", u"Slippe manipulator", None))

        self.comboBox_Y_btn.setItemText(0, QCoreApplication.translate("MainWindow", u"Kamera-toggle", None))

        self.comboBox_LT_btn.setItemText(0, QCoreApplication.translate("MainWindow", u"ROV ned/hiv", None))

#if QT_CONFIG(tooltip)
        self.btn_kontroller_info.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/images/6dofkontroller.png\"/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_kontroller_info.setText(QCoreApplication.translate("MainWindow", u" Informasjon", None))
        self.btn_save_profile.setText(QCoreApplication.translate("MainWindow", u" Lagre", None))
        self.text_ingen_endringer.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Du har ikke gjort noen endringer enda.</p></body></html>", None))
        self.version.setText("")
        self.grip_icon.setText("")
    # retranslateUi

