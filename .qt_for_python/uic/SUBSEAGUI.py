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
        MainWindow.resize(1233, 855)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setEnabled(True)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(39, 35, 62);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-co"
                        "lor: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(74, 8"
                        "2, 91);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(74, 82, 91);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(31, 35, 41);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"\n"
"\n"
"/* Toggle Button */\n"
"#btn_toggle {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#btn_toggle:hover {"
                        "\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#btn_toggle:pressed {\n"
"	background-color: rgb(74, 82, 91);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(74, 82, 91)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-s"
                        "tyle: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(74, 82, 91);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(31, 35, 41);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"\n"
"\n"
"\n"
"/* "
                        "Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(74, 82, 91); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-l"
                        "eft: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(74, 82, 91);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(74, 82, 91);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, "
                        "49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(74, 82, 91);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* ///////////////////////////////////////////////////////////////////////////////////////////////"
                        "//\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(74, 82, 91);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(74, 82, 91);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: "
                        "rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
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
"	background: rgb(74, 82, 91);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: n"
                        "one;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicat"
                        "or:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, "
                        "43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(74, 82, 91);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QS"
                        "lider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(149, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(127, 123, 204);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(102, 91, 201);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(157, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(185, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    backg"
                        "round-color: rgb(102, 91, 201);\n"
"}\n"
"\n"
".QSlider {\n"
"    min-height: 68px;\n"
"    max-height: 68px;\n"
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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////////"
                        "/////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.appMargins = QGridLayout(self.styleSheet)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 40))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 40))
        self.topLogoInfo.setStyleSheet(u"b")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.topLogoInfo)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.topLogoInfo)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(35, 35))
        self.logo.setMaximumSize(QSize(35, 35))
        self.logo.setPixmap(QPixmap(u":/images/images/logo.png"))
        self.logo.setScaledContents(True)

        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.leftMenuFrame.setLineWidth(0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setGeometry(QRect(0, 3, 60, 45))
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.toggleBox)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMinimumSize(QSize(0, 45))
        self.btn_toggle.setFont(font)
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setLayoutDirection(Qt.LeftToRight)
        self.btn_toggle.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.btn_toggle)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setGeometry(QRect(0, 48, 60, 90))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_informasjon = QPushButton(self.topMenu)
        self.btn_informasjon.setObjectName(u"btn_informasjon")
        sizePolicy.setHeightForWidth(self.btn_informasjon.sizePolicy().hasHeightForWidth())
        self.btn_informasjon.setSizePolicy(sizePolicy)
        self.btn_informasjon.setMinimumSize(QSize(0, 45))
        self.btn_informasjon.setFont(font)
        self.btn_informasjon.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_informasjon.setLayoutDirection(Qt.LeftToRight)
        self.btn_informasjon.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")
        self.btn_informasjon.setCheckable(True)

        self.verticalLayout_8.addWidget(self.btn_informasjon)

        self.btn_kontroller = QPushButton(self.topMenu)
        self.btn_kontroller.setObjectName(u"btn_kontroller")
        sizePolicy.setHeightForWidth(self.btn_kontroller.sizePolicy().hasHeightForWidth())
        self.btn_kontroller.setSizePolicy(sizePolicy)
        self.btn_kontroller.setMinimumSize(QSize(0, 45))
        self.btn_kontroller.setFont(font)
        self.btn_kontroller.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_kontroller.setLayoutDirection(Qt.LeftToRight)
        self.btn_kontroller.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")
        icon = QIcon()
        icon.addFile(u"../../Downloads/uis-subsea/Subsea_QT_GUI/images/kontroller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_kontroller.setIcon(icon)
        self.btn_kontroller.setCheckable(True)

        self.verticalLayout_8.addWidget(self.btn_kontroller)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setGeometry(QRect(0, 793, 60, 45))
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

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
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
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
        self.titleRightInfo.setFont(font)
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
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setFont(font)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon1)
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
        self.pagesContainer.setStyleSheet(u"background-color: transparent;")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.pagesContainer)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.QVBoxLayout = QVBoxLayout()
        self.QVBoxLayout.setSpacing(0)
        self.QVBoxLayout.setObjectName(u"QVBoxLayout")
        self.QVBoxLayout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.horizontalLayout_16.addLayout(self.QVBoxLayout)

        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(1100, 16777215))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"background-color: transparent;")
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
        self.row.setFrameShape(QFrame.NoFrame)
        self.row.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.row)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.row)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContent = QWidget()
        self.scrollAreaWidgetContent.setObjectName(u"scrollAreaWidgetContent")
        self.scrollAreaWidgetContent.setGeometry(QRect(0, 0, 1164, 800))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContent)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.column1 = QFrame(self.scrollAreaWidgetContent)
        self.column1.setObjectName(u"column1")
        sizePolicy3.setHeightForWidth(self.column1.sizePolicy().hasHeightForWidth())
        self.column1.setSizePolicy(sizePolicy3)
        self.column1.setMinimumSize(QSize(500, 800))
        self.column1.setFrameShape(QFrame.NoFrame)
        self.column1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.column1)
        self.verticalLayout_26.setSpacing(7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.kjoringContainer = QFrame(self.column1)
        self.kjoringContainer.setObjectName(u"kjoringContainer")
        self.kjoringContainer.setMinimumSize(QSize(400, 0))
        self.kjoringContainer.setMaximumSize(QSize(0, 16777215))
        self.kjoringContainer.setStyleSheet(u"")
        self.kjoringContainer.setFrameShape(QFrame.NoFrame)
        self.kjoringContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.kjoringContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.title_kjoring = QLabel(self.kjoringContainer)
        self.title_kjoring.setObjectName(u"title_kjoring")
        self.title_kjoring.setMinimumSize(QSize(0, 20))
        self.title_kjoring.setFont(font)
        self.title_kjoring.setStyleSheet(u"")

        self.verticalLayout_15.addWidget(self.title_kjoring)

        self.label_kjoring = QLabel(self.kjoringContainer)
        self.label_kjoring.setObjectName(u"label_kjoring")
        self.label_kjoring.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.label_kjoring.setLineWidth(1)
        self.label_kjoring.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_15.addWidget(self.label_kjoring)

        self.btn_manuell = QPushButton(self.kjoringContainer)
        self.btn_manuell.setObjectName(u"btn_manuell")
        self.btn_manuell.setMinimumSize(QSize(150, 45))
        self.btn_manuell.setMaximumSize(QSize(16777215, 16777215))
        self.btn_manuell.setFont(font)
        self.btn_manuell.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_manuell.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); } QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: rgb(35, 41, 54); border: 1px solid rgb(23, 27, 37); }\n"
