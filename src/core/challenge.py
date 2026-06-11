import sys
import random
import string
from PyQt6.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, 
                            QLabel, QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt
from src.core.mainnn import HomeScreen

class CryptoChallengeWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cryptographic Gateway")
        self.resize(500, 350)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        self.challenge_text = ""
        self.solution = ""
        self.generate_challenge()
        self.init_ui()

    def generate_challenge(self):
        # Using a simple Caesar cipher for the challenge
        self.solution = ''.join(random.choices(string.ascii_uppercase, k=8))
        shift = random.randint(1, 25)
        
        self.challenge_text = ""
        for char in self.solution:
            shifted = (ord(char) - ord('A') + shift) % 26
            self.challenge_text += chr(ord('A') + shifted)
        
        self.hint = f"Hint: Caesar Cipher (Shift: {shift})"

    def init_ui(self):
        # Main widget to hold the background
        self.container = QWidget(self)
        self.container.setGeometry(0, 0, 500, 350)
        self.container.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(10, 40, 50, 255), stop:1 rgba(30, 100, 110, 255));
                border-radius: 20px;
                border: 2px solid rgba(255, 255, 255, 0.1);
            }
        """)

        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        title = QLabel("ACCESS CHALLENGE")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: white; font-size: 24px; font-weight: bold; background: transparent; border: none;")
        layout.addWidget(title)

        subtitle = QLabel("Decrypt the following string to enter:")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #cccccc; font-size: 14px; background: transparent; border: none;")
        layout.addWidget(subtitle)

        self.challenge_label = QLabel(self.challenge_text)
        self.challenge_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.challenge_label.setStyleSheet("""
            color: #50fa7b; 
            font-size: 32px; 
            font-family: 'Courier New'; 
            font-weight: bold;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            padding: 10px;
            border: 1px solid rgba(80, 250, 123, 0.3);
        """)
        layout.addWidget(self.challenge_label)

        hint_label = QLabel(self.hint)
        hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hint_label.setStyleSheet("color: #888888; font-style: italic; background: transparent; border: none;")
        layout.addWidget(hint_label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter Decrypted Text...")
        self.input_field.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_field.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.1);
                border: 2px solid rgba(30, 123, 111, 0.7);
                border-radius: 10px;
                color: white;
                font-size: 18px;
                padding: 10px;
            }
            QLineEdit:focus {
                border: 2px solid rgba(60, 150, 220, 1);
            }
        """)
        layout.addWidget(self.input_field)

        btn_layout = QHBoxLayout()
        
        self.submit_btn = QPushButton("DECRYPT")
        self.submit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                    stop:0 rgba(30, 123, 111, 255), stop:1 rgba(60, 150, 220, 255));
                color: white;
                border-radius: 15px;
                padding: 10px;
                font-weight: bold;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                    stop:0 rgba(40, 140, 130, 255), stop:1 rgba(70, 160, 230, 255));
            }
        """)
        self.submit_btn.clicked.connect(self.check_answer)
        btn_layout.addWidget(self.submit_btn)

        self.close_btn = QPushButton("EXIT")
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 85, 85, 0.2);
                color: #ff5555;
                border: 1px solid #ff5555;
                border-radius: 15px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(255, 85, 85, 0.4);
            }
        """)
        self.close_btn.clicked.connect(QApplication.instance().quit)
        btn_layout.addWidget(self.close_btn)
        
        layout.addLayout(btn_layout)

    def check_answer(self):
        user_input = self.input_field.text().strip().upper()
        if user_input == self.solution:
            QMessageBox.information(self, "Success", "Access Granted! Welcome to the Cryptography System.")
            self.home_window = HomeScreen()
            self.home_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "Failed", "Incorrect decryption! Please try again.")
            self.input_field.clear()
            self.generate_challenge()
            self.challenge_label.setText(self.challenge_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CryptoChallengeWindow()
    window.show()
    sys.exit(app.exec())
