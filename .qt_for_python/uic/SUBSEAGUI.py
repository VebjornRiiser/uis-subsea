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
        MainWindow.resize(1423, 890)
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
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hov"
                        "er {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
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
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); bo"
                        "rder-style: solid; border-radius: 4px; }\n"
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
""
                        "/* Top Buttons */\n"
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
"	paddin"
                        "g-left: 44px;\n"
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
"    border-right: 1px solid rgb(4"
                        "4, 49, 60);\n"
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
"/* ////////////////////////////////////////////////////////////////////////////////////////////"
                        "/////\n"
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
"    backgroun"
                        "d: rgb(55, 63, 77);\n"
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
"     border"
                        ": none;\n"
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
"QCheckBox::indi"
                        "cator:hover {\n"
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
"	border: 2px solid rgb(33, 3"
                        "7, 43);\n"
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
""
                        "QSlider::groove:horizontal:hover {\n"
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
"    bac"
                        "kground-color: rgb(102, 91, 201);\n"
"}\n"
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
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
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
"	bord"
                        "er: 2px solid rgb(43, 50, 61);\n"
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
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setGeometry(QRect(0, 48, 60, 90))
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.informasjon_btn = QPushButton(self.topMenu)
        self.informasjon_btn.setObjectName(u"informasjon_btn")
        sizePolicy.setHeightForWidth(self.informasjon_btn.sizePolicy().hasHeightForWidth())
        self.informasjon_btn.setSizePolicy(sizePolicy)
        self.informasjon_btn.setMinimumSize(QSize(0, 45))
        self.informasjon_btn.setFont(font)
        self.informasjon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.informasjon_btn.setLayoutDirection(Qt.LeftToRight)
        self.informasjon_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")
        self.informasjon_btn.setCheckable(True)

        self.verticalLayout_8.addWidget(self.informasjon_btn)

        self.kontroller_btn = QPushButton(self.topMenu)
        self.kontroller_btn.setObjectName(u"kontroller_btn")
        sizePolicy.setHeightForWidth(self.kontroller_btn.sizePolicy().hasHeightForWidth())
        self.kontroller_btn.setSizePolicy(sizePolicy)
        self.kontroller_btn.setMinimumSize(QSize(0, 45))
        self.kontroller_btn.setFont(font)
        self.kontroller_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.kontroller_btn.setLayoutDirection(Qt.LeftToRight)
        self.kontroller_btn.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")
        icon = QIcon()
        icon.addFile(u"../../Downloads/uis-subsea/Subsea_QT_GUI/images/kontroller.png", QSize(), QIcon.Normal, QIcon.Off)
        self.kontroller_btn.setIcon(icon)
        self.kontroller_btn.setCheckable(True)

        self.verticalLayout_8.addWidget(self.kontroller_btn)

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
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
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
        self.frame_3 = QFrame(self.contentBottom)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(800, 16777215))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.toolButton_kjoremodus = QToolButton(self.frame_3)
        self.toolButton_kjoremodus.setObjectName(u"toolButton_kjoremodus")
        self.toolButton_kjoremodus.setMinimumSize(QSize(100, 0))
        self.toolButton_kjoremodus.setStyleSheet(u"background-color: black; color: white;")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_kjoremodus.setIcon(icon4)
        self.toolButton_kjoremodus.setCheckable(True)
        self.toolButton_kjoremodus.setChecked(True)
        self.toolButton_kjoremodus.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_kjoremodus.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_kjoremodus.setAutoRaise(False)
        self.toolButton_kjoremodus.setArrowType(Qt.NoArrow)

        self.horizontalLayout_16.addWidget(self.toolButton_kjoremodus)

        self.toolButton_effekt = QToolButton(self.frame_3)
        self.toolButton_effekt.setObjectName(u"toolButton_effekt")
        self.toolButton_effekt.setMinimumSize(QSize(100, 0))
        self.toolButton_effekt.setStyleSheet(u"background-color: black; color: white;")
        self.toolButton_effekt.setIcon(icon4)
        self.toolButton_effekt.setCheckable(True)
        self.toolButton_effekt.setChecked(True)
        self.toolButton_effekt.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_effekt.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_effekt.setAutoRaise(False)
        self.toolButton_effekt.setArrowType(Qt.NoArrow)

        self.horizontalLayout_16.addWidget(self.toolButton_effekt)

        self.toolButton_temp = QToolButton(self.frame_3)
        self.toolButton_temp.setObjectName(u"toolButton_temp")
        self.toolButton_temp.setMinimumSize(QSize(100, 0))
        self.toolButton_temp.setStyleSheet(u"background-color: black; color: white;")
        self.toolButton_temp.setIcon(icon4)
        self.toolButton_temp.setCheckable(True)
        self.toolButton_temp.setChecked(True)
        self.toolButton_temp.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_temp.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_temp.setAutoRaise(False)
        self.toolButton_temp.setArrowType(Qt.NoArrow)

        self.horizontalLayout_16.addWidget(self.toolButton_temp)

        self.toolButton_vann = QToolButton(self.frame_3)
        self.toolButton_vann.setObjectName(u"toolButton_vann")
        self.toolButton_vann.setMinimumSize(QSize(100, 0))
        self.toolButton_vann.setStyleSheet(u"background-color: black; color: white;")
        self.toolButton_vann.setIcon(icon4)
        self.toolButton_vann.setCheckable(True)
        self.toolButton_vann.setChecked(True)
        self.toolButton_vann.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_vann.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_vann.setAutoRaise(False)
        self.toolButton_vann.setArrowType(Qt.NoArrow)

        self.horizontalLayout_16.addWidget(self.toolButton_vann)

        self.toolButton_motorpaadrag = QToolButton(self.frame_3)
        self.toolButton_motorpaadrag.setObjectName(u"toolButton_motorpaadrag")
        self.toolButton_motorpaadrag.setMinimumSize(QSize(100, 0))
        self.toolButton_motorpaadrag.setStyleSheet(u"background-color: black; color: white;")
        self.toolButton_motorpaadrag.setIcon(icon4)
        self.toolButton_motorpaadrag.setCheckable(True)
        self.toolButton_motorpaadrag.setChecked(True)
        self.toolButton_motorpaadrag.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_motorpaadrag.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_motorpaadrag.setAutoRaise(False)
        self.toolButton_motorpaadrag.setArrowType(Qt.NoArrow)

        self.horizontalLayout_16.addWidget(self.toolButton_motorpaadrag)

        self.toolButton_bilde = QToolButton(self.frame_3)
        self.toolButton_bilde.setObjectName(u"toolButton_bilde")
        self.toolButton_bilde.setMinimumSize(QSize(100, 0))
        self.toolButton_bilde.setStyleSheet(u"background-color: black; color: white;")
        self.toolButton_bilde.setIcon(icon4)
        self.toolButton_bilde.setCheckable(True)
        self.toolButton_bilde.setChecked(True)
        self.toolButton_bilde.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_bilde.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_bilde.setAutoRaise(False)
        self.toolButton_bilde.setArrowType(Qt.NoArrow)

        self.horizontalLayout_16.addWidget(self.toolButton_bilde)

        self.toolButton_kamera = QToolButton(self.frame_3)
        self.toolButton_kamera.setObjectName(u"toolButton_kamera")
        self.toolButton_kamera.setMinimumSize(QSize(100, 0))
        self.toolButton_kamera.setStyleSheet(u"background-color: black; color: white;")
        self.toolButton_kamera.setIcon(icon4)
        self.toolButton_kamera.setCheckable(True)
        self.toolButton_kamera.setChecked(True)
        self.toolButton_kamera.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_kamera.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_kamera.setAutoRaise(False)
        self.toolButton_kamera.setArrowType(Qt.NoArrow)

        self.horizontalLayout_16.addWidget(self.toolButton_kamera)


        self.verticalLayout_6.addWidget(self.frame_3)

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
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.horizontalLayout_17 = QHBoxLayout(self.home)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(900, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame)

        self.QVBoxLayout = QVBoxLayout()
        self.QVBoxLayout.setObjectName(u"QVBoxLayout")
        self.QVBoxLayout.setContentsMargins(12, 12, 12, 12)

        self.horizontalLayout_17.addLayout(self.QVBoxLayout)

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
        self.scrollAreaWidgetContent.setGeometry(QRect(0, 0, 1361, 800))
        self.horizontalLayout_10 = QHBoxLayout(self.scrollAreaWidgetContent)
#ifndef Q_OS_MAC
        self.horizontalLayout_10.setSpacing(-1)
#endif
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.column1 = QFrame(self.scrollAreaWidgetContent)
        self.column1.setObjectName(u"column1")
        sizePolicy3.setHeightForWidth(self.column1.sizePolicy().hasHeightForWidth())
        self.column1.setSizePolicy(sizePolicy3)
        self.column1.setMinimumSize(QSize(500, 800))
        self.column1.setMaximumSize(QSize(440, 800))
        self.column1.setFrameShape(QFrame.NoFrame)
        self.column1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.column1)
#ifndef Q_OS_MAC
        self.verticalLayout_26.setSpacing(-1)
#endif
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 12, 12, 20)
        self.kjoring_container = QFrame(self.column1)
        self.kjoring_container.setObjectName(u"kjoring_container")
        self.kjoring_container.setMinimumSize(QSize(0, 0))
        self.kjoring_container.setMaximumSize(QSize(16777215, 200))
        self.kjoring_container.setStyleSheet(u"")
        self.kjoring_container.setFrameShape(QFrame.NoFrame)
        self.kjoring_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.kjoring_container)
#ifndef Q_OS_MAC
        self.verticalLayout_25.setSpacing(-1)
#endif
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.kjoring_title = QLabel(self.kjoring_container)
        self.kjoring_title.setObjectName(u"kjoring_title")
        self.kjoring_title.setMinimumSize(QSize(0, 20))
        self.kjoring_title.setFont(font)
        self.kjoring_title.setStyleSheet(u"")

        self.verticalLayout_25.addWidget(self.kjoring_title)

        self.kjoring_label = QLabel(self.kjoring_container)
        self.kjoring_label.setObjectName(u"kjoring_label")
        self.kjoring_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.kjoring_label.setLineWidth(1)
        self.kjoring_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.kjoring_label)

        self.pushButton = QPushButton(self.kjoring_container)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 45))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")

        self.verticalLayout_25.addWidget(self.pushButton)

        self.manuell_btn = QPushButton(self.kjoring_container)
        self.manuell_btn.setObjectName(u"manuell_btn")
        self.manuell_btn.setMinimumSize(QSize(150, 45))
        self.manuell_btn.setFont(font)
        self.manuell_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.manuell_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}\n"
