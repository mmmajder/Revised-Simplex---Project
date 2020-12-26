import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from calculating_functions import calculate_calories
from interface.calculator import Calculator


class Calculator_GUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
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
        # start_amount()
        print(calculate_calories(age, gender, height, weight, activity, goal))


def start_calculator():
    app = QApplication(sys.argv)
    cal = Calculator_GUI()
    cal.raise_()
    cal.activateWindow()
    app.exec_()
