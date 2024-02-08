import os
import sys
import requests
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui


class Triple(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('design.ui', self)
        self.find.clicked.connect(self.finding)

    def finding(self):
        coords = self.coords.text()
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&spn=30,30&l=sat"
        response = requests.get(map_request)
        if not response:
            sys.exit(1)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.pix = QtGui.QPixmap('map.png')
        self.picture.setPixmap(self.pix)
        os.remove(map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Triple()
    ex.show()
    sys.exit(app.exec_())
