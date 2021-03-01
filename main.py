import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import math


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner

        self.primer = ''
        self.btn1.clicked.connect(self.zapis)
        self.btn2.clicked.connect(self.zapis1)
        self.btn3.clicked.connect(self.zapis2)
        self.btn4.clicked.connect(self.zapis3)
        self.btn5.clicked.connect(self.zapis4)
        self.btn6.clicked.connect(self.zapis5)
        self.btn7.clicked.connect(self.zapis6)
        self.btn8.clicked.connect(self.zapis7)
        self.btn9.clicked.connect(self.zapis8)
        self.btn0.clicked.connect(self.zapis0)
        self.btn_plus.clicked.connect(self.zapis11)
        self.btn_minus.clicked.connect(self.zapis12)
        self.btn_mult.clicked.connect(self.zapis13)
        self.btn_div.clicked.connect(self.zapis14)
        self.btn_pow.clicked.connect(self.zapis15)
        self.btn_fact.clicked.connect(self.zapis16)
        self.btn_sqrt.clicked.connect(self.zapis17)
        self.btn_dot.clicked.connect(self.zapis18)
        self.btn_clear.clicked.connect(self.zapis19)
        self.btn_eq.clicked.connect(self.zapis20)

    def zapis(self):
        self.primer += '1'
        self.table.display(self.primer)

    def zapis1(self):
        self.primer += '2'
        self.table.display(self.primer)

    def zapis2(self):
        self.primer += '3'
        self.table.display(self.primer)

    def zapis3(self):
        self.primer += '4'
        self.table.display(self.primer)

    def zapis4(self):
        self.primer += '5'
        self.table.display(self.primer)

    def zapis5(self):
        self.primer += '6'
        self.table.display(self.primer)

    def zapis6(self):
        self.primer += '7'
        self.table.display(self.primer)

    def zapis7(self):
        self.primer += '8'
        self.table.display(self.primer)

    def zapis8(self):
        self.primer += '9'
        self.table.display(self.primer)

    def zapis0(self):
        self.primer += '0'
        self.table.display(self.primer)

    def zapis11(self):
        self.primer += '+'
        self.table.display('plus')

    def zapis12(self):
        self.primer += '-'
        self.table.display('minus')

    def zapis13(self):
        self.primer += '*'
        self.table.display('mult')

    def zapis14(self):
        self.primer += '/'
        self.table.display('div')

    def zapis15(self):
        self.primer += '**'
        self.table.display('pov')

    def zapis16(self):
        self.table.display(math.factorial(int(self.primer)))
        self.primer = ''

    def zapis17(self):
        self.primer += ' ** 0.5'
        print(self.primer)
        self.table.display(eval(self.primer))
        self.primer = ''

    def zapis18(self):
        self.primer += '.'
        self.table.display(self.primer)

    def zapis19(self):
        self.primer = ''
        self.table.display(self.primer)

    def zapis20(self):
        self.table.display(eval(self.primer))
        self.primer = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
