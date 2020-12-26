import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem

from calculating_functions import get_dishes, save_dishes, get_dish
from interface.Amounts import Amounts


class Amounts_GUI(QtWidgets.QWidget):
    def __init__(self, nutrient_range, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Amounts(nutrient_range)
        self.ui.select.clicked.connect(self.selected)
        self.ui.save_changes.clicked.connect(self.save_changes_to_file)

    def error(self, text):
        QtWidgets.QMessageBox.question(self, 'Error', text,
                                       QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def selected(self):
        current_row = self.ui.table.currentRow()
        if current_row >= len(get_dishes("material/dishes.txt")):
            self.error("You have to save changes first.")
        else:
            rowCount = self.ui.dish_amount_table.rowCount()
            self.ui.dish_amount_table.insertRow(rowCount)
            self.ui.dish_amount_table.setItem(rowCount, 0, QTableWidgetItem(self.ui.table.item(current_row, 0)))
            for i in range(1, 7):
                self.ui.dish_amount_table.setItem(rowCount, i, QTableWidgetItem('-'))

    def save_changes_to_file(self):
        dishes = []
        rowCount = self.ui.table.rowCount()
        for i in range(rowCount):
            if self.check_row(i):
                dishes.append(get_dish(self.ui.table.item(i, 0).text()))
            else:
                self.error("Error in the row " + str(i) + ".")
                return
        save_dishes("material/dishes.txt", dishes)

    def check_row(self, row):
        if self.ui.table.item(row, 0).text().strip() == "":
            self.error("You have to enter the name of the dish at row" + str(row) + ".")
        try:
            x = float(self.ui.table.item(row, 1).text())
        except:
            self.error("You have to enter the double value.")


def start_amount(nutrient_range):
    app = QApplication(sys.argv)
    cal = Amounts_GUI(nutrient_range)
    cal.raise_()
    cal.activateWindow()
    app.exec_()
