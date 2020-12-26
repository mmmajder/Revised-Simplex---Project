from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

from Dish_Table import Dish_Table, Dish_Amount
from stylesheet import *

calories, proteins, fats, carbs = 2400, 65, 45, 200


class Amounts(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setup()
        self.show()

    def setup(self):
        self.setFixedSize(1700, 800)
        self.setStyleSheet(GENERAL_STYLE_SHEET)
        self.setWindowTitle("Calculate Amounts of Dishes")
        self.setWindowIcon(get_icon())

        main_layout = QVBoxLayout()

        daily_needs_label = QLabel("After calculating your daily needs, we recommend you consume: ")
        daily_needs_label.setStyleSheet(LABEL_STYLE_SHEET)
        main_layout.addWidget(daily_needs_label)

        daily_needs = QLabel("Calories: " + str(calories) + "kcal\tProteins: " + str(proteins) + "g\tCarbs: " + str(
            carbs) + "g\tFats: " + str(fats) + "g")
        daily_needs.setStyleSheet(TITLE_STYLE_SHEET)
        main_layout.addWidget(daily_needs)

        label_select_dishes = QLabel("Select dishes you want to eat today: ")
        label_select_dishes.setStyleSheet(LABEL_STYLE_SHEET)
        main_layout.addWidget(label_select_dishes)

        table_layout = QHBoxLayout()
        table = Dish_Table()
        table_layout.addWidget(table)
        buttonLayout = QVBoxLayout()
        select = QPushButton('Select Dish')
        select.setStyleSheet(BUTTON_STYLE_SHEET)
        select.clicked.connect(table._addRow)
        buttonLayout.addWidget(select)
        button_new = QPushButton('Add New Dish')
        button_new.setStyleSheet(BUTTON_STYLE_SHEET)
        button_new.clicked.connect(table._addRow)
        buttonLayout.addWidget(button_new)
        save_changes = QPushButton('Save changes')
        save_changes.setStyleSheet(BUTTON_STYLE_SHEET)
        save_changes.clicked.connect(table._addRow)
        buttonLayout.addWidget(save_changes)
        table_layout.addLayout(buttonLayout)
        button_calculate = QPushButton('CALCULATE')
        button_calculate.setStyleSheet(BUTTON_STYLE_SHEET)
        # button_calculate.clicked.connect(table._addRow)
        buttonLayout.addWidget(button_calculate)
        main_layout.addLayout(table_layout)
        label_select_dishes = QLabel("Amount of dishes you should eat today: ")
        label_select_dishes.setStyleSheet(LABEL_STYLE_SHEET)
        main_layout.addWidget(label_select_dishes)
        table2 = Dish_Amount()
        main_layout.addWidget(table2)
        total = QLabel("Total price: 0€")
        total.setStyleSheet(TITLE_STYLE_SHEET)
        total.setAlignment(QtCore.Qt.AlignRight)
        main_layout.addWidget(total)
        self.setLayout(main_layout)
