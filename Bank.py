import sys, time

import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog, QTableWidgetItem


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
        self.userInfo.clicked.connect(self.uinfo)
        self.connection = sqlite3.connect("bank_db.sqlite")

    def uinfo(self):
        res = self.connection.cursor().execute("""SELECT * FROM users""").fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'ФИО', 'Дата рождения',
                                                  'Серия и номер паспорта', 'id кредита', 'id вклада'])
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BogomolBankBegin()
    ex.show()
    sys.exit(app.exec())