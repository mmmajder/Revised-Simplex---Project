from PyQt5.QtWidgets import QWidget, QPushButton, QTableWidget, \
    QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView


def get_dishes(file_name):
    dishes = []
    file = open(file_name)
    for line in file.readlines():
        dishes.append(line.rstrip().split('|'))
    file.close()
    return dishes


def save_dishes(file_name, dishes):
    file = open(file_name, 'w')
    for dish in dishes:
        file.write(dish.join('|'))
    file.close()


class Dish_Table(QTableWidget):
    def __init__(self):
        super().__init__(1, 8)
        self.setHorizontalHeaderLabels(
            ["Name", "Calories(kcal)", "Proteins(%)", "Carbs(%)", "Fats(%)", "Min Amount(g)", "Max Amount(g)", "Price(€)"])
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
        for item in get_dishes("material/dishes.txt"):
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
        #self.add_dishes()
        self.removeRow(0)

    def _addRow(self):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

    def _save(self):
        dishes = []

    def add_dishes(self):
        rowPosition = self.rowCount()
        self.insertRow(rowPosition)
        for item in get_dishes("material/dishes.txt"):
            for i in range(8):
                self.setItem(rowPosition, i, QTableWidgetItem(item[i]))
            rowPosition = self.rowCount()
            self.insertRow(rowPosition)
        self.removeRow(self.rowCount() - 1)


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 600)

        mainLayout = QHBoxLayout()
        table = Dish_Table()
        mainLayout.addWidget(table)
        buttonLayout = QVBoxLayout()
        mainLayout.addStretch(1)

        button_new = QPushButton('New')
        button_new.clicked.connect(table._addRow)
        buttonLayout.addWidget(button_new)

        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)

#
# app = QApplication(sys.argv)
# app.setStyleSheet('QPushButton{font-size: 20px; width: 200px; height: 50px}')
# demo = AppDemo()
# demo.show()
# sys.exit(app.exec_())
