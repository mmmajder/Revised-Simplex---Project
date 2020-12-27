from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QComboBox, QRadioButton

from calculating_functions import list_of_strings_in_range, get_activities, get_goals
from material.stylesheet import *


class Calculator(QWidget):
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
        self.setWindowTitle("Calories Calculator")
        self.setPalette(get_palette("material/calories_calculator.jpg"))
        self.setWindowIcon(get_icon())

    def setup_button(self):
        self.calculate = QPushButton("CALCULATE", self)
        self.calculate.setGeometry(QtCore.QRect(250, 450, 300, 60))
        self.calculate.setStyleSheet(BUTTON_STYLE_SHEET)

    def setup_data(self):
        start = 250
        x = 130
        y = 50
        d = 40
        self.age = QComboBox(self)
        self.age.setGeometry(QtCore.QRect(start, x, 300, d))
        self.age.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.age.addItems(list_of_strings_in_range(15, 80, ""))
        self.age.setCurrentIndex(10)

        self.male = QRadioButton(self)
        self.male.setText("male")
        self.male.setStyleSheet(LABEL_STYLE_SHEET)
        self.male.setChecked(True)
        self.male.setGeometry(QtCore.QRect(start, x + y + 5, 300, d))

        self.female = QRadioButton(self)
        self.female.setText("female")
        self.female.setStyleSheet(LABEL_STYLE_SHEET)
        self.female.setGeometry(QtCore.QRect(start + 100, x + y + 5, 300, d))

        self.height = QComboBox(self)
        self.height.setGeometry(QtCore.QRect(start, x + 2 * y, 300, d))
        self.height.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.height.addItems(list_of_strings_in_range(150, 210, " cm"))
        self.height.setCurrentIndex(20)

        self.weight = QComboBox(self)
        self.weight.setGeometry(QtCore.QRect(250, x + 3 * y, 300, d))
        self.weight.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.weight.addItems(list_of_strings_in_range(10, 200, " kg"))
        self.weight.setCurrentIndex(45)

        self.activity = QComboBox(self)
        self.activity.setGeometry(QtCore.QRect(start, x + 4 * y, 300, d))
        self.activity.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.activity.addItems(get_activities())
        self.activity.setCurrentIndex(1)

        self.goal = QComboBox(self)
        self.goal.setGeometry(QtCore.QRect(start, x + 5 * y, 300, d))
        self.goal.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.goal.addItems(get_goals())
