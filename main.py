import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.setPen(pen)
        ri = randint(100, 250)
        qp.drawEllipse(220, 70, ri, ri)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
