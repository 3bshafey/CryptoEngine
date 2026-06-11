from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import string

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
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)\n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7); \n"
"    color: white;\n"
"    padding-bottom: 7px;\n"
"    font-size: 16px; \n"
"    border-radius: 5px; \n"
"}\n"
"\n"
"#lineEdit_2:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7), \n"
"        stop:1 rgba(60, 150, 220, 0.7)  \n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1); \n"
"    outline: none; \n"
"}\n"
"\n"
"#lineEdit_2:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
"}\n"
"\n"
"#lineEdit_2:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6); \n"
"    color: rgba(128, 128, 128, 0.6); \n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6); \n"
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
"        stop:0 rgba(30, 123, 111, 255),  \n"
"        stop:1 rgba(60, 150, 220, 255) \n"
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
"        stop:1 rgba(50, 135, 210, 255)   \n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120); \n"
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
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)  \n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7); \n"
"    color: white;\n"
"    padding-bottom: 7px; \n"
"    font-size: 16px; \n"
"    border-radius: 5px; \n"
"}\n"
"\n"
"#lineEdit_4:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7), \n"
"        stop:1 rgba(60, 150, 220, 0.7)  \n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1); \n"
"    outline: none; \n"
"}\n"
"\n"
"#lineEdit_4:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1); \n"
"}\n"
"\n"
"#lineEdit_4:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6); \n"
"    color: rgba(128, 128, 128, 0.6); \n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6); \n"
"}\n"
"")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 280, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("#lineEdit_5 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.5),\n"
"        stop:1 rgba(60, 150, 220, 0.5)  \n"
"    );\n"
"    border: none;\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 0.7); \n"
"    color: white; \n"
"    padding-bottom: 7px; \n"
"    font-size: 16px; \n"
"    border-radius: 5px; \n"
"}\n"
"\n"
"#lineEdit_5:focus {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 0.7), \n"
"        stop:1 rgba(60, 150, 220, 0.7) \n"
"    );\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1); \n"
"    outline: none;\n"
"}\n"
"\n"
"#lineEdit_5:hover {\n"
"    border-bottom: 2px solid rgba(30, 123, 111, 1); \n"
"}\n"
"\n"
"#lineEdit_5:disabled {\n"
"    background-color: rgba(240, 240, 240, 0.6); \n"
"    color: rgba(128, 128, 128, 0.6); \n"
"    border-bottom: 2px solid rgba(200, 200, 200, 0.6); \n"
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
"        stop:0 rgba(30, 123, 111, 255),    \n"
"        stop:1 rgba(60, 150, 220, 255)   \n"
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
"        stop:1 rgba(50, 135, 210, 255) \n"
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
        self.pushButton_4.setGeometry(QtCore.QRect(580, 350, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    background-color: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 rgba(30, 123, 111, 255),     \n"
"        stop:1 rgba(60, 150, 220, 255)    \n"
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
"        stop:1 rgba(50, 135, 210, 255)     \n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120); \n"
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
"        stop:0 rgba(30, 123, 111, 255),     \n"
"        stop:1 rgba(60, 150, 220, 255)     \n"
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
"        stop:1 rgba(50, 135, 210, 255)     \n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton_5:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    background-color: rgb(20, 100, 120);   \n"
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
        self.label_2.setGeometry(QtCore.QRect(410, 60, 381, 41))
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
"        stop:0 rgba(30, 123, 111, 255),    \n"
"        stop:1 rgba(60, 150, 220, 255)     \n"
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
"    background-color: rgb(20, 100, 120); \n"
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
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Cipher Text"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "KEY"))
        self.pushButton_3.setText(_translate("Form", "Download File"))
        self.pushButton_4.setText(_translate("Form", "CLEAR"))
        self.pushButton_5.setText(_translate("Form", "CONVERT"))
        self.radioButton.setText(_translate("Form", "DECRYPTION"))
        self.radioButton_2.setText(_translate("Form", "ENCRYPTION"))
        self.label_2.setText(_translate("Form", "Playfair Cipher"))
        self.pushButton_6.setText(_translate("Form", "BACK"))

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
            return  # No file selected

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()

            content = content.strip()
            if not content:
                self.show_alert("Empty File", "The selected file is empty.")
                return

            if not all(char.isalpha() or char.isspace() for char in content):
                self.show_alert("Invalid Content",
                                "File should contain only alphabetic characters (A-Z, a-z) and spaces.")
                return

            if self.radioButton_2.isChecked():  # Encryption mode
                self.lineEdit_2.setText(content)
            else:  # Decryption mode
                self.lineEdit_4.setText(content)

        except Exception as e:
            import traceback
            print("Error reading file:", traceback.format_exc())
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
        """Clear all input fields"""
        self.lineEdit_2.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()

    def validate_input(self, text):
        """Validate that text contains only alphabetic characters and spaces"""
        return text.replace(' ', '').isalpha()

    def validate_key(self, key):
        """Validate that key contains only alphabetic characters"""
        return key.isalpha()

    def toLowerCase(self, text):
        """Convert the string to lowercase"""
        return text.lower()

    def removeSpaces(self, text):
        """Remove all spaces in a string"""
        newText = ""
        for i in text:
            if i == " ":
                continue
            else:
                newText = newText + i
        return newText

    def Diagraph(self, text):
        """Group 2 elements of a string as a list element"""
        Diagraph = []
        group = 0
        for i in range(2, len(text), 2):
            Diagraph.append(text[group:i])
            group = i
        Diagraph.append(text[group:])
        return Diagraph

    def FillerLetter(self, text):
        """Fill a letter in a string element if 2 letters in the same string match"""
        k = len(text)
        if k % 2 == 0:
            for i in range(0, k, 2):
                if text[i] == text[i+1]:
                    new_word = text[0:i+1] + 'x' + text[i+1:]
                    new_word = self.FillerLetter(new_word)
                    break
                else:
                    new_word = text
        else:
            for i in range(0, k-1, 2):
                if text[i] == text[i+1]:
                    new_word = text[0:i+1] + 'x' + text[i+1:]
                    new_word = self.FillerLetter(new_word)
                    break
                else:
                    new_word = text
        return new_word

    def generateKeyTable(self, word):
        """Generate the 5x5 key square matrix"""
        list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        key_letters = []
        for i in word:
            if i not in key_letters:
                key_letters.append(i)

        compElements = []
        for i in key_letters:
            if i not in compElements:
                compElements.append(i)
        for i in list1:
            if i not in compElements:
                compElements.append(i)

        matrix = []
        while compElements:
            matrix.append(compElements[:5])
            compElements = compElements[5:]

        return matrix

    def search(self, mat, element):
        """Search for an element in the matrix and return its position"""
        for i in range(5):
            for j in range(5):
                if mat[i][j] == element:
                    return i, j
        return None

    def encrypt_RowRule(self, matr, e1r, e1c, e2r, e2c):
        """Encrypt using row rule"""
        char1 = matr[e1r][0] if e1c == 4 else matr[e1r][e1c+1]
        char2 = matr[e2r][0] if e2c == 4 else matr[e2r][e2c+1]
        return char1, char2

    def encrypt_ColumnRule(self, matr, e1r, e1c, e2r, e2c):
        """Encrypt using column rule"""
        char1 = matr[0][e1c] if e1r == 4 else matr[e1r+1][e1c]
        char2 = matr[0][e2c] if e2r == 4 else matr[e2r+1][e2c]
        return char1, char2

    def encrypt_RectangleRule(self, matr, e1r, e1c, e2r, e2c):
        """Encrypt using rectangle rule"""
        char1 = matr[e1r][e2c]
        char2 = matr[e2r][e1c]
        return char1, char2

    def decrypt_RowRule(self, matr, e1r, e1c, e2r, e2c):
        """Decrypt using row rule"""
        char1 = matr[e1r][4] if e1c == 0 else matr[e1r][e1c-1]
        char2 = matr[e2r][4] if e2c == 0 else matr[e2r][e2c-1]
        return char1, char2

    def decrypt_ColumnRule(self, matr, e1r, e1c, e2r, e2c):
        """Decrypt using column rule"""
        char1 = matr[4][e1c] if e1r == 0 else matr[e1r-1][e1c]
        char2 = matr[4][e2c] if e2r == 0 else matr[e2r-1][e2c]
        return char1, char2

    def decrypt_RectangleRule(self, matr, e1r, e1c, e2r, e2c):
        """Decrypt using rectangle rule"""
        char1 = matr[e1r][e2c]
        char2 = matr[e2r][e1c]
        return char1, char2

    def encryptByPlayfairCipher(self, Matrix, plainList):
        """Encrypt using Playfair cipher"""
        CipherText = []
        for i in range(len(plainList)):
            ele1_x, ele1_y = self.search(Matrix, plainList[i][0])
            ele2_x, ele2_y = self.search(Matrix, plainList[i][1])

            if ele1_x is None or ele2_x is None:
                return None  # Invalid character in plaintext

            if ele1_x == ele2_x:
                c1, c2 = self.encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            elif ele1_y == ele2_y:
                c1, c2 = self.encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = self.encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

            cipher = c1 + c2
            CipherText.append(cipher)
        return CipherText

    def decryptByPlayfairCipher(self, Matrix, cipherList):
        """Decrypt using Playfair cipher"""
        PlainText = []
        for i in range(len(cipherList)):
            ele1_x, ele1_y = self.search(Matrix, cipherList[i][0])
            ele2_x, ele2_y = self.search(Matrix, cipherList[i][1])

            if ele1_x is None or ele2_x is None:
                return None  # Invalid character in ciphertext

            if ele1_x == ele2_x:
                c1, c2 = self.decrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            elif ele1_y == ele2_y:
                c1, c2 = self.decrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = self.decrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

            plain = c1 + c2
            PlainText.append(plain)
        return PlainText

    def convert_text(self):
        """Convert text using Playfair cipher with validation"""
        # Validate key
        key = self.lineEdit_5.text()
        if not key:
            self.show_alert("Missing Key", "Please enter a key!")
            return

        if not self.validate_key(key):
            self.show_alert("Invalid Key", "Key must contain only alphabetic characters (A-Z, a-z)!")
            return

        key = self.toLowerCase(key).replace('j', 'i')
        Matrix = self.generateKeyTable(key)

        if self.radioButton_2.isChecked():  # Encryption
            plain_text = self.lineEdit_2.text()
            if not plain_text:
                self.show_alert("Missing Text", "Please enter text to encrypt!")
                return

            if not self.validate_input(plain_text):
                self.show_alert("Invalid Text", "Text should contain only alphabetic characters (A-Z, a-z) and spaces.")
                return

            plain_text = self.removeSpaces(self.toLowerCase(plain_text)).replace('j', 'i')
            PlainTextList = self.Diagraph(self.FillerLetter(plain_text))
            if len(PlainTextList[-1]) != 2:
                PlainTextList[-1] = PlainTextList[-1] + 'z'

            CipherList = self.encryptByPlayfairCipher(Matrix, PlainTextList)
            if CipherList is None:
                self.show_alert("Invalid Input", "Text contains invalid characters for Playfair cipher.")
                return

            CipherText = "".join(CipherList)
            self.lineEdit_4.setText(CipherText)
        else:  # Decryption
            cipher_text = self.lineEdit_4.text()
            if not cipher_text:
                self.show_alert("Missing Text", "Please enter text to decrypt!")
                return

            if not self.validate_input(cipher_text):
                self.show_alert("Invalid Text", "Text should contain only alphabetic characters (A-Z, a-z) and spaces.")
                return

            cipher_text = self.removeSpaces(self.toLowerCase(cipher_text)).replace('j', 'i')
            if len(cipher_text) % 2 != 0:
                self.show_alert("Invalid Cipher Text", "Cipher text length must be even for Playfair cipher.")
                return

            CipherTextList = self.Diagraph(cipher_text)
            PlainList = self.decryptByPlayfairCipher(Matrix, CipherTextList)
            if PlainList is None:
                self.show_alert("Invalid Input", "Cipher text contains invalid characters for Playfair cipher.")
                return

            PlainText = "".join(PlainList)
            self.lineEdit_2.setText(PlainText)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())