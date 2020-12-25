from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QComboBox, QRadioButton
from stylesheet import *

goals = ['lose weigth', 'gain weigth', 'gain muscle']
activities = ['little or no exercise',
              'light: 1-3 trainings a week',
              'moderate: 4-5 trainings a week',
              'active: 6-7 trainings a week',
              'very active: intense trainings 6-7 times a week']
ages = []
for i in range(2, 100):
    ages.append(str(i))


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
        self.setPalette(get_palette("calories_calculator.jpg"))
        self.setWindowIcon(get_icon())

    def setup_button(self):
        self.calculate = QPushButton("calculate", self)
        self.calculate.setGeometry(QtCore.QRect(250, 480, 300, 60))
        self.calculate.setStyleSheet(BUTTON_STYLE_SHEET)

    def setup_data(self):
        self.age = QComboBox(self)
        self.age.setGeometry(QtCore.QRect(430, 620, 700, 30))
        self.age.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.age.addItems(ages)

        self.male = QRadioButton(self)
        self.male.setGeometry(QtCore.QRect(430, 620, 700, 30))

        self.female = QRadioButton(self)
        self.female.setGeometry(QtCore.QRect(430, 620, 700, 30))

        self.height = QComboBox(self)
        self.height.setGeometry(QtCore.QRect(430, 620, 700, 30))
        self.height.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.height.addItems(range(150, 210))

        self.weight = QComboBox(self)
        self.weight.setGeometry(QtCore.QRect(430, 620, 700, 30))
        self.weight.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.weight.addItems(range(10, 200))

        self.goal = QComboBox(self)
        self.goal.setGeometry(QtCore.QRect(430, 620, 700, 30))
        self.goal.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.goal.addItems(goals)

        self.activity = QComboBox(self)
        self.activity.setGeometry(QtCore.QRect(430, 620, 700, 30))
        self.activity.setStyleSheet(COMBOBOX_STYLE_SHEET)
        self.activity.addItems(activities)