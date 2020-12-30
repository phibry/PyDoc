# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

#class Sub(QtWidgets.QMainWindow):
#    def setupUi(self, MainWindow):
#        MainWindow.setObjectName("MainWindow")
#        MainWindow.resize(297, 285)
#        self.centralwidget = QtWidgets.QWidget(MainWindow)
#        self.centralwidget.setObjectName("centralwidget")
#        
#        self.listView = QtWidgets.QListView(self.centralwidget)
#        self.listView.setGeometry(QtCore.QRect(10, 20, 281, 171))
#        self.listView.setObjectName("listView")
#        
#        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
#        self.buttonBox.setGeometry(QtCore.QRect(10, 200, 191, 31))
#        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
#        self.buttonBox.setObjectName("buttonBox")
#        
#        MainWindow.setCentralWidget(self.centralwidget)
#        self.menubar = QtWidgets.QMenuBar(MainWindow)
#        self.menubar.setGeometry(QtCore.QRect(0, 0, 297, 26))
#        self.menubar.setObjectName("menubar")
#        self.menuWas_f_r_ein_Konto_m_chten_Sie_er_ffnen = QtWidgets.QMenu(self.menubar)
#        self.menuWas_f_r_ein_Konto_m_chten_Sie_er_ffnen.setObjectName("menuWas_f_r_ein_Konto_m_chten_Sie_er_ffnen")
#        MainWindow.setMenuBar(self.menubar)
#        self.statusbar = QtWidgets.QStatusBar(MainWindow)
#        self.statusbar.setObjectName("statusbar")
#        MainWindow.setStatusBar(self.statusbar)
#        self.menubar.addAction(self.menuWas_f_r_ein_Konto_m_chten_Sie_er_ffnen.menuAction())
# 
#        self.retranslateUi(MainWindow)
#        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# 
#    def retranslateUi(self, MainWindow):
#        _translate = QtCore.QCoreApplication.translate
#        MainWindow.setWindowTitle(_translate("MainWindow", "Konto eröffnen"))
#        self.menuWas_f_r_ein_Konto_m_chten_Sie_er_ffnen.setTitle(_translate("MainWindow", "Was für ein Konto möchten Sie eröffnen"))
    
class Bank: 
    
    def __init__(self):
        self.amount = 0
        
    def naming(self, owner):
        self.owner = owner
    
    def deposit(self, amount):
        self.amount = self.amount + amount
        return self.amount
                         
    def withdraw(self, amount):
        if self.amount - amount < 0:
            self.amount -= amount * 1.02
        else:
            self.amount -= amount
        return self.amount
    
    def balance(self, zeit):
        time.sleep(zeit)
        self.amount = self.amount * (1 + interest_s)**(int(time.time() - starttime))
        return self.amount   
    
starttime = time.time()
zeit = 1    
interest_s = 0.01

a1 = Bank()
a2 = Bank()
a3 = Bank()
 
a1.naming("Ken")
a2.naming("Remo")
a3.naming("Philipp")
 
 
 
accounts = [a1, a2, a3]
names = ["Ken", "Remo", "Philipp"]


class Ui_MainWindow(QtWidgets.QMainWindow, Bank):
    
    def __init__(self):
        QMainWindow.__init__(self)
        Bank.__init__(self)
        self.setupUi(self)
        
#    def openwindow(self):
#        self.window = QtWidgets.QMainWindow()
#        self.ui = Sub()
#        self.ui.setupUi(self.window)
#        self.window.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 815)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(560, 100, 241, 121))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display(self.amount)
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(660, 270, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(660, 330, 141, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 270, 150, 46))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.deposit)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 330, 150, 46))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.withdraw)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 390, 150, 46))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.balance)        
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 510, 761, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.append("{0}: ** PostFinance Asset Management started **".format(time.asctime(time.localtime())))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 470, 161, 25))
        self.label.setObjectName("label")
        
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(60, 40, 341, 391))
        self.listWidget_2.setObjectName("listWidget_2")
        
        for element in names:
            self.listWidget_2.addItem(element)
        
        self.listWidget_2.itemClicked.connect(self.liste)
       
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 38))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PostFinance Asset Management"))
        self.pushButton.setText(_translate("MainWindow", "Deposit"))
        self.pushButton_2.setText(_translate("MainWindow", "Withdraw"))
        self.pushButton_3.setText(_translate("MainWindow", "Balance"))
        self.label.setText(_translate("MainWindow", "Transaction Log"))
        
    def deposit(self):
        amount = int(self.lineEdit.text())
        self.current_account.amount = self.current_account.amount + amount
        self.lcdNumber.display(self.current_account.amount)
        #self.amount = self.amount + amount
        self.textBrowser.append("Deposit: " + str(self.lineEdit.text()))
        #self.lcdNumber.display(self.amount)

        
    def withdraw(self):
        amount = int(self.lineEdit_2.text())
        self.current_account.amount = self.current_account.amount - amount
        self.lcdNumber.display(self.current_account.amount)
        if self.amount - amount < 0:
            self.amount -= amount * 1.02
            self.textBrowser.append("Withdraw: " + str(self.lineEdit_2.text() + " negative Balance"))
        else:
            self.amount -= amount
            self.textBrowser.append("Withdraw: " + str(self.lineEdit_2.text()))
        #self.lcdNumber.display(self.amount)
        
    def balance(self, zeit):
        self.current_account.amount = self.amount * (1 + interest_s)**(int(time.time() - starttime))
        self.textBrowser.append("Balance: " + str(self.current_account.amount))
        self.lcdNumber.display(self.current_account.amount)
        
    def liste(self, item):
        item = item
        name = str(item.text())
        name = name.lower()
        self.name = str(item.text())
        
        if name == "Ken":
            self.current_account = accounts[0]
            self.lcdNumber.display(self.current_account.amount)
            
        if name == "Remo":
            self.current_account = accounts[1]
            self.lcdNumber.display(self.current_account.amount)
            
        if name == "Philipp":
            self.current_account = accounts[2]
            self.lcdNumber.display(self.current_account.amount)
        
app = QApplication(sys.argv)
screen = Ui_MainWindow()
screen.show()
sys.exit(app.exec_())


