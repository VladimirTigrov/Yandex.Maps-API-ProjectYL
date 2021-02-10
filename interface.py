from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PIL import Image, ImageQt
from func import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Большая задача по Maps API. Часть №1')
        self.setFixedSize(625, 550)
        mainlayout = QVBoxLayout(self)

        hlayout = QHBoxLayout(self)

        label = QLabel(self)
        label.setText('Координаты: ')
        hlayout.addWidget(label)

        self.coords = QLineEdit(self)
        hlayout.addWidget(self.coords)

        btnCoords = QPushButton('Вывести', self)
        btnCoords.clicked.connect(self.click)
        hlayout.addWidget(btnCoords)

        mainlayout.addLayout(hlayout)

        self.image = QLabel()
        self.image.setPixmap(QPixmap('icon.png'))
        mainlayout.addWidget(self.image)
        self.show()

    def click(self):
        try:
            map_result = get_map(self.coords.text())
            if map_result:
                pixmap = QPixmap()
                pixmap.loadFromData(map_result)
                self.image.setPixmap(pixmap)
        except:
            pass


app = QApplication([])
w = Window()
w.show()
app.exec()
