from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests
import sys
import os
from io import BytesIO


class Triple(QMainWindow):
    def __init__(self):
        super().__init__()
        self.spn = 30
        uic.loadUi('design.ui', self)
        self.find.clicked.connect(self.finding)

    def finding(self):
        coords = self.coords.text()
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&spn={self.spn},{self.spn}&l=map"
        response = requests.get(map_request)
        if not response:
            print('ПОКА')
            sys.exit(1)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
        self.pix = QPixmap('map.png')
        self.picture.setPixmap(self.pix)
        os.remove(map_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.spn += 10
            if self.spn >= 90:
                self.spn = 90
            self.finding()
        if event.key() == Qt.Key_PageDown:
            self.spn -= 5
            if self.spn <= 0:
                self.spn = 1
            self.finding()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Triple()
    ex.show()
    sys.exit(app.exec_())

# 133.795393,-25.694776
