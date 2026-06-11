from PyQt6 import QtCore, QtGui, QtWidgets


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
        self.label.setGeometry(QtCore.QRect(10, 0, 501, 551))
        self.label.setStyleSheet("border-image: url(\"G:/CyberTest/New folder/Gemini_Generated_Image_k3pdhzk3pdhzk3pd.jpeg\");"
                         "border-top-left-radius: 50px;"
                         "border-bottom-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(510, 0, 501, 551))
        self.label_2.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"border-bottom-right-radius:50px;\n"
"border-top-right-radius:50px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(710, 40, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_3.setObjectName("label_3")
        self.user_name = QtWidgets.QLineEdit(parent=self.widget)
        self.user_name.setGeometry(QtCore.QRect(560, 120, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 0.8);\n"
"color: rgba(0, 0, 0, 0.8);\n"
"padding-bottom: 7px;\n"
"")
        self.user_name.setText("")
        self.user_name.setObjectName("user_name")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 280, 381, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 0.8);\n"
"color: rgba(0, 0, 0, 0.8);\n"
"padding-bottom: 7px;\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(570, 430, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 123, 111, 255), stop:1 rgba(95, 112, 228, 255));\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 123, 111, 255), stop:1 rgba(81, 84, 228, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(30, 123, 111);\n"
"}\n"
"\n"
"QPushButton#pushButton_2 {\n"
"    background-color: transparent;\n"
"    color: rgba(85, 98, 112, 1);\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    color: rgba(131, 96, 53, 1);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    color: rgba(91, 88, 53, 1);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(560, 360, 381, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 0.8);\n"
"color: rgba(0, 0, 0, 0.8);\n"
"padding-bottom: 7px;\n"
"")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(560, 190, 381, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(46, 82, 101, 0.8);\n"
"color: rgba(0, 0, 0, 0.8);\n"
"padding-bottom: 7px; \n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 500, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(7)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 123, 111, 255), stop:1 rgba(95, 112, 228, 255));\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 123, 111, 255), stop:1 rgba(81, 84, 228, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(30, 123, 111);\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(670, 510, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Sign Up"))
        self.user_name.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "R e g i s t e r "))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Email Address"))
        self.pushButton_2.setText(_translate("Form", "Log In"))
        self.label_4.setText(_translate("Form", "Log In?"))

