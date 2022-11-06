import sys, time

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog


class BogomolBankBegin(QDialog):  # Стартовая страница
    def __init__(self):
        super().__init__()
        uic.loadUi('StartPage.ui', self)
        self.startButton.clicked.connect(self.start_process)

    def start_process(self):
        for i in range(101):
            time.sleep(0.05)
            self.progressBar.setValue(i)
        self.registerpage = BogomolBankRegister()  # Появление переменной в которой хранится класс для его появления
        self.registerpage.show()
        self.hide()  # Закрытие стартовой страницы



class BogomolBankRegister(QDialog):  # Страница выбора режима
    def __init__(self):
        super().__init__()
        uic.loadUi('RegisterPage.ui', self)
        self.userButton.clicked.connect(self.user)
        self.adminButton.clicked.connect(self.admin)

    def admin(self):
        self.adminpage = BogomolBankAdmin()
        self.adminpage.show()
        self.hide()

    def user(self):
        pass


class BogomolBankAdmin(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('AdminPage.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BogomolBankBegin()
    ex.show()
    sys.exit(app.exec())