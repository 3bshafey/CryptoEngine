from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

# Import all UI classes
from .HOME import Ui_Form as HomeUi
from src.ciphers.ROOT13 import Ui_Form as ROOT13Ui
from src.ciphers.ceaser import Ui_Form as caesarUi
from src.ciphers.Hill import Ui_Form as HillUi
from src.ciphers.playfair import Ui_Form as PlayFairUi
from src.ciphers.Transposition import Ui_Form as TransUi
from src.ciphers.QUAD import Ui_Form as QuadUi
from src.ciphers.substtt import Ui_Form as SubstitutionUi

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = HomeUi()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("G:/CyberTest/New folder/smart-lock.png"))

        # Connect buttons to their respective screens
        self.ui.pushButton.clicked.connect(self.open_root13)  # Root 13 button
        self.ui.pushButton_2.clicked.connect(self.open_caesar)  # Caesar button
        self.ui.pushButton_6.clicked.connect(self.open_hill)  # Hill button
        self.ui.pushButton_5.clicked.connect(self.open_playfair)  # Play Fair button
        self.ui.pushButton_7.clicked.connect(self.open_transposition)  # Transposition button
        self.ui.pushButton_8.clicked.connect(self.open_quad)  # Quad M&B button
        self.ui.pushButton_4.clicked.connect(self.open_substitution)  # Substitution button

    def open_root13(self):
        self.root13_screen = CipherApp(self)
        self.root13_screen.show()
        self.hide()

    def open_caesar(self):
        self.caesar_screen = CaesarScreen(self)
        self.caesar_screen.show()
        self.hide()

    def open_hill(self):
        self.hill_screen = HillScreen(self)
        self.hill_screen.show()
        self.hide()

    def open_playfair(self):
        self.playfair_screen = PlayFairScreen(self)
        self.playfair_screen.show()
        self.hide()

    def open_transposition(self):
        self.transposition_screen = TranspositionScreen(self)
        self.transposition_screen.show()
        self.hide()

    def open_quad(self):
        self.quad_screen = QuadScreen(self)
        self.quad_screen.show()
        self.hide()

    def open_substitution(self):
        self.substitution_screen = SubstitutionScreen(self)
        self.substitution_screen.show()
        self.hide()

class CipherApp(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = ROOT13Ui()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("G:/CyberTest/New folder/smart-lock.png"))
        self.ui.pushButton_6.clicked.connect(self.back_to_home)

    def back_to_home(self):
        if self.parent:
            self.parent.show()
        self.close()

class CaesarScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = caesarUi()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("G:/CyberTest/New folder/smart-lock.png"))
        self.ui.pushButton_6.clicked.connect(self.back_to_home)

    def back_to_home(self):
        if self.parent:
            self.parent.show()
        self.close()

class HillScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = HillUi()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("G:/CyberTest/New folder/smart-lock.png"))
        self.ui.pushButton_6.clicked.connect(self.back_to_home)

    def back_to_home(self):
        if self.parent:
            self.parent.show()
        self.close()

class PlayFairScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = PlayFairUi()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("G:/CyberTest/New folder/smart-lock.png"))
        self.ui.pushButton_6.clicked.connect(self.back_to_home)

    def back_to_home(self):
        if self.parent:
            self.parent.show()
        self.close()

class TranspositionScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = TransUi()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("G:/CyberTest/New folder/smart-lock.png"))
        self.ui.pushButton_6.clicked.connect(self.back_to_home)

    def back_to_home(self):
        if self.parent:
            self.parent.show()
        self.close()

class QuadScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = QuadUi()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("G:/CyberTest/New folder/smart-lock.png"))
        self.ui.pushButton_6.clicked.connect(self.back_to_home)

    def back_to_home(self):
        if self.parent:
            self.parent.show()
        self.close()

class SubstitutionScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.ui = SubstitutionUi()
        self.ui.setupUi(self)
        # self.setWindowIcon(QIcon("G:/CyberTest/New folder/smart-lock.png"))
        self.ui.pushButton_6.clicked.connect(self.back_to_home)

    def back_to_home(self):
        if self.parent:
            self.parent.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_screen = HomeScreen()
    home_screen.show()
    sys.exit(app.exec())