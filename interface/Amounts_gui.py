import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem

from calculating_functions import get_dishes, save_dishes, get_dish
from classes.Dish import Dish
from get_data_from_gui import calculate_amounts
from interface.Amounts import Amounts


class Amounts_GUI(QtWidgets.QWidget):
    def __init__(self, nutrient_range, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Amounts(nutrient_range)
        self.nutrient_range = nutrient_range
        self.ui.select.clicked.connect(self.selected)
        self.ui.save_changes.clicked.connect(self.save_changes_to_file)
        self.ui.button_calculate.clicked.connect(self.calculate)

    def error(self, text):
        QtWidgets.QMessageBox.question(self, 'Error', text,
                                       QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

    def selected(self):
        current_row = self.ui.table.currentRow()
        if current_row >= len(get_dishes("material/dishes.txt")):
            self.error("You have to save changes first.")
        else:
            self.add_dish_to_amount_table(current_row)

    def add_dish_to_amount_table(self, current_row):
        rowCount = self.ui.dish_amount_table.rowCount()
        self.ui.dish_amount_table.insertRow(rowCount)
        self.ui.dish_amount_table.setItem(rowCount, 0, QTableWidgetItem(self.ui.table.item(current_row, 0)))
        for i in range(1, 7):
            self.ui.dish_amount_table.setItem(rowCount, i, QTableWidgetItem('-'))

    def save_changes_to_file(self):
        dishes = []
        for row in range(self.ui.table.rowCount()):
            if not self.check_row(row):
                self.error("Error in the row " + str(row + 1) + ".")
                return
            dishes.append(self.get_current_dish(row))
        save_dishes("material/dishes.txt", dishes)

    def get_current_dish(self, i):
        dish = get_dish(self.ui.table.item(i, 0).text())
        if not dish:
            return Dish([self.ui.table.item(i, 0).text(), self.ui.table.item(i, 1).text(),
                         self.ui.table.item(i, 2).text(), self.ui.table.item(i, 3).text(),
                         self.ui.table.item(i, 4).text(), self.ui.table.item(i, 5).text(),
                         self.ui.table.item(i, 6).text(), self.ui.table.item(i, 7).text()])
        return dish

    def check_row(self, row):
        return self.empty_name_check(row) and self.correct_float_values(row) and self.min_and_max_amount_check(row)

    def empty_name_check(self, row):
        if self.ui.table.item(row, 0).text().strip() == "":
            return False
        return True

    def correct_float_values(self, row):
        try:
            for i in range(1, 7):
                x = float(self.ui.table.item(row, i).text())
                if x < 0:
                    return False
            return True
        except:
            return False

    def min_and_max_amount_check(self, row):
        if float(self.ui.table.item(row, 6).text()) < float(self.ui.table.item(row, 5).text()):
            return False
        return True

    def get_selected_dishes(self):
        dishes = []
        for row in range(self.ui.dish_amount_table.rowCount()):
            dishes.append(get_dish(self.ui.dish_amount_table.item(row, 0).text()))
        return dishes

    def calculate(self):
        selected_dishes = self.get_selected_dishes()
        calculate_amounts(selected_dishes, self.nutrient_range)


def start_amount(nutrient_range):
    app = QApplication(sys.argv)
    cal = Amounts_GUI(nutrient_range)
    cal.raise_()
    cal.activateWindow()
    app.exec_()
