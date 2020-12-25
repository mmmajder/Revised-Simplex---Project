from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication
from calculator import *


class Calculator_GUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Calculator()
#        self.ui.kalendar.selectionChanged.connect(self.update_na_promenu_kalendar)
 #       self.ui.spisak_pregleda_za_oznacen_dan.currentTextChanged.connect(self.update_o_pacijentu)

    # def update_na_promenu_kalendar(self):
    #     selektovan_datum = self.ui.kalendar.selectedDate().toString('dd.MM.yyyy.')
    #     self.update_labela_pregledi(selektovan_datum)
    #     lista_obaveza = get_lista_obaveza_za_trenutnog_lekara_po_datumu(selektovan_datum)
    #     self.update_spisak_pregleda_za_oznacen_dan(lista_obaveza)
    #
    # def update_spisak_pregleda_za_oznacen_dan(self, lista_obaveza):
    #     self.ui.spisak_pregleda_za_oznacen_dan.clear()
    #     self.ui.spisak_pregleda_za_oznacen_dan.addItems(get_liste_obaveza(lista_obaveza))
    #
    # def update_labela_pregledi(self, selektovan_datum):
    #     self.ui.labela_pregledi.clear()
    #     self.ui.labela_pregledi.setText("Spisak svih Vaših obaveza datuma " + selektovan_datum + "")
    #
    # def update_o_pacijentu(self):
    #     self.ui.tabela_pacijent.clear()
    #     pregled = self.ui.spisak_pregleda_za_oznacen_dan.currentText()
    #     if pregled:
    #         vrednosti = get_podaci_o_pacijentu(pregled)
    #         for broj_reda in range(5):
    #             self.ui.tabela_pacijent.setItem(broj_reda, 0,
    #                                             QtWidgets.QTableWidgetItem(KLJUCEVI_TABELA_PACIJENT[broj_reda]))
    #             self.ui.tabela_pacijent.setItem(broj_reda, 1, QtWidgets.QTableWidgetItem(vrednosti[broj_reda]))


def start_calculator():
    app = QApplication(sys.argv)
    cal = Calculator_GUI()
    cal.raise_()
    cal.activateWindow()
    app.exec_()