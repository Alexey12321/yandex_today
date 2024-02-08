from PyQt5 import QMainWindow, QPixmap, uic
import requests
import sys


class Triple(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)