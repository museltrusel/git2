import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        super().__init__()
        uic.loadUi('miniplanir.ui', self)
        self.get_zapis.clicked.connect(self.zapis)
        self.sp = list()


    def zapis(self):
        date = self.calendarWidget.selectedDate().toString('yyyy.M.d ')
        time = self.time.dateTime().toString('h:m')
        self.sp.append(f'{date}{time} - {self.t1.text()}')
        self.listic.clear()
        self.sp.sort()
        for text in self.sp:
            self.listic.addItem(text)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