"")
        self.btn_manuell.setCheckable(True)
        self.btn_manuell.setChecked(False)
        self.btn_manuell.setAutoRepeat(False)

        self.verticalLayout_15.addWidget(self.btn_manuell)

        self.btn_finn_fisk = QPushButton(self.kjoringContainer)
        self.btn_finn_fisk.setObjectName(u"btn_finn_fisk")
        self.btn_finn_fisk.setMinimumSize(QSize(150, 45))
        self.btn_finn_fisk.setFont(font)
        self.btn_finn_fisk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_finn_fisk.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")

        self.verticalLayout_15.addWidget(self.btn_finn_fisk)

        self.btn_autonom_merd = QPushButton(self.kjoringContainer)
        self.btn_autonom_merd.setObjectName(u"btn_autonom_merd")
        self.btn_autonom_merd.setMinimumSize(QSize(150, 45))
        self.btn_autonom_merd.setFont(font)
        self.btn_autonom_merd.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_autonom_merd.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")

        self.verticalLayout_15.addWidget(self.btn_autonom_merd)

        self.btn_bildemoasaikk = QPushButton(self.kjoringContainer)
        self.btn_bildemoasaikk.setObjectName(u"btn_bildemoasaikk")
        self.btn_bildemoasaikk.setMinimumSize(QSize(150, 45))
        self.btn_bildemoasaikk.setFont(font)
        self.btn_bildemoasaikk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bildemoasaikk.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")

        self.verticalLayout_15.addWidget(self.btn_bildemoasaikk)

        self.btn_autonom_parkering = QPushButton(self.kjoringContainer)
        self.btn_autonom_parkering.setObjectName(u"btn_autonom_parkering")
        self.btn_autonom_parkering.setMinimumSize(QSize(150, 45))
        self.btn_autonom_parkering.setFont(font)
        self.btn_autonom_parkering.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_autonom_parkering.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")

        self.verticalLayout_15.addWidget(self.btn_autonom_parkering)

        self.bildebehandlingContainer = QHBoxLayout()
        self.bildebehandlingContainer.setObjectName(u"bildebehandlingContainer")
        self.text_bildebehandlingsmodus = QLabel(self.kjoringContainer)
        self.text_bildebehandlingsmodus.setObjectName(u"text_bildebehandlingsmodus")
        self.text_bildebehandlingsmodus.setMinimumSize(QSize(0, 20))
        self.text_bildebehandlingsmodus.setFont(font)
        self.text_bildebehandlingsmodus.setStyleSheet(u"")

        self.bildebehandlingContainer.addWidget(self.text_bildebehandlingsmodus)

        self.label_bildebehandlingsmodus = QLabel(self.kjoringContainer)
        self.label_bildebehandlingsmodus.setObjectName(u"label_bildebehandlingsmodus")
        self.label_bildebehandlingsmodus.setMinimumSize(QSize(40, 30))
        self.label_bildebehandlingsmodus.setMaximumSize(QSize(16777215, 16777215))
        self.label_bildebehandlingsmodus.setFont(font)
        self.label_bildebehandlingsmodus.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_bildebehandlingsmodus.setFrameShape(QFrame.NoFrame)
        self.label_bildebehandlingsmodus.setLineWidth(0)
        self.label_bildebehandlingsmodus.setMidLineWidth(0)
        self.label_bildebehandlingsmodus.setAlignment(Qt.AlignCenter)

        self.bildebehandlingContainer.addWidget(self.label_bildebehandlingsmodus)


        self.verticalLayout_15.addLayout(self.bildebehandlingContainer)


        self.verticalLayout_26.addWidget(self.kjoringContainer)

        self.bildeContainer2 = QFrame(self.column1)
        self.bildeContainer2.setObjectName(u"bildeContainer2")
        self.bildeContainer2.setMinimumSize(QSize(0, 0))
        self.bildeContainer2.setMaximumSize(QSize(16777215, 16777215))
        self.bildeContainer2.setFrameShape(QFrame.NoFrame)
        self.bildeContainer2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.bildeContainer2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_26.addWidget(self.bildeContainer2)

        self.rovContainer = QFrame(self.column1)
        self.rovContainer.setObjectName(u"rovContainer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.rovContainer.sizePolicy().hasHeightForWidth())
        self.rovContainer.setSizePolicy(sizePolicy4)
        self.rovContainer.setMinimumSize(QSize(0, 0))
        self.rovContainer.setMaximumSize(QSize(16777215, 300))
        self.rovContainer.setFrameShape(QFrame.NoFrame)
        self.rovContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.rovContainer)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.rovColumn2 = QFrame(self.rovContainer)
        self.rovColumn2.setObjectName(u"rovColumn2")
        self.rovColumn2.setMinimumSize(QSize(0, 0))
        self.rovColumn2.setMaximumSize(QSize(16777215, 16777215))
        self.rovColumn2.setFrameShape(QFrame.NoFrame)
        self.rovColumn2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.rovColumn2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.rovRow2 = QFrame(self.rovColumn2)
        self.rovRow2.setObjectName(u"rovRow2")
        self.rovRow2.setMinimumSize(QSize(240, 140))
        self.rovRow2.setMaximumSize(QSize(16777215, 200))
        self.rovRow2.setStyleSheet(u"QPushButton { background-color: rgb(109, 156, 113) } QPushButton#lys_av_btn, QPushButton#dybde_av_btn, QPushButton#helning_av_btn, QPushButton#mani_av_btn{ background-color: rgb(192, 108, 109) } QPushButton:hover { background-color: rgba(255, 255, 255, 110) } QPushButton#dybde_av_btn:hover, QPushButton#helning_av_btn:hover, QPushButton#mani_av_btn:hover { background-color: rgba(255, 255, 255, 110) }")
        self.rovRow2.setFrameShape(QFrame.NoFrame)
        self.rovRow2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.rovRow2)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.toogleBtnContainer = QFrame(self.rovRow2)
        self.toogleBtnContainer.setObjectName(u"toogleBtnContainer")
        self.toogleBtnContainer.setFrameShape(QFrame.NoFrame)
        self.toogleBtnContainer.setFrameShadow(QFrame.Raised)
        self.toggle_layout = QVBoxLayout(self.toogleBtnContainer)
        self.toggle_layout.setObjectName(u"toggle_layout")
        self.toggle_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_20.addWidget(self.toogleBtnContainer)

        self.toogleBtnLabels = QFrame(self.rovRow2)
        self.toogleBtnLabels.setObjectName(u"toogleBtnLabels")
        self.toogleBtnLabels.setFrameShape(QFrame.NoFrame)
        self.toogleBtnLabels.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.toogleBtnLabels)
        self.verticalLayout_32.setSpacing(7)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 10, 0, 10)
        self.text_mani = QLabel(self.toogleBtnLabels)
        self.text_mani.setObjectName(u"text_mani")
        self.text_mani.setFont(font)
        self.text_mani.setTextFormat(Qt.PlainText)

        self.verticalLayout_32.addWidget(self.text_mani)

        self.text_dybde_reg = QLabel(self.toogleBtnLabels)
        self.text_dybde_reg.setObjectName(u"text_dybde_reg")
        self.text_dybde_reg.setFont(font)
        self.text_dybde_reg.setTextFormat(Qt.PlainText)

        self.verticalLayout_32.addWidget(self.text_dybde_reg)

        self.text_helning = QLabel(self.toogleBtnLabels)
        self.text_helning.setObjectName(u"text_helning")
        self.text_helning.setMinimumSize(QSize(0, 0))
        self.text_helning.setFont(font)
        self.text_helning.setTextFormat(Qt.PlainText)

        self.verticalLayout_32.addWidget(self.text_helning)

        self.text_frontlys = QLabel(self.toogleBtnLabels)
        self.text_frontlys.setObjectName(u"text_frontlys")
        self.text_frontlys.setFont(font)
        self.text_frontlys.setTextFormat(Qt.RichText)

        self.verticalLayout_32.addWidget(self.text_frontlys)

        self.text_havbunnslys = QLabel(self.toogleBtnLabels)
        self.text_havbunnslys.setObjectName(u"text_havbunnslys")
        self.text_havbunnslys.setFont(font)
        self.text_havbunnslys.setTextFormat(Qt.RichText)

        self.verticalLayout_32.addWidget(self.text_havbunnslys)


        self.horizontalLayout_20.addWidget(self.toogleBtnLabels)


        self.verticalLayout_23.addWidget(self.rovRow2)


        self.gridLayout_5.addWidget(self.rovColumn2, 0, 1, 1, 1)

        self.rovColumn = QFrame(self.rovContainer)
        self.rovColumn.setObjectName(u"rovColumn")
        self.rovColumn.setMinimumSize(QSize(0, 0))
        self.rovColumn.setMaximumSize(QSize(16777215, 16777215))
        self.rovColumn.setFrameShape(QFrame.NoFrame)
        self.rovColumn.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.rovColumn)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_reset_sikring_thrustere = QPushButton(self.rovColumn)
        self.btn_reset_sikring_thrustere.setObjectName(u"btn_reset_sikring_thrustere")
        self.btn_reset_sikring_thrustere.setMinimumSize(QSize(45, 30))
        self.btn_reset_sikring_thrustere.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_sikring_thrustere.setFont(font)
        self.btn_reset_sikring_thrustere.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_sikring_thrustere.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); } QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: rgb(35, 41, 54); border: 1px solid rgb(23, 27, 37); }\n"
"")
        self.btn_reset_sikring_thrustere.setCheckable(False)
        self.btn_reset_sikring_thrustere.setChecked(False)
        self.btn_reset_sikring_thrustere.setAutoRepeat(False)

        self.gridLayout_4.addWidget(self.btn_reset_sikring_thrustere, 10, 3, 1, 1)

        self.btn_reset_nullpunkt = QPushButton(self.rovColumn)
        self.btn_reset_nullpunkt.setObjectName(u"btn_reset_nullpunkt")
        self.btn_reset_nullpunkt.setMinimumSize(QSize(45, 30))
        self.btn_reset_nullpunkt.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_nullpunkt.setFont(font)
        self.btn_reset_nullpunkt.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_nullpunkt.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); } QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: rgb(35, 41, 54); border: 1px solid rgb(23, 27, 37); }\n"
"")
        self.btn_reset_nullpunkt.setCheckable(False)
        self.btn_reset_nullpunkt.setChecked(False)
        self.btn_reset_nullpunkt.setAutoRepeat(False)

        self.gridLayout_4.addWidget(self.btn_reset_nullpunkt, 2, 2, 1, 2)

        self.btn_regulator_manipulator = QPushButton(self.rovColumn)
        self.btn_regulator_manipulator.setObjectName(u"btn_regulator_manipulator")
        self.btn_regulator_manipulator.setMinimumSize(QSize(45, 30))
        self.btn_regulator_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.btn_regulator_manipulator.setFont(font)
        self.btn_regulator_manipulator.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_regulator_manipulator.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); } QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: rgb(35, 41, 54); border: 1px solid rgb(23, 27, 37); }\n"
"")
        self.btn_regulator_manipulator.setCheckable(True)
        self.btn_regulator_manipulator.setChecked(False)
        self.btn_regulator_manipulator.setAutoRepeat(False)

        self.gridLayout_4.addWidget(self.btn_regulator_manipulator, 11, 2, 1, 1)

        self.label_effekt_thrustere = QLabel(self.rovColumn)
        self.label_effekt_thrustere.setObjectName(u"label_effekt_thrustere")
        self.label_effekt_thrustere.setMinimumSize(QSize(40, 30))
        self.label_effekt_thrustere.setMaximumSize(QSize(16777215, 16777215))
        self.label_effekt_thrustere.setFont(font)
        self.label_effekt_thrustere.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_effekt_thrustere.setFrameShape(QFrame.NoFrame)
        self.label_effekt_thrustere.setLineWidth(0)
        self.label_effekt_thrustere.setMidLineWidth(0)
        self.label_effekt_thrustere.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_effekt_thrustere, 10, 1, 1, 1)

        self.title_effektforbruk = QLabel(self.rovColumn)
        self.title_effektforbruk.setObjectName(u"title_effektforbruk")
        self.title_effektforbruk.setMinimumSize(QSize(100, 0))
        self.title_effektforbruk.setMaximumSize(QSize(16777215, 16777215))
        self.title_effektforbruk.setFont(font)
        self.title_effektforbruk.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.title_effektforbruk, 4, 0, 1, 1)

        self.text_effekt_elektronikk = QLabel(self.rovColumn)
        self.text_effekt_elektronikk.setObjectName(u"text_effekt_elektronikk")
        self.text_effekt_elektronikk.setMinimumSize(QSize(100, 30))
        self.text_effekt_elektronikk.setFont(font)
        self.text_effekt_elektronikk.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_effekt_elektronikk.setTextFormat(Qt.RichText)

        self.gridLayout_4.addWidget(self.text_effekt_elektronikk, 6, 0, 1, 1)

        self.label_effekt_manipulator = QLabel(self.rovColumn)
        self.label_effekt_manipulator.setObjectName(u"label_effekt_manipulator")
        self.label_effekt_manipulator.setMinimumSize(QSize(40, 30))
        self.label_effekt_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.label_effekt_manipulator.setFont(font)
        self.label_effekt_manipulator.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_effekt_manipulator.setFrameShape(QFrame.NoFrame)
        self.label_effekt_manipulator.setLineWidth(0)
        self.label_effekt_manipulator.setMidLineWidth(0)
        self.label_effekt_manipulator.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_effekt_manipulator, 11, 1, 1, 1)

        self.text_effekt_manipulator = QLabel(self.rovColumn)
        self.text_effekt_manipulator.setObjectName(u"text_effekt_manipulator")
        self.text_effekt_manipulator.setMinimumSize(QSize(100, 30))
        self.text_effekt_manipulator.setFont(font)
        self.text_effekt_manipulator.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_effekt_manipulator.setTextFormat(Qt.RichText)

        self.gridLayout_4.addWidget(self.text_effekt_manipulator, 11, 0, 1, 1)

        self.label_tid = QLabel(self.rovColumn)
        self.label_tid.setObjectName(u"label_tid")
        self.label_tid.setMinimumSize(QSize(70, 30))
        self.label_tid.setMaximumSize(QSize(70, 30))
        self.label_tid.setFont(font)
        self.label_tid.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_tid.setFrameShape(QFrame.NoFrame)
        self.label_tid.setLineWidth(0)
        self.label_tid.setMidLineWidth(0)
        self.label_tid.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_tid, 0, 1, 1, 1)

        self.label_dybde = QLabel(self.rovColumn)
        self.label_dybde.setObjectName(u"label_dybde")
        self.label_dybde.setMinimumSize(QSize(70, 30))
        self.label_dybde.setMaximumSize(QSize(70, 30))
        self.label_dybde.setFont(font)
        self.label_dybde.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_dybde.setFrameShape(QFrame.NoFrame)
        self.label_dybde.setLineWidth(0)
        self.label_dybde.setMidLineWidth(0)
        self.label_dybde.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_dybde, 2, 1, 1, 1)

        self.text_tid = QLabel(self.rovColumn)
        self.text_tid.setObjectName(u"text_tid")
        self.text_tid.setMinimumSize(QSize(100, 30))
        self.text_tid.setFont(font)
        self.text_tid.setTextFormat(Qt.RichText)

        self.gridLayout_4.addWidget(self.text_tid, 0, 0, 1, 1)

        self.text_effekt_thrustere = QLabel(self.rovColumn)
        self.text_effekt_thrustere.setObjectName(u"text_effekt_thrustere")
        self.text_effekt_thrustere.setMinimumSize(QSize(100, 30))
        self.text_effekt_thrustere.setFont(font)
        self.text_effekt_thrustere.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_effekt_thrustere.setTextFormat(Qt.PlainText)

        self.gridLayout_4.addWidget(self.text_effekt_thrustere, 10, 0, 1, 1)

        self.text_dybde = QLabel(self.rovColumn)
        self.text_dybde.setObjectName(u"text_dybde")
        self.text_dybde.setMinimumSize(QSize(100, 30))
        self.text_dybde.setFont(font)
        self.text_dybde.setTextFormat(Qt.RichText)

        self.gridLayout_4.addWidget(self.text_dybde, 2, 0, 1, 1)

        self.btn_reset_sikring_manipulator = QPushButton(self.rovColumn)
        self.btn_reset_sikring_manipulator.setObjectName(u"btn_reset_sikring_manipulator")
        self.btn_reset_sikring_manipulator.setMinimumSize(QSize(45, 30))
        self.btn_reset_sikring_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_sikring_manipulator.setFont(font)
        self.btn_reset_sikring_manipulator.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_sikring_manipulator.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); } QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: rgb(35, 41, 54); border: 1px solid rgb(23, 27, 37); }\n"
