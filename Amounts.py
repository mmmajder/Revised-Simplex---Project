from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton

from stylesheet import *


class Amounts(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setup()
        self.show()

    def setup(self):
        self.setup_general()
        self.setup_button()
        self.setup_data()

    def setup_general(self):
        self.setFixedSize(600, 900)
        self.setStyleSheet(GENERAL_STYLE_SHEET)
        self.setWindowTitle("Amounts")
        #self.setPalette(get_palette("calories_calculator.jpg"))
        self.setWindowIcon(get_icon())

    def setup_button(self):
        self.calculate = QPushButton("CALCULATE", self)
        self.calculate.setGeometry(QtCore.QRect(250, 450, 300, 60))
        self.calculate.setStyleSheet(BUTTON_STYLE_SHEET)
