from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import sys


# ================= Rail Fence Cipher Functions ====================
def fence(lst, numrails):
    fence = [[None] * len(lst) for _ in range(numrails)]
    rails = list(range(numrails - 1)) + list(range(numrails - 1, 0, -1))
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x
    return [c for rail in fence for c in rail if c is not None]


def encode(text, n):
    # Track space positions before removing them
    space_positions = [i for i, char in enumerate(text) if char == ' ']
    text_no_spaces = text.replace(" ", "")
    cipher_text = ''.join(fence(text_no_spaces, n))
    return cipher_text, space_positions


def decode(text, n, space_positions=None):
    text_no_spaces = text.replace(" ", "")
    rng = range(len(text_no_spaces))
    pos = fence(rng, n)
    decoded = ''.join(text_no_spaces[pos.index(i)] for i in rng)

    # Restore spaces if positions were provided
    if space_positions:
        result = []
        text_ptr = 0
        for i in range(len(decoded) + len(space_positions)):
            if i in space_positions:
                result.append(' ')
            else:
                if text_ptr < len(decoded):
                    result.append(decoded[text_ptr])
                    text_ptr += 1
        return ''.join(result)
    return decoded


# ================= PyQt6 UI Class ======================
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

        # Plain Text Input
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 200, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(
            "#lineEdit_2 {\n"
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
            "#lineEdit_2:focus {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(30, 123, 111, 0.7),\n"
            "        stop:1 rgba(60, 150, 220, 0.7)\n"
            "    );\n"
            "    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
            "    outline: none;\n"
            "}\n"
            "#lineEdit_2:hover {\n"
            "    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
            "}\n"
            "#lineEdit_2:disabled {\n"
            "    background-color: rgba(240, 240, 240, 0.6);\n"
            "    color: rgba(128, 128, 128, 0.6);\n"
            "    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
            "}\n"
        )
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")

        # Import File Button
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(460, 410, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "QPushButton#pushButton {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(30, 123, 111, 255),\n"
            "        stop:1 rgba(60, 150, 220, 255)\n"
            "    );\n"
            "    color: white;\n"
            "    border-radius: 20px;\n"
            "    padding: 8px 20px;\n"
            "}\n"
            "QPushButton#pushButton:hover {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(25, 115, 105, 255),\n"
            "        stop:1 rgba(50, 135, 210, 255)\n"
            "    );\n"
            "}\n"
            "QPushButton#pushButton:pressed {\n"
            "    padding-top: 5px;\n"
            "    padding-left: 5px;\n"
            "    background-color: rgb(20, 100, 120);\n"
            "}\n"
        )
        self.pushButton.setObjectName("pushButton")

        # Cipher Text Input
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(550, 200, 271, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(
            "#lineEdit_4 {\n"
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
            "#lineEdit_4:focus {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(30, 123, 111, 0.7),\n"
            "        stop:1 rgba(60, 150, 220, 0.7)\n"
            "    );\n"
            "    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
            "    outline: none;\n"
            "}\n"
            "#lineEdit_4:hover {\n"
            "    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
            "}\n"
            "#lineEdit_4:disabled {\n"
            "    background-color: rgba(240, 240, 240, 0.6);\n"
            "    color: rgba(128, 128, 128, 0.6);\n"
            "    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
            "}\n"
        )
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")

        # Key Input
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 280, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(
            "#lineEdit_5 {\n"
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
            "#lineEdit_5:focus {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(30, 123, 111, 0.7),\n"
            "        stop:1 rgba(60, 150, 220, 0.7)\n"
            "    );\n"
            "    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
            "    outline: none;\n"
            "}\n"
            "#lineEdit_5:hover {\n"
            "    border-bottom: 2px solid rgba(30, 123, 111, 1);\n"
            "}\n"
            "#lineEdit_5:disabled {\n"
            "    background-color: rgba(240, 240, 240, 0.6);\n"
            "    color: rgba(128, 128, 128, 0.6);\n"
            "    border-bottom: 2px solid rgba(200, 200, 200, 0.6);\n"
            "}\n"
        )
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")

        # Download File Button
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 470, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(
            "QPushButton#pushButton_3 {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(30, 123, 111, 255),\n"
            "        stop:1 rgba(60, 150, 220, 255)\n"
            "    );\n"
            "    color: white;\n"
            "    border-radius: 20px;\n"
            "    padding: 8px 20px;\n"
            "}\n"
            "QPushButton#pushButton_3:hover {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(25, 115, 105, 255),\n"
            "        stop:1 rgba(50, 135, 210, 255)\n"
            "    );\n"
            "}\n"
            "QPushButton#pushButton_3:pressed {\n"
            "    padding-top: 5px;\n"
            "    padding-left: 5px;\n"
            "    background-color: rgb(20, 100, 120);\n"
            "}\n"
        )
        self.pushButton_3.setObjectName("pushButton_3")

        # Clear Button
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(580, 350, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(
            "QPushButton#pushButton_4 {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(30, 123, 111, 255),\n"
            "        stop:1 rgba(60, 150, 220, 255)\n"
            "    );\n"
            "    color: white;\n"
            "    border-radius: 20px;\n"
            "    padding: 8px 20px;\n"
            "}\n"
            "QPushButton#pushButton_4:hover {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(25, 115, 105, 255),\n"
            "        stop:1 rgba(50, 135, 210, 255)\n"
            "    );\n"
            "}\n"
            "QPushButton#pushButton_4:pressed {\n"
            "    padding-top: 5px;\n"
            "    padding-left: 5px;\n"
            "    background-color: rgb(20, 100, 120);\n"
            "}\n"
        )
        self.pushButton_4.setObjectName("pushButton_4")

        # Convert Button
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 350, 141, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(
            "QPushButton#pushButton_5 {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(30, 123, 111, 255),\n"
            "        stop:1 rgba(60, 150, 220, 255)\n"
            "    );\n"
            "    color: white;\n"
            "    border-radius: 20px;\n"
            "    padding: 8px 20px;\n"
            "}\n"
            "QPushButton#pushButton_5:hover {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(25, 115, 105, 255),\n"
            "        stop:1 rgba(50, 135, 210, 255)\n"
            "    );\n"
            "}\n"
            "QPushButton#pushButton_5:pressed {\n"
            "    padding-top: 5px;\n"
            "    padding-left: 5px;\n"
            "    background-color: rgb(20, 100, 120);\n"
            "}\n"
        )
        self.pushButton_5.setObjectName("pushButton_5")

        # Decryption Radio Button
        self.radioButton = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton.setGeometry(QtCore.QRect(550, 120, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(
            "QRadioButton#radioButton {\n"
            "    color: white;\n"
            "    padding: 10px;\n"
            "}\n"
            "QRadioButton#radioButton::indicator {\n"
            "    border: 2px solid rgba(30, 123, 111, 255);\n"
            "    border-radius: 10px;\n"
            "    width: 20px;\n"
            "    height: 20px;\n"
            "    background-color: rgba(60, 150, 220, 255);\n"
            "}\n"
            "QRadioButton#radioButton::indicator:checked {\n"
            "    background-color: rgba(25, 115, 105, 255);\n"
            "    border: 2px solid rgba(50, 135, 210, 255);\n"
            "}\n"
            "QRadioButton#radioButton::indicator:hover {\n"
            "    background-color: rgba(50, 135, 210, 255);\n"
            "    border: 2px solid rgba(30, 123, 111, 255);\n"
            "}\n"
        )
        self.radioButton.setObjectName("radioButton")

        # Encryption Radio Button
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(330, 120, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(
            "QRadioButton#radioButton_2 {\n"
            "    color: white;\n"
            "    padding: 10px;\n"
            "}\n"
            "QRadioButton#radioButton_2::indicator {\n"
            "    border: 2px solid rgba(30, 123, 111, 255);\n"
            "    border-radius: 10px;\n"
            "    width: 20px;\n"
            "    height: 20px;\n"
            "    background-color: rgba(60, 150, 220, 255);\n"
            "}\n"
            "QRadioButton#radioButton_2::indicator:checked {\n"
            "    background-color: rgba(25, 115, 105, 255);\n"
            "    border: 2px solid rgba(50, 135, 210, 255);\n"
            "}\n"
            "QRadioButton#radioButton_2::indicator:hover {\n"
            "    background-color: rgba(50, 135, 210, 255);\n"
            "    border: 2px solid rgba(30, 123, 111, 255);\n"
            "}\n"
        )
        self.radioButton_2.setObjectName("radioButton_2")

        # Title Label
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(400, 60, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")

        # Back Button
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(40, 490, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(
            "QPushButton#pushButton_6 {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(30, 123, 111, 255),\n"
            "        stop:1 rgba(60, 150, 220, 255)\n"
            "    );\n"
            "    color: white;\n"
            "    border-radius: 20px;\n"
            "    padding: 8px 20px;\n"
            "}\n"
            "QPushButton#pushButton_6:hover {\n"
            "    background-color: qlineargradient(\n"
            "        spread:pad, x1:0, y1:0, x2:1, y2:0,\n"
            "        stop:0 rgba(25, 115, 105, 255),\n"
            "        stop:1 rgba(50, 135, 210, 255)\n"
            "    );\n"
            "}\n"
            "QPushButton#pushButton_6:pressed {\n"
            "    padding-top: 5px;\n"
            "    padding-left: 5px;\n"
            "    background-color: rgb(20, 100, 120);\n"
            "}\n"
        )
        self.pushButton_6.setObjectName("pushButton_6")

        # Connect buttons to their functions
        self.pushButton.clicked.connect(self.import_file)
        self.pushButton_3.clicked.connect(self.download_file)
        self.pushButton_4.clicked.connect(self.clear_fields)
        self.pushButton_5.clicked.connect(self.convert_text)
        self.pushButton_6.clicked.connect(lambda: Form.close())

        # Set default radio button
        self.radioButton_2.setChecked(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Rail Fence Cipher"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Plain Text"))
        self.pushButton.setText(_translate("Form", "Import File"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Cipher Text"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "KEY"))
        self.pushButton_3.setText(_translate("Form", "Download File"))
        self.pushButton_4.setText(_translate("Form", "CLEAR"))
        self.pushButton_5.setText(_translate("Form", "CONVERT"))
        self.radioButton.setText(_translate("Form", "DECRYPTION"))
        self.radioButton_2.setText(_translate("Form", "ENCRYPTION"))
        self.label_2.setText(_translate("Form", "Rail Fence CYPHER"))
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
        file_path, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Text Files (.txt);;All Files ()")
        if not file_path:
            return

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read().strip()

            if not content:
                self.show_alert("Empty File", "The selected file is empty.")
                return

            if not all(char.isalpha() or char.isspace() for char in content):
                self.show_alert("Invalid Content",
                                "File should contain only alphabetic characters (A-Z, a-z) and spaces.")
                return

            if self.radioButton_2.isChecked():
                self.lineEdit_2.setText(content)
            else:
                self.lineEdit_4.setText(content)

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

        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Text Files (.txt);;All Files ()")
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
        self.lineEdit_5.setToolTip("")

    def convert_text(self):
        """Convert text using Rail Fence cipher with validation"""
        key_text = self.lineEdit_5.text()
        if not key_text:
            self.show_alert("Missing Key", "Please enter a key!")
            return

        try:
            key = int(key_text)
            if key < 2:
                self.show_alert("Invalid Key", "Key must be an integer greater than or equal to 2!")
                return
        except ValueError:
            self.show_alert("Invalid Key", "Key must be an integer without spaces!")
            return

        if self.radioButton_2.isChecked():  # Encryption
            plain_text = self.lineEdit_2.text()
            if not plain_text:
                self.show_alert("Missing Text", "Please enter text to encrypt!")
                return

            if not all(char.isalpha() or char.isspace() for char in plain_text):
                self.show_alert("Invalid Text", "Text should contain only alphabetic characters (A-Z, a-z) and spaces.")
                return

            text_without_spaces = plain_text.replace(" ", "")
            if key >= len(text_without_spaces):
                self.show_alert("Invalid Key", "Key must be less than the length of the plain text (excluding spaces)!")
                return

            cipher_text, space_positions = encode(plain_text, key)
            self.lineEdit_4.setText(cipher_text)
            # Store space positions in lineEdit_5's tooltip for decryption
            self.lineEdit_5.setToolTip(','.join(map(str, space_positions)))

        else:  # Decryption
            cipher_text = self.lineEdit_4.text()
            if not cipher_text:
                self.show_alert("Missing Text", "Please enter text to decrypt!")
                return

            if not all(char.isalpha() or char.isspace() for char in cipher_text):
                self.show_alert("Invalid Text", "Text should contain only alphabetic characters (A-Z, a-z) and spaces.")
                return

            text_without_spaces = cipher_text.replace(" ", "")
            if key >= len(text_without_spaces):
                self.show_alert("Invalid Key",
                                "Key must be less than the length of the cipher text (excluding spaces)!")
                return

            # Get space positions from lineEdit_5's tooltip
            space_positions = []
            if self.lineEdit_5.toolTip():
                space_positions = list(map(int, self.lineEdit_5.toolTip().split(',')))

            plain_text = decode(cipher_text, key, space_positions)
            self.lineEdit_2.setText(plain_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())