import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from interface.Amounts import Amounts


class Amounts_GUI(QtWidgets.QWidget):
    def __init__(self, nutrient_range, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Amounts(nutrient_range)
#        self.ui.calculate.clicked.connect(self.open_new_window)


def start_amount(nutrient_range):
    app = QApplication(sys.argv)
    cal = Amounts_GUI(nutrient_range)
    cal.raise_()
    cal.activateWindow()
    app.exec_()
