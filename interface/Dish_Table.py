from PyQt5.QtWidgets import QTableWidget, \
    QTableWidgetItem, QHeaderView

from calculating_functions import get_string_dishes


class Dish_Table(QTableWidget):
    def __init__(self):
        super().__init__(1, 8)
        self.setHorizontalHeaderLabels(
            ["Name", "Calories(kcal)", "Proteins(%)", "Carbs(%)", "Fats(%)", "Min Amount(g)", "Max Amount(g)",
             "Price(€)"])
        self.horizontalHeader().setDefaultSectionSize(160)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.add_dishes()
        self.removeRow(0)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

    def add_dishes(self):
        rowPosition = self.rowCount()
        self.insertRow(rowPosition)
        for item in get_string_dishes("material/dishes.txt"):
            for i in range(8):
                self.setItem(rowPosition, i, QTableWidgetItem(item[i]))
            rowPosition = self.rowCount()
            self.insertRow(rowPosition)
        self.removeRow(self.rowCount() - 1)


class Dish_Amount(QTableWidget):
    def __init__(self):
        super().__init__(1, 7)
        self.setHorizontalHeaderLabels(
            ["Name", "Calories(kcal)", "Proteins(g)", "Carbs(g)", "Fats(g)", "Amount(g)", "Price(€)"])
        self.horizontalHeader().setDefaultSectionSize(160)
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.removeRow(0)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

    def _save(self):
        dishes = []

