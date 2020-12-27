from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

from calculating_functions import get_nutrient_range_string
from interface.Dish_Table import Dish_Amount, Dish_Table
from material.stylesheet import *


class Amounts(QWidget):
    def __init__(self, nutrient_range):
        QWidget.__init__(self)
        self.setup(nutrient_range)
        self.show()

    def setup(self, nutrient_range):
        self.setFixedSize(1700, 800)
        self.setStyleSheet(GENERAL_STYLE_SHEET)
        self.setWindowTitle("Calculate Amounts of Dishes")
        self.setWindowIcon(get_icon())

        main_layout = QVBoxLayout()

        daily_needs_label = QLabel("After calculating your daily needs, we recommend you consume: ")
        daily_needs_label.setStyleSheet(LABEL_STYLE_SHEET)
        main_layout.addWidget(daily_needs_label)

        daily_needs = QLabel(get_nutrient_range_string(nutrient_range))
        daily_needs.setStyleSheet(TITLE_STYLE_SHEET)
        main_layout.addWidget(daily_needs)

        label_select_dishes = QLabel("Select dishes you want to eat today: ")
        label_select_dishes.setStyleSheet(LABEL_STYLE_SHEET)
        main_layout.addWidget(label_select_dishes)

        table_layout = QHBoxLayout()

        self.table = Dish_Table()
        table_layout.addWidget(self.table)

        buttonLayout = QVBoxLayout()

        self.select = QPushButton('Select Dish')
        self.select.setStyleSheet(BUTTON_STYLE_SHEET)
        buttonLayout.addWidget(self.select)

        button_new = QPushButton('Add New Dish')
        button_new.setStyleSheet(BUTTON_STYLE_SHEET)
        button_new.clicked.connect(self.table._addRow)
        buttonLayout.addWidget(button_new)

        self.save_changes = QPushButton('Save changes')
        self.save_changes.setStyleSheet(BUTTON_STYLE_SHEET)
        buttonLayout.addWidget(self.save_changes)

        table_layout.addLayout(buttonLayout)

        self.button_calculate = QPushButton('CALCULATE')
        self.button_calculate.setStyleSheet(BUTTON_STYLE_SHEET)
        buttonLayout.addWidget(self.button_calculate)

        main_layout.addLayout(table_layout)

        label_select_dishes = QLabel("Amount of dishes you should eat today: ")
        label_select_dishes.setStyleSheet(LABEL_STYLE_SHEET)
        main_layout.addWidget(label_select_dishes)

        self.dish_amount_table = Dish_Amount()
        main_layout.addWidget(self.dish_amount_table)

        self.total = QLabel("Total price: 0€")
        self.total.setStyleSheet(TITLE_STYLE_SHEET)
        self.total.setAlignment(QtCore.Qt.AlignRight)
        main_layout.addWidget(self.total)

        self.setLayout(main_layout)