"")
        self.btn_reset_sikring_manipulator.setCheckable(False)
        self.btn_reset_sikring_manipulator.setChecked(False)
        self.btn_reset_sikring_manipulator.setAutoRepeat(False)

        self.gridLayout_4.addWidget(self.btn_reset_sikring_manipulator, 11, 3, 1, 1)

        self.btn_regulator_elektronikk = QPushButton(self.rovColumn)
        self.btn_regulator_elektronikk.setObjectName(u"btn_regulator_elektronikk")
        self.btn_regulator_elektronikk.setMinimumSize(QSize(45, 30))
        self.btn_regulator_elektronikk.setMaximumSize(QSize(16777215, 16777215))
        self.btn_regulator_elektronikk.setFont(font)
        self.btn_regulator_elektronikk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_regulator_elektronikk.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); } QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: rgb(35, 41, 54); border: 1px solid rgb(23, 27, 37); }\n"
"")
        self.btn_regulator_elektronikk.setCheckable(True)
        self.btn_regulator_elektronikk.setChecked(False)
        self.btn_regulator_elektronikk.setAutoRepeat(False)

        self.gridLayout_4.addWidget(self.btn_regulator_elektronikk, 6, 2, 1, 1)

        self.btn_regulator_thrustere = QPushButton(self.rovColumn)
        self.btn_regulator_thrustere.setObjectName(u"btn_regulator_thrustere")
        self.btn_regulator_thrustere.setMinimumSize(QSize(45, 30))
        self.btn_regulator_thrustere.setMaximumSize(QSize(16777215, 16777215))
        self.btn_regulator_thrustere.setFont(font)
        self.btn_regulator_thrustere.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_regulator_thrustere.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); } QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: rgb(35, 41, 54); border: 1px solid rgb(23, 27, 37); }\n"
"")
        self.btn_regulator_thrustere.setCheckable(True)
        self.btn_regulator_thrustere.setChecked(False)
        self.btn_regulator_thrustere.setAutoRepeat(False)

        self.gridLayout_4.addWidget(self.btn_regulator_thrustere, 10, 2, 1, 1)

        self.label_effekt_elektronikk = QLabel(self.rovColumn)
        self.label_effekt_elektronikk.setObjectName(u"label_effekt_elektronikk")
        self.label_effekt_elektronikk.setMinimumSize(QSize(40, 30))
        self.label_effekt_elektronikk.setMaximumSize(QSize(16777215, 16777215))
        self.label_effekt_elektronikk.setFont(font)
        self.label_effekt_elektronikk.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_effekt_elektronikk.setFrameShape(QFrame.NoFrame)
        self.label_effekt_elektronikk.setLineWidth(0)
        self.label_effekt_elektronikk.setMidLineWidth(0)
        self.label_effekt_elektronikk.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_effekt_elektronikk, 6, 1, 1, 1)

        self.text_orientering = QLabel(self.rovColumn)
        self.text_orientering.setObjectName(u"text_orientering")
        self.text_orientering.setMinimumSize(QSize(100, 30))
        self.text_orientering.setFont(font)
        self.text_orientering.setTextFormat(Qt.PlainText)

        self.gridLayout_4.addWidget(self.text_orientering, 1, 0, 1, 1)

        self.label_orientering = QLabel(self.rovColumn)
        self.label_orientering.setObjectName(u"label_orientering")
        self.label_orientering.setMinimumSize(QSize(70, 30))
        self.label_orientering.setMaximumSize(QSize(70, 30))
        self.label_orientering.setFont(font)
        self.label_orientering.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_orientering.setFrameShape(QFrame.NoFrame)
        self.label_orientering.setLineWidth(0)
        self.label_orientering.setMidLineWidth(0)
        self.label_orientering.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_orientering, 1, 1, 1, 1)

        self.btn_reset_sikring_elektronikk = QPushButton(self.rovColumn)
        self.btn_reset_sikring_elektronikk.setObjectName(u"btn_reset_sikring_elektronikk")
        self.btn_reset_sikring_elektronikk.setMinimumSize(QSize(45, 30))
        self.btn_reset_sikring_elektronikk.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reset_sikring_elektronikk.setFont(font)
        self.btn_reset_sikring_elektronikk.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset_sikring_elektronikk.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); } QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: rgb(35, 41, 54); border: 1px solid rgb(23, 27, 37); }\n"
