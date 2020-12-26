import sys

from PyQt5.QtWidgets import *

from calculating_functions import nutrient_range
from classes.Nutrients import Nutrients
from interface.calculator import Calculator

NUTRIENT_RANGE = Nutrients(0, 0, 0, 0, 0, 0, 0)


class Calculator_GUI(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Calculator()
        self.ui.calculate.clicked.connect(self.open_new_window)

    def open_new_window(self):
        age = int(self.ui.age.currentText())
        gender = "female"
        if self.ui.male.isChecked():
            gender = "male"
        height = int(self.ui.height.currentText().replace(" cm", ""))
        weight = int(self.ui.weight.currentText().replace(" kg", ""))
        activity = self.ui.activity.currentIndex()
        goal = self.ui.goal.currentIndex()
        global NUTRIENT_RANGE
        NUTRIENT_RANGE = nutrient_range(age, gender, height, weight, activity, goal)
        self.ui.close()


def start_calculator():
    app = QApplication(sys.argv)
    cal = Calculator_GUI()
    cal.raise_()
    cal.activateWindow()
    app.exec_()
    return NUTRIENT_RANGE
