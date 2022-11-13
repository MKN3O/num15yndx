import sys, time, datetime

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
            time.sleep(0.01)
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
        self.loginpage = BogomolBankLogin()
        self.loginpage.show()
        self.hide()


class BogomolBankAdmin(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('AdminPage.ui', self)
        self.userInfo.clicked.connect(self.uinfo)
        self.connection = sqlite3.connect("bank_db.sqlite")
        self.creditList.clicked.connect(self.crinfo)
        self.depositList.clicked.connect(self.dpinfo)

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

    def crinfo(self):
        res = self.connection.cursor().execute("""SELECT * FROM credits""").fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'id пользователя', 'Дата начала',
                                                    'Сумма, руб.', 'Процент', 'Лет, длительность'])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def dpinfo(self):
        res = self.connection.cursor().execute("""SELECT * FROM deposits""").fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'id пользователя', 'Дата начала',
                                                    'Сумма, руб.', 'Процент', 'Лет, длительность'])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


class BogomolBankLogin(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('LoginPage.ui', self)
        self.loginbutton.clicked.connect(self.login_process)

    def login_process(self):
        self.name = (self.surnameline.text())
        con = sqlite3.connect("bank_db.sqlite")
        cur = con.cursor()
        if self.name not in cur.execute('''SELECT username FROM users''').fetchall()[0]:
            cur.execute(f"""INSERT INTO users(username,birthdate,passportns, creditid, depositid)
            VALUES('{self.surnameline.text()}','{self.birthdayline.text()}','{self.passportline.text()}','No', 'No')""")
            con.commit()
        self.clientpage = BogomolBankClient(self.name)
        self.clientpage.show()
        self.hide()


class BogomolBankClient(QDialog):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('ClientPage.ui', self)
        self.name = name
        self.label_2.setText(name)
        self.accountbutton.clicked.connect(self.account)
        self.creditbutton.clicked.connect(self.credit_making)
        self.depositbutton.clicked.connect(self.deposit_making)
        self.creditList.clicked.connect(self.creditlst)
        self.depositList.clicked.connect(self.depositlst)

    def account(self):
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT * FROM users
                                      WHERE username = '{self.name}'""").fetchall()

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setVerticalHeaderLabels(['Пользователь'])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def credit_making(self):
        self.creditpage = BogomolBankCredit(self.name)
        self.creditpage.show()
        self.hide()

    def deposit_making(self):
        self.depositpage = BogomolBankDeposit(self.name)
        self.depositpage.show()
        self.hide()

    def creditlst(self):
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT * FROM credits
                                            WHERE user_id in 
                                            (SELECT id FROM users
                                            WHERE username = '{self.name}')""").fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'ваш id', 'Дата начала', 'Сумма, рублей',
                                                    'Процент', 'Продолжительность, лет'])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def depositlst(self):
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT * FROM deposits
                                                    WHERE user_id in 
                                                    (SELECT id FROM users
                                                    WHERE username = '{self.name}')""").fetchall()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'ваш id', 'Дата начала', 'Сумма, рублей',
                                                    'Процент', 'Продолжительность, лет'])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()


class BogomolBankCredit(QDialog):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('CreditPage.ui', self)
        self.pushButton.clicked.connect(self.credit_save)
        self.name = name

    def credit_save(self):
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT id FROM users
                                   WHERE username = '{self.name}'""").fetchall()[0][0]
        cur = con.cursor()
        data = datetime.date.today().strftime(('%d.%m.%Y'))
        percent = 10
        cur.execute(f"""INSERT INTO credits(user_id,startdate,summa,percent,years)
        VALUES('{res}','{data}','{self.sumline.text()}','{percent}', '{self.lengthline.text()}')""")
        con.commit()

class BogomolBankDeposit(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('DepositPage.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BogomolBankBegin()
    ex.show()
    sys.exit(app.exec())