import sys
import re
import csv
import os
import random
import string
import smtplib
from src.core.mainnn import HomeScreen
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QWidget, 
                            QLineEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt6.QtGui import QIcon, QPixmap, QColor, QPainter
from PyQt6.QtCore import Qt, QTimer
from src.core.lastwelcomme import Ui_Form as WelcomeUI
from src.core.lastloog import Ui_Form as LoginUI
from src.core.lastregggg import Ui_Form as RegisterUI
from cryptography.fernet import Fernet


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "cybersystem100@gmail.com"  
EMAIL_PASSWORD = "eibihmhuuqqhvrdi"   
VERIFICATION_EXPIRE_MINUTES = 30

class VerificationManager:
    def __init__(self):
        self.verification_file = "verification_codes.csv"
        
    def generate_verification_code(self, email):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        expiration = datetime.now() + timedelta(minutes=VERIFICATION_EXPIRE_MINUTES)
        
        try:
            file_exists = os.path.exists(self.verification_file)
            with open(self.verification_file, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['email', 'code', 'expiration'])
                if not file_exists:
                    writer.writeheader()
                writer.writerow({
                    'email': email,
                    'code': code,
                    'expiration': expiration.strftime("%Y-%m-%d %H:%M:%S")
                })
        except Exception as e:
            print(f"Error saving verification code: {str(e)}")
            return None
            
        return code
        
    def verify_code(self, email, code):
        try:
            with open(self.verification_file, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['email'] == email and row['code'] == code:
                        expiration = datetime.strptime(row['expiration'], "%Y-%m-%d %H:%M:%S")
                        if datetime.now() <= expiration:
                            return True
        except FileNotFoundError:
            return False
        return False
        
    def send_verification_email(self, email, code):
        try:
            subject = "Email Verification Code"
            body = f"""
            <html>
                <body>
                    <h2>Your Verification Code</h2>
                    <p>Please use the following code to verify your email address:</p>
                    <h3 style="color: #1e6b6f;">{code}</h3>
                    <p>This code will expire in {VERIFICATION_EXPIRE_MINUTES} minutes.</p>
                    <p>Thanks For Using Our Application ❤️.</p>
                </body>
            </html>
            """
            
            msg = MIMEText(body, 'html')
            msg['Subject'] = subject
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = email
            
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                
            return True
        except Exception as e:
            print(f"Error sending verification email: {str(e)}")
            return False

class EncryptionManager:
    def __init__(self):
        self.key_file = "encryption_key.key"
        self.key = self._get_or_create_key()
        self.cipher_suite = Fernet(self.key)
    
    def _get_or_create_key(self):
        """Get the encryption key or create one if it doesn't exist"""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key
    
    def encrypt(self, data):
        """Encrypt data"""
        if isinstance(data, str):
            data = data.encode()
        return self.cipher_suite.encrypt(data).decode()
    
    def decrypt(self, encrypted_data):
        """Decrypt data"""
        if isinstance(encrypted_data, str):
            encrypted_data = encrypted_data.encode()
        return self.cipher_suite.decrypt(encrypted_data).decode()

class UserManager:
    def __init__(self):
        self.filename = "users.csv"
        self.encryption = EncryptionManager()
        self.verification = VerificationManager()
        
    def register_user(self, username, email, password):
        if self.user_exists(username, email):
            return False, "Username or email already exists"
            
        encrypted_password = self.encryption.encrypt(password)
        verification_code = self.verification.generate_verification_code(email)
        
        if not verification_code:
            return False, "Failed to generate verification code"
            
        if not self.verification.send_verification_email(email, verification_code):
            return False, "Failed to send verification email"
            
        try:
            file_exists = os.path.exists(self.filename)
            with open(self.filename, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['username', 'email', 'password', 'verified'])
                if not file_exists:
                    writer.writeheader()
                writer.writerow({
                    'username': username,
                    'email': email,
                    'password': encrypted_password,
                    'verified': 'False'
                })
            return True, f"Registration successful. Verification email sent to {email}"
        except Exception as e:
            return False, f"Error saving user: {str(e)}"
            
    def verify_user_email(self, email, code):
        if self.verification.verify_code(email, code):
            try:
                users = []
                verified = False
                
                with open(self.filename, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if row['email'] == email:
                            row['verified'] = 'True'
                            verified = True
                        users.append(row)
                
                if verified:
                    with open(self.filename, 'w', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=['username', 'email', 'password', 'verified'])
                        writer.writeheader()
                        writer.writerows(users)
                    return True, "Welcome to Our system! Email verified successfully!"
                return False, "Email not found in our records"
            except Exception as e:
                return False, f"Error updating verification status: {str(e)}"
        return False, "Invalid or expired verification code. Please enter the correct code or request a new one."
            
    def user_exists(self, username, email):
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'] == username or row['email'] == email:
                        return True
        except FileNotFoundError:
            return False
        return False
        
    def authenticate_user(self, username, password):
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'] == username:
                        if row.get('verified', 'False').lower() != 'true':
                            return False, "Email not verified. Please check your email for verification link."
                            
                        try:
                            decrypted_password = self.encryption.decrypt(row['password'])
                            if decrypted_password == password:
                                return True, "Login successful"
                        except:
                            return False, "Invalid credentials"
            return False, "Invalid username or password"
        except FileNotFoundError:
            return False, "No users registered yet"
        except Exception as e:
            return False, f"Error during authentication: {str(e)}"

class SecurityAlert(QMessageBox):
    def __init__(self, title, message, alert_type, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setText(message)

        if alert_type == QMessageBox.Icon.Critical:
            self.setup_error_style()
        elif alert_type == QMessageBox.Icon.Information:
            self.setup_success_style()
        else:
            self.setup_default_style()

        self.setWindowIcon(QIcon(self.create_security_icon(alert_type)))
        self.add_security_tips(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        ok_button = self.button(QMessageBox.StandardButton.Ok)
        ok_button.setText("OK")
        ok_button.setCursor(Qt.CursorShape.PointingHandCursor)

    def setup_error_style(self):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setStyleSheet("""
            QMessageBox {
                background-color: white;
                color: #333333;
                font-family: 'Segoe UI', Arial, sans-serif;
                border-radius: 20px;
                padding: 8px 20px;
            }
            QMessageBox QLabel {
                color: #333333;
                font-size: 14px;
            }
            QMessageBox QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 123, 111, 255), stop:1 rgba(95, 112, 228, 255));
                color: white;
                border-radius: 10px;
                padding: 4px 12px;
                min-width: 60px;
                max-width: 80px;
                font-size: 12px;
                font-weight: bold;
                border: 1px solid #1e6b6f;
            }
            QMessageBox QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(25, 103, 91, 255), stop:1 rgba(85, 102, 218, 255));
            }
            QMessageBox QPushButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 83, 71, 255), stop:1 rgba(75, 92, 208, 255));
                border: 1px inset #1e6b6f;
            }
        """)

    def setup_success_style(self):
        self.setIcon(QMessageBox.Icon.Information)
        self.setStyleSheet("""
            QMessageBox {
                background-color: white;
                color: #333333;
                font-family: 'Segoe UI', Arial, sans-serif;
                border-radius: 20px;
                padding: 8px 20px;
            }
            QMessageBox QLabel {
                color: #333333;
                font-size: 14px;
            }
            QMessageBox QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 123, 111, 255), stop:1 rgba(95, 112, 228, 255));
                color: white;
                border-radius: 10px;
                padding: 4px 12px;
                min-width: 60px;
                max-width: 80px;
                font-size: 12px;
                font-weight: bold;
                border: 1px solid #1e6b6f;
            }
            QMessageBox QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(25, 103, 91, 255), stop:1 rgba(85, 102, 218, 255));
            }
            QMessageBox QPushButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 83, 71, 255), stop:1 rgba(75, 92, 208, 255));
                border: 1px inset #1e6b6f;
            }
        """)

    def setup_default_style(self):
        self.setStyleSheet("""
            QMessageBox {
                background-color: white;
                color: #333333;
                font-family: 'Segoe UI', Arial, sans-serif;
                border-radius: 20px;
                padding: 8px 20px;
            }
            QMessageBox QLabel {
                color: #333333;
                font-size: 14px;
            }
            QMessageBox QPushButton {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(30, 123, 111, 255), stop:1 rgba(95, 112, 228, 255));
                color: white;
                border-radius: 10px;
                padding: 4px 12px;
                min-width: 60px;
                max-width: 80px;
                font-size: 12px;
                font-weight: bold;
                border: 1px solid #1e6b6f;
            }
            QMessageBox QPushButton:hover {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(25, 103, 91, 255), stop:1 rgba(85, 102, 218, 255));
            }
            QMessageBox QPushButton:pressed {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(20, 83, 71, 255), stop:1 rgba(75, 92, 208, 255));
                border: 1px inset #1e6b6f;
            }
        """)

    def create_security_icon(self, alert_type):
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if alert_type == QMessageBox.Icon.Critical:
            painter.setBrush(QColor("#ff5555"))
            painter.setPen(QColor("#ff5555"))
            painter.drawEllipse(0, 0, 32, 32)
            painter.setPen(QColor("#ffffff"))
            painter.drawText(8, 24, "!")
        elif alert_type == QMessageBox.Icon.Information:
            painter.setBrush(QColor("#50fa7b"))
            painter.setPen(QColor("#50fa7b"))
            painter.drawEllipse(0, 0, 32, 32)
            painter.setPen(QColor("#ffffff"))
            painter.drawText(12, 24, "✓")
        else:
            painter.setBrush(QColor("#3298dc"))
            painter.setPen(QColor("#3298dc"))
            painter.drawEllipse(0, 0, 32, 32)
            painter.setPen(QColor("#ffffff"))
            painter.drawText(12, 24, "i")

        painter.end()
        return pixmap

    def add_security_tips(self, message):
        if "password" in message.lower():
            self.setDetailedText(
                "🔒 Security Tips:\n• Use at least 12 characters\n• Mix letters, numbers & symbols\n• Avoid common words\n• Don't reuse passwords")
        elif "username" in message.lower():
            self.setDetailedText(
                "👤 Username Tips:\n• 3-20 characters\n• Letters and numbers only\n• Avoid personal info")
        elif "email" in message.lower():
            self.setDetailedText(
                "📧 Email Tips:\n• Use a valid, accessible email\n• We'll send verification links\n• Keep your email secure")
        elif "invalid" in message.lower() and "login" in message.lower():
            self.setDetailedText(
                "⚠️ Account Protection:\n• Check Caps Lock\n• Try resetting password\n• Contact support if locked out")

class VerificationWindow(QWidget):
    def __init__(self, email, user_manager, parent=None):
        super().__init__(parent)
        self.email = email
        self.user_manager = user_manager
        self.setWindowTitle("Email Verification")
        self.setGeometry(300, 300, 400, 250)
        
        layout = QVBoxLayout()
        
        self.label = QLabel(f"Enter verification code sent to {email}")
        layout.addWidget(self.label)
        
        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText("Verification Code")
        layout.addWidget(self.code_input)
        
        self.verify_button = QPushButton("Verify")
        self.verify_button.clicked.connect(self.handle_verification)
        layout.addWidget(self.verify_button)
        
        self.resend_button = QPushButton("Resend Code")
        self.resend_button.clicked.connect(self.handle_resend_code)
        layout.addWidget(self.resend_button)
        
        self.setLayout(layout)
    
    def handle_verification(self):
        code = self.code_input.text().strip()
        if not code:
            QMessageBox.warning(self, "Error", "Please enter the verification code")
            return
            
        success, message = self.user_manager.verify_user_email(self.email, code)
        if success:
            QMessageBox.information(self, "Success", message)
            self.close()
            # Open main application window or login window here if needed
        else:
            QMessageBox.critical(self, "Error", message)
    
    def handle_resend_code(self):
        # Generate a new verification code and send it
        verification_code = self.user_manager.verification.generate_verification_code(self.email)
        if verification_code:
            if self.user_manager.verification.send_verification_email(self.email, verification_code):
                QMessageBox.information(self, "Success", "New verification code has been sent to your email")
            else:
                QMessageBox.critical(self, "Error", "Failed to send new verification code")
        else:
            QMessageBox.critical(self, "Error", "Failed to generate new verification code")

from src.core.challenge import CryptoChallengeWindow

class WelcomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = WelcomeUI()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.open_challenge)

    def open_challenge(self):
        self.challenge_window = CryptoChallengeWindow()
        self.challenge_window.show()
        self.close()

    def show_message(self, title, message, icon):
        alert = SecurityAlert(title, message, icon, self)
        alert.exec()

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginUI()
        self.ui.setupUi(self)
        self.user_manager = UserManager()
        self.ui.pushButton.clicked.connect(self.handle_login)
        self.ui.pushButton_2.clicked.connect(self.open_register)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if not username or not password:
            self.show_message("Error", "Please enter both username and password", QMessageBox.Icon.Critical)
            return

        success, message = self.user_manager.authenticate_user(username, password)
        if success:
            self.show_message("Success", message, QMessageBox.Icon.Information)
            self.home_screen = HomeScreen()
            self.home_screen.show()
            self.close()
        else:
            self.show_message("Error", message, QMessageBox.Icon.Critical)

    def open_register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()

    def show_message(self, title, message, icon):
        alert = SecurityAlert(title, message, icon, self)
        alert.exec()

class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = RegisterUI()
        self.ui.setupUi(self)
        self.user_manager = UserManager()
        self.ui.pushButton.clicked.connect(self.handle_register)
        self.ui.pushButton_2.clicked.connect(self.open_login)
        self.ui.user_name.textChanged.connect(self.validate_username)
        self.ui.lineEdit_4.textChanged.connect(self.validate_email)
        self.ui.lineEdit_2.textChanged.connect(self.validate_passwords)
        self.ui.lineEdit_3.textChanged.connect(self.validate_passwords)

        self.ui.user_name.setPlaceholderText("Username")
        self.ui.lineEdit_4.setPlaceholderText("Email")
        self.ui.lineEdit_2.setPlaceholderText("Password")
        self.ui.lineEdit_3.setPlaceholderText("Confirm Password")

    def validate_username(self, text):
        username_exists = False
        try:
            with open(self.user_manager.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'] == text:
                        username_exists = True
                        break
        except FileNotFoundError:
            username_exists = False

        is_valid = len(text) >= 3 and not username_exists if text else False
        border_color = "rgba(0, 200, 0, 0.8)" if is_valid else "rgba(255, 0, 0, 0.8)" if text else "rgba(46, 82, 101, 0.8)"
        self.ui.user_name.setStyleSheet(f"""
            background-color: rgba(0, 0, 0, 0);
            border: none;
            border-bottom: 2px solid {border_color};
            color: rgba(0, 0, 0, 0.8);
            padding-bottom: 7px;
        """)

    def validate_email(self, text):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email_exists = False
        try:
            with open(self.user_manager.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['email'] == text:
                        email_exists = True
                        break
        except FileNotFoundError:
            email_exists = False

        is_valid = re.match(pattern, text) is not None and not email_exists if text else False
        border_color = "rgba(0, 200, 0, 0.8)" if is_valid else "rgba(255, 0, 0, 0.8)" if text else "rgba(46, 82, 101, 0.8)"
        self.ui.lineEdit_4.setStyleSheet(f"""
            background-color: rgba(0, 0, 0, 0);
            border: none;
            border-bottom: 2px solid {border_color};
            color: rgba(0, 0, 0, 0.8);
            padding-bottom: 7px;
        """)

    def validate_passwords(self):
        password = self.ui.lineEdit_2.text()
        confirm = self.ui.lineEdit_3.text()
        passwords_match = password == confirm if (password and confirm) else None
        pass1_color = "rgba(0, 200, 0, 0.8)" if passwords_match is True else "rgba(255, 0, 0, 0.8)" if passwords_match is False else "rgba(46, 82, 101, 0.8)"
        pass2_color = pass1_color
        self.ui.lineEdit_2.setStyleSheet(f"""
            background-color: rgba(0, 0, 0, 0);
            border: none;
            border-bottom: 2px solid {pass1_color};
            color: rgba(0, 0, 0, 0.8);
            padding-bottom: 7px;
        """)
        self.ui.lineEdit_3.setStyleSheet(f"""
            background-color: rgba(0, 0, 0, 0);
            border: none;
            border-bottom: 2px solid {pass2_color};
            color: rgba(0, 0, 0, 0.8);
            padding-bottom: 7px;
        """)

    def handle_register(self):
        username = self.ui.user_name.text()
        email = self.ui.lineEdit_4.text()
        password = self.ui.lineEdit_2.text()
        confirm_password = self.ui.lineEdit_3.text()

        if not all([username, email, password, confirm_password]):
            self.show_message("Error", "All fields are required", QMessageBox.Icon.Critical)
            return

        if len(username) < 3:
            self.show_message("Error", "Username must be at least 3 characters", QMessageBox.Icon.Critical)
            return

        username_exists = False
        try:
            with open(self.user_manager.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'] == username:
                        username_exists = True
                        break
        except FileNotFoundError:
            username_exists = False

        if username_exists:
            self.show_message("Error", "The username you have provided is already associated with an account. Please use a different username.", QMessageBox.Icon.Critical)
            return

        email_exists = False
        try:
            with open(self.user_manager.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['email'] == email:
                        email_exists = True
                        break
        except FileNotFoundError:
            email_exists = False

        if email_exists:
            self.show_message("Error", "The email you have provided is already associated with an account. Sign in or reset your password.", QMessageBox.Icon.Critical)
            return

        if password != confirm_password:
            self.show_message("Error", "Passwords do not match", QMessageBox.Icon.Critical)
            return

        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            self.show_message("Error", "Please enter a valid email address", QMessageBox.Icon.Critical)
            return

        success, message = self.user_manager.register_user(username, email, password)
        if success:
            self.show_message("Success", message, QMessageBox.Icon.Information)
            self.verification_window = VerificationWindow(email, self.user_manager)
            self.verification_window.show()
        else:
            self.show_message("Error", message, QMessageBox.Icon.Critical)

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def show_message(self, title, message, icon):
        alert = SecurityAlert(title, message, icon, self)
        alert.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_window = WelcomeWindow()
    welcome_window.show()
    sys.exit(app.exec())