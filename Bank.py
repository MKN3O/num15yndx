import sys, time, datetime

import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 871)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 90, 931, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(420, 360, 201, 101))
        self.startButton.setObjectName("startButton")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(300, 620, 461, 51))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BOGOMOL ONLINE BANK"))
        self.startButton.setText(_translate("Dialog", "НАЧАТЬ РАБОТУ"))


class BogomolBankBegin(QDialog, Ui_Dialog):  # Стартовая страница
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.start_process)

    def start_process(self):
        for i in range(101):
            time.sleep(0.01)
            self.progressBar.setValue(i)
        self.registerpage = BogomolBankRegister()  # Появление переменной в которой хранится класс для его появления
        self.registerpage.show()
        self.hide()  # Закрытие стартовой страницы


class Ui_Page3(object):
    def setupUi(self, Page3):
        Page3.setObjectName("Page3")
        Page3.resize(1134, 871)
        self.label = QtWidgets.QLabel(Page3)
        self.label.setGeometry(QtCore.QRect(90, 90, 931, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Page3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 290, 541, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.adminButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.adminButton.setObjectName("adminButton")
        self.horizontalLayout.addWidget(self.adminButton)
        self.userButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.userButton.setObjectName("userButton")
        self.horizontalLayout.addWidget(self.userButton)
        self.label_2 = QtWidgets.QLabel(Page3)
        self.label_2.setGeometry(QtCore.QRect(400, 230, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Page3)
        QtCore.QMetaObject.connectSlotsByName(Page3)

    def retranslateUi(self, Page3):
        _translate = QtCore.QCoreApplication.translate
        Page3.setWindowTitle(_translate("Page3", "Dialog"))
        self.label.setText(_translate("Page3", "BOGOMOL ONLINE BANK"))
        self.adminButton.setText(_translate("Page3", "Войти как администратор"))
        self.userButton.setText(_translate("Page3", "Войти как клиент"))
        self.label_2.setText(_translate("Page3", "РЕГИСТРАЦИЯ"))



class BogomolBankRegister(QDialog, Ui_Page3):  # Страница выбора режима
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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




class Ui_Dialog_4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 871)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(8, 4, 1101, 831))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.creditList = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.creditList.setObjectName("creditList")
        self.gridLayout.addWidget(self.creditList, 1, 0, 1, 1)
        self.userInfo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.userInfo.setObjectName("userInfo")
        self.gridLayout.addWidget(self.userInfo, 0, 0, 1, 1)
        self.depositList = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.depositList.setObjectName("depositList")
        self.gridLayout.addWidget(self.depositList, 2, 0, 1, 1)
        self.creditSum = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.creditSum.setObjectName("creditSum")
        self.gridLayout.addWidget(self.creditSum, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.depositSum = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.depositSum.setObjectName("depositSum")
        self.gridLayout.addWidget(self.depositSum, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">BOGOMOL ONLINE BANK</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Возможности администратора</p></body></html>"))
        self.creditList.setText(_translate("Dialog", "Вывести список оформленных кредитов"))
        self.userInfo.setText(_translate("Dialog", "Вывести информацию о клиентах"))
        self.depositList.setText(_translate("Dialog", "Вывести список активных вкладов"))
        self.creditSum.setText(_translate("Dialog", "TextLabel"))
        self.depositSum.setText(_translate("Dialog", "TextLabel"))


class BogomolBankAdmin(QDialog, Ui_Dialog_4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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





class Ui_Dialog_5(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 871)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 90, 931, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 330, 581, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.surnameline = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.surnameline.setText("")
        self.surnameline.setClearButtonEnabled(False)
        self.surnameline.setObjectName("surnameline")
        self.verticalLayout.addWidget(self.surnameline)
        self.birthdayline = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.birthdayline.setText("")
        self.birthdayline.setObjectName("birthdayline")
        self.verticalLayout.addWidget(self.birthdayline)
        self.passportline = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.passportline.setText("")
        self.passportline.setObjectName("passportline")
        self.verticalLayout.addWidget(self.passportline)
        self.loginbutton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.loginbutton.setObjectName("loginbutton")
        self.verticalLayout.addWidget(self.loginbutton)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 230, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BOGOMOL ONLINE BANK"))
        self.surnameline.setPlaceholderText(_translate("Dialog", "Введите ФИО"))
        self.birthdayline.setPlaceholderText(_translate("Dialog", "Введите дату рождения (в формате dd.mm.year)"))
        self.passportline.setPlaceholderText(_translate("Dialog", "Введите серию и номер паспорта без пробелов"))
        self.loginbutton.setText(_translate("Dialog", "Войти"))
        self.label_2.setText(_translate("Dialog", "РЕГИСТРАЦИЯ"))


class BogomolBankLogin(QDialog, Ui_Dialog_5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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




class Ui_Dialog_6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(912, 620)
        Dialog.setMaximumSize(QtCore.QSize(912, 620))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 911, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 1)
        self.accountbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.accountbutton.setObjectName("accountbutton")
        self.gridLayout.addWidget(self.accountbutton, 2, 0, 1, 1)
        self.depositbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.depositbutton.setObjectName("depositbutton")
        self.gridLayout.addWidget(self.depositbutton, 1, 0, 1, 1)
        self.changeinfo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changeinfo.setObjectName("changeinfo")
        self.gridLayout.addWidget(self.changeinfo, 6, 0, 1, 1)
        self.creditbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.creditbutton.setObjectName("creditbutton")
        self.gridLayout.addWidget(self.creditbutton, 0, 0, 1, 1)
        self.creditList = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.creditList.setObjectName("creditList")
        self.gridLayout.addWidget(self.creditList, 3, 0, 1, 1)
        self.depositList = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.depositList.setObjectName("depositList")
        self.gridLayout.addWidget(self.depositList, 4, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">BOGOMOL ONLINE BANK</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Ваш аккаунт</p></body></html>"))
        self.accountbutton.setText(_translate("Dialog", "Личные данные"))
        self.depositbutton.setText(_translate("Dialog", "Оформить вклад"))
        self.changeinfo.setText(_translate("Dialog", "Изменить информацию о себе"))
        self.creditbutton.setText(_translate("Dialog", "Оформить кредит"))
        self.creditList.setText(_translate("Dialog", "Ваши кредиты"))
        self.depositList.setText(_translate("Dialog", "Ваши вклады"))


class BogomolBankClient(QDialog, Ui_Dialog_6):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
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
        self.tableWidget.setHorizontalHeaderLabels(['id', 'ФИО', 'Дата рождения', 'Данные паспорта',
                                                    'Наличие кредитов', 'Наличие вкладов'])
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





class Ui_Dialog_7(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 871)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 931, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 100, 571, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 190, 983, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lengthline = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lengthline.setObjectName("lengthline")
        self.gridLayout.addWidget(self.lengthline, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.sumline = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sumline.setObjectName("sumline")
        self.gridLayout.addWidget(self.sumline, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 480, 1024, 115))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BOGOMOL ONLINE BANK"))
        self.label_2.setText(_translate("Dialog", "Оформление кредита"))
        self.lengthline.setPlaceholderText(_translate("Dialog", "Кредит разрешено брать на срок до 30 лет!"))
        self.label_3.setText(_translate("Dialog", "Срок выплаты кредита"))
        self.pushButton.setText(_translate("Dialog", "Подтвердить оформление кредита "))
        self.label_5.setText(_translate("Dialog", "Кредитная ставка = 10%"))
        self.sumline.setPlaceholderText(_translate("Dialog", "Введите сумму от 1 до 100 млн рублей"))
        self.label_4.setText(_translate("Dialog", "Сумма кредита"))
        self.label_6.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Выплаты по кредиту вычисляются по специальной формуле Bogomol Online Bank:</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Месячный платёж = (S * k^n) // 12*n</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Каждый месяц выплачиватеся одинаковая сумма!</span></p></body></html>"))



class BogomolBankCredit(QDialog, Ui_Dialog_7):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
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




class Ui_Dialog_8(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 871)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 931, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 100, 571, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 190, 983, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lengthline = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lengthline.setObjectName("lengthline")
        self.gridLayout.addWidget(self.lengthline, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.sumline = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.sumline.setObjectName("sumline")
        self.gridLayout.addWidget(self.sumline, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BOGOMOL ONLINE BANK"))
        self.label_2.setText(_translate("Dialog", "Оформление вклада"))
        self.lengthline.setPlaceholderText(_translate("Dialog", "Вклад разрешено оформить на срок до 5 лет!"))
        self.label_3.setText(_translate("Dialog", "Срок вклада"))
        self.pushButton.setText(_translate("Dialog", "Подтвердить оформление вклада"))
        self.label_5.setText(_translate("Dialog", "Ставка вклада = 7%"))
        self.sumline.setPlaceholderText(_translate("Dialog", "Введите сумму от 1 до 100 млн рублей"))
        self.label_4.setText(_translate("Dialog", "Сумма вклада"))


class BogomolBankDeposit(QDialog, Ui_Dialog_8):
    def __init__(self, name):
        super().__init__()
        self.setupUi(self)
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





class Ui_Dialog_9(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 871)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 931, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 110, 591, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(330, 200, 401, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.summaline = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.summaline.setObjectName("summaline")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.summaline)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.longline = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.longline.setObjectName("longline")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.longline)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.debtline = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.debtline.setObjectName("debtline")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.debtline)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.monthpayline = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.monthpayline.setObjectName("monthpayline")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.monthpayline)
        self.acceptButton = QtWidgets.QPushButton(Dialog)
        self.acceptButton.setGeometry(QtCore.QRect(335, 347, 391, 161))
        self.acceptButton.setObjectName("acceptButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BOGOMOL ONLINE BANK"))
        self.label_2.setText(_translate("Dialog", "Ваш кредит оформлен!"))
        self.label_3.setText(_translate("Dialog", "Сумма кредита"))
        self.label_4.setText(_translate("Dialog", "Срок кредита (лет)"))
        self.label_5.setText(_translate("Dialog", "Общая задолженность"))
        self.label_6.setText(_translate("Dialog", "Месячный платёж"))
        self.acceptButton.setText(_translate("Dialog", "Вернуться на главную страницу"))


