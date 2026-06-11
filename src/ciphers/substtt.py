from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox


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
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 200, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("#lineEdit_2 {\n"
                                      "    background-color: qlineargradient(\n"
                                      "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
                                      "        stop:0 rgba(30, 123, 111, 0.5), /* أخضر مزرق مع شفافية */\n"
                                      "        stop:1 rgba(60, 150, 220, 0.5)  /* أزرق مع شفافية */\n"
                                      "    );\n"
                                      "    border: none;\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 0.7); /* حد سفلي بلون أخضر مع شفافية */\n"
                                      "    color: white; /* تغيير لون النص إلى الأبيض */\n"
                                      "    padding-bottom: 7px; /* المسافة الداخلية السفلية */\n"
                                      "    font-size: 16px; /* حجم الخط */\n"
                                      "    border-radius: 5px; /* حواف دائرية خفيفة */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_2:focus {\n"
                                      "    background-color: qlineargradient(\n"
                                      "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
                                      "        stop:0 rgba(30, 123, 111, 0.7), /* أخضر مزرق مع شفافية عند التركيز */\n"
                                      "        stop:1 rgba(60, 150, 220, 0.7)  /* أزرق مع شفافية عند التركيز */\n"
                                      "    );\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 1); /* حد سفلي أخضر عند التركيز */\n"
                                      "    outline: none; /* إزالة الخط المحيط عند التركيز */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_2:hover {\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 1); /* تفاعل عند المرور بالماوس */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_2:disabled {\n"
                                      "    background-color: rgba(240, 240, 240, 0.6); /* خلفية باهتة عند تعطيل الحقل */\n"
                                      "    color: rgba(128, 128, 128, 0.6); /* لون النص عند تعطيل الحقل */\n"
                                      "    border-bottom: 2px solid rgba(200, 200, 200, 0.6); /* حدود باهتة عند تعطيل الحقل */\n"
                                      "}\n"
                                      "")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(460, 410, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
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
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(550, 200, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("#lineEdit_4 {\n"
                                      "    background-color: qlineargradient(\n"
                                      "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
                                      "        stop:0 rgba(30, 123, 111, 0.5), /* أخضر مزرق مع شفافية */\n"
                                      "        stop:1 rgba(60, 150, 220, 0.5)  /* أزرق مع شفافية */\n"
                                      "    );\n"
                                      "    border: none;\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 0.7); /* حد سفلي بلون أخضر مع شفافية */\n"
                                      "    color: white; /* تغيير لون النص إلى الأبيض */\n"
                                      "    padding-bottom: 7px; /* المسافة الداخلية السفلية */\n"
                                      "    font-size: 16px; /* حجم الخط */\n"
                                      "    border-radius: 5px; /* حواف دائرية خفيفة */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_4:focus {\n"
                                      "    background-color: qlineargradient(\n"
                                      "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
                                      "        stop:0 rgba(30, 123, 111, 0.7), /* أخضر مزرق مع شفافية عند التركيز */\n"
                                      "        stop:1 rgba(60, 150, 220, 0.7)  /* أزرق مع شفافية عند التركيز */\n"
                                      "    );\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 1); /* حد سفلي أخضر عند التركيز */\n"
                                      "    outline: none; /* إزالة الخط المحيط عند التركيز */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_4:hover {\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 1); /* تفاعل عند المرور بالماوس */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_4:disabled {\n"
                                      "    background-color: rgba(240, 240, 240, 0.6); /* خلفية باهتة عند تعطيل الحقل */\n"
                                      "    color: rgba(128, 128, 128, 0.6); /* لون النص عند تعطيل الحقل */\n"
                                      "    border-bottom: 2px solid rgba(200, 200, 200, 0.6); /* حدود باهتة عند تعطيل الحقل */\n"
                                      "}\n"
                                      "")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(390, 280, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("#lineEdit_5 {\n"
                                      "    background-color: qlineargradient(\n"
                                      "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
                                      "        stop:0 rgba(30, 123, 111, 0.5), /* أخضر مزرق مع شفافية */\n"
                                      "        stop:1 rgba(60, 150, 220, 0.5)  /* أزرق مع شفافية */\n"
                                      "    );\n"
                                      "    border: none;\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 0.7); /* حد سفلي بلون أخضر مع شفافية */\n"
                                      "    color: white; /* تغيير لون النص إلى الأبيض */\n"
                                      "    padding-bottom: 7px; /* المسافة الداخلية السفلية */\n"
                                      "    font-size: 16px; /* حجم الخط */\n"
                                      "    border-radius: 5px; /* حواف دائرية خفيفة */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_5:focus {\n"
                                      "    background-color: qlineargradient(\n"
                                      "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
                                      "        stop:0 rgba(30, 123, 111, 0.7), /* أخضر مزرق مع شفافية عند التركيز */\n"
                                      "        stop:1 rgba(60, 150, 220, 0.7)  /* أزرق مع شفافية عند التركيز */\n"
                                      "    );\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 1); /* حد سفلي أخضر عند التركيز */\n"
                                      "    outline: none; /* إزالة الخط المحيط عند التركيز */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_5:hover {\n"
                                      "    border-bottom: 2px solid rgba(30, 123, 111, 1); /* تفاعل عند المرور بالماوس */\n"
                                      "}\n"
                                      "\n"
                                      "#lineEdit_5:disabled {\n"
                                      "    background-color: rgba(240, 240, 240, 0.6); /* خلفية باهتة عند تعطيل الحقل */\n"
                                      "    color: rgba(128, 128, 128, 0.6); /* لون النص عند تعطيل الحقل */\n"
                                      "    border-bottom: 2px solid rgba(200, 200, 200, 0.6); /* حدود باهتة عند تعطيل الحقل */\n"
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
                                        "        stop:0 rgba(30, 123, 111, 255),     /* بداية التدرج – أخضر مزرق */\n"
                                        "        stop:1 rgba(60, 150, 220, 255)      /* نهاية التدرج – أزرق أوضح */\n"
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
                                        "        stop:1 rgba(50, 135, 210, 255)      /* زر hover بدرجة أزرق أوضح */\n"
                                        "    );\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#pushButton_3:pressed {\n"
                                        "    padding-top: 5px;\n"
                                        "    padding-left: 5px;\n"
                                        "    background-color: rgb(20, 100, 120);   /* أزرق مخضر غامق وقت الضغط */\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 350, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
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
        self.pushButton_5.setGeometry(QtCore.QRect(340, 350, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
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
        self.radioButton = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton.setGeometry(QtCore.QRect(550, 120, 161, 51))
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
                                       "    border: 2px solid rgba(30, 123, 111, 255); /* Outer border color – bluish green */\n"
                                       "    border-radius: 10px;\n"
                                       "    width: 20px;\n"
                                       "    height: 20px;\n"
                                       "    background-color: rgba(60, 150, 220, 255); /* Base color – light blue */\n"
                                       "}\n"
                                       "\n"
                                       "QRadioButton#radioButton::indicator:checked {\n"
                                       "    background-color: rgba(25, 115, 105, 255); /* When checked – greenish blue */\n"
                                       "    border: 2px solid rgba(50, 135, 210, 255); /* Border color when checked */\n"
                                       "}\n"
                                       "\n"
                                       "QRadioButton#radioButton::indicator:hover {\n"
                                       "    background-color: rgba(50, 135, 210, 255); /* Light blue on hover */\n"
                                       "    border: 2px solid rgba(30, 123, 111, 255); /* Border color on hover */\n"
                                       "}\n"
                                       "")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 120, 161, 51))
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
                                         "    border: 2px solid rgba(30, 123, 111, 255); /* Outer border color – bluish green */\n"
                                         "    border-radius: 10px;\n"
                                         "    width: 20px;\n"
                                         "    height: 20px;\n"
                                         "    background-color: rgba(60, 150, 220, 255); /* Base color – light blue */\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton#radioButton_2::indicator:checked {\n"
                                         "    background-color: rgba(25, 115, 105, 255); /* When checked – greenish blue */\n"
                                         "    border: 2px solid rgba(50, 135, 210, 255); /* Border color when checked */\n"
                                         "}\n"
                                         "\n"
                                         "QRadioButton#radioButton_2::indicator:hover {\n"
                                         "    background-color: rgba(50, 135, 210, 255); /* Light blue on hover */\n"
                                         "    border: 2px solid rgba(30, 123, 111, 255); /* Border color on hover */\n"
                                         "}\n"
                                         "")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(340, 60, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
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

        # Connect buttons to their functions
        self.pushButton.clicked.connect(self.import_file)
        self.pushButton_3.clicked.connect(self.download_file)
        self.pushButton_4.clicked.connect(self.clear_fields)
        self.pushButton_5.clicked.connect(self.convert_text)

        # Set default radio button
        self.radioButton_2.setChecked(True)

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
        self.label_2.setText(_translate("Form", "Substitution CYPHER"))
        self.pushButton_6.setText(_translate("Form", "BACK"))

    def show_alert(self, title, message, icon=QMessageBox.Icon.Warning):
        """Show an alert message box"""
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def validate_fields(self):
        """Validate all required fields based on current mode"""
        # Check if all fields are empty
        if (not self.lineEdit_2.text() and not self.lineEdit_4.text() and
                not self.lineEdit_5.text()):
            self.show_alert("Empty Fields", "All fields are empty! Please fill in the required fields.")
            return False

        if self.radioButton_2.isChecked():  # Encryption mode
            if not self.lineEdit_2.text():
                self.show_alert("Empty Field", "Please enter text to encrypt!")
                return False
        else:  # Decryption mode
            if not self.lineEdit_4.text():
                self.show_alert("Empty Field", "Please enter text to decrypt!")
                return False

        if not self.lineEdit_5.text():
            self.show_alert("Empty Field", "Please enter a substitution key!")
            return False

        return True

    def validate_input_text(self, text):
        """Validate that text contains at least one alphabetic character"""
        if not any(char.isalpha() for char in text):
            if any(char.isdigit() for char in text):
                self.show_alert("Invalid Input", "Text contains only digits! Validate that text contains only alphabetic characters and spaces.")
            else:
                self.show_alert("Invalid Input", "Text contains only digits! Validate that text contains only alphabetic characters and spaces.")
            return False
        return True

    def import_file(self):

        """Import text from a file"""
        file_path, _ = QFileDialog.getOpenFileName(
            None, "Open File", "", "Text Files (.txt);;All Files ()"
        )

        # If user cancels file selection
        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read().strip()

            # Check if file is empty
            if not content:
                self.show_alert("Empty File", "The selected file is empty. Please choose a file with content.")
                return

            # Check if target field already has content
            target_field = self.lineEdit_2 if self.radioButton_2.isChecked() else self.lineEdit_4
            if target_field.text():
                reply = QMessageBox.question(
                    None,
                    'Field Not Empty',
                    'Target field already contains text. Overwrite existing content?',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if reply == QMessageBox.StandardButton.No:
                    return

            # Display in appropriate field
            target_field.setText(content)

        except Exception as e:
            self.show_alert("File Error", f"An error occurred while reading the file: {str(e)}")

    def download_file(self):
        """Download the result to a file"""
        if self.radioButton_2.isChecked():  # Encryption mode
            content = self.lineEdit_4.text()
            if not content:
                self.show_alert("No Content", "No encrypted text to save! Please encrypt some text first.")
                return
        else:  # Decryption mode
            content = self.lineEdit_2.text()
            if not content:
                self.show_alert("No Content", "No decrypted text to save! Please decrypt some text first.")
                return

        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text Files (.txt);;All Files ()")

        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            return

    def clear_fields(self):
        """Clear all input fields"""
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

    def is_valid_key(self, key):
        """Validate the substitution cipher key"""
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = key.upper()

        if not key:
            self.show_alert("Empty Key", "Key cannot be empty!")
            return False

        if len(key) != 26:
            self.show_alert("Invalid Key Length", "The key must contain exactly 26 unique letters with no duplicates and no spaces!")
            return False

        if not all(char in LETTERS for char in key):
            self.show_alert("Invalid Characters",
                            "Key must contain only uppercase letters A-Z!")
            return False

        if len(set(key)) != 26:
            self.show_alert("Duplicate Letters",
                            "Key must contain all 26 unique letters with no duplicates!")
            return False

        return True

    def convert_text(self):
        """Convert text using substitution cipher with comprehensive validation"""
        # First validate all required fields
        if not self.validate_fields():
            return

        # Get the key and validate it
        key_text = self.lineEdit_5.text().strip()
        if not self.is_valid_key(key_text):
            return

        # Validate input text based on current mode
        if self.radioButton_2.isChecked():  # Encryption
            plain_text = self.lineEdit_2.text()
            if not self.validate_input_text(plain_text):
                return
        else:  # Decryption
            cipher_text = self.lineEdit_4.text()
            if not self.validate_input_text(cipher_text):
                return

        # Perform conversion only if there are alphabetic characters
        try:
            if self.radioButton_2.isChecked():  # Encryption
                plain_text = self.lineEdit_2.text()
                if any(char.isalpha() for char in plain_text):
                    cipher_text = self.substitution_cipher(plain_text, key_text, mode='encrypt')
                    self.lineEdit_4.setText(cipher_text)
            else:  # Decryption
                cipher_text = self.lineEdit_4.text()
                if any(char.isalpha() for char in cipher_text):
                    plain_text = self.substitution_cipher(cipher_text, key_text, mode='decrypt')
                    self.lineEdit_2.setText(plain_text)
        except Exception as e:
            return

    def substitution_cipher(self, text, key, mode='encrypt'):
        """Implement substitution cipher algorithm with case preservation
        and passing through non-alphabetic characters unchanged"""
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        key = key.upper()

        for char in text:
            if char == ' ':
                result.append(' ')
                continue

            if char.isalpha():
                if mode == 'encrypt':
                    if char.isupper():
                        index = LETTERS.find(char)
                        result.append(key[index])
                    else:
                        index = LETTERS.find(char.upper())
                        result.append(key[index].lower())
                else:  # decrypt
                    if char.isupper():
                        index = key.find(char)
                        result.append(LETTERS[index])
                    else:
                        index = key.find(char.upper())
                        result.append(LETTERS[index].lower())
            else:
                # Pass through non-alphabetic characters unchanged
                result.append(char)

        return ''.join(result)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())