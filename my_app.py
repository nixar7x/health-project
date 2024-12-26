from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from inst import *
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(win_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.hello_text = QLabel()
        self.instruction = QLabel()
        self.button = QPushButton()
        self.layout = QVBoxLayout()
        self.hello_text.addWidget(self.layout)
        self.instruction.addWidget(self.layout)
        self.button.addwidget(self.layout,alignment=Qt.AlignCenter)
    def connects(self):
        self.button.clicked.connect(self.next_click)
    def show(self):
        self.show()
    def next_click(self):
        self.hide()
        self.sw=TestWin()
        self.sw.show()