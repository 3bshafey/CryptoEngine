


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1061, 600)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        font = QtGui.QFont()
        font.setFamily("Marlett")
        font.setPointSize(20)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(40, 20, 1011, 561))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(10, 0, 941, 551))
        self.label.setStyleSheet(
    "background-color: qlineargradient(\n"
    "    spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
    "    stop:0 rgba(10, 40, 50, 255),     /* Dark slate blue */\n"
    "    stop:1 rgba(30, 100, 110, 255)    /* Teal */\n"
    ");"
    "border-bottom-left-radius: 50px;"
    "border-top-right-radius: 50px;"
    "border-top-left-radius: 50px;"
    "border-bottom-right-radius: 50px;"
)
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(270, 150, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),     /* بداية التدرج – أخضر مزرق */\n"
"        stop:1 rgba(60, 150, 220, 255)      /* نهاية التدرج – أزرق أوضح */\n"
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
"        stop:1 rgba(50, 135, 210, 255)      /* زر hover بدرجة أزرق أوضح */\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);   /* أزرق مخضر غامق وقت الضغط */\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 150, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),     /* بداية التدرج – أخضر مزرق */\n"
"        stop:1 rgba(60, 150, 220, 255)      /* نهاية التدرج – أزرق أوضح */\n"
"    );\n"
"    color: white;\n"
"    border-radius: 20px;\n"
"    padding: 8px 20px;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(25, 115, 105, 255),\n"
"        stop:1 rgba(50, 135, 210, 255)      /* زر hover بدرجة أزرق أوضح */\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);   /* أزرق مخضر غامق وقت الضغط */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 400, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),     /* بداية التدرج – أخضر مزرق */\n"
"        stop:1 rgba(60, 150, 220, 255)      /* نهاية التدرج – أزرق أوضح */\n"
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
"        stop:1 rgba(50, 135, 210, 255)      /* زر hover بدرجة أزرق أوضح */\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);   /* أزرق مخضر غامق وقت الضغط */\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 280, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),     /* بداية التدرج – أخضر مزرق */\n"
"        stop:1 rgba(60, 150, 220, 255)      /* نهاية التدرج – أزرق أوضح */\n"
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
"        stop:1 rgba(50, 135, 210, 255)      /* زر hover بدرجة أزرق أوضح */\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_5:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);   /* أزرق مخضر غامق وقت الضغط */\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 280, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton#pushButton_6 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),     /* بداية التدرج – أخضر مزرق */\n"
"        stop:1 rgba(60, 150, 220, 255)      /* نهاية التدرج – أزرق أوضح */\n"
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
"        stop:1 rgba(50, 135, 210, 255)      /* زر hover بدرجة أزرق أوضح */\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_6:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);   /* أزرق مخضر غامق وقت الضغط */\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 400, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton#pushButton_7 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),     /* بداية التدرج – أخضر مزرق */\n"
"        stop:1 rgba(60, 150, 220, 255)      /* نهاية التدرج – أزرق أوضح */\n"
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
"        stop:1 rgba(50, 135, 210, 255)      /* زر hover بدرجة أزرق أوضح */\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_7:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);   /* أزرق مخضر غامق وقت الضغط */\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 301, 91))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(400, 490, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton#pushButton_8 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),     /* بداية التدرج – أخضر مزرق */\n"
"        stop:1 rgba(60, 150, 220, 255)      /* نهاية التدرج – أزرق أوضح */\n"
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
"        stop:1 rgba(50, 135, 210, 255)      /* زر hover بدرجة أزرق أوضح */\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_8:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);   /* أزرق مخضر غامق وقت الضغط */\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Root 13"))
        self.pushButton_2.setText(_translate("Form", "Ceaser"))
        self.pushButton_4.setText(_translate("Form", "Substitution"))
        self.pushButton_5.setText(_translate("Form", "Play Fair"))
        self.pushButton_6.setText(_translate("Form", "Rail Fence"))
        self.pushButton_7.setText(_translate("Form", "Transposition"))
        self.label_2.setText(_translate("Form", "CHOOSE CYPHER"))
        self.pushButton_8.setText(_translate("Form", "RSA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
