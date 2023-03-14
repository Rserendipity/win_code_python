from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)
import sys


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setFixedSize(600, 800)
        btn1 = QPushButton('这是第一个按键', self)
        btn2 = QPushButton('这是第二个按键', self)
        btn1.move(300, 400)
        btn1.senderSignalIndex()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    app.exec_()