"QPushButton:checked { background-color: grey }")
        self.manuell_btn.setCheckable(True)
        self.manuell_btn.setChecked(True)
        self.manuell_btn.setAutoRepeat(False)

        self.verticalLayout_25.addWidget(self.manuell_btn)


        self.verticalLayout_26.addWidget(self.kjoring_container)

        self.ROV_container = QFrame(self.column1)
        self.ROV_container.setObjectName(u"ROV_container")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ROV_container.sizePolicy().hasHeightForWidth())
        self.ROV_container.setSizePolicy(sizePolicy4)
        self.ROV_container.setMinimumSize(QSize(0, 0))
        self.ROV_container.setMaximumSize(QSize(16777215, 500))
        self.ROV_container.setFrameShape(QFrame.NoFrame)
        self.ROV_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.ROV_container)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ROV_column_2 = QFrame(self.ROV_container)
        self.ROV_column_2.setObjectName(u"ROV_column_2")
        self.ROV_column_2.setMinimumSize(QSize(0, 0))
        self.ROV_column_2.setMaximumSize(QSize(16777215, 16777215))
        self.ROV_column_2.setFrameShape(QFrame.NoFrame)
        self.ROV_column_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.ROV_column_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.ROV_row_2 = QFrame(self.ROV_column_2)
        self.ROV_row_2.setObjectName(u"ROV_row_2")
        self.ROV_row_2.setMinimumSize(QSize(240, 140))
        self.ROV_row_2.setMaximumSize(QSize(16777215, 200))
        self.ROV_row_2.setStyleSheet(u"QPushButton { background-color: rgb(109, 156, 113) } QPushButton#lys_av_btn, QPushButton#dybde_av_btn, QPushButton#helning_av_btn, QPushButton#mani_av_btn{ background-color: rgb(192, 108, 109) } QPushButton:hover { background-color: rgba(255, 255, 255, 110) } QPushButton#dybde_av_btn:hover, QPushButton#helning_av_btn:hover, QPushButton#mani_av_btn:hover { background-color: rgba(255, 255, 255, 110) }")
        self.ROV_row_2.setFrameShape(QFrame.NoFrame)
        self.ROV_row_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ROV_row_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lys_av_btn = QPushButton(self.ROV_row_2)
        self.lys_av_btn.setObjectName(u"lys_av_btn")
        self.lys_av_btn.setMaximumSize(QSize(40, 16777215))
        self.lys_av_btn.setFont(font)
        self.lys_av_btn.setStyleSheet(u"padding: 4px;")

        self.gridLayout_3.addWidget(self.lys_av_btn, 9, 2, 1, 1)

        self.dybde_reg_label = QLabel(self.ROV_row_2)
        self.dybde_reg_label.setObjectName(u"dybde_reg_label")
        self.dybde_reg_label.setFont(font)
        self.dybde_reg_label.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.dybde_reg_label, 3, 4, 1, 1)

        self.dybde_paa_btn = QPushButton(self.ROV_row_2)
        self.dybde_paa_btn.setObjectName(u"dybde_paa_btn")
        self.dybde_paa_btn.setMaximumSize(QSize(40, 16777215))
        self.dybde_paa_btn.setFont(font)
        self.dybde_paa_btn.setStyleSheet(u"padding: 4px;")

        self.gridLayout_3.addWidget(self.dybde_paa_btn, 3, 0, 1, 1)

        self.mani_av_btn = QPushButton(self.ROV_row_2)
        self.mani_av_btn.setObjectName(u"mani_av_btn")
        self.mani_av_btn.setMaximumSize(QSize(40, 16777215))
        self.mani_av_btn.setFont(font)
        self.mani_av_btn.setStyleSheet(u"padding: 4px;")

        self.gridLayout_3.addWidget(self.mani_av_btn, 2, 2, 1, 1)

        self.mani_paa_btn = QPushButton(self.ROV_row_2)
        self.mani_paa_btn.setObjectName(u"mani_paa_btn")
        self.mani_paa_btn.setMaximumSize(QSize(40, 16777215))
        self.mani_paa_btn.setFont(font)
        self.mani_paa_btn.setStyleSheet(u"padding: 4px;")

        self.gridLayout_3.addWidget(self.mani_paa_btn, 2, 0, 1, 1)

        self.mani_label = QLabel(self.ROV_row_2)
        self.mani_label.setObjectName(u"mani_label")
        self.mani_label.setFont(font)
        self.mani_label.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.mani_label, 2, 4, 1, 1)

        self.lys_label_2 = QLabel(self.ROV_row_2)
        self.lys_label_2.setObjectName(u"lys_label_2")
        self.lys_label_2.setFont(font)
        self.lys_label_2.setTextFormat(Qt.RichText)

        self.gridLayout_3.addWidget(self.lys_label_2, 9, 4, 1, 1)

        self.lys_paa_btn = QPushButton(self.ROV_row_2)
        self.lys_paa_btn.setObjectName(u"lys_paa_btn")
        self.lys_paa_btn.setMinimumSize(QSize(0, 0))
        self.lys_paa_btn.setMaximumSize(QSize(40, 16777215))
        self.lys_paa_btn.setFont(font)
        self.lys_paa_btn.setStyleSheet(u"padding: 4px;")

        self.gridLayout_3.addWidget(self.lys_paa_btn, 9, 0, 1, 1)

        self.helning_label = QLabel(self.ROV_row_2)
        self.helning_label.setObjectName(u"helning_label")
        self.helning_label.setMinimumSize(QSize(0, 0))
        self.helning_label.setFont(font)
        self.helning_label.setTextFormat(Qt.PlainText)

        self.gridLayout_3.addWidget(self.helning_label, 8, 4, 1, 1)

        self.helning_paa_btn = QPushButton(self.ROV_row_2)
        self.helning_paa_btn.setObjectName(u"helning_paa_btn")
        self.helning_paa_btn.setMaximumSize(QSize(40, 16777215))
        self.helning_paa_btn.setFont(font)
        self.helning_paa_btn.setStyleSheet(u"padding: 4px;")

        self.gridLayout_3.addWidget(self.helning_paa_btn, 8, 0, 1, 1)

        self.dybde_av_btn = QPushButton(self.ROV_row_2)
        self.dybde_av_btn.setObjectName(u"dybde_av_btn")
        self.dybde_av_btn.setMaximumSize(QSize(40, 16777215))
        self.dybde_av_btn.setFont(font)
        self.dybde_av_btn.setStyleSheet(u"padding: 4px;")

        self.gridLayout_3.addWidget(self.dybde_av_btn, 3, 2, 1, 1)

        self.helning_av_btn = QPushButton(self.ROV_row_2)
        self.helning_av_btn.setObjectName(u"helning_av_btn")
        self.helning_av_btn.setMaximumSize(QSize(40, 16777215))
        self.helning_av_btn.setFont(font)
        self.helning_av_btn.setStyleSheet(u"padding: 4px;")

        self.gridLayout_3.addWidget(self.helning_av_btn, 8, 2, 1, 1)


        self.verticalLayout_23.addWidget(self.ROV_row_2)

        self.lys_container = QFrame(self.ROV_column_2)
        self.lys_container.setObjectName(u"lys_container")
        self.lys_container.setMinimumSize(QSize(0, 0))
        self.lys_container.setMaximumSize(QSize(16777215, 16777215))
        self.lys_container.setFrameShape(QFrame.NoFrame)
        self.lys_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.lys_container)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lys_container_2 = QFrame(self.lys_container)
        self.lys_container_2.setObjectName(u"lys_container_2")
        self.lys_container_2.setMinimumSize(QSize(0, 0))
        self.lys_container_2.setMaximumSize(QSize(16777215, 150))
        self.lys_container_2.setFrameShape(QFrame.NoFrame)
        self.lys_container_2.setFrameShadow(QFrame.Raised)
        self.lys_label = QLabel(self.lys_container_2)
        self.lys_label.setObjectName(u"lys_label")
        self.lys_label.setGeometry(QRect(34, 66, 50, 50))
        self.lys_label.setMinimumSize(QSize(50, 40))
        self.lys_label.setFont(font)
        self.lys_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.lys_label.setTextFormat(Qt.RichText)
        self.lys_slider = QSlider(self.lys_container_2)
        self.lys_slider.setObjectName(u"lys_slider")
        self.lys_slider.setGeometry(QRect(70, 70, 91, 40))
        self.lys_slider.setMinimumSize(QSize(0, 40))
        self.lys_slider.setMaximumSize(QSize(150, 40))
        self.lys_slider.setFont(font)
        self.lys_slider.setStyleSheet(u"")
        self.lys_slider.setMaximum(100)
        self.lys_slider.setOrientation(Qt.Horizontal)
        self.lys_slider.setInvertedAppearance(False)
        self.lys_slider.setInvertedControls(False)
        self.lys_slider.setTickPosition(QSlider.NoTicks)
        self.lys_circle = QFrame(self.lys_container_2)
        self.lys_circle.setObjectName(u"lys_circle")
        self.lys_circle.setGeometry(QRect(90, 10, 50, 50))
        self.lys_circle.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.lys_circle.setFrameShape(QFrame.StyledPanel)
        self.lys_circle.setFrameShadow(QFrame.Raised)
        self.lys_percentage = QLabel(self.lys_circle)
        self.lys_percentage.setObjectName(u"lys_percentage")
        self.lys_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.lys_percentage.setFont(font)
        self.lys_percentage.setAutoFillBackground(False)
        self.lys_percentage.setScaledContents(False)
        self.lys_percentage.setAlignment(Qt.AlignCenter)
        self.lys_percentage.setWordWrap(False)
        self.lys = QFrame(self.lys_container_2)
        self.lys.setObjectName(u"lys")
        self.lys.setGeometry(QRect(85, 5, 60, 60))
        self.lys.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.lys.setFrameShape(QFrame.NoFrame)
        self.lys.setFrameShadow(QFrame.Raised)
        self.lys.raise_()
        self.lys_circle.raise_()
        self.lys_label.raise_()
        self.lys_slider.raise_()

        self.verticalLayout_24.addWidget(self.lys_container_2)


        self.verticalLayout_23.addWidget(self.lys_container)


        self.gridLayout_5.addWidget(self.ROV_column_2, 0, 1, 1, 1)

        self.ROV_column = QFrame(self.ROV_container)
        self.ROV_column.setObjectName(u"ROV_column")
        self.ROV_column.setMinimumSize(QSize(0, 0))
        self.ROV_column.setMaximumSize(QSize(16777215, 16777215))
        self.ROV_column.setFrameShape(QFrame.NoFrame)
        self.ROV_column.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.ROV_column)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.tid_label = QLabel(self.ROV_column)
        self.tid_label.setObjectName(u"tid_label")
        self.tid_label.setMinimumSize(QSize(100, 30))
        self.tid_label.setFont(font)
        self.tid_label.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.tid_label)

        self.tid = QLabel(self.ROV_column)
        self.tid.setObjectName(u"tid")
        self.tid.setMinimumSize(QSize(90, 30))
        self.tid.setMaximumSize(QSize(90, 30))
        self.tid.setFont(font)
        self.tid.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.tid.setFrameShape(QFrame.NoFrame)
        self.tid.setLineWidth(0)
        self.tid.setMidLineWidth(0)
        self.tid.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.tid)

        self.dybde_label = QLabel(self.ROV_column)
        self.dybde_label.setObjectName(u"dybde_label")
        self.dybde_label.setMinimumSize(QSize(100, 30))
        self.dybde_label.setFont(font)
        self.dybde_label.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dybde_label)

        self.dybde = QLabel(self.ROV_column)
        self.dybde.setObjectName(u"dybde")
        self.dybde.setMinimumSize(QSize(90, 30))
        self.dybde.setMaximumSize(QSize(90, 30))
        self.dybde.setFont(font)
        self.dybde.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.dybde.setFrameShape(QFrame.NoFrame)
        self.dybde.setLineWidth(0)
        self.dybde.setMidLineWidth(0)
        self.dybde.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dybde)

        self.spenning_label = QLabel(self.ROV_column)
        self.spenning_label.setObjectName(u"spenning_label")
        self.spenning_label.setMinimumSize(QSize(100, 30))
        self.spenning_label.setFont(font)
        self.spenning_label.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.spenning_label)

        self.spenning = QLabel(self.ROV_column)
        self.spenning.setObjectName(u"spenning")
        self.spenning.setMinimumSize(QSize(90, 30))
        self.spenning.setMaximumSize(QSize(90, 30))
        self.spenning.setFont(font)
        self.spenning.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.spenning.setFrameShape(QFrame.NoFrame)
        self.spenning.setFrameShadow(QFrame.Raised)
        self.spenning.setLineWidth(0)
        self.spenning.setMidLineWidth(0)
        self.spenning.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spenning)

        self.orientering_label = QLabel(self.ROV_column)
        self.orientering_label.setObjectName(u"orientering_label")
        self.orientering_label.setMinimumSize(QSize(100, 30))
        self.orientering_label.setFont(font)
        self.orientering_label.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.orientering_label)

        self.orientering = QLabel(self.ROV_column)
        self.orientering.setObjectName(u"orientering")
        self.orientering.setMinimumSize(QSize(90, 30))
        self.orientering.setMaximumSize(QSize(90, 30))
        self.orientering.setFont(font)
        self.orientering.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.orientering.setFrameShape(QFrame.NoFrame)
        self.orientering.setLineWidth(0)
        self.orientering.setMidLineWidth(0)
        self.orientering.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.orientering)

        self.effektforbruk_label = QLabel(self.ROV_column)
        self.effektforbruk_label.setObjectName(u"effektforbruk_label")
        self.effektforbruk_label.setMinimumSize(QSize(100, 0))
        self.effektforbruk_label.setMaximumSize(QSize(16777215, 16777215))
        self.effektforbruk_label.setFont(font)
        self.effektforbruk_label.setStyleSheet(u"")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.effektforbruk_label)

        self.effekt_elektronikk_label = QLabel(self.ROV_column)
        self.effekt_elektronikk_label.setObjectName(u"effekt_elektronikk_label")
        self.effekt_elektronikk_label.setMinimumSize(QSize(100, 30))
        self.effekt_elektronikk_label.setFont(font)
        self.effekt_elektronikk_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.effekt_elektronikk_label.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.effekt_elektronikk_label)

        self.effekt_elektronikk = QLabel(self.ROV_column)
        self.effekt_elektronikk.setObjectName(u"effekt_elektronikk")
        self.effekt_elektronikk.setMinimumSize(QSize(90, 30))
        self.effekt_elektronikk.setMaximumSize(QSize(90, 30))
        self.effekt_elektronikk.setFont(font)
        self.effekt_elektronikk.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.effekt_elektronikk.setFrameShape(QFrame.NoFrame)
        self.effekt_elektronikk.setLineWidth(0)
        self.effekt_elektronikk.setMidLineWidth(0)
        self.effekt_elektronikk.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.effekt_elektronikk)

        self.effekt_thrustere_label = QLabel(self.ROV_column)
        self.effekt_thrustere_label.setObjectName(u"effekt_thrustere_label")
        self.effekt_thrustere_label.setMinimumSize(QSize(100, 30))
        self.effekt_thrustere_label.setFont(font)
        self.effekt_thrustere_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.effekt_thrustere_label.setTextFormat(Qt.PlainText)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.effekt_thrustere_label)

        self.effekt_thrustere = QLabel(self.ROV_column)
        self.effekt_thrustere.setObjectName(u"effekt_thrustere")
        self.effekt_thrustere.setMinimumSize(QSize(90, 30))
        self.effekt_thrustere.setMaximumSize(QSize(90, 30))
        self.effekt_thrustere.setFont(font)
        self.effekt_thrustere.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.effekt_thrustere.setFrameShape(QFrame.NoFrame)
        self.effekt_thrustere.setLineWidth(0)
        self.effekt_thrustere.setMidLineWidth(0)
        self.effekt_thrustere.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.effekt_thrustere)

        self.effekt_manipulator_label = QLabel(self.ROV_column)
        self.effekt_manipulator_label.setObjectName(u"effekt_manipulator_label")
        self.effekt_manipulator_label.setMinimumSize(QSize(100, 30))
        self.effekt_manipulator_label.setFont(font)
        self.effekt_manipulator_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.effekt_manipulator_label.setTextFormat(Qt.RichText)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.effekt_manipulator_label)

        self.effekt_manipulator = QLabel(self.ROV_column)
        self.effekt_manipulator.setObjectName(u"effekt_manipulator")
        self.effekt_manipulator.setMinimumSize(QSize(90, 30))
        self.effekt_manipulator.setMaximumSize(QSize(90, 30))
        self.effekt_manipulator.setFont(font)
        self.effekt_manipulator.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.effekt_manipulator.setFrameShape(QFrame.NoFrame)
        self.effekt_manipulator.setLineWidth(0)
        self.effekt_manipulator.setMidLineWidth(0)
        self.effekt_manipulator.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.effekt_manipulator)


        self.gridLayout_5.addWidget(self.ROV_column, 0, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.ROV_container)

        self.temperatur_container = QFrame(self.column1)
        self.temperatur_container.setObjectName(u"temperatur_container")
        self.temperatur_container.setMinimumSize(QSize(250, 0))
        self.temperatur_container.setMaximumSize(QSize(16777215, 80))
        self.temperatur_container.setFrameShape(QFrame.NoFrame)
        self.temperatur_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.temperatur_container)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.temp_ROV_label = QLabel(self.temperatur_container)
        self.temp_ROV_label.setObjectName(u"temp_ROV_label")
        self.temp_ROV_label.setMaximumSize(QSize(16777215, 16777215))
        self.temp_ROV_label.setFont(font)
        self.temp_ROV_label.setTextFormat(Qt.PlainText)

        self.verticalLayout_17.addWidget(self.temp_ROV_label)

        self.temp_rov = QFrame(self.temperatur_container)
        self.temp_rov.setObjectName(u"temp_rov")
        self.temp_rov.setMinimumSize(QSize(0, 0))
        self.temp_rov.setMaximumSize(QSize(420, 100))
        self.temp_rov.setFrameShape(QFrame.NoFrame)
        self.temp_rov.setFrameShadow(QFrame.Raised)
        self.temp_rov.setLineWidth(0)
        self.horizontalLayout_14 = QHBoxLayout(self.temp_rov)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.temp_btn_container = QFrame(self.temp_rov)
        self.temp_btn_container.setObjectName(u"temp_btn_container")
        self.temp_btn_container.setMaximumSize(QSize(200, 16777215))
        self.temp_btn_container.setFrameShape(QFrame.StyledPanel)
        self.temp_btn_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.temp_btn_container)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.temp_ROV_1 = QLabel(self.temp_btn_container)
        self.temp_ROV_1.setObjectName(u"temp_ROV_1")
        self.temp_ROV_1.setMinimumSize(QSize(50, 30))
        self.temp_ROV_1.setMaximumSize(QSize(50, 30))
        self.temp_ROV_1.setFont(font)
        self.temp_ROV_1.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.temp_ROV_1.setFrameShape(QFrame.NoFrame)
        self.temp_ROV_1.setLineWidth(0)
        self.temp_ROV_1.setMidLineWidth(0)
        self.temp_ROV_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.temp_ROV_1)

        self.temp_ROV_2 = QLabel(self.temp_btn_container)
        self.temp_ROV_2.setObjectName(u"temp_ROV_2")
        self.temp_ROV_2.setMinimumSize(QSize(50, 30))
        self.temp_ROV_2.setMaximumSize(QSize(50, 30))
        self.temp_ROV_2.setFont(font)
        self.temp_ROV_2.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.temp_ROV_2.setFrameShape(QFrame.NoFrame)
        self.temp_ROV_2.setLineWidth(0)
        self.temp_ROV_2.setMidLineWidth(0)
        self.temp_ROV_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.temp_ROV_2)

        self.temp_ROV_3 = QLabel(self.temp_btn_container)
        self.temp_ROV_3.setObjectName(u"temp_ROV_3")
        self.temp_ROV_3.setMinimumSize(QSize(50, 30))
        self.temp_ROV_3.setMaximumSize(QSize(50, 30))
        self.temp_ROV_3.setFont(font)
        self.temp_ROV_3.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.temp_ROV_3.setFrameShape(QFrame.NoFrame)
        self.temp_ROV_3.setLineWidth(0)
        self.temp_ROV_3.setMidLineWidth(0)
        self.temp_ROV_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.temp_ROV_3)


        self.horizontalLayout_14.addWidget(self.temp_btn_container)

        self.gjsnitttemp_label = QLabel(self.temp_rov)
        self.gjsnitttemp_label.setObjectName(u"gjsnitttemp_label")
        self.gjsnitttemp_label.setMinimumSize(QSize(150, 0))
        self.gjsnitttemp_label.setMaximumSize(QSize(100, 16777215))
        self.gjsnitttemp_label.setFont(font)
        self.gjsnitttemp_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.gjsnitttemp_label.setTextFormat(Qt.PlainText)
        self.gjsnitttemp_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.gjsnitttemp_label)

        self.gjsnitt_temp_ROV = QLabel(self.temp_rov)
        self.gjsnitt_temp_ROV.setObjectName(u"gjsnitt_temp_ROV")
        self.gjsnitt_temp_ROV.setMinimumSize(QSize(50, 30))
        self.gjsnitt_temp_ROV.setMaximumSize(QSize(50, 30))
        self.gjsnitt_temp_ROV.setFont(font)
        self.gjsnitt_temp_ROV.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.gjsnitt_temp_ROV.setFrameShape(QFrame.NoFrame)
        self.gjsnitt_temp_ROV.setLineWidth(0)
        self.gjsnitt_temp_ROV.setMidLineWidth(0)
        self.gjsnitt_temp_ROV.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.gjsnitt_temp_ROV)


        self.verticalLayout_17.addWidget(self.temp_rov)


        self.verticalLayout_26.addWidget(self.temperatur_container)

        self.vannlekk_container = QFrame(self.column1)
        self.vannlekk_container.setObjectName(u"vannlekk_container")
        self.vannlekk_container.setMinimumSize(QSize(0, 0))
        self.vannlekk_container.setMaximumSize(QSize(16777215, 80))
        self.vannlekk_container.setFrameShape(QFrame.NoFrame)
        self.vannlekk_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.vannlekk_container)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.vannlekk_label = QLabel(self.vannlekk_container)
        self.vannlekk_label.setObjectName(u"vannlekk_label")
        self.vannlekk_label.setMaximumSize(QSize(16777215, 16777215))
        self.vannlekk_label.setFont(font)
        self.vannlekk_label.setTextFormat(Qt.PlainText)

        self.verticalLayout_21.addWidget(self.vannlekk_label)

        self.vannlekk_btn_container = QFrame(self.vannlekk_container)
        self.vannlekk_btn_container.setObjectName(u"vannlekk_btn_container")
        self.vannlekk_btn_container.setMinimumSize(QSize(0, 0))
        self.vannlekk_btn_container.setMaximumSize(QSize(300, 100))
        self.vannlekk_btn_container.setFrameShape(QFrame.NoFrame)
        self.vannlekk_btn_container.setFrameShadow(QFrame.Raised)
        self.vannlekk_btn_container.setLineWidth(0)
        self.horizontalLayout_15 = QHBoxLayout(self.vannlekk_btn_container)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.vannlekk_btn = QFrame(self.vannlekk_btn_container)
        self.vannlekk_btn.setObjectName(u"vannlekk_btn")
        self.vannlekk_btn.setMaximumSize(QSize(190, 16777215))
        self.vannlekk_btn.setFrameShape(QFrame.NoFrame)
        self.vannlekk_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.vannlekk_btn)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.vannlekk_1 = QLabel(self.vannlekk_btn)
        self.vannlekk_1.setObjectName(u"vannlekk_1")
        self.vannlekk_1.setMinimumSize(QSize(50, 30))
        self.vannlekk_1.setMaximumSize(QSize(50, 30))
        self.vannlekk_1.setFont(font)
        self.vannlekk_1.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.vannlekk_1.setFrameShape(QFrame.NoFrame)
        self.vannlekk_1.setLineWidth(0)
        self.vannlekk_1.setMidLineWidth(0)
        self.vannlekk_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.vannlekk_1)

        self.vannlekk_2 = QLabel(self.vannlekk_btn)
        self.vannlekk_2.setObjectName(u"vannlekk_2")
        self.vannlekk_2.setMinimumSize(QSize(50, 30))
        self.vannlekk_2.setMaximumSize(QSize(50, 30))
        self.vannlekk_2.setFont(font)
        self.vannlekk_2.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.vannlekk_2.setFrameShape(QFrame.NoFrame)
        self.vannlekk_2.setLineWidth(0)
        self.vannlekk_2.setMidLineWidth(0)
        self.vannlekk_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.vannlekk_2)

        self.vannlekk_3 = QLabel(self.vannlekk_btn)
        self.vannlekk_3.setObjectName(u"vannlekk_3")
        self.vannlekk_3.setMinimumSize(QSize(50, 30))
        self.vannlekk_3.setMaximumSize(QSize(50, 30))
        self.vannlekk_3.setFont(font)
        self.vannlekk_3.setStyleSheet(u"background-color: rgb(30, 33, 38); border-radius: 5px; border: 1px solid rgb(30, 30, 30);")
        self.vannlekk_3.setFrameShape(QFrame.NoFrame)
        self.vannlekk_3.setLineWidth(0)
        self.vannlekk_3.setMidLineWidth(0)
        self.vannlekk_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.vannlekk_3)


        self.horizontalLayout_15.addWidget(self.vannlekk_btn)


        self.verticalLayout_21.addWidget(self.vannlekk_btn_container)


        self.verticalLayout_26.addWidget(self.vannlekk_container)


        self.horizontalLayout_10.addWidget(self.column1)

        self.column2 = QFrame(self.scrollAreaWidgetContent)
        self.column2.setObjectName(u"column2")
        self.column2.setMinimumSize(QSize(350, 700))
        self.column2.setMaximumSize(QSize(350, 700))
        self.column2.setFrameShape(QFrame.NoFrame)
        self.column2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.column2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.motor_title = QLabel(self.column2)
        self.motor_title.setObjectName(u"motor_title")
        self.motor_title.setFont(font)

        self.verticalLayout_16.addWidget(self.motor_title)

        self.rov_label = QLabel(self.column2)
        self.rov_label.setObjectName(u"rov_label")
        self.rov_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.rov_label.setLineWidth(1)
        self.rov_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.rov_label)

        self.motor_containter = QFrame(self.column2)
        self.motor_containter.setObjectName(u"motor_containter")
        self.motor_containter.setMinimumSize(QSize(0, 300))
        self.motor_containter.setFrameShape(QFrame.NoFrame)
        self.motor_containter.setFrameShadow(QFrame.Raised)
        self.motor_img = QLabel(self.motor_containter)
        self.motor_img.setObjectName(u"motor_img")
        self.motor_img.setGeometry(QRect(100, 30, 141, 181))
        self.motor_img.setMinimumSize(QSize(0, 0))
        self.motor_img.setMaximumSize(QSize(16777215, 16777215))
        self.motor_img.setSizeIncrement(QSize(0, 0))
        self.motor_img.setPixmap(QPixmap(u":/images/images/thrustere.png"))
        self.motor_img.setScaledContents(True)
        self.VHF2 = QFrame(self.motor_containter)
        self.VHF2.setObjectName(u"VHF2")
        self.VHF2.setGeometry(QRect(19, 11, 50, 51))
        self.VHF2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.VHF2.setFrameShape(QFrame.StyledPanel)
        self.VHF2.setFrameShadow(QFrame.Raised)
        self.VHF_percentage = QLabel(self.VHF2)
        self.VHF_percentage.setObjectName(u"VHF_percentage")
        self.VHF_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.VHF_percentage.setFont(font)
        self.VHF_percentage.setAutoFillBackground(False)
        self.VHF_percentage.setScaledContents(False)
        self.VHF_percentage.setAlignment(Qt.AlignCenter)
        self.VHF_percentage.setWordWrap(False)
        self.VHF = QFrame(self.motor_containter)
        self.VHF.setObjectName(u"VHF")
        self.VHF.setGeometry(QRect(14, 7, 60, 60))
        self.VHF.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.VHF.setFrameShape(QFrame.NoFrame)
        self.VHF.setFrameShadow(QFrame.Raised)
        self.VVF = QFrame(self.motor_containter)
        self.VVF.setObjectName(u"VVF")
        self.VVF.setGeometry(QRect(75, 25, 60, 60))
        self.VVF.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.VVF.setFrameShape(QFrame.NoFrame)
        self.VVF.setFrameShadow(QFrame.Raised)
        self.VVF2 = QFrame(self.motor_containter)
        self.VVF2.setObjectName(u"VVF2")
        self.VVF2.setGeometry(QRect(80, 30, 50, 50))
        self.VVF2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.VVF2.setFrameShape(QFrame.NoFrame)
        self.VVF2.setFrameShadow(QFrame.Raised)
        self.VVF_percentage = QLabel(self.VVF2)
        self.VVF_percentage.setObjectName(u"VVF_percentage")
        self.VVF_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.VVF_percentage.setFont(font)
        self.VVF_percentage.setAutoFillBackground(False)
        self.VVF_percentage.setScaledContents(False)
        self.VVF_percentage.setAlignment(Qt.AlignCenter)
        self.VVF_percentage.setWordWrap(False)
        self.HHF2 = QFrame(self.motor_containter)
        self.HHF2.setObjectName(u"HHF2")
        self.HHF2.setGeometry(QRect(270, 10, 50, 50))
        self.HHF2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.HHF2.setFrameShape(QFrame.StyledPanel)
        self.HHF2.setFrameShadow(QFrame.Raised)
        self.HHF_percentage = QLabel(self.HHF2)
        self.HHF_percentage.setObjectName(u"HHF_percentage")
        self.HHF_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.HHF_percentage.setFont(font)
        self.HHF_percentage.setAutoFillBackground(False)
        self.HHF_percentage.setScaledContents(False)
        self.HHF_percentage.setAlignment(Qt.AlignCenter)
        self.HHF_percentage.setWordWrap(False)
        self.HHF = QFrame(self.motor_containter)
        self.HHF.setObjectName(u"HHF")
        self.HHF.setGeometry(QRect(265, 5, 60, 60))
        self.HHF.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.HHF.setFrameShape(QFrame.NoFrame)
        self.HHF.setFrameShadow(QFrame.Raised)
        self.HVF2 = QFrame(self.motor_containter)
        self.HVF2.setObjectName(u"HVF2")
        self.HVF2.setGeometry(QRect(210, 30, 50, 50))
        self.HVF2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.HVF2.setFrameShape(QFrame.StyledPanel)
        self.HVF2.setFrameShadow(QFrame.Raised)
        self.HVF_percentage = QLabel(self.HVF2)
        self.HVF_percentage.setObjectName(u"HVF_percentage")
        self.HVF_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.HVF_percentage.setFont(font)
        self.HVF_percentage.setAutoFillBackground(False)
        self.HVF_percentage.setScaledContents(False)
        self.HVF_percentage.setAlignment(Qt.AlignCenter)
        self.HVF_percentage.setWordWrap(False)
        self.HVF = QFrame(self.motor_containter)
        self.HVF.setObjectName(u"HVF")
        self.HVF.setGeometry(QRect(205, 25, 60, 60))
        self.HVF.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.HVF.setFrameShape(QFrame.NoFrame)
        self.HVF.setFrameShadow(QFrame.Raised)
        self.HVB2 = QFrame(self.motor_containter)
        self.HVB2.setObjectName(u"HVB2")
        self.HVB2.setGeometry(QRect(220, 140, 50, 50))
        self.HVB2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.HVB2.setFrameShape(QFrame.StyledPanel)
        self.HVB2.setFrameShadow(QFrame.Raised)
        self.HVB_percentage = QLabel(self.HVB2)
        self.HVB_percentage.setObjectName(u"HVB_percentage")
        self.HVB_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.HVB_percentage.setFont(font)
        self.HVB_percentage.setAutoFillBackground(False)
        self.HVB_percentage.setScaledContents(False)
        self.HVB_percentage.setAlignment(Qt.AlignCenter)
        self.HVB_percentage.setWordWrap(False)
        self.HVB = QFrame(self.motor_containter)
        self.HVB.setObjectName(u"HVB")
        self.HVB.setGeometry(QRect(215, 135, 60, 60))
        self.HVB.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.HVB.setFrameShape(QFrame.NoFrame)
        self.HVB.setFrameShadow(QFrame.Raised)
        self.HHB2 = QFrame(self.motor_containter)
        self.HHB2.setObjectName(u"HHB2")
        self.HHB2.setGeometry(QRect(260, 185, 50, 50))
        self.HHB2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.HHB2.setFrameShape(QFrame.StyledPanel)
        self.HHB2.setFrameShadow(QFrame.Raised)
        self.HHB_percentage = QLabel(self.HHB2)
        self.HHB_percentage.setObjectName(u"HHB_percentage")
        self.HHB_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.HHB_percentage.setFont(font)
        self.HHB_percentage.setAutoFillBackground(False)
        self.HHB_percentage.setScaledContents(False)
        self.HHB_percentage.setAlignment(Qt.AlignCenter)
        self.HHB_percentage.setWordWrap(False)
        self.HHB = QFrame(self.motor_containter)
        self.HHB.setObjectName(u"HHB")
        self.HHB.setGeometry(QRect(255, 180, 60, 60))
        self.HHB.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.HHB.setFrameShape(QFrame.NoFrame)
        self.HHB.setFrameShadow(QFrame.Raised)
        self.VVB = QFrame(self.motor_containter)
        self.VVB.setObjectName(u"VVB")
        self.VVB.setGeometry(QRect(70, 160, 60, 60))
        self.VVB.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.VVB.setFrameShape(QFrame.NoFrame)
        self.VVB.setFrameShadow(QFrame.Raised)
        self.VVB2 = QFrame(self.motor_containter)
        self.VVB2.setObjectName(u"VVB2")
        self.VVB2.setGeometry(QRect(75, 165, 50, 50))
        self.VVB2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.VVB2.setFrameShape(QFrame.StyledPanel)
        self.VVB2.setFrameShadow(QFrame.Raised)
        self.VVB_percentage = QLabel(self.VVB2)
        self.VVB_percentage.setObjectName(u"VVB_percentage")
        self.VVB_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.VVB_percentage.setFont(font)
        self.VVB_percentage.setAutoFillBackground(False)
        self.VVB_percentage.setScaledContents(False)
        self.VVB_percentage.setAlignment(Qt.AlignCenter)
        self.VVB_percentage.setWordWrap(False)
        self.VHB2 = QFrame(self.motor_containter)
        self.VHB2.setObjectName(u"VHB2")
        self.VHB2.setGeometry(QRect(10, 190, 50, 50))
        self.VHB2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.VHB2.setFrameShape(QFrame.StyledPanel)
        self.VHB2.setFrameShadow(QFrame.Raised)
        self.VHB_percentage = QLabel(self.VHB2)
        self.VHB_percentage.setObjectName(u"VHB_percentage")
        self.VHB_percentage.setGeometry(QRect(6, 13, 37, 21))
        self.VHB_percentage.setFont(font)
        self.VHB_percentage.setAutoFillBackground(False)
        self.VHB_percentage.setScaledContents(False)
        self.VHB_percentage.setAlignment(Qt.AlignCenter)
        self.VHB_percentage.setWordWrap(False)
        self.VHB = QFrame(self.motor_containter)
        self.VHB.setObjectName(u"VHB")
        self.VHB.setGeometry(QRect(5, 185, 60, 60))
        self.VHB.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.VHB.setFrameShape(QFrame.NoFrame)
        self.VHB.setFrameShadow(QFrame.Raised)
        self.motor_img.raise_()
        self.VHB.raise_()
        self.HVB.raise_()
        self.HHB.raise_()
        self.HHF.raise_()
        self.HVF.raise_()
        self.VHF.raise_()
        self.VHF2.raise_()
        self.VVF.raise_()
        self.VVF2.raise_()
        self.HHF2.raise_()
        self.HVF2.raise_()
        self.HVB2.raise_()
        self.HHB2.raise_()
        self.VVB.raise_()
        self.VVB2.raise_()
        self.VHB2.raise_()

        self.verticalLayout_16.addWidget(self.motor_containter)

        self.manipulator_label = QLabel(self.column2)
        self.manipulator_label.setObjectName(u"manipulator_label")
        self.manipulator_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.manipulator_label.setLineWidth(1)
        self.manipulator_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.manipulator_label)

        self.mani_container = QFrame(self.column2)
        self.mani_container.setObjectName(u"mani_container")
        self.mani_container.setMinimumSize(QSize(0, 190))
        self.mani_container.setFrameShape(QFrame.NoFrame)
        self.mani_container.setFrameShadow(QFrame.Raised)
        self.manipulator_img = QLabel(self.mani_container)
        self.manipulator_img.setObjectName(u"manipulator_img")
        self.manipulator_img.setGeometry(QRect(20, 30, 320, 150))
        self.manipulator_img.setMinimumSize(QSize(320, 0))
        self.manipulator_img.setMaximumSize(QSize(320, 150))
        self.manipulator_img.setSizeIncrement(QSize(0, 0))
        self.manipulator_img.setPixmap(QPixmap(u":/images/images/manipulator.png"))
        self.manipulator_img.setScaledContents(True)
        self.mani_circle_2 = QFrame(self.mani_container)
        self.mani_circle_2.setObjectName(u"mani_circle_2")
        self.mani_circle_2.setGeometry(QRect(150, 40, 50, 50))
        self.mani_circle_2.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.mani_circle_2.setFrameShape(QFrame.StyledPanel)
        self.mani_circle_2.setFrameShadow(QFrame.Raised)
        self.mani_percentage_2 = QLabel(self.mani_circle_2)
        self.mani_percentage_2.setObjectName(u"mani_percentage_2")
        self.mani_percentage_2.setGeometry(QRect(6, 13, 37, 21))
        self.mani_percentage_2.setFont(font)
        self.mani_percentage_2.setAutoFillBackground(False)
        self.mani_percentage_2.setScaledContents(False)
        self.mani_percentage_2.setAlignment(Qt.AlignCenter)
        self.mani_percentage_2.setWordWrap(False)
        self.mani_1 = QFrame(self.mani_container)
        self.mani_1.setObjectName(u"mani_1")
        self.mani_1.setGeometry(QRect(145, 35, 60, 60))
        self.mani_1.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.mani_1.setFrameShape(QFrame.NoFrame)
        self.mani_1.setFrameShadow(QFrame.Raised)
        self.mani_2 = QFrame(self.mani_container)
        self.mani_2.setObjectName(u"mani_2")
        self.mani_2.setGeometry(QRect(200, 110, 60, 60))
        self.mani_2.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.mani_2.setFrameShape(QFrame.NoFrame)
        self.mani_2.setFrameShadow(QFrame.Raised)
        self.mani_circle_3 = QFrame(self.mani_container)
        self.mani_circle_3.setObjectName(u"mani_circle_3")
        self.mani_circle_3.setGeometry(QRect(205, 115, 50, 50))
        self.mani_circle_3.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.mani_circle_3.setFrameShape(QFrame.StyledPanel)
        self.mani_circle_3.setFrameShadow(QFrame.Raised)
        self.mani_percentage_3 = QLabel(self.mani_circle_3)
        self.mani_percentage_3.setObjectName(u"mani_percentage_3")
        self.mani_percentage_3.setGeometry(QRect(6, 13, 37, 21))
        self.mani_percentage_3.setFont(font)
        self.mani_percentage_3.setAutoFillBackground(False)
        self.mani_percentage_3.setScaledContents(False)
        self.mani_percentage_3.setAlignment(Qt.AlignCenter)
        self.mani_percentage_3.setWordWrap(False)
        self.mani_3 = QFrame(self.mani_container)
        self.mani_3.setObjectName(u"mani_3")
        self.mani_3.setGeometry(QRect(54, 115, 60, 60))
        self.mani_3.setStyleSheet(u"QFrame { border-radius: 30px; background-color: rgba(77, 77, 127, 100); }")
        self.mani_3.setFrameShape(QFrame.NoFrame)
        self.mani_3.setFrameShadow(QFrame.Raised)
        self.mani_circle_1 = QFrame(self.mani_container)
        self.mani_circle_1.setObjectName(u"mani_circle_1")
        self.mani_circle_1.setGeometry(QRect(59, 120, 50, 50))
        self.mani_circle_1.setStyleSheet(u"QFrame { border-radius: 25px; background-color: rgba(77, 77, 127, 255); }")
        self.mani_circle_1.setFrameShape(QFrame.StyledPanel)
        self.mani_circle_1.setFrameShadow(QFrame.Raised)
        self.mani_percentage_1 = QLabel(self.mani_circle_1)
        self.mani_percentage_1.setObjectName(u"mani_percentage_1")
        self.mani_percentage_1.setGeometry(QRect(6, 13, 37, 21))
        self.mani_percentage_1.setFont(font)
        self.mani_percentage_1.setAutoFillBackground(False)
        self.mani_percentage_1.setScaledContents(False)
        self.mani_percentage_1.setAlignment(Qt.AlignCenter)
        self.mani_percentage_1.setWordWrap(False)
        self.mani_1.raise_()
        self.manipulator_img.raise_()
        self.mani_circle_2.raise_()
        self.mani_2.raise_()
        self.mani_circle_3.raise_()
        self.mani_3.raise_()
        self.mani_circle_1.raise_()

        self.verticalLayout_16.addWidget(self.mani_container)

        self.test_label = QLabel(self.column2)
        self.test_label.setObjectName(u"test_label")
        self.test_label.setMinimumSize(QSize(0, 0))
        self.test_label.setMaximumSize(QSize(16777215, 16777215))
        self.test_label.setFont(font)
        self.test_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.test_label.setFrameShadow(QFrame.Plain)
        self.test_label.setTextFormat(Qt.PlainText)

        self.verticalLayout_16.addWidget(self.test_label)

        self.slider = QSlider(self.column2)
        self.slider.setObjectName(u"slider")
        self.slider.setMinimumSize(QSize(100, 30))
        self.slider.setMaximumSize(QSize(150, 20))
        self.slider.setMinimum(-100)
        self.slider.setMaximum(100)
        self.slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_16.addWidget(self.slider)

        self.sensor_lekk_label_3 = QLabel(self.column2)
        self.sensor_lekk_label_3.setObjectName(u"sensor_lekk_label_3")
        self.sensor_lekk_label_3.setMinimumSize(QSize(0, 40))
        self.sensor_lekk_label_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.sensor_lekk_label_3.setLineWidth(1)
        self.sensor_lekk_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_16.addWidget(self.sensor_lekk_label_3)


        self.horizontalLayout_10.addWidget(self.column2)

        self.column3 = QFrame(self.scrollAreaWidgetContent)
        self.column3.setObjectName(u"column3")
        self.column3.setMinimumSize(QSize(400, 700))
        self.column3.setMaximumSize(QSize(350, 700))
        self.column3.setFrameShape(QFrame.NoFrame)
        self.column3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.column3)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(12, 12, 12, 12)
        self.bilde_container = QFrame(self.column3)
        self.bilde_container.setObjectName(u"bilde_container")
        self.bilde_container.setMinimumSize(QSize(0, 0))
        self.bilde_container.setMaximumSize(QSize(16777215, 150))
        self.bilde_container.setFrameShape(QFrame.NoFrame)
        self.bilde_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.bilde_container)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.bilde_title = QLabel(self.bilde_container)
        self.bilde_title.setObjectName(u"bilde_title")
        self.bilde_title.setFont(font)
        self.bilde_title.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.bilde_title)

        self.bilde_container_2 = QFrame(self.bilde_container)
        self.bilde_container_2.setObjectName(u"bilde_container_2")
        self.bilde_container_2.setFrameShape(QFrame.NoFrame)
        self.bilde_container_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.bilde_container_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.korallrev_btn = QPushButton(self.bilde_container_2)
        self.korallrev_btn.setObjectName(u"korallrev_btn")
        self.korallrev_btn.setMinimumSize(QSize(150, 45))
        self.korallrev_btn.setFont(font)
        self.korallrev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.korallrev_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")

        self.gridLayout.addWidget(self.korallrev_btn, 0, 0, 1, 1)

        self.bilde_label_3 = QLabel(self.bilde_container_2)
        self.bilde_label_3.setObjectName(u"bilde_label_3")
        self.bilde_label_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.bilde_label_3.setLineWidth(1)
        self.bilde_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.bilde_label_3, 0, 1, 1, 1)

        self.fotomoasaikk_btn = QPushButton(self.bilde_container_2)
        self.fotomoasaikk_btn.setObjectName(u"fotomoasaikk_btn")
        self.fotomoasaikk_btn.setMinimumSize(QSize(150, 45))
        self.fotomoasaikk_btn.setFont(font)
        self.fotomoasaikk_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.fotomoasaikk_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")

        self.gridLayout.addWidget(self.fotomoasaikk_btn, 1, 0, 1, 1)

        self.bilde_label_2 = QLabel(self.bilde_container_2)
        self.bilde_label_2.setObjectName(u"bilde_label_2")
        self.bilde_label_2.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.bilde_label_2.setLineWidth(1)
        self.bilde_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.bilde_label_2, 1, 1, 1, 1)


        self.verticalLayout_27.addWidget(self.bilde_container_2)


        self.verticalLayout_39.addWidget(self.bilde_container)

        self.kamera_container = QFrame(self.column3)
        self.kamera_container.setObjectName(u"kamera_container")
        self.kamera_container.setMaximumSize(QSize(16777215, 550))
        self.kamera_container.setFrameShape(QFrame.NoFrame)
        self.kamera_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.kamera_container)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.kamera_title = QLabel(self.kamera_container)
        self.kamera_title.setObjectName(u"kamera_title")
        self.kamera_title.setFont(font)
        self.kamera_title.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.kamera_title)

        self.ta_bilde_frontkamera_btn = QPushButton(self.kamera_container)
        self.ta_bilde_frontkamera_btn.setObjectName(u"ta_bilde_frontkamera_btn")
        self.ta_bilde_frontkamera_btn.setMinimumSize(QSize(150, 45))
        self.ta_bilde_frontkamera_btn.setFont(font)
        self.ta_bilde_frontkamera_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ta_bilde_frontkamera_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        icon5 = QIcon()
        icon5.addFile(u":/images/images/camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ta_bilde_frontkamera_btn.setIcon(icon5)

        self.verticalLayout_28.addWidget(self.ta_bilde_frontkamera_btn)

        self.ta_bilde_havbunn_btn = QPushButton(self.kamera_container)
        self.ta_bilde_havbunn_btn.setObjectName(u"ta_bilde_havbunn_btn")
        self.ta_bilde_havbunn_btn.setMinimumSize(QSize(150, 45))
        self.ta_bilde_havbunn_btn.setFont(font)
        self.ta_bilde_havbunn_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ta_bilde_havbunn_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        self.ta_bilde_havbunn_btn.setIcon(icon5)

        self.verticalLayout_28.addWidget(self.ta_bilde_havbunn_btn)

        self.slett_bilde_btn = QPushButton(self.kamera_container)
        self.slett_bilde_btn.setObjectName(u"slett_bilde_btn")
        self.slett_bilde_btn.setMinimumSize(QSize(150, 45))
        self.slett_bilde_btn.setFont(font)
        self.slett_bilde_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.slett_bilde_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255));} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255));}")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.slett_bilde_btn.setIcon(icon6)

        self.verticalLayout_28.addWidget(self.slett_bilde_btn)

        self.siste_bilde_label = QLabel(self.kamera_container)
        self.siste_bilde_label.setObjectName(u"siste_bilde_label")
        self.siste_bilde_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.siste_bilde_label.setLineWidth(1)
        self.siste_bilde_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.siste_bilde_label)

        self.show_image = QLabel(self.kamera_container)
        self.show_image.setObjectName(u"show_image")
        self.show_image.setMinimumSize(QSize(0, 250))
        self.show_image.setMaximumSize(QSize(360, 250))
        self.show_image.setPixmap(QPixmap(u":/images/images/show_image.png"))
        self.show_image.setScaledContents(True)
        self.show_image.setAlignment(Qt.AlignCenter)
        self.show_image.setMargin(0)

        self.verticalLayout_28.addWidget(self.show_image)


        self.verticalLayout_39.addWidget(self.kamera_container)


        self.horizontalLayout_10.addWidget(self.column3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContent)

        self.horizontalLayout_6.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.row)

        self.stackedWidget.addWidget(self.informasjon)
        self.kontroller = QWidget()
        self.kontroller.setObjectName(u"kontroller")
        self.verticalLayout_20 = QVBoxLayout(self.kontroller)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.hoved_frame_column = QFrame(self.kontroller)
        self.hoved_frame_column.setObjectName(u"hoved_frame_column")
        self.hoved_frame_column.setStyleSheet(u"color: black;")
        self.hoved_frame_column.setFrameShape(QFrame.NoFrame)
        self.hoved_frame_column.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.hoved_frame_column)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(12, 0, 12, -1)
        self.scrollarea = QScrollArea(self.hoved_frame_column)
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setFrameShape(QFrame.NoFrame)
        self.scrollarea.setFrameShadow(QFrame.Plain)
        self.scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollarea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollarea.setWidgetResizable(True)
        self.scrollarea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1313, 842))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.kontroller_container = QFrame(self.scrollAreaWidgetContents)
        self.kontroller_container.setObjectName(u"kontroller_container")
        self.kontroller_container.setFrameShape(QFrame.NoFrame)
        self.kontroller_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.kontroller_container)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.kontroller_rows = QFrame(self.kontroller_container)
        self.kontroller_rows.setObjectName(u"kontroller_rows")
        self.kontroller_rows.setMaximumSize(QSize(1400, 16777215))
        self.kontroller_rows.setFrameShape(QFrame.StyledPanel)
        self.kontroller_rows.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.kontroller_rows)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.kontroller_btn_container = QFrame(self.kontroller_rows)
        self.kontroller_btn_container.setObjectName(u"kontroller_btn_container")
        self.kontroller_btn_container.setMaximumSize(QSize(16777215, 200))
        self.kontroller_btn_container.setFrameShape(QFrame.NoFrame)
        self.kontroller_btn_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.kontroller_btn_container)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.text_container = QFrame(self.kontroller_btn_container)
        self.text_container.setObjectName(u"text_container")
        self.text_container.setFrameShape(QFrame.StyledPanel)
        self.text_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.text_container)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.kontroller_title = QLabel(self.text_container)
        self.kontroller_title.setObjectName(u"kontroller_title")
        self.kontroller_title.setMinimumSize(QSize(0, 20))
        self.kontroller_title.setFont(font)
        self.kontroller_title.setStyleSheet(u"color: #dddddd;")
        self.kontroller_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_22.addWidget(self.kontroller_title)

        self.kontroller_text_label = QLabel(self.text_container)
        self.kontroller_text_label.setObjectName(u"kontroller_text_label")
        self.kontroller_text_label.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.kontroller_text_label.setLineWidth(1)
        self.kontroller_text_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.kontroller_text_label.setWordWrap(True)

        self.verticalLayout_22.addWidget(self.kontroller_text_label)


        self.horizontalLayout_13.addWidget(self.text_container)

        self.profile_container = QFrame(self.kontroller_btn_container)
        self.profile_container.setObjectName(u"profile_container")
        self.profile_container.setMinimumSize(QSize(0, 0))
        self.profile_container.setMaximumSize(QSize(350, 200))
        self.profile_container.setFrameShape(QFrame.NoFrame)
        self.profile_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.profile_container)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 30)
        self.velg_profil_label = QLabel(self.profile_container)
        self.velg_profil_label.setObjectName(u"velg_profil_label")
        self.velg_profil_label.setMinimumSize(QSize(0, 40))
        self.velg_profil_label.setMaximumSize(QSize(100, 40))
        self.velg_profil_label.setFont(font)
        self.velg_profil_label.setStyleSheet(u"color: #dddddd;")

        self.horizontalLayout_11.addWidget(self.velg_profil_label)

        self.comboBox_velg_profil = QComboBox(self.profile_container)
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


        self.horizontalLayout_13.addWidget(self.profile_container)

        self.profile_btn_container = QFrame(self.kontroller_btn_container)
        self.profile_btn_container.setObjectName(u"profile_btn_container")
        self.profile_btn_container.setMinimumSize(QSize(0, 120))
        self.profile_btn_container.setFrameShape(QFrame.NoFrame)
        self.profile_btn_container.setFrameShadow(QFrame.Raised)
        self.reset_btn = QPushButton(self.profile_btn_container)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(40, 70, 201, 45))
        self.reset_btn.setMinimumSize(QSize(150, 45))
        self.reset_btn.setFont(font)
        self.reset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); color: white;} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255)); color: white;}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reset_btn.setIcon(icon7)
        self.make_new_profile_btn = QPushButton(self.profile_btn_container)
        self.make_new_profile_btn.setObjectName(u"make_new_profile_btn")
        self.make_new_profile_btn.setGeometry(QRect(40, 20, 201, 45))
        self.make_new_profile_btn.setMinimumSize(QSize(150, 45))
        self.make_new_profile_btn.setFont(font)
        self.make_new_profile_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.make_new_profile_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); color: white;} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255)); color: white;}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.make_new_profile_btn.setIcon(icon8)

        self.horizontalLayout_13.addWidget(self.profile_btn_container)


        self.verticalLayout_19.addWidget(self.kontroller_btn_container)

        self.kontroller_image = QFrame(self.kontroller_rows)
        self.kontroller_image.setObjectName(u"kontroller_image")
        self.kontroller_image.setMinimumSize(QSize(1300, 680))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setKerning(False)
        self.kontroller_image.setFont(font2)
        self.kontroller_image.setFrameShape(QFrame.NoFrame)
        self.kontroller_image.setFrameShadow(QFrame.Raised)
        self.xbox_image = QLabel(self.kontroller_image)
        self.xbox_image.setObjectName(u"xbox_image")
        self.xbox_image.setGeometry(QRect(140, -20, 801, 771))
        self.xbox_image.setPixmap(QPixmap(u":/images/images/xboxOne.png"))
        self.xbox_image.setScaledContents(True)
        self.comboBox_right_stick_btn = QComboBox(self.kontroller_image)
        self.comboBox_right_stick_btn.addItem("")
        self.comboBox_right_stick_btn.setObjectName(u"comboBox_right_stick_btn")
        self.comboBox_right_stick_btn.setGeometry(QRect(790, 580, 230, 32))
        self.comboBox_right_stick_btn.setFont(font)
        self.comboBox_right_stick_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_right_stick_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_directional_pad_leftright = QComboBox(self.kontroller_image)
        self.comboBox_directional_pad_leftright.addItem("")
        self.comboBox_directional_pad_leftright.setObjectName(u"comboBox_directional_pad_leftright")
        self.comboBox_directional_pad_leftright.setEnabled(False)
        self.comboBox_directional_pad_leftright.setGeometry(QRect(50, 360, 210, 32))
        self.comboBox_directional_pad_leftright.setFont(font)
        self.comboBox_directional_pad_leftright.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_directional_pad_leftright.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_directional_pad_leftright.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_right_stick_x = QComboBox(self.kontroller_image)
        self.comboBox_right_stick_x.addItem("")
        self.comboBox_right_stick_x.setObjectName(u"comboBox_right_stick_x")
        self.comboBox_right_stick_x.setGeometry(QRect(880, 470, 210, 32))
        self.comboBox_right_stick_x.setFont(font)
        self.comboBox_right_stick_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_x.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_right_stick_x.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_RB_btn = QComboBox(self.kontroller_image)
        self.comboBox_RB_btn.addItem("")
        self.comboBox_RB_btn.setObjectName(u"comboBox_RB_btn")
        self.comboBox_RB_btn.setGeometry(QRect(800, 161, 230, 32))
        self.comboBox_RB_btn.setFont(font)
        self.comboBox_RB_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_RB_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_RB_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_left_stick_btn = QComboBox(self.kontroller_image)
        self.comboBox_left_stick_btn.addItem("")
        self.comboBox_left_stick_btn.setObjectName(u"comboBox_left_stick_btn")
        self.comboBox_left_stick_btn.setGeometry(QRect(60, 530, 230, 32))
        self.comboBox_left_stick_btn.setFont(font)
        self.comboBox_left_stick_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_RT_btn = QComboBox(self.kontroller_image)
        self.comboBox_RT_btn.addItem("")
        self.comboBox_RT_btn.setObjectName(u"comboBox_RT_btn")
        self.comboBox_RT_btn.setGeometry(QRect(800, 110, 230, 32))
        self.comboBox_RT_btn.setFont(font)
        self.comboBox_RT_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_RT_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_RT_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_left_stick_x = QComboBox(self.kontroller_image)
        self.comboBox_left_stick_x.addItem("")
        self.comboBox_left_stick_x.setObjectName(u"comboBox_left_stick_x")
        self.comboBox_left_stick_x.setGeometry(QRect(20, 280, 241, 32))
        self.comboBox_left_stick_x.setFont(font)
        self.comboBox_left_stick_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_x.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_x.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_menu_btn = QComboBox(self.kontroller_image)
        self.comboBox_menu_btn.setObjectName(u"comboBox_menu_btn")
        self.comboBox_menu_btn.setGeometry(QRect(560, 20, 230, 32))
        self.comboBox_menu_btn.setFont(font)
        self.comboBox_menu_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_menu_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_menu_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_right_stick_y = QComboBox(self.kontroller_image)
        self.comboBox_right_stick_y.addItem("")
        self.comboBox_right_stick_y.setObjectName(u"comboBox_right_stick_y")
        self.comboBox_right_stick_y.setGeometry(QRect(530, 530, 251, 32))
        self.comboBox_right_stick_y.setFont(font)
        self.comboBox_right_stick_y.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_right_stick_y.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_right_stick_y.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_view_btn = QComboBox(self.kontroller_image)
        self.comboBox_view_btn.setObjectName(u"comboBox_view_btn")
        self.comboBox_view_btn.setGeometry(QRect(280, 20, 230, 32))
        self.comboBox_view_btn.setFont(font)
        self.comboBox_view_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_view_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_view_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_B_btn = QComboBox(self.kontroller_image)
        self.comboBox_B_btn.setObjectName(u"comboBox_B_btn")
        self.comboBox_B_btn.setGeometry(QRect(810, 280, 230, 32))
        self.comboBox_B_btn.setFont(font)
        self.comboBox_B_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_B_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_B_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_X_btn = QComboBox(self.kontroller_image)
        self.comboBox_X_btn.setObjectName(u"comboBox_X_btn")
        self.comboBox_X_btn.setGeometry(QRect(820, 340, 230, 32))
        self.comboBox_X_btn.setFont(font)
        self.comboBox_X_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_X_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_X_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_directional_pad_updown = QComboBox(self.kontroller_image)
        self.comboBox_directional_pad_updown.addItem("")
        self.comboBox_directional_pad_updown.setObjectName(u"comboBox_directional_pad_updown")
        self.comboBox_directional_pad_updown.setEnabled(False)
        self.comboBox_directional_pad_updown.setGeometry(QRect(310, 560, 210, 32))
        self.comboBox_directional_pad_updown.setFont(font)
        self.comboBox_directional_pad_updown.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_directional_pad_updown.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_directional_pad_updown.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_A_btn = QComboBox(self.kontroller_image)
        self.comboBox_A_btn.setObjectName(u"comboBox_A_btn")
        self.comboBox_A_btn.setGeometry(QRect(840, 410, 230, 32))
        self.comboBox_A_btn.setFont(font)
        self.comboBox_A_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_A_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_A_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_left_stick_y = QComboBox(self.kontroller_image)
        self.comboBox_left_stick_y.addItem("")
        self.comboBox_left_stick_y.setObjectName(u"comboBox_left_stick_y")
        self.comboBox_left_stick_y.setGeometry(QRect(0, 219, 210, 32))
        self.comboBox_left_stick_y.setFont(font)
        self.comboBox_left_stick_y.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_left_stick_y.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_left_stick_y.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_LB_btn = QComboBox(self.kontroller_image)
        self.comboBox_LB_btn.addItem("")
        self.comboBox_LB_btn.setObjectName(u"comboBox_LB_btn")
        self.comboBox_LB_btn.setGeometry(QRect(70, 170, 230, 32))
        self.comboBox_LB_btn.setFont(font)
        self.comboBox_LB_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_LB_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_LB_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_Y_btn = QComboBox(self.kontroller_image)
        self.comboBox_Y_btn.addItem("")
        self.comboBox_Y_btn.setObjectName(u"comboBox_Y_btn")
        self.comboBox_Y_btn.setGeometry(QRect(818, 220, 230, 32))
        self.comboBox_Y_btn.setFont(font)
        self.comboBox_Y_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_Y_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_Y_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.comboBox_LT_btn = QComboBox(self.kontroller_image)
        self.comboBox_LT_btn.addItem("")
        self.comboBox_LT_btn.setObjectName(u"comboBox_LT_btn")
        self.comboBox_LT_btn.setGeometry(QRect(100, 120, 230, 32))
        self.comboBox_LT_btn.setFont(font)
        self.comboBox_LT_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_LT_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.comboBox_LT_btn.setStyleSheet(u"background-color: rgb(30, 33, 38); color: #dddddd;")
        self.save_profile_btn = QPushButton(self.kontroller_image)
        self.save_profile_btn.setObjectName(u"save_profile_btn")
        self.save_profile_btn.setEnabled(False)
        self.save_profile_btn.setGeometry(QRect(1090, 620, 201, 45))
        self.save_profile_btn.setMinimumSize(QSize(150, 45))
        self.save_profile_btn.setFont(font)
        self.save_profile_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_profile_btn.setStyleSheet(u"QPushButton { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(71, 81, 99, 255), stop:1 rgba(52, 59, 72, 255)); color: white;} QPushButton:hover { background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(92, 104, 128, 255), stop:1 rgba(61, 69, 85, 255)); color: white;} QPushButton:disabled { background-color: rgba(67, 69, 72, 0.6); color: rgba(154, 154, 154, 0.632); border: 2px solid rgba(52, 59, 72, 0.632);}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_profile_btn.setIcon(icon9)

        self.verticalLayout_19.addWidget(self.kontroller_image)


        self.horizontalLayout_9.addWidget(self.kontroller_rows)


        self.verticalLayout_18.addWidget(self.kontroller_container)

        self.scrollarea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_8.addWidget(self.scrollarea)


        self.verticalLayout_20.addWidget(self.hoved_frame_column)

        self.stackedWidget.addWidget(self.kontroller)

        self.verticalLayout_15.addWidget(self.stackedWidget)


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
        self.toolButton_kjoremodus.clicked.connect(self.kjoring_container.setHidden)
        self.toolButton_kjoremodus.clicked.connect(self.kjoring_container.setVisible)
        self.toolButton_motorpaadrag.clicked.connect(self.column2.setHidden)
        self.toolButton_motorpaadrag.clicked.connect(self.column2.setVisible)
        self.toolButton_bilde.clicked.connect(self.bilde_container.setHidden)
        self.toolButton_bilde.clicked.connect(self.bilde_container.setVisible)
        self.toolButton_temp.clicked.connect(self.temperatur_container.setHidden)
        self.toolButton_temp.clicked.connect(self.temperatur_container.setVisible)
        self.toolButton_vann.clicked.connect(self.vannlekk_container.setHidden)
        self.toolButton_vann.clicked.connect(self.vannlekk_container.setVisible)
        self.toolButton_effekt.clicked.connect(self.ROV_container.setHidden)
        self.toolButton_effekt.clicked.connect(self.ROV_container.setVisible)
        self.toolButton_kamera.clicked.connect(self.kamera_container.setHidden)
        self.toolButton_kamera.clicked.connect(self.kamera_container.setVisible)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.informasjon_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.kontroller_btn.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
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
        self.toolButton_kjoremodus.setText(QCoreApplication.translate("MainWindow", u"Kj\u00f8remodus", None))
        self.toolButton_effekt.setText(QCoreApplication.translate("MainWindow", u"Effektforbruk", None))
        self.toolButton_temp.setText(QCoreApplication.translate("MainWindow", u"Temperatur", None))
        self.toolButton_vann.setText(QCoreApplication.translate("MainWindow", u"Vannlekkasje", None))
        self.toolButton_motorpaadrag.setText(QCoreApplication.translate("MainWindow", u"Motorp\u00e5drag", None))
        self.toolButton_bilde.setText(QCoreApplication.translate("MainWindow", u"Bildebehandling", None))
        self.toolButton_kamera.setText(QCoreApplication.translate("MainWindow", u"Kamera", None))
        self.kjoring_title.setText(QCoreApplication.translate("MainWindow", u"KJ\u00d8REMODUS", None))
        self.kjoring_label.setText(QCoreApplication.translate("MainWindow", u"Velg mellom automatisk eller manuell kj\u00f8ring", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Automatisk", None))
        self.manuell_btn.setText(QCoreApplication.translate("MainWindow", u"Manuell", None))
        self.lys_av_btn.setText(QCoreApplication.translate("MainWindow", u"Av", None))
        self.dybde_reg_label.setText(QCoreApplication.translate("MainWindow", u"Dybde regulator", None))
        self.dybde_paa_btn.setText(QCoreApplication.translate("MainWindow", u"P\u00e5", None))
        self.mani_av_btn.setText(QCoreApplication.translate("MainWindow", u"Av", None))
        self.mani_paa_btn.setText(QCoreApplication.translate("MainWindow", u"P\u00e5", None))
        self.mani_label.setText(QCoreApplication.translate("MainWindow", u"Manipulator", None))
        self.lys_label_2.setText(QCoreApplication.translate("MainWindow", u"Lys", None))
        self.lys_paa_btn.setText(QCoreApplication.translate("MainWindow", u"P\u00e5", None))
        self.helning_label.setText(QCoreApplication.translate("MainWindow", u"Helningsregulator", None))
        self.helning_paa_btn.setText(QCoreApplication.translate("MainWindow", u"P\u00e5", None))
        self.dybde_av_btn.setText(QCoreApplication.translate("MainWindow", u"Av", None))
        self.helning_av_btn.setText(QCoreApplication.translate("MainWindow", u"Av", None))
        self.lys_label.setText(QCoreApplication.translate("MainWindow", u"Lys:", None))
        self.lys_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.tid_label.setText(QCoreApplication.translate("MainWindow", u"Tid:", None))
        self.tid.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.dybde_label.setText(QCoreApplication.translate("MainWindow", u"Dybde:", None))
        self.dybde.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.spenning_label.setText(QCoreApplication.translate("MainWindow", u"Spenning:", None))
        self.spenning.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.orientering_label.setText(QCoreApplication.translate("MainWindow", u"Orientering:", None))
        self.orientering.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.effektforbruk_label.setText(QCoreApplication.translate("MainWindow", u"EFFEKTFORBRUK", None))
        self.effekt_elektronikk_label.setText(QCoreApplication.translate("MainWindow", u"Elektronikk:", None))
        self.effekt_elektronikk.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.effekt_thrustere_label.setText(QCoreApplication.translate("MainWindow", u"Thrustere:", None))
        self.effekt_thrustere.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.effekt_manipulator_label.setText(QCoreApplication.translate("MainWindow", u"Manipulator:", None))
        self.effekt_manipulator.setText(QCoreApplication.translate("MainWindow", u"-----", None))
        self.temp_ROV_label.setText(QCoreApplication.translate("MainWindow", u"TEMPERATUR I ROV", None))
        self.temp_ROV_1.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.temp_ROV_2.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.temp_ROV_3.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.gjsnitttemp_label.setText(QCoreApplication.translate("MainWindow", u"Gj.snittstemperatur:", None))
        self.gjsnitt_temp_ROV.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.vannlekk_label.setText(QCoreApplication.translate("MainWindow", u"VANNLEKKASJE I ROV", None))
        self.vannlekk_1.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.vannlekk_2.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.vannlekk_3.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.motor_title.setText(QCoreApplication.translate("MainWindow", u"MOTORP\u00c5DRAG", None))
        self.rov_label.setText(QCoreApplication.translate("MainWindow", u"ROV", None))
        self.motor_img.setText("")
        self.VHF_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.VVF_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.HHF_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.HVF_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.HVB_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.HHB_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.VVB_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.VHB_percentage.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.manipulator_label.setText(QCoreApplication.translate("MainWindow", u"MANIPULATOR", None))
        self.manipulator_img.setText("")
        self.mani_percentage_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.mani_percentage_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0<span style=\" vertical-align:super;\">%</span></p></body></html>", None))
        self.mani_percentage_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">0</span><span style=\" font-size:9pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.test_label.setText(QCoreApplication.translate("MainWindow", u"Test av p\u00e5dragsverdier:", None))
        self.sensor_lekk_label_3.setText("")
        self.bilde_title.setText(QCoreApplication.translate("MainWindow", u"BILDEBEHANDLING", None))
        self.korallrev_btn.setText(QCoreApplication.translate("MainWindow", u"Beregne st\u00f8rrelse", None))
        self.bilde_label_3.setText(QCoreApplication.translate("MainWindow", u"Siste bilde analyseres", None))
        self.fotomoasaikk_btn.setText(QCoreApplication.translate("MainWindow", u"Fotomoasaikk", None))
        self.bilde_label_2.setText(QCoreApplication.translate("MainWindow", u"Siste bilde analyseres", None))
        self.kamera_title.setText(QCoreApplication.translate("MainWindow", u"KAMERA", None))
        self.ta_bilde_frontkamera_btn.setText(QCoreApplication.translate("MainWindow", u" Ta bilde frontkamera", None))
        self.ta_bilde_havbunn_btn.setText(QCoreApplication.translate("MainWindow", u" Ta bilde havbunnskamera", None))
        self.slett_bilde_btn.setText(QCoreApplication.translate("MainWindow", u" Slett det siste bildet", None))
        self.siste_bilde_label.setText(QCoreApplication.translate("MainWindow", u"Siste bilde tatt vises her:", None))
        self.show_image.setText("")
        self.kontroller_title.setText(QCoreApplication.translate("MainWindow", u"ENDRE KONTROLLER-KNAPPER", None))
        self.kontroller_text_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Her kan du endre funksjonene til knappene p\u00e5 Xbox-kontrolleren.</p><p>Lag en ny profil hvis du \u00f8nsker \u00e5 lagre endringene til senere.</p></body></html>", None))
        self.velg_profil_label.setText(QCoreApplication.translate("MainWindow", u"Velg profil:", None))
        self.comboBox_velg_profil.setItemText(0, QCoreApplication.translate("MainWindow", u"Standard profil", None))
        self.comboBox_velg_profil.setItemText(1, QCoreApplication.translate("MainWindow", u"Egendefinert profil", None))

        self.reset_btn.setText(QCoreApplication.translate("MainWindow", u" Reset", None))
        self.make_new_profile_btn.setText(QCoreApplication.translate("MainWindow", u" Lag ny profil", None))
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

        self.save_profile_btn.setText(QCoreApplication.translate("MainWindow", u" Lagre", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.version.setText("")
        self.grip_icon.setText("")
    # retranslateUi

