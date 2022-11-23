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
        res = self.connection.cursor().execute("""SELECT summa FROM credits""").fetchall()
        res1 = self.connection.cursor().execute("""SELECT summa FROM deposits""").fetchall()
        dps = 0
        crs = 0
        for i in res:
            for j in i:
                dps += float(j)
        for i in res1:
            for j in i:
                crs += float(j)
        self.creditList.clicked.connect(self.crinfo)
        self.depositList.clicked.connect(self.dpinfo)
        self.depositSum.setText(f'{str(dps)} - сумма депозитов')
        self.creditSum.setText(f'{str(crs)} - сумма кредитов')

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
        self.tableWidget.itemChanged.connect(self.chgn)
        self.clmns = {1: 'UserName', 2: 'birthdate', 3: 'passportns'}
        con = sqlite3.connect("bank_db.sqlite")
        self.id = con.cursor().execute(f"""SELECT id FROM users
                                      WHERE username = '{self.name}'""").fetchall()[0][0]

    def account(self):
        self.changeable = True
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT * FROM users
                                      WHERE id = '{self.id}'""").fetchall()

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
        self.changeable = False
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT * FROM credits
                                            WHERE user_id =
                                            '{self.id}'""").fetchall()
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
        self.changeable = False
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT * FROM deposits
                                                    WHERE user_id =
                                                    '{self.id}'""").fetchall()
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


    def chgn(self, item):
        if int(item.column()) != 5 and int(item.column()) != 4 and int(item.column()) != 0 and self.changeable:
            con = sqlite3.connect("bank_db.sqlite")
            con.cursor().execute(f"""UPDATE users
                                  SET {self.clmns[item.column()]} = '{str(item.text())}'
                                  WHERE id = '{self.id}'""")
            if item.column() == 1:
                self.name = item.text()
            con.commit()


class BogomolBankCredit(QDialog):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('CreditPage.ui', self)
        self.pushButton.clicked.connect(self.credit_save)
        self.name = name

    def credit_save(self):
        self.sumcredit = str(self.sumline.text())
        self.longcredit = str(self.lengthline.text())
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT id FROM users
                                   WHERE username = '{self.name}'""").fetchall()[0][0]
        cur = con.cursor()
        data = datetime.date.today().strftime(('%d.%m.%Y'))
        percent = 10
        cur.execute(f"""INSERT INTO credits(user_id,startdate,summa,percent,years)
        VALUES('{res}','{data}','{self.sumline.text()}','{percent}', '{self.lengthline.text()}')""")
        cur.execute(f"""UPDATE users SET creditid = 'Yes' WHERE username = '{self.name}'""")
        con.commit()
        self.thankscredit = BogomolBankThanksCredit(self.sumcredit, self.longcredit)
        self.thankscredit.show()
        self.hide()

class BogomolBankDeposit(QDialog):
    def __init__(self, name):
        super().__init__()
        uic.loadUi('DepositPage.ui', self)
        self.pushButton.clicked.connect(self.deposit_save)
        self.name = name

    def deposit_save(self):
        self.sumdeposit = str(self.sumline.text())
        self.longdeposit = str(self.lengthline.text())
        con = sqlite3.connect("bank_db.sqlite")
        res = con.cursor().execute(f"""SELECT id FROM users
                                           WHERE username = '{self.name}'""").fetchall()[0][0]
        cur = con.cursor()
        data = datetime.date.today().strftime(('%d.%m.%Y'))
        percent = 7
        cur.execute(f"""INSERT INTO deposits(user_id,startdate,summa,percent,years)
                VALUES('{res}','{data}','{self.sumline.text()}','{percent}', '{self.lengthline.text()}')""")
        cur.execute(f"""UPDATE users SET depositid = 'Yes' WHERE username = '{self.name}'""")
        con.commit()
        self.thanksdeposit = BogomolBankThanksDeposit(self.sumdeposit, self.longdeposit)
        self.thanksdeposit.show()
        self.hide()


class BogomolBankThanksCredit(QDialog):
    def __init__(self, sumcredit, longcredit):
        super().__init__()
        uic.loadUi('ThanksCreditPage.ui', self)
        self.finalsum = sumcredit
        self.finallong = longcredit
        debt = round((int(sumcredit) * (1.1 ** int(longcredit))))
        monthly = debt // (int(longcredit) * 12)
        self.summaline.setText(str(self.finalsum))
        self.longline.setText(str(self.finallong))
        self.debtline.setText(str(debt))
        self.monthpayline.setText(str(monthly))
        self.acceptButton.clicked.connect(self.turnback)

    def turnback(self):
        self.turningback = BogomolBankRegister()
        self.turningback.show()



class BogomolBankThanksDeposit(QDialog):
    def __init__(self, sumdeposit, longdeposit):
        super().__init__()
        uic.loadUi('ThanksDepositPage.ui', self)
        self.finalsum = sumdeposit
        self.finallong = longdeposit
        profit = round((int(sumdeposit) * (1.07 ** int(longdeposit))))
        monthly = profit // (int(longdeposit) * 12)
        self.summaline.setText(str(self.finalsum))
        self.longline.setText(str(self.finallong))
        self.profitline.setText(str(profit))
        self.monthprofitline.setText(str(monthly))
        self.backbutton.clicked.connect(self.turnback)

    def turnback(self):
        self.turningback = BogomolBankRegister()
        self.turningback.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BogomolBankBegin()
    ex.show()
    sys.exit(app.exec())
