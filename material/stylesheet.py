from PyQt5 import QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QBrush, QPalette, QImage, QIcon

TITLE_STYLE_SHEET = "color: #018673; font-size: 30px; padding-bottom: 10px; font-family: Arial, Helvetica, sans-serif; font-style: bold;"
LABEL_STYLE_SHEET = "color: #018673; font-size: 22px; padding-bottom: 10px; font-family: Arial, Helvetica, sans-serif;"
BUTTON_STYLE_SHEET = "background-color: #018673; border: none; color: white; font-weight: bold; padding: 15px 32px;" \
                     "text-align: center; text-decoration: none; display: inline-block; font-size: 20px; margin: 4px 2px; cursor: pointer"
COMBOBOX_STYLE_SHEET = "background: #ffffff; border: 1px solid #dfdfdf;"
ICON_PATH = "diet.png"
TABLE_STYLE_SHEET = "border: 1px solid #ddd; text-align: left; border-collapse: collapse; width: 100%; padding: 15px;"
GROUP_BOX_STYLE_SHEET = "background-color: #ffffff;"
GENERAL_STYLE_SHEET = "color: #018673; font-size: 22px;"


def get_palette(background):
    o_image = QImage(background)
    s_image = o_image.scaled(QSize(600, 900))
    palette = QPalette()
    palette.setBrush(QPalette.Window, QBrush(s_image))
    return palette


def get_icon():
    icon = QIcon()
    icon.addPixmap(QtGui.QPixmap(ICON_PATH), QtGui.QIcon.Selected, QtGui.QIcon.On)
    return icon