class BogomolBankThanksCredit(QDialog, Ui_Dialog_9):
    def __init__(self, sumcredit, longcredit):
        super().__init__()
        self.setupUi(self)
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
        self.hide()




class Ui_Dialog_10(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1134, 871)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 931, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 110, 591, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(330, 200, 401, 221))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.summaline = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.summaline.setObjectName("summaline")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.summaline)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.longline = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.longline.setObjectName("longline")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.longline)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.profitline = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.profitline.setObjectName("profitline")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.profitline)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.monthprofitline = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.monthprofitline.setObjectName("monthprofitline")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.monthprofitline)
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(335, 347, 391, 161))
        self.backbutton.setObjectName("backbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "BOGOMOL ONLINE BANK"))
        self.label_2.setText(_translate("Dialog", "Ваш вклад оформлен!"))
        self.label_3.setText(_translate("Dialog", "Сумма вклада"))
        self.label_4.setText(_translate("Dialog", "Срок вклада (лет)"))
        self.label_5.setText(_translate("Dialog", "Общая выплата"))
        self.label_6.setText(_translate("Dialog", "Месячная выплата"))
        self.backbutton.setText(_translate("Dialog", "Вернуться на главную страницу"))


class BogomolBankThanksDeposit(QDialog, Ui_Dialog_10):
    def __init__(self, sumdeposit, longdeposit):
        super().__init__()
        self.setupUi(self)
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
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BogomolBankBegin()
    ex.show()
    sys.exit(app.exec())