"")
        self.btn_reset_sikring_elektronikk.setCheckable(False)
        self.btn_reset_sikring_elektronikk.setChecked(False)
        self.btn_reset_sikring_elektronikk.setAutoRepeat(False)

        self.gridLayout_4.addWidget(self.btn_reset_sikring_elektronikk, 6, 3, 1, 1)


        self.gridLayout_5.addWidget(self.rovColumn, 0, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.rovContainer)

        self.rovTempContainer = QFrame(self.column1)
        self.rovTempContainer.setObjectName(u"rovTempContainer")
        self.rovTempContainer.setMinimumSize(QSize(250, 0))
        self.rovTempContainer.setMaximumSize(QSize(16777215, 80))
        self.rovTempContainer.setFrameShape(QFrame.NoFrame)
        self.rovTempContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.rovTempContainer)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_temp_ROV = QLabel(self.rovTempContainer)
        self.label_temp_ROV.setObjectName(u"label_temp_ROV")
        self.label_temp_ROV.setMaximumSize(QSize(16777215, 16777215))
        self.label_temp_ROV.setFont(font)
        self.label_temp_ROV.setTextFormat(Qt.PlainText)

        self.verticalLayout_17.addWidget(self.label_temp_ROV)

        self.rovTempContainer2 = QFrame(self.rovTempContainer)
        self.rovTempContainer2.setObjectName(u"rovTempContainer2")
        self.rovTempContainer2.setMinimumSize(QSize(0, 0))
        self.rovTempContainer2.setMaximumSize(QSize(420, 100))
        self.rovTempContainer2.setFrameShape(QFrame.NoFrame)
        self.rovTempContainer2.setFrameShadow(QFrame.Raised)
        self.rovTempContainer2.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.rovTempContainer2)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.tempBtnContainer = QFrame(self.rovTempContainer2)
        self.tempBtnContainer.setObjectName(u"tempBtnContainer")
        self.tempBtnContainer.setMaximumSize(QSize(200, 16777215))
        self.tempBtnContainer.setFrameShape(QFrame.StyledPanel)
        self.tempBtnContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.tempBtnContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.label_temp_ROV_1 = QLabel(self.tempBtnContainer)
        self.label_temp_ROV_1.setObjectName(u"label_temp_ROV_1")
        self.label_temp_ROV_1.setMinimumSize(QSize(50, 30))
        self.label_temp_ROV_1.setMaximumSize(QSize(50, 30))
        self.label_temp_ROV_1.setFont(font)
        self.label_temp_ROV_1.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_temp_ROV_1.setFrameShape(QFrame.NoFrame)
        self.label_temp_ROV_1.setLineWidth(0)
        self.label_temp_ROV_1.setMidLineWidth(0)
        self.label_temp_ROV_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_temp_ROV_1)

        self.labe_temp_ROV_2 = QLabel(self.tempBtnContainer)
        self.labe_temp_ROV_2.setObjectName(u"labe_temp_ROV_2")
        self.labe_temp_ROV_2.setMinimumSize(QSize(50, 30))
        self.labe_temp_ROV_2.setMaximumSize(QSize(50, 30))
        self.labe_temp_ROV_2.setFont(font)
        self.labe_temp_ROV_2.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.labe_temp_ROV_2.setFrameShape(QFrame.NoFrame)
        self.labe_temp_ROV_2.setLineWidth(0)
        self.labe_temp_ROV_2.setMidLineWidth(0)
        self.labe_temp_ROV_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.labe_temp_ROV_2)

        self.label_temp_ROV_3 = QLabel(self.tempBtnContainer)
        self.label_temp_ROV_3.setObjectName(u"label_temp_ROV_3")
        self.label_temp_ROV_3.setMinimumSize(QSize(50, 30))
        self.label_temp_ROV_3.setMaximumSize(QSize(50, 30))
        self.label_temp_ROV_3.setFont(font)
        self.label_temp_ROV_3.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_temp_ROV_3.setFrameShape(QFrame.NoFrame)
        self.label_temp_ROV_3.setLineWidth(0)
        self.label_temp_ROV_3.setMidLineWidth(0)
        self.label_temp_ROV_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_temp_ROV_3)


        self.horizontalLayout_14.addWidget(self.tempBtnContainer)

        self.text_gjsnitttemp = QLabel(self.rovTempContainer2)
        self.text_gjsnitttemp.setObjectName(u"text_gjsnitttemp")
        self.text_gjsnitttemp.setMinimumSize(QSize(150, 0))
        self.text_gjsnitttemp.setMaximumSize(QSize(100, 16777215))
        self.text_gjsnitttemp.setFont(font)
        self.text_gjsnitttemp.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_gjsnitttemp.setTextFormat(Qt.PlainText)
        self.text_gjsnitttemp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.text_gjsnitttemp)

        self.label_gjsnitt_temp_ROV = QLabel(self.rovTempContainer2)
        self.label_gjsnitt_temp_ROV.setObjectName(u"label_gjsnitt_temp_ROV")
        self.label_gjsnitt_temp_ROV.setMinimumSize(QSize(50, 30))
        self.label_gjsnitt_temp_ROV.setMaximumSize(QSize(50, 30))
        self.label_gjsnitt_temp_ROV.setFont(font)
        self.label_gjsnitt_temp_ROV.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_gjsnitt_temp_ROV.setFrameShape(QFrame.NoFrame)
        self.label_gjsnitt_temp_ROV.setLineWidth(0)
        self.label_gjsnitt_temp_ROV.setMidLineWidth(0)
        self.label_gjsnitt_temp_ROV.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_gjsnitt_temp_ROV)


        self.verticalLayout_17.addWidget(self.rovTempContainer2)


        self.verticalLayout_26.addWidget(self.rovTempContainer)

        self.vannlekkContainer = QFrame(self.column1)
        self.vannlekkContainer.setObjectName(u"vannlekkContainer")
        self.vannlekkContainer.setMinimumSize(QSize(0, 0))
        self.vannlekkContainer.setMaximumSize(QSize(16777215, 80))
        self.vannlekkContainer.setFrameShape(QFrame.NoFrame)
        self.vannlekkContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.vannlekkContainer)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.title_vannlekk = QLabel(self.vannlekkContainer)
        self.title_vannlekk.setObjectName(u"title_vannlekk")
        self.title_vannlekk.setMaximumSize(QSize(16777215, 16777215))
        self.title_vannlekk.setFont(font)
        self.title_vannlekk.setTextFormat(Qt.PlainText)

        self.verticalLayout_21.addWidget(self.title_vannlekk)

        self.vannlekkBtnContainer = QFrame(self.vannlekkContainer)
        self.vannlekkBtnContainer.setObjectName(u"vannlekkBtnContainer")
        self.vannlekkBtnContainer.setMinimumSize(QSize(0, 0))
        self.vannlekkBtnContainer.setMaximumSize(QSize(300, 100))
        self.vannlekkBtnContainer.setFrameShape(QFrame.NoFrame)
        self.vannlekkBtnContainer.setFrameShadow(QFrame.Raised)
        self.vannlekkBtnContainer.setLineWidth(0)
        self.horizontalLayout_15 = QHBoxLayout(self.vannlekkBtnContainer)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.vannlekkBtnContainer2 = QFrame(self.vannlekkBtnContainer)
        self.vannlekkBtnContainer2.setObjectName(u"vannlekkBtnContainer2")
        self.vannlekkBtnContainer2.setMaximumSize(QSize(190, 16777215))
        self.vannlekkBtnContainer2.setFrameShape(QFrame.NoFrame)
        self.vannlekkBtnContainer2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.vannlekkBtnContainer2)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_vannlekk_1 = QLabel(self.vannlekkBtnContainer2)
        self.label_vannlekk_1.setObjectName(u"label_vannlekk_1")
        self.label_vannlekk_1.setMinimumSize(QSize(50, 30))
        self.label_vannlekk_1.setMaximumSize(QSize(50, 30))
        self.label_vannlekk_1.setFont(font)
        self.label_vannlekk_1.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_vannlekk_1.setFrameShape(QFrame.NoFrame)
        self.label_vannlekk_1.setLineWidth(0)
        self.label_vannlekk_1.setMidLineWidth(0)
        self.label_vannlekk_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_vannlekk_1)

        self.label_vannlekk_2 = QLabel(self.vannlekkBtnContainer2)
        self.label_vannlekk_2.setObjectName(u"label_vannlekk_2")
        self.label_vannlekk_2.setMinimumSize(QSize(50, 30))
        self.label_vannlekk_2.setMaximumSize(QSize(50, 30))
        self.label_vannlekk_2.setFont(font)
        self.label_vannlekk_2.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_vannlekk_2.setFrameShape(QFrame.NoFrame)
        self.label_vannlekk_2.setLineWidth(0)
        self.label_vannlekk_2.setMidLineWidth(0)
        self.label_vannlekk_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_vannlekk_2)

        self.label_vannlekk_3 = QLabel(self.vannlekkBtnContainer2)
        self.label_vannlekk_3.setObjectName(u"label_vannlekk_3")
        self.label_vannlekk_3.setMinimumSize(QSize(50, 30))
        self.label_vannlekk_3.setMaximumSize(QSize(50, 30))
        self.label_vannlekk_3.setFont(font)
        self.label_vannlekk_3.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.label_vannlekk_3.setFrameShape(QFrame.NoFrame)
        self.label_vannlekk_3.setLineWidth(0)
        self.label_vannlekk_3.setMidLineWidth(0)
        self.label_vannlekk_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_vannlekk_3)


        self.horizontalLayout_15.addWidget(self.vannlekkBtnContainer2)


        self.verticalLayout_21.addWidget(self.vannlekkBtnContainer)


        self.verticalLayout_26.addWidget(self.vannlekkContainer)


        self.horizontalLayout_10.addWidget(self.column1)

        self.column2 = QFrame(self.scrollAreaWidgetContent)
        self.column2.setObjectName(u"column2")
        self.column2.setMinimumSize(QSize(350, 0))
        self.column2.setMaximumSize(QSize(16777215, 16777215))
        self.column2.setFrameShape(QFrame.NoFrame)
        self.column2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.column2)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.motorpaadragContainer = QFrame(self.column2)
        self.motorpaadragContainer.setObjectName(u"motorpaadragContainer")
        self.motorpaadragContainer.setMinimumSize(QSize(0, 0))
        self.motorpaadragContainer.setMaximumSize(QSize(16777215, 540))
        self.motorpaadragContainer.setFrameShape(QFrame.NoFrame)
        self.motorpaadragContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.motorpaadragContainer)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.title_motor = QLabel(self.motorpaadragContainer)
        self.title_motor.setObjectName(u"title_motor")
        self.title_motor.setFont(font)

        self.verticalLayout_31.addWidget(self.title_motor)

        self.text_rov = QLabel(self.motorpaadragContainer)
        self.text_rov.setObjectName(u"text_rov")
        self.text_rov.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_rov.setLineWidth(1)
        self.text_rov.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_31.addWidget(self.text_rov)

        self.motorContainter = QFrame(self.motorpaadragContainer)
        self.motorContainter.setObjectName(u"motorContainter")
        self.motorContainter.setMinimumSize(QSize(0, 260))
        self.motorContainter.setFrameShape(QFrame.NoFrame)
        self.motorContainter.setFrameShadow(QFrame.Raised)
        self.img_motor = QLabel(self.motorContainter)
        self.img_motor.setObjectName(u"img_motor")
        self.img_motor.setGeometry(QRect(100, 30, 141, 181))
        self.img_motor.setMinimumSize(QSize(0, 0))
        self.img_motor.setMaximumSize(QSize(16777215, 16777215))
        self.img_motor.setSizeIncrement(QSize(0, 0))
        self.img_motor.setPixmap(QPixmap(u":/images/images/thrustere.png"))
        self.img_motor.setScaledContents(True)
        self.frame_VHF_2 = QFrame(self.motorContainter)
        self.frame_VHF_2.setObjectName(u"frame_VHF_2")
        self.frame_VHF_2.setGeometry(QRect(19, 11, 50, 51))
        self.frame_VHF_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.frame_VHF_2.setFrameShape(QFrame.StyledPanel)
        self.frame_VHF_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_VHF = QLabel(self.frame_VHF_2)
        self.label_percentage_VHF.setObjectName(u"label_percentage_VHF")
        self.label_percentage_VHF.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_VHF.setFont(font)
        self.label_percentage_VHF.setAutoFillBackground(False)
        self.label_percentage_VHF.setScaledContents(False)
        self.label_percentage_VHF.setAlignment(Qt.AlignCenter)
        self.label_percentage_VHF.setWordWrap(False)
        self.frame_VHF = QFrame(self.motorContainter)
        self.frame_VHF.setObjectName(u"frame_VHF")
        self.frame_VHF.setGeometry(QRect(14, 7, 60, 60))
        self.frame_VHF.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_VHF.setFrameShape(QFrame.NoFrame)
        self.frame_VHF.setFrameShadow(QFrame.Raised)
        self.frame_VVF = QFrame(self.motorContainter)
        self.frame_VVF.setObjectName(u"frame_VVF")
        self.frame_VVF.setGeometry(QRect(75, 25, 60, 60))
        self.frame_VVF.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_VVF.setFrameShape(QFrame.NoFrame)
        self.frame_VVF.setFrameShadow(QFrame.Raised)
        self.frame_VVF_2 = QFrame(self.motorContainter)
        self.frame_VVF_2.setObjectName(u"frame_VVF_2")
        self.frame_VVF_2.setGeometry(QRect(80, 30, 50, 50))
        self.frame_VVF_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.frame_VVF_2.setFrameShape(QFrame.NoFrame)
        self.frame_VVF_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_VVF = QLabel(self.frame_VVF_2)
        self.label_percentage_VVF.setObjectName(u"label_percentage_VVF")
        self.label_percentage_VVF.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_VVF.setFont(font)
        self.label_percentage_VVF.setAutoFillBackground(False)
        self.label_percentage_VVF.setScaledContents(False)
        self.label_percentage_VVF.setAlignment(Qt.AlignCenter)
        self.label_percentage_VVF.setWordWrap(False)
        self.frame_HHF_2 = QFrame(self.motorContainter)
        self.frame_HHF_2.setObjectName(u"frame_HHF_2")
        self.frame_HHF_2.setGeometry(QRect(270, 10, 50, 50))
        self.frame_HHF_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.frame_HHF_2.setFrameShape(QFrame.StyledPanel)
        self.frame_HHF_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_HHF = QLabel(self.frame_HHF_2)
        self.label_percentage_HHF.setObjectName(u"label_percentage_HHF")
        self.label_percentage_HHF.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_HHF.setFont(font)
        self.label_percentage_HHF.setAutoFillBackground(False)
        self.label_percentage_HHF.setScaledContents(False)
        self.label_percentage_HHF.setAlignment(Qt.AlignCenter)
        self.label_percentage_HHF.setWordWrap(False)
        self.frame_HHF = QFrame(self.motorContainter)
        self.frame_HHF.setObjectName(u"frame_HHF")
        self.frame_HHF.setGeometry(QRect(265, 5, 60, 60))
        self.frame_HHF.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_HHF.setFrameShape(QFrame.NoFrame)
        self.frame_HHF.setFrameShadow(QFrame.Raised)
        self.frame_HVF_2 = QFrame(self.motorContainter)
        self.frame_HVF_2.setObjectName(u"frame_HVF_2")
        self.frame_HVF_2.setGeometry(QRect(210, 30, 50, 50))
        self.frame_HVF_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.frame_HVF_2.setFrameShape(QFrame.StyledPanel)
        self.frame_HVF_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_HVF = QLabel(self.frame_HVF_2)
        self.label_percentage_HVF.setObjectName(u"label_percentage_HVF")
        self.label_percentage_HVF.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_HVF.setFont(font)
        self.label_percentage_HVF.setAutoFillBackground(False)
        self.label_percentage_HVF.setScaledContents(False)
        self.label_percentage_HVF.setAlignment(Qt.AlignCenter)
        self.label_percentage_HVF.setWordWrap(False)
        self.frame_HVF = QFrame(self.motorContainter)
        self.frame_HVF.setObjectName(u"frame_HVF")
        self.frame_HVF.setGeometry(QRect(205, 25, 60, 60))
        self.frame_HVF.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_HVF.setFrameShape(QFrame.NoFrame)
        self.frame_HVF.setFrameShadow(QFrame.Raised)
        self.frame_HVB_2 = QFrame(self.motorContainter)
        self.frame_HVB_2.setObjectName(u"frame_HVB_2")
        self.frame_HVB_2.setGeometry(QRect(220, 140, 50, 50))
        self.frame_HVB_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.frame_HVB_2.setFrameShape(QFrame.StyledPanel)
        self.frame_HVB_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_HVB = QLabel(self.frame_HVB_2)
        self.label_percentage_HVB.setObjectName(u"label_percentage_HVB")
        self.label_percentage_HVB.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_HVB.setFont(font)
        self.label_percentage_HVB.setAutoFillBackground(False)
        self.label_percentage_HVB.setScaledContents(False)
        self.label_percentage_HVB.setAlignment(Qt.AlignCenter)
        self.label_percentage_HVB.setWordWrap(False)
        self.frame_HVB = QFrame(self.motorContainter)
        self.frame_HVB.setObjectName(u"frame_HVB")
        self.frame_HVB.setGeometry(QRect(215, 135, 60, 60))
        self.frame_HVB.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_HVB.setFrameShape(QFrame.NoFrame)
        self.frame_HVB.setFrameShadow(QFrame.Raised)
        self.frame_HHB_2 = QFrame(self.motorContainter)
        self.frame_HHB_2.setObjectName(u"frame_HHB_2")
        self.frame_HHB_2.setGeometry(QRect(260, 185, 50, 50))
        self.frame_HHB_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.frame_HHB_2.setFrameShape(QFrame.StyledPanel)
        self.frame_HHB_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_HHB = QLabel(self.frame_HHB_2)
        self.label_percentage_HHB.setObjectName(u"label_percentage_HHB")
        self.label_percentage_HHB.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_HHB.setFont(font)
        self.label_percentage_HHB.setAutoFillBackground(False)
        self.label_percentage_HHB.setScaledContents(False)
        self.label_percentage_HHB.setAlignment(Qt.AlignCenter)
        self.label_percentage_HHB.setWordWrap(False)
        self.frame_HHB = QFrame(self.motorContainter)
        self.frame_HHB.setObjectName(u"frame_HHB")
        self.frame_HHB.setGeometry(QRect(255, 180, 60, 60))
        self.frame_HHB.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_HHB.setFrameShape(QFrame.NoFrame)
        self.frame_HHB.setFrameShadow(QFrame.Raised)
        self.frame_VVB = QFrame(self.motorContainter)
        self.frame_VVB.setObjectName(u"frame_VVB")
        self.frame_VVB.setGeometry(QRect(70, 160, 60, 60))
        self.frame_VVB.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_VVB.setFrameShape(QFrame.NoFrame)
        self.frame_VVB.setFrameShadow(QFrame.Raised)
        self.frame_VVB_2 = QFrame(self.motorContainter)
        self.frame_VVB_2.setObjectName(u"frame_VVB_2")
        self.frame_VVB_2.setGeometry(QRect(75, 165, 50, 50))
        self.frame_VVB_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.frame_VVB_2.setFrameShape(QFrame.StyledPanel)
        self.frame_VVB_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_VVB = QLabel(self.frame_VVB_2)
        self.label_percentage_VVB.setObjectName(u"label_percentage_VVB")
        self.label_percentage_VVB.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_VVB.setFont(font)
        self.label_percentage_VVB.setAutoFillBackground(False)
        self.label_percentage_VVB.setScaledContents(False)
        self.label_percentage_VVB.setAlignment(Qt.AlignCenter)
        self.label_percentage_VVB.setWordWrap(False)
        self.frame_VHB_2 = QFrame(self.motorContainter)
        self.frame_VHB_2.setObjectName(u"frame_VHB_2")
        self.frame_VHB_2.setGeometry(QRect(10, 190, 50, 50))
        self.frame_VHB_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.frame_VHB_2.setFrameShape(QFrame.StyledPanel)
        self.frame_VHB_2.setFrameShadow(QFrame.Raised)
        self.label_percentage_VHB = QLabel(self.frame_VHB_2)
        self.label_percentage_VHB.setObjectName(u"label_percentage_VHB")
        self.label_percentage_VHB.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_VHB.setFont(font)
        self.label_percentage_VHB.setAutoFillBackground(False)
        self.label_percentage_VHB.setScaledContents(False)
        self.label_percentage_VHB.setAlignment(Qt.AlignCenter)
        self.label_percentage_VHB.setWordWrap(False)
        self.frame_VHB = QFrame(self.motorContainter)
        self.frame_VHB.setObjectName(u"frame_VHB")
        self.frame_VHB.setGeometry(QRect(5, 185, 60, 60))
        self.frame_VHB.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_VHB.setFrameShape(QFrame.NoFrame)
        self.frame_VHB.setFrameShadow(QFrame.Raised)
        self.img_motor.raise_()
        self.frame_VHB.raise_()
        self.frame_HVB.raise_()
        self.frame_HHB.raise_()
        self.frame_HHF.raise_()
        self.frame_HVF.raise_()
        self.frame_VHF.raise_()
        self.frame_VHF_2.raise_()
        self.frame_VVF.raise_()
        self.frame_VVF_2.raise_()
        self.frame_HHF_2.raise_()
        self.frame_HVF_2.raise_()
        self.frame_HVB_2.raise_()
        self.frame_HHB_2.raise_()
        self.frame_VVB.raise_()
        self.frame_VVB_2.raise_()
        self.frame_VHB_2.raise_()

        self.verticalLayout_31.addWidget(self.motorContainter)

        self.text_manipulator = QLabel(self.motorpaadragContainer)
        self.text_manipulator.setObjectName(u"text_manipulator")
        self.text_manipulator.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_manipulator.setLineWidth(1)
        self.text_manipulator.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_31.addWidget(self.text_manipulator)

        self.maniContainer = QFrame(self.motorpaadragContainer)
        self.maniContainer.setObjectName(u"maniContainer")
        self.maniContainer.setMinimumSize(QSize(0, 180))
        self.maniContainer.setFrameShape(QFrame.NoFrame)
        self.maniContainer.setFrameShadow(QFrame.Raised)
        self.img_manipulator = QLabel(self.maniContainer)
        self.img_manipulator.setObjectName(u"img_manipulator")
        self.img_manipulator.setGeometry(QRect(20, 10, 320, 150))
        self.img_manipulator.setMinimumSize(QSize(320, 0))
        self.img_manipulator.setMaximumSize(QSize(16777215, 16777215))
        self.img_manipulator.setSizeIncrement(QSize(0, 0))
        self.img_manipulator.setPixmap(QPixmap(u":/images/images/manipulator.png"))
        self.img_manipulator.setScaledContents(True)
        self.maniCircle2 = QFrame(self.maniContainer)
        self.maniCircle2.setObjectName(u"maniCircle2")
        self.maniCircle2.setGeometry(QRect(150, 20, 50, 50))
        self.maniCircle2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.maniCircle2.setFrameShape(QFrame.StyledPanel)
        self.maniCircle2.setFrameShadow(QFrame.Raised)
        self.label_percentage_mani_2 = QLabel(self.maniCircle2)
        self.label_percentage_mani_2.setObjectName(u"label_percentage_mani_2")
        self.label_percentage_mani_2.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_mani_2.setFont(font)
        self.label_percentage_mani_2.setAutoFillBackground(False)
        self.label_percentage_mani_2.setScaledContents(False)
        self.label_percentage_mani_2.setAlignment(Qt.AlignCenter)
        self.label_percentage_mani_2.setWordWrap(False)
        self.frame_mani_2 = QFrame(self.maniContainer)
        self.frame_mani_2.setObjectName(u"frame_mani_2")
        self.frame_mani_2.setGeometry(QRect(145, 15, 60, 60))
        self.frame_mani_2.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_mani_2.setFrameShape(QFrame.NoFrame)
        self.frame_mani_2.setFrameShadow(QFrame.Raised)
        self.frame_mani_3 = QFrame(self.maniContainer)
        self.frame_mani_3.setObjectName(u"frame_mani_3")
        self.frame_mani_3.setGeometry(QRect(200, 90, 60, 60))
        self.frame_mani_3.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_mani_3.setFrameShape(QFrame.NoFrame)
        self.frame_mani_3.setFrameShadow(QFrame.Raised)
        self.maniCircle3 = QFrame(self.maniContainer)
        self.maniCircle3.setObjectName(u"maniCircle3")
        self.maniCircle3.setGeometry(QRect(205, 94, 51, 51))
        self.maniCircle3.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.maniCircle3.setFrameShape(QFrame.StyledPanel)
        self.maniCircle3.setFrameShadow(QFrame.Raised)
        self.label_percentage_mani_3 = QLabel(self.maniCircle3)
        self.label_percentage_mani_3.setObjectName(u"label_percentage_mani_3")
        self.label_percentage_mani_3.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_mani_3.setFont(font)
        self.label_percentage_mani_3.setAutoFillBackground(False)
        self.label_percentage_mani_3.setScaledContents(False)
        self.label_percentage_mani_3.setAlignment(Qt.AlignCenter)
        self.label_percentage_mani_3.setWordWrap(False)
        self.frame_mani_1 = QFrame(self.maniContainer)
        self.frame_mani_1.setObjectName(u"frame_mani_1")
        self.frame_mani_1.setGeometry(QRect(54, 95, 60, 60))
        self.frame_mani_1.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_mani_1.setFrameShape(QFrame.NoFrame)
        self.frame_mani_1.setFrameShadow(QFrame.Raised)
        self.maniCircle = QFrame(self.maniContainer)
        self.maniCircle.setObjectName(u"maniCircle")
        self.maniCircle.setGeometry(QRect(59, 100, 50, 50))
        self.maniCircle.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.maniCircle.setFrameShape(QFrame.StyledPanel)
        self.maniCircle.setFrameShadow(QFrame.Raised)
        self.label_percentage_mani_1 = QLabel(self.maniCircle)
        self.label_percentage_mani_1.setObjectName(u"label_percentage_mani_1")
        self.label_percentage_mani_1.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_mani_1.setFont(font)
        self.label_percentage_mani_1.setAutoFillBackground(False)
        self.label_percentage_mani_1.setScaledContents(False)
        self.label_percentage_mani_1.setAlignment(Qt.AlignCenter)
        self.label_percentage_mani_1.setWordWrap(False)
        self.img_manipulator.raise_()
        self.frame_mani_2.raise_()
        self.maniCircle2.raise_()
        self.frame_mani_3.raise_()
        self.maniCircle3.raise_()
        self.frame_mani_1.raise_()
        self.maniCircle.raise_()

        self.verticalLayout_31.addWidget(self.maniContainer)

        self.maniContainer.raise_()
        self.motorContainter.raise_()
        self.title_motor.raise_()
        self.text_rov.raise_()
        self.text_manipulator.raise_()

        self.verticalLayout_16.addWidget(self.motorpaadragContainer)

        self.lysFrame = QFrame(self.column2)
        self.lysFrame.setObjectName(u"lysFrame")
        self.lysFrame.setMinimumSize(QSize(0, 0))
        self.lysFrame.setMaximumSize(QSize(16777215, 150))
        self.lysFrame.setFrameShape(QFrame.NoFrame)
        self.lysFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.lysFrame)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.lys_title = QLabel(self.lysFrame)
        self.lys_title.setObjectName(u"lys_title")
        self.lys_title.setMinimumSize(QSize(0, 0))
        self.lys_title.setMaximumSize(QSize(16777215, 16777215))
        self.lys_title.setFont(font)
        self.lys_title.setTextFormat(Qt.PlainText)

        self.verticalLayout_29.addWidget(self.lys_title)

        self.lysContainer = QFrame(self.lysFrame)
        self.lysContainer.setObjectName(u"lysContainer")
        self.lysContainer.setMinimumSize(QSize(0, 0))
        self.lysContainer.setMaximumSize(QSize(16777215, 16777215))
        self.lysContainer.setFrameShape(QFrame.NoFrame)
        self.lysContainer.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.lysContainer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.text_lys_down = QLabel(self.lysContainer)
        self.text_lys_down.setObjectName(u"text_lys_down")
        self.text_lys_down.setMinimumSize(QSize(50, 40))
        self.text_lys_down.setFont(font)
        self.text_lys_down.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_lys_down.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_lys_down, 2, 0, 1, 1)

        self.text_lys_forward = QLabel(self.lysContainer)
        self.text_lys_forward.setObjectName(u"text_lys_forward")
        self.text_lys_forward.setMinimumSize(QSize(50, 40))
        self.text_lys_forward.setFont(font)
        self.text_lys_forward.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_lys_forward.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.text_lys_forward, 0, 0, 1, 1)

        self.slider_lys_forward = QSlider(self.lysContainer)
        self.slider_lys_forward.setObjectName(u"slider_lys_forward")
        self.slider_lys_forward.setMinimumSize(QSize(0, 68))
        self.slider_lys_forward.setMaximumSize(QSize(150, 68))
        self.slider_lys_forward.setFont(font)
        self.slider_lys_forward.setStyleSheet(u"")
        self.slider_lys_forward.setMaximum(100)
        self.slider_lys_forward.setOrientation(Qt.Horizontal)
        self.slider_lys_forward.setInvertedAppearance(False)
        self.slider_lys_forward.setInvertedControls(False)
        self.slider_lys_forward.setTickPosition(QSlider.TicksBothSides)
        self.slider_lys_forward.setTickInterval(10)

        self.gridLayout_3.addWidget(self.slider_lys_forward, 0, 1, 1, 1)

        self.lysForwardFrame = QFrame(self.lysContainer)
        self.lysForwardFrame.setObjectName(u"lysForwardFrame")
        self.lysForwardFrame.setMinimumSize(QSize(70, 70))
        self.lysForwardFrame.setFrameShape(QFrame.NoFrame)
        self.lysForwardFrame.setFrameShadow(QFrame.Raised)
        self.frame_lys_forward = QFrame(self.lysForwardFrame)
        self.frame_lys_forward.setObjectName(u"frame_lys_forward")
        self.frame_lys_forward.setGeometry(QRect(2, 3, 60, 60))
        self.frame_lys_forward.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_lys_forward.setFrameShape(QFrame.NoFrame)
        self.frame_lys_forward.setFrameShadow(QFrame.Raised)
        self.lysForwardContainer = QFrame(self.lysForwardFrame)
        self.lysForwardContainer.setObjectName(u"lysForwardContainer")
        self.lysForwardContainer.setGeometry(QRect(7, 8, 50, 50))
        self.lysForwardContainer.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.lysForwardContainer.setFrameShape(QFrame.StyledPanel)
        self.lysForwardContainer.setFrameShadow(QFrame.Raised)
        self.label_percentage_lys_forward = QLabel(self.lysForwardContainer)
        self.label_percentage_lys_forward.setObjectName(u"label_percentage_lys_forward")
        self.label_percentage_lys_forward.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_lys_forward.setFont(font)
        self.label_percentage_lys_forward.setAutoFillBackground(False)
        self.label_percentage_lys_forward.setScaledContents(False)
        self.label_percentage_lys_forward.setAlignment(Qt.AlignCenter)
        self.label_percentage_lys_forward.setWordWrap(False)

        self.gridLayout_3.addWidget(self.lysForwardFrame, 0, 2, 1, 1)

        self.slider_lys_down = QSlider(self.lysContainer)
        self.slider_lys_down.setObjectName(u"slider_lys_down")
        self.slider_lys_down.setMinimumSize(QSize(0, 68))
        self.slider_lys_down.setMaximumSize(QSize(150, 68))
        self.slider_lys_down.setFont(font)
        self.slider_lys_down.setStyleSheet(u"")
        self.slider_lys_down.setMaximum(100)
        self.slider_lys_down.setOrientation(Qt.Horizontal)
        self.slider_lys_down.setInvertedAppearance(False)
        self.slider_lys_down.setInvertedControls(False)
        self.slider_lys_down.setTickPosition(QSlider.NoTicks)

        self.gridLayout_3.addWidget(self.slider_lys_down, 2, 1, 1, 1)

        self.lysDownFrame = QFrame(self.lysContainer)
        self.lysDownFrame.setObjectName(u"lysDownFrame")
        self.lysDownFrame.setMinimumSize(QSize(70, 70))
        self.lysDownFrame.setFrameShape(QFrame.NoFrame)
        self.lysDownFrame.setFrameShadow(QFrame.Raised)
        self.frame_lys_down = QFrame(self.lysDownFrame)
        self.frame_lys_down.setObjectName(u"frame_lys_down")
        self.frame_lys_down.setGeometry(QRect(4, 1, 60, 60))
        self.frame_lys_down.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.frame_lys_down.setFrameShape(QFrame.NoFrame)
        self.frame_lys_down.setFrameShadow(QFrame.Raised)
        self.lysDownContainer = QFrame(self.lysDownFrame)
        self.lysDownContainer.setObjectName(u"lysDownContainer")
        self.lysDownContainer.setGeometry(QRect(9, 6, 50, 50))
        self.lysDownContainer.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.lysDownContainer.setFrameShape(QFrame.StyledPanel)
        self.lysDownContainer.setFrameShadow(QFrame.Raised)
        self.label_percentage_lys_down = QLabel(self.lysDownContainer)
        self.label_percentage_lys_down.setObjectName(u"label_percentage_lys_down")
        self.label_percentage_lys_down.setGeometry(QRect(6, 13, 37, 21))
        self.label_percentage_lys_down.setFont(font)
        self.label_percentage_lys_down.setAutoFillBackground(False)
        self.label_percentage_lys_down.setScaledContents(False)
        self.label_percentage_lys_down.setAlignment(Qt.AlignCenter)
        self.label_percentage_lys_down.setWordWrap(False)

        self.gridLayout_3.addWidget(self.lysDownFrame, 2, 2, 1, 1)


        self.verticalLayout_29.addWidget(self.lysContainer)


        self.verticalLayout_16.addWidget(self.lysFrame)


        self.horizontalLayout_10.addWidget(self.column2)

        self.column3 = QFrame(self.scrollAreaWidgetContent)
        self.column3.setObjectName(u"column3")
        self.column3.setMinimumSize(QSize(300, 0))
        self.column3.setMaximumSize(QSize(16777215, 16777215))
        self.column3.setFrameShape(QFrame.NoFrame)
        self.column3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.column3)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.kameraContainer = QFrame(self.column3)
        self.kameraContainer.setObjectName(u"kameraContainer")
        self.kameraContainer.setMinimumSize(QSize(0, 500))
        self.kameraContainer.setMaximumSize(QSize(16777215, 1000))
        self.kameraContainer.setFrameShape(QFrame.NoFrame)
        self.kameraContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.kameraContainer)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.title_video = QLabel(self.kameraContainer)
        self.title_video.setObjectName(u"title_video")
        self.title_video.setFont(font)
        self.title_video.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.title_video)

        self.title_start_videoopptak = QLabel(self.kameraContainer)
        self.title_start_videoopptak.setObjectName(u"title_start_videoopptak")
        self.title_start_videoopptak.setMaximumSize(QSize(16777215, 16777215))
        self.title_start_videoopptak.setFont(font)
        self.title_start_videoopptak.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.title_start_videoopptak)

        self.videoopptakContainer = QHBoxLayout()
        self.videoopptakContainer.setObjectName(u"videoopptakContainer")
        self.btn_start_video_frontkamera = QPushButton(self.kameraContainer)
        self.btn_start_video_frontkamera.setObjectName(u"btn_start_video_frontkamera")
        self.btn_start_video_frontkamera.setMinimumSize(QSize(150, 45))
        self.btn_start_video_frontkamera.setFont(font)
        self.btn_start_video_frontkamera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_video_frontkamera.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start_video_frontkamera.setIcon(icon4)

        self.videoopptakContainer.addWidget(self.btn_start_video_frontkamera)

        self.btn_stopp_video_frontkamera = QPushButton(self.kameraContainer)
        self.btn_stopp_video_frontkamera.setObjectName(u"btn_stopp_video_frontkamera")
        self.btn_stopp_video_frontkamera.setMinimumSize(QSize(150, 45))
        self.btn_stopp_video_frontkamera.setFont(font)
        self.btn_stopp_video_frontkamera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stopp_video_frontkamera.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_stopp_video_frontkamera.setIcon(icon5)

        self.videoopptakContainer.addWidget(self.btn_stopp_video_frontkamera)


        self.verticalLayout_28.addLayout(self.videoopptakContainer)

        self.VideoopptakContainer2 = QHBoxLayout()
        self.VideoopptakContainer2.setObjectName(u"VideoopptakContainer2")
        self.btn_start_video_havbunn = QPushButton(self.kameraContainer)
        self.btn_start_video_havbunn.setObjectName(u"btn_start_video_havbunn")
        self.btn_start_video_havbunn.setMinimumSize(QSize(150, 45))
        self.btn_start_video_havbunn.setFont(font)
        self.btn_start_video_havbunn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start_video_havbunn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        self.btn_start_video_havbunn.setIcon(icon4)

        self.VideoopptakContainer2.addWidget(self.btn_start_video_havbunn)

        self.btn_stopp_video_havbunn = QPushButton(self.kameraContainer)
        self.btn_stopp_video_havbunn.setObjectName(u"btn_stopp_video_havbunn")
        self.btn_stopp_video_havbunn.setMinimumSize(QSize(150, 45))
        self.btn_stopp_video_havbunn.setFont(font)
        self.btn_stopp_video_havbunn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stopp_video_havbunn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        self.btn_stopp_video_havbunn.setIcon(icon5)

        self.VideoopptakContainer2.addWidget(self.btn_stopp_video_havbunn)


        self.verticalLayout_28.addLayout(self.VideoopptakContainer2)

        self.tite_kamera = QLabel(self.kameraContainer)
        self.tite_kamera.setObjectName(u"tite_kamera")
        self.tite_kamera.setFont(font)
        self.tite_kamera.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.tite_kamera)

        self.taBildeContainer = QHBoxLayout()
        self.taBildeContainer.setObjectName(u"taBildeContainer")
        self.btn_ta_bilde_frontkamera = QPushButton(self.kameraContainer)
        self.btn_ta_bilde_frontkamera.setObjectName(u"btn_ta_bilde_frontkamera")
        self.btn_ta_bilde_frontkamera.setMinimumSize(QSize(150, 45))
        self.btn_ta_bilde_frontkamera.setFont(font)
        self.btn_ta_bilde_frontkamera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ta_bilde_frontkamera.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ta_bilde_frontkamera.setIcon(icon6)

        self.taBildeContainer.addWidget(self.btn_ta_bilde_frontkamera)

        self.btn_ta_bilde_havbunn = QPushButton(self.kameraContainer)
        self.btn_ta_bilde_havbunn.setObjectName(u"btn_ta_bilde_havbunn")
        self.btn_ta_bilde_havbunn.setMinimumSize(QSize(150, 45))
        self.btn_ta_bilde_havbunn.setFont(font)
        self.btn_ta_bilde_havbunn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ta_bilde_havbunn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        self.btn_ta_bilde_havbunn.setIcon(icon6)

        self.taBildeContainer.addWidget(self.btn_ta_bilde_havbunn)


        self.verticalLayout_28.addLayout(self.taBildeContainer)

        self.btn_slett_bilde = QPushButton(self.kameraContainer)
        self.btn_slett_bilde.setObjectName(u"btn_slett_bilde")
        self.btn_slett_bilde.setMinimumSize(QSize(150, 40))
        self.btn_slett_bilde.setFont(font)
        self.btn_slett_bilde.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_slett_bilde.setStyleSheet(u"QPushButton { border-color: rgb(80, 36, 37); background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.495, y2:1, stop:0.00492611 rgba(211, 94, 94, 255), stop:1 rgba(96, 14, 14, 255))} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.495, y2:1, stop:0.00492611 rgba(255, 113, 113, 255), stop:0.995074 rgba(120, 18, 18, 255))}")
        icon7 = QIcon()
        icon7.addFile(u":/images/images/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_slett_bilde.setIcon(icon7)

        self.verticalLayout_28.addWidget(self.btn_slett_bilde)

        self.text_siste_bilde = QLabel(self.kameraContainer)
        self.text_siste_bilde.setObjectName(u"text_siste_bilde")
        self.text_siste_bilde.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_siste_bilde.setLineWidth(1)
        self.text_siste_bilde.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.text_siste_bilde)

        self.img_recent = QLabel(self.kameraContainer)
        self.img_recent.setObjectName(u"img_recent")
        self.img_recent.setMinimumSize(QSize(0, 200))
        self.img_recent.setMaximumSize(QSize(360, 200))
        self.img_recent.setStyleSheet(u"")
        self.img_recent.setPixmap(QPixmap(u":/images/images/underwater.png"))
        self.img_recent.setScaledContents(True)
        self.img_recent.setAlignment(Qt.AlignCenter)
        self.img_recent.setMargin(0)

        self.verticalLayout_28.addWidget(self.img_recent)


        self.verticalLayout_39.addWidget(self.kameraContainer)


        self.horizontalLayout_10.addWidget(self.column3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContent)

        self.horizontalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.row)

        self.stackedWidget.addWidget(self.informasjon)
        self.kontroller = QWidget()
        self.kontroller.setObjectName(u"kontroller")
        self.verticalLayout_20 = QVBoxLayout(self.kontroller)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.hovedFrameColumn = QFrame(self.kontroller)
        self.hovedFrameColumn.setObjectName(u"hovedFrameColumn")
        self.hovedFrameColumn.setStyleSheet(u"color: black;")
        self.hovedFrameColumn.setFrameShape(QFrame.NoFrame)
        self.hovedFrameColumn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.hovedFrameColumn)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(12, 0, 12, -1)
        self.scrollArea2 = QScrollArea(self.hovedFrameColumn)
        self.scrollArea2.setObjectName(u"scrollArea2")
        self.scrollArea2.setFrameShape(QFrame.NoFrame)
        self.scrollArea2.setFrameShadow(QFrame.Plain)
        self.scrollArea2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1302, 842))
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
        self.kontrollerRows.setMaximumSize(QSize(1400, 16777215))
        self.kontrollerRows.setFrameShape(QFrame.StyledPanel)
        self.kontrollerRows.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.kontrollerRows)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_kontroller_container = QFrame(self.kontrollerRows)
        self.btn_kontroller_container.setObjectName(u"btn_kontroller_container")
        self.btn_kontroller_container.setMaximumSize(QSize(16777215, 200))
        self.btn_kontroller_container.setFrameShape(QFrame.NoFrame)
        self.btn_kontroller_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.btn_kontroller_container)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.kontrollerTextContainer = QFrame(self.btn_kontroller_container)
        self.kontrollerTextContainer.setObjectName(u"kontrollerTextContainer")
        self.kontrollerTextContainer.setFrameShape(QFrame.StyledPanel)
        self.kontrollerTextContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.kontrollerTextContainer)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.title_kontroller = QLabel(self.kontrollerTextContainer)
        self.title_kontroller.setObjectName(u"title_kontroller")
        self.title_kontroller.setMinimumSize(QSize(0, 20))
        self.title_kontroller.setFont(font)
        self.title_kontroller.setStyleSheet(u"color: #dddddd;")
        self.title_kontroller.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.title_kontroller)

        self.text_kontroller_description = QLabel(self.kontrollerTextContainer)
        self.text_kontroller_description.setObjectName(u"text_kontroller_description")
        self.text_kontroller_description.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.text_kontroller_description.setLineWidth(1)
        self.text_kontroller_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.text_kontroller_description.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.text_kontroller_description)


        self.horizontalLayout_13.addWidget(self.kontrollerTextContainer)

        self.profileContainer = QFrame(self.btn_kontroller_container)
        self.profileContainer.setObjectName(u"profileContainer")
        self.profileContainer.setMinimumSize(QSize(0, 0))
        self.profileContainer.setMaximumSize(QSize(350, 200))
        self.profileContainer.setFrameShape(QFrame.NoFrame)
        self.profileContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.profileContainer)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 30)
        self.text_velg_profil = QLabel(self.profileContainer)
        self.text_velg_profil.setObjectName(u"text_velg_profil")
        self.text_velg_profil.setMinimumSize(QSize(0, 40))
        self.text_velg_profil.setMaximumSize(QSize(100, 40))
        self.text_velg_profil.setFont(font)
        self.text_velg_profil.setStyleSheet(u"color: #dddddd;")

        self.horizontalLayout_11.addWidget(self.text_velg_profil)

        self.comboBox_velg_profil = QComboBox(self.profileContainer)
        self.comboBox_velg_profil.addItem("")
        self.comboBox_velg_profil.addItem("")
        self.comboBox_velg_profil.setObjectName(u"comboBox_velg_profil")
        sizePolicy3.setHeightForWidth(self.comboBox_velg_profil.sizePolicy().hasHeightForWidth())
        self.comboBox_velg_profil.setSizePolicy(sizePolicy3)
        self.comboBox_velg_profil.setMinimumSize(QSize(220, 0))
        self.comboBox_velg_profil.setMaximumSize(QSize(16777215, 30))
        self.comboBox_velg_profil.setFont(font)
        self.comboBox_velg_profil.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_velg_profil.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
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
        self.btn_reset.setFont(font)
        self.btn_reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reset.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); color: white;} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255)); color: white;}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reset.setIcon(icon8)
        self.btn_make_new_profile = QPushButton(self.profileBtnContainer)
        self.btn_make_new_profile.setObjectName(u"btn_make_new_profile")
        self.btn_make_new_profile.setGeometry(QRect(40, 20, 201, 45))
        self.btn_make_new_profile.setMinimumSize(QSize(150, 45))
        self.btn_make_new_profile.setFont(font)
        self.btn_make_new_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_make_new_profile.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); color: white;} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255)); color: white;}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_make_new_profile.setIcon(icon9)

        self.horizontalLayout_13.addWidget(self.profileBtnContainer)


        self.verticalLayout_19.addWidget(self.btn_kontroller_container)

        self.kontrollerImgContainer = QFrame(self.kontrollerRows)
        self.kontrollerImgContainer.setObjectName(u"kontrollerImgContainer")
        self.kontrollerImgContainer.setMinimumSize(QSize(1300, 680))
        self.kontrollerImgContainer.setFont(font)
        self.kontrollerImgContainer.setFrameShape(QFrame.NoFrame)
        self.kontrollerImgContainer.setFrameShadow(QFrame.Raised)
        self.xbox_image = QLabel(self.kontrollerImgContainer)
        self.xbox_image.setObjectName(u"xbox_image")
        self.xbox_image.setGeometry(QRect(140, -20, 801, 771))
        self.xbox_image.setPixmap(QPixmap(u":/images/images/xboxOne.png"))
        self.xbox_image.setScaledContents(True)
        self.comboBox_right_stick_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_right_stick_btn.addItem("")
        self.comboBox_right_stick_btn.setObjectName(u"comboBox_right_stick_btn")
        self.comboBox_right_stick_btn.setGeometry(QRect(790, 580, 230, 32))
        self.comboBox_right_stick_btn.setFont(font)
        self.comboBox_right_stick_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_right_stick_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_directional_pad_leftright = QComboBox(self.kontrollerImgContainer)
        self.comboBox_directional_pad_leftright.addItem("")
        self.comboBox_directional_pad_leftright.setObjectName(u"comboBox_directional_pad_leftright")
        self.comboBox_directional_pad_leftright.setEnabled(False)
        self.comboBox_directional_pad_leftright.setGeometry(QRect(50, 360, 210, 32))
        self.comboBox_directional_pad_leftright.setFont(font)
        self.comboBox_directional_pad_leftright.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_directional_pad_leftright.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_directional_pad_leftright.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_right_stick_x = QComboBox(self.kontrollerImgContainer)
        self.comboBox_right_stick_x.addItem("")
        self.comboBox_right_stick_x.setObjectName(u"comboBox_right_stick_x")
        self.comboBox_right_stick_x.setGeometry(QRect(880, 470, 210, 32))
        self.comboBox_right_stick_x.setFont(font)
        self.comboBox_right_stick_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_x.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_right_stick_x.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_RB_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_RB_btn.addItem("")
        self.comboBox_RB_btn.setObjectName(u"comboBox_RB_btn")
        self.comboBox_RB_btn.setGeometry(QRect(800, 161, 230, 32))
        self.comboBox_RB_btn.setFont(font)
        self.comboBox_RB_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_RB_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_RB_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_left_stick_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_left_stick_btn.addItem("")
        self.comboBox_left_stick_btn.setObjectName(u"comboBox_left_stick_btn")
        self.comboBox_left_stick_btn.setGeometry(QRect(60, 530, 230, 32))
        self.comboBox_left_stick_btn.setFont(font)
        self.comboBox_left_stick_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_RT_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_RT_btn.addItem("")
        self.comboBox_RT_btn.setObjectName(u"comboBox_RT_btn")
        self.comboBox_RT_btn.setGeometry(QRect(800, 110, 230, 32))
        self.comboBox_RT_btn.setFont(font)
        self.comboBox_RT_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_RT_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_RT_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_left_stick_x = QComboBox(self.kontrollerImgContainer)
        self.comboBox_left_stick_x.addItem("")
        self.comboBox_left_stick_x.setObjectName(u"comboBox_left_stick_x")
        self.comboBox_left_stick_x.setGeometry(QRect(20, 280, 241, 32))
        self.comboBox_left_stick_x.setFont(font)
        self.comboBox_left_stick_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_x.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_x.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_menu_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_menu_btn.setObjectName(u"comboBox_menu_btn")
        self.comboBox_menu_btn.setGeometry(QRect(560, 20, 230, 32))
        self.comboBox_menu_btn.setFont(font)
        self.comboBox_menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_menu_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_menu_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_right_stick_y = QComboBox(self.kontrollerImgContainer)
        self.comboBox_right_stick_y.addItem("")
        self.comboBox_right_stick_y.setObjectName(u"comboBox_right_stick_y")
        self.comboBox_right_stick_y.setGeometry(QRect(530, 530, 251, 32))
        self.comboBox_right_stick_y.setFont(font)
        self.comboBox_right_stick_y.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_y.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_right_stick_y.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_view_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_view_btn.setObjectName(u"comboBox_view_btn")
        self.comboBox_view_btn.setGeometry(QRect(280, 20, 230, 32))
        self.comboBox_view_btn.setFont(font)
        self.comboBox_view_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_view_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_view_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_B_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_B_btn.setObjectName(u"comboBox_B_btn")
        self.comboBox_B_btn.setGeometry(QRect(810, 280, 230, 32))
        self.comboBox_B_btn.setFont(font)
        self.comboBox_B_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_B_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_B_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_X_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_X_btn.setObjectName(u"comboBox_X_btn")
        self.comboBox_X_btn.setGeometry(QRect(820, 340, 230, 32))
        self.comboBox_X_btn.setFont(font)
        self.comboBox_X_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_X_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_X_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_directional_pad_updown = QComboBox(self.kontrollerImgContainer)
        self.comboBox_directional_pad_updown.addItem("")
        self.comboBox_directional_pad_updown.setObjectName(u"comboBox_directional_pad_updown")
        self.comboBox_directional_pad_updown.setEnabled(False)
        self.comboBox_directional_pad_updown.setGeometry(QRect(310, 560, 210, 32))
        self.comboBox_directional_pad_updown.setFont(font)
        self.comboBox_directional_pad_updown.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_directional_pad_updown.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_directional_pad_updown.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_A_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_A_btn.setObjectName(u"comboBox_A_btn")
        self.comboBox_A_btn.setGeometry(QRect(840, 410, 230, 32))
        self.comboBox_A_btn.setFont(font)
        self.comboBox_A_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_A_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_A_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_left_stick_y = QComboBox(self.kontrollerImgContainer)
        self.comboBox_left_stick_y.addItem("")
        self.comboBox_left_stick_y.setObjectName(u"comboBox_left_stick_y")
        self.comboBox_left_stick_y.setGeometry(QRect(0, 219, 210, 32))
        self.comboBox_left_stick_y.setFont(font)
        self.comboBox_left_stick_y.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_y.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_y.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_LB_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_LB_btn.addItem("")
        self.comboBox_LB_btn.setObjectName(u"comboBox_LB_btn")
        self.comboBox_LB_btn.setGeometry(QRect(70, 170, 230, 32))
        self.comboBox_LB_btn.setFont(font)
        self.comboBox_LB_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_LB_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_LB_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_Y_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_Y_btn.addItem("")
        self.comboBox_Y_btn.setObjectName(u"comboBox_Y_btn")
        self.comboBox_Y_btn.setGeometry(QRect(818, 220, 230, 32))
        self.comboBox_Y_btn.setFont(font)
        self.comboBox_Y_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_Y_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_Y_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_LT_btn = QComboBox(self.kontrollerImgContainer)
        self.comboBox_LT_btn.addItem("")
        self.comboBox_LT_btn.setObjectName(u"comboBox_LT_btn")
        self.comboBox_LT_btn.setGeometry(QRect(100, 120, 230, 32))
        self.comboBox_LT_btn.setFont(font)
        self.comboBox_LT_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_LT_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_LT_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.btn_save_profile = QPushButton(self.kontrollerImgContainer)
        self.btn_save_profile.setObjectName(u"btn_save_profile")
        self.btn_save_profile.setEnabled(False)
        self.btn_save_profile.setGeometry(QRect(1090, 620, 201, 45))
        self.btn_save_profile.setMinimumSize(QSize(150, 45))
        self.btn_save_profile.setFont(font)
        self.btn_save_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_profile.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); color: white;} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255)); color: white;} QPushButton:disabled { background-color: rgba(67, 69, 72, 0.6); color: rgba(154, 154, 154, 0.632); border: 2px solid rgba(52, 59, 72, 0.632);}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save_profile.setIcon(icon10)

        self.verticalLayout_19.addWidget(self.kontrollerImgContainer)


        self.horizontalLayout_9.addWidget(self.kontrollerRows)


        self.verticalLayout_18.addWidget(self.kontrollerContainer)

        self.scrollArea2.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_8.addWidget(self.scrollArea2)


        self.verticalLayout_20.addWidget(self.hovedFrameColumn)

        self.stackedWidget.addWidget(self.kontroller)

        self.horizontalLayout_16.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


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
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)
        self.grip_icon = QLabel(self.frame_size_grip)
        self.grip_icon.setObjectName(u"grip_icon")
        self.grip_icon.setGeometry(QRect(-7, -4, 30, 20))
        self.grip_icon.setPixmap(QPixmap(u":/icons/images/icons/cil-size-grip.png"))
        self.grip_icon.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_informasjon.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_kontroller.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><"
                        "span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; "
                        "margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"UiS Subsea", None))
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
        self.title_kjoring.setText(QCoreApplication.translate("MainWindow", u"KJ\u00d8REMODUS", None))
        self.label_kjoring.setText(QCoreApplication.translate("MainWindow", u"Velg kj\u00f8remodus", None))
        self.btn_manuell.setText(QCoreApplication.translate("MainWindow", u"Manuell kj\u00f8ring", None))
        self.btn_finn_fisk.setText(QCoreApplication.translate("MainWindow", u"Finn fisk (og kalkul\u00e9r n\u00e6rmeste avstand)", None))
        self.btn_autonom_merd.setText(QCoreApplication.translate("MainWindow", u"Autonom merd", None))
        self.btn_bildemoasaikk.setText(QCoreApplication.translate("MainWindow", u"Bildemoasaikk", None))
        self.btn_autonom_parkering.setText(QCoreApplication.translate("MainWindow", u"Autonom parkering", None))
        self.text_bildebehandlingsmodus.setText(QCoreApplication.translate("MainWindow", u"Bildebehandlingen som kj\u00f8res:", None))
        self.label_bildebehandlingsmodus.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.text_mani.setText(QCoreApplication.translate("MainWindow", u"Manipulator", None))
        self.text_dybde_reg.setText(QCoreApplication.translate("MainWindow", u"Dybde regulator", None))
        self.text_helning.setText(QCoreApplication.translate("MainWindow", u"Helningsregulator", None))
        self.text_frontlys.setText(QCoreApplication.translate("MainWindow", u"Frontlys", None))
        self.text_havbunnslys.setText(QCoreApplication.translate("MainWindow", u"Havbunnslys", None))
        self.btn_reset_sikring_thrustere.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_reset_nullpunkt.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_regulator_manipulator.setText(QCoreApplication.translate("MainWindow", u"Av/P\u00e5", None))
        self.label_effekt_thrustere.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.title_effektforbruk.setText(QCoreApplication.translate("MainWindow", u"EFFEKTFORBRUK", None))
        self.text_effekt_elektronikk.setText(QCoreApplication.translate("MainWindow", u"Elektronikk:", None))
        self.label_effekt_manipulator.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.text_effekt_manipulator.setText(QCoreApplication.translate("MainWindow", u"Manipulator:", None))
        self.label_tid.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_dybde.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.text_tid.setText(QCoreApplication.translate("MainWindow", u"Tid:", None))
        self.text_effekt_thrustere.setText(QCoreApplication.translate("MainWindow", u"Thrustere:", None))
        self.text_dybde.setText(QCoreApplication.translate("MainWindow", u"Dybde:", None))
        self.btn_reset_sikring_manipulator.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_regulator_elektronikk.setText(QCoreApplication.translate("MainWindow", u"Av/P\u00e5", None))
        self.btn_regulator_thrustere.setText(QCoreApplication.translate("MainWindow", u"Av/P\u00e5", None))
        self.label_effekt_elektronikk.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.text_orientering.setText(QCoreApplication.translate("MainWindow", u"Orientering:", None))
        self.label_orientering.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.btn_reset_sikring_elektronikk.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_temp_ROV.setText(QCoreApplication.translate("MainWindow", u"TEMPERATUR I ROV", None))
        self.label_temp_ROV_1.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.labe_temp_ROV_2.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_temp_ROV_3.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.text_gjsnitttemp.setText(QCoreApplication.translate("MainWindow", u"Gj.snittstemperatur:", None))
        self.label_gjsnitt_temp_ROV.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.title_vannlekk.setText(QCoreApplication.translate("MainWindow", u"VANNLEKKASJE I ROV", None))
        self.label_vannlekk_1.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_vannlekk_2.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_vannlekk_3.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.title_motor.setText(QCoreApplication.translate("MainWindow", u"MOTORP\u00c5DRAG", None))
        self.text_rov.setText(QCoreApplication.translate("MainWindow", u"ROV", None))
        self.img_motor.setText("")
        self.label_percentage_VHF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_VVF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_HHF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_HVF.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_HVB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_HHB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_VVB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_VHB.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.text_manipulator.setText(QCoreApplication.translate("MainWindow", u"MANIPULATOR", None))
        self.img_manipulator.setText("")
        self.label_percentage_mani_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_mani_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0<span style=\" vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_mani_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.lys_title.setText(QCoreApplication.translate("MainWindow", u"LYS", None))
        self.text_lys_down.setText(QCoreApplication.translate("MainWindow", u"Havbunnslys:", None))
        self.text_lys_forward.setText(QCoreApplication.translate("MainWindow", u"Frontlys:", None))
        self.label_percentage_lys_forward.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.label_percentage_lys_down.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.title_video.setText(QCoreApplication.translate("MainWindow", u"KAMERA", None))
        self.title_start_videoopptak.setText(QCoreApplication.translate("MainWindow", u"Start og stopp videoopptak", None))
        self.btn_start_video_frontkamera.setText(QCoreApplication.translate("MainWindow", u"Frontkamera", None))
        self.btn_stopp_video_frontkamera.setText(QCoreApplication.translate("MainWindow", u"Frontkamera", None))
        self.btn_start_video_havbunn.setText(QCoreApplication.translate("MainWindow", u"Havbunnskamera", None))
        self.btn_stopp_video_havbunn.setText(QCoreApplication.translate("MainWindow", u" Havbunnskamera", None))
        self.tite_kamera.setText(QCoreApplication.translate("MainWindow", u"Ta bilde", None))
        self.btn_ta_bilde_frontkamera.setText(QCoreApplication.translate("MainWindow", u" Frontkamera", None))
        self.btn_ta_bilde_havbunn.setText(QCoreApplication.translate("MainWindow", u"Havbunnskamera", None))
        self.btn_slett_bilde.setText(QCoreApplication.translate("MainWindow", u" Slett det siste bildet", None))
        self.text_siste_bilde.setText(QCoreApplication.translate("MainWindow", u"Siste bilde tatt vises her:", None))
        self.img_recent.setText("")
        self.title_kontroller.setText(QCoreApplication.translate("MainWindow", u"ENDRE KONTROLLER-KNAPPER", None))
        self.text_kontroller_description.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Her kan du endre funksjonene til knappene p\u00e5 Xbox-kontrolleren.</p><p>Lag en ny profil hvis du \u00f8nsker \u00e5 lagre endringene til senere.</p></body></html>", None))
        self.text_velg_profil.setText(QCoreApplication.translate("MainWindow", u"Velg profil:", None))
        self.comboBox_velg_profil.setItemText(0, QCoreApplication.translate("MainWindow", u"Standard profil", None))
        self.comboBox_velg_profil.setItemText(1, QCoreApplication.translate("MainWindow", u"Egendefinert profil", None))

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

        self.btn_save_profile.setText(QCoreApplication.translate("MainWindow", u" Lagre", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.version.setText("")
        self.grip_icon.setText("")
    # retranslateUi

