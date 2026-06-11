from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import sys
import math

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1061, 600)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        font = QtGui.QFont()
        font.setFamily("Marlett")
        font.setPointSize(10)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(9, 19, 1011, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 971, 551))
        self.label.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(10, 40, 50, 255), stop:1 rgba(30, 100, 110, 255));"
                "border-bottom-left-radius: 50px;\n"
                "border-top-right-radius: 50px;\n"
                "border-top-left-radius: 50px;\n"
                "border-bottom-right-radius: 50px;\n"
        )
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 160, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("#lineEdit_2 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)\n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7);\n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_2:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7),\n"
"        stop:1 rgba(60, 150, 220, 0.7)\n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"    outline: none;\n"
"}\n"
"\n"
"#lineEdit_2:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"}\n"
"\n"
"#lineEdit_2:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6);\n"
"    color: rgba(128, 128, 128, 0.6);\n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
"}\n"
"")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(460, 390, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),\n"
"        stop:1 rgba(60, 150, 220, 255)\n"
"    );\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(25, 115, 105, 255),\n"
"        stop:1 rgba(50, 135, 210, 255)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(550, 160, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("#lineEdit_4 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)\n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7);\n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_4:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7),\n"
"        stop:1 rgba(60, 150, 220, 0.7)\n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"    outline: none;\n"
"}\n"
"\n"
"#lineEdit_4:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"}\n"
"\n"
"#lineEdit_4:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6);\n"
"    color: rgba(128, 128, 128, 0.6);\n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
"}\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 240, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("#lineEdit_5 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)\n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7);\n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_5:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7),\n"
"        stop:1 rgba(60, 150, 220, 0.7)\n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"    outline: none;\n"
"}\n"
"\n"
"#lineEdit_5:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"}\n"
"\n"
"#lineEdit_5:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6);\n"
"    color: rgba(128, 128, 128, 0.6);\n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
"}\n"
"")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 470, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),\n"
"        stop:1 rgba(60, 150, 220, 255)\n"
"    );\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(25, 115, 105, 255),\n"
"        stop:1 rgba(50, 135, 210, 255)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 310, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),\n"
"        stop:1 rgba(60, 150, 220, 255)\n"
"    );\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(25, 115, 105, 255),\n"
"        stop:1 rgba(50, 135, 210, 255)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 310, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),\n"
"        stop:1 rgba(60, 150, 220, 255)\n"
"    );\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_5:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(25, 115, 105, 255),\n"
"        stop:1 rgba(50, 135, 210, 255)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_5:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.radioButton = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton.setGeometry(QtCore.QRect(550, 80, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("QRadioButton#radioButton {\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QRadioButton#radioButton::indicator {\n"
"    border: 2px solid rgba(30, 123, 111, 255);\n"
"    border-radius: 10px;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: rgba(60, 150, 220, 255);\n"
"}\n"
"\n"
"QRadioButton#radioButton::indicator:checked {\n"
"    background-color: rgba(25, 115, 105, 255);\n"
"    border: 2px solid rgba(50, 135, 210, 255);\n"
"}\n"
"\n"
"QRadioButton#radioButton::indicator:hover {\n"
"    background-color: rgba(50, 135, 210, 255);\n"
"    border: 2px solid rgba(30, 123, 111, 255);\n"
"}\n"
"")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(300, 80, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("QRadioButton#radioButton_2 {\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QRadioButton#radioButton_2::indicator {\n"
"    border: 2px solid rgba(30, 123, 111, 255);\n"
"    border-radius: 10px;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    background-color: rgba(60, 150, 220, 255);\n"
"}\n"
"\n"
"QRadioButton#radioButton_2::indicator:checked {\n"
"    background-color: rgba(25, 115, 105, 255);\n"
"    border: 2px solid rgba(50, 135, 210, 255);\n"
"}\n"
"\n"
"QRadioButton#radioButton_2::indicator:hover {\n"
"    background-color: rgba(50, 135, 210, 255);\n"
"    border: 2px solid rgba(30, 123, 111, 255);\n"
"}\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(420, 20, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton#pushButton_6 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),\n"
"        stop:1 rgba(60, 150, 220, 255)\n"
"    );\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_6:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(25, 115, 105, 255),\n"
"        stop:1 rgba(50, 135, 210, 255)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_6:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(730, 370, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("#lineEdit_6 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)\n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7);\n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_6:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7),\n"
"        stop:1 rgba(60, 150, 220, 0.7)\n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"    outline: none;\n"
"}\n"
"\n"
"#lineEdit_6:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"}\n"
"\n"
"#lineEdit_6:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6);\n"
"    color: rgba(128, 128, 128, 0.6);\n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
"}\n"
"")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_7.setGeometry(QtCore.QRect(730, 430, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("#lineEdit_7 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)\n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7);\n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_7:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7),\n"
"        stop:1 rgba(60, 150, 220, 0.7)\n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"    outline: none;\n"
"}\n"
"\n"
"#lineEdit_7:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"}\n"
"\n"
"#lineEdit_7:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6);\n"
"    color: rgba(128, 128, 128, 0.6);\n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
"}\n"
"")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(720, 500, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton#pushButton_7 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),\n"
"        stop:1 rgba(60, 150, 220, 255)\n"
"    );\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_7:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(25, 115, 105, 255),\n"
"        stop:1 rgba(50, 135, 210, 255)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_7:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_8.setGeometry(QtCore.QRect(830, 370, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("#lineEdit_8{\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)\n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7);\n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_8:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7),\n"
"        stop:1 rgba(60, 150, 220, 0.7)\n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"    outline: none;\n"
"}\n"
"\n"
"#lineEdit_8:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"}\n"
"\n"
"#lineEdit_8:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6);\n"
"    color: rgba(128, 128, 128, 0.6);\n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
"}\n"
"")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_9.setGeometry(QtCore.QRect(830, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("#lineEdit_9 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)\n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7);\n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#lineEdit_9:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7),\n"
"        stop:1 rgba(60, 150, 220, 0.7)\n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"    outline: none;\n"
"}\n"
"\n"
"#lineEdit_9:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"}\n"
"\n"
"#lineEdit_9:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6);\n"
"    color: rgba(128, 128, 128, 0.6);\n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
"}\n"
"")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(830, 500, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton#pushButton_8{\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),\n"
"        stop:1 rgba(60, 150, 220, 255)\n"
"    );\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_8:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(25, 115, 105, 255),\n"
"        stop:1 rgba(50, 135, 210, 255)\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_8:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")

        # Connect buttons to their functions
        self.pushButton.clicked.connect(self.import_file)
        self.pushButton_3.clicked.connect(self.download_file)
        self.pushButton_4.clicked.connect(self.clear_fields)
        self.pushButton_5.clicked.connect(self.convert_text)
        self.pushButton_7.clicked.connect(self.clear_key_fields)
        self.pushButton_8.clicked.connect(self.generate_keys)
        # Connect radio buttons to update key field on mode change
        self.radioButton.toggled.connect(self.update_key_field)
        self.radioButton_2.toggled.connect(self.update_key_field)

        # Set default radio button
        self.radioButton_2.setChecked(True)
        # Update key field based on default mode
        self.update_key_field()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Plain Text"))
        self.pushButton.setText(_translate("Form", "Import File"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Cypher Text"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "KEY"))
        self.pushButton_3.setText(_translate("Form", "Download File"))
        self.pushButton_4.setText(_translate("Form", "CLEAR"))
        self.pushButton_5.setText(_translate("Form", "CONVERT"))
        self.radioButton.setText(_translate("Form", "DECRYPTION"))
        self.radioButton_2.setText(_translate("Form", "ENCRYPTION"))
        self.label_2.setText(_translate("Form", "RSA CYPHER"))
        self.pushButton_6.setText(_translate("Form", "BACK"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "P"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Q"))
        self.pushButton_7.setText(_translate("Form", "CLEAR"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "Private Key"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "Public Key"))
        self.pushButton_8.setText(_translate("Form", "Generate"))

    def show_alert(self, title, message, icon=QMessageBox.Icon.Warning):
        """Show an alert message box"""
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def import_file(self):
        """Import text from a file"""
        file_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read().strip()

            if not content:
                self.show_alert("Empty File", "The selected file is empty.")
                return

            # Validate content: numbers or space-separated numbers
            try:
                if self.radioButton_2.isChecked():  # Encryption
                    # For plaintext, expect a single number or space-separated numbers
                    numbers = [int(x) for x in content.split()]
                    if not numbers:
                        raise ValueError
                    self.lineEdit_2.setText(content)
                else:  # Decryption
                    # For ciphertext, expect a single number or space-separated numbers
                    numbers = [int(x) for x in content.split()]
                    if not numbers:
                        raise ValueError
                    self.lineEdit_4.setText(content)
            except ValueError:
                self.show_alert("Invalid Content", "File should contain valid numbers (e.g., '123' or '123 456').")
                return

        except Exception as e:
            self.show_alert("Error", f"Could not read file: {str(e)}")

    def download_file(self):
        """Download the result to a file"""
        content = ""
        if self.radioButton_2.isChecked() and self.lineEdit_4.text():
            content = self.lineEdit_4.text()
        elif self.radioButton.isChecked() and self.lineEdit_2.text():
            content = self.lineEdit_2.text()

        if not content:
            self.show_alert("Warning", "No content to save!")
            return

        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.show_alert("Success", "File saved successfully!", QMessageBox.Icon.Information)
            except Exception as e:
                self.show_alert("Error", f"Could not save file: {str(e)}")

    def clear_fields(self):
        """Clear input fields for text and key"""
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

    def clear_key_fields(self):
        """Clear key generation fields"""
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
        # Update key field after clearing
        self.update_key_field()

    def is_prime(self, n):
        """Check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def validate_key(self, key_text):
        """Validate if key is in format 'number,number'"""
        if not key_text:
            return False
        try:
            key_parts = key_text.split(',')
            if len(key_parts) != 2:
                return False
            int(key_parts[0])  # Check if first part is integer
            int(key_parts[1])  # Check if second part is integer
            return True
        except ValueError:
            return False

    def update_key_field(self):
        """Update key field based on selected mode"""
        if self.radioButton_2.isChecked():  # Encryption
            public_key = self.lineEdit_9.text()
            if self.validate_key(public_key):
                self.lineEdit_5.setText(public_key)
            else:
                self.lineEdit_5.clear()  # Clear if invalid or empty
        else:  # Decryption
            private_key = self.lineEdit_8.text()
            if self.validate_key(private_key):
                self.lineEdit_5.setText(private_key)
            else:
                self.lineEdit_5.clear()  # Clear if invalid or empty

    def generate_keys(self):
        """Generate RSA public and private keys"""
        p_text = self.lineEdit_6.text()
        q_text = self.lineEdit_7.text()

        if not p_text or not q_text:
            self.show_alert("Missing Input", "Please enter both p and q values!")
            return

        try:
            p = int(p_text)
            q = int(q_text)
        except ValueError:
            self.show_alert("Invalid Input", "p and q must be integers!")
            return

        if p == q:
            self.show_alert("Invalid Input", "p and q must be different!")
            return

        if not self.is_prime(p) or not self.is_prime(q):
            self.show_alert("Invalid Input", "p and q must be prime numbers!")
            return

        try:
            public_key, private_key = self.rsa_generate_keys(p, q)
            self.lineEdit_9.setText(f"{public_key[0]},{public_key[1]}")  # e,n
            self.lineEdit_8.setText(f"{private_key[0]},{private_key[1]}")  # d,n
            # Update key field based on current mode
            self.update_key_field()
        except Exception as e:
            self.show_alert("Error", f"Failed to generate keys: {str(e)}")

    def convert_text(self):
        """Convert text using RSA cipher"""
        # Update key field based on mode before conversion
        self.update_key_field()

        key_text = self.lineEdit_5.text()
        if not key_text:
            self.show_alert("Missing Key", "Please enter a key (e,n for encryption or d,n for decryption)!")
            return

        try:
            key_parts = key_text.split(',')
            if len(key_parts) != 2:
                raise ValueError
            key_value = int(key_parts[0])  # e or d
            n = int(key_parts[1])  # modulus n
        except ValueError:
            self.show_alert("Invalid Key", "Key must be in format 'number,number' (e.g., '65537,3233')!")
            return

        if self.radioButton_2.isChecked():  # Encryption
            plain_text = self.lineEdit_2.text()
            if not plain_text:
                self.show_alert("Missing Text", "Please enter text to encrypt!")
                return

            try:
                numbers = [int(x) for x in plain_text.split()]
                if not numbers:
                    raise ValueError
                # Validate numbers are less than n
                if any(num >= n for num in numbers):
                    self.show_alert("Invalid Input", f"Plaintext numbers must be less than n ({n})!")
                    return
                cipher_numbers = [self.rsa_encrypt(num, key_value, n) for num in numbers]
                self.lineEdit_4.setText(' '.join(map(str, cipher_numbers)))
            except ValueError:
                self.show_alert("Invalid Text", "Plain text must contain valid numbers (e.g., '123' or '123 456')!")
                return

        else:  # Decryption
            cipher_text = self.lineEdit_4.text()
            if not cipher_text:
                self.show_alert("Missing Text", "Please enter text to decrypt!")
                return

            try:
                numbers = [int(x) for x in cipher_text.split()]
                if not numbers:
                    raise ValueError
                # Validate numbers are less than n
                if any(num >= n for num in numbers):
                    self.show_alert("Invalid Input", f"Ciphertext numbers must be less than n ({n})!")
                    return
                plain_numbers = [self.rsa_decrypt(num, key_value, n) for num in numbers]
                self.lineEdit_2.setText(' '.join(map(str, plain_numbers)))
            except ValueError:
                self.show_alert("Invalid Text", "Cipher text must contain valid numbers (e.g., '123' or '123 456')!")
                return

    def rsa_power(self, base, expo, m):
        """Fast modular exponentiation"""
        res = 1
        base = base % m
        while expo > 0:
            if expo & 1:
                res = (res * base) % m
            base = (base * base) % m
            expo = expo // 2
        return res

    def rsa_gcd(self, a, b):
        """Calculate GCD of two numbers"""
        while b != 0:
            a, b = b, a % b
        return a

    def rsa_extended_gcd(self, a, b):
        """Extended Euclidean algorithm"""
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.rsa_extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def rsa_modinv(self, a, m):
        """Calculate modular inverse"""
        g, x, y = self.rsa_extended_gcd(a, m)
        if g != 1:
            return None
        else:
            return x % m

    def rsa_generate_keys(self, p, q):
            """Generate RSA public and private keys"""
            n = p * q
            phi = (p - 1) * (q - 1)

            # Choose e such that 1 < e < phi and gcd(e, phi) == 1
            e = 0
            for e in range(2, phi):
                    if self.rsa_gcd(e, phi) == 1:
                            break

            # Compute d such that e * d ≡ 1 (mod phi(n))
            d = self.rsa_modinv(e, phi)
            if d is None:
                    raise ValueError("Modular inverse does not exist!")

            return (e, n), (d, n)

    def rsa_encrypt(self, m, e, n):
        """Encrypt a number using RSA"""
        return self.rsa_power(m, e, n)

    def rsa_decrypt(self, c, d, n):
        """Decrypt a number using RSA"""
        return self.rsa_power(c, d, n)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())