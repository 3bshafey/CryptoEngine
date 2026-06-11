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
        self.label.setGeometry(QtCore.QRect(10, 20, 911, 531))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet(
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(10, 40, 50, 255), stop:1 rgba(30, 100, 110, 255));"
        "border-top-left-radius: 50px;"
        "border-bottom-left-radius: 50px;"
        "border: 1px solid transparent;"  # Needed for border-image to work
    )

        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 490, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(135, 206, 250, 255),   /* Light Sky Blue */\n"
"        stop:1 rgba(0, 102, 204, 255));    /* Strong Blue */\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(100, 181, 246, 255),   /* Slightly darker */\n"
"        stop:1 rgba(0, 85, 170, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(0, 85, 170);   /* Deep blue on press */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(320, 170, 341, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(28)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(350, 240, 481, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "Get Start"))
        self.label_3.setText(_translate("Form", "CYBER SECURITY"))
        self.label_4.setText(_translate("Form", "C  R Y P T O G R A P H Y  S Y S T E M"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
