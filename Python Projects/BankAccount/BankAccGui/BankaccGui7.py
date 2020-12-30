# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\phili\Desktop\Prog_Sem_2\Python\BankAccGui_P03\BankAccGui7.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore

from BankACC import *

class Bankgui(QtWidgets.QWidget):
#    def __str__(self):
#        return("hello")
        
    def __init__(self, parent = None):
        
#        hiho.setObjectName("BankAccount KPR")
#        hiho.resize(521, 799)
        
        QtWidgets.QWidget.__init__(self, parent)
        
        self.layoutWidget = QtWidgets.QWidget(self) #
        self.layoutWidget.setGeometry(QtCore.QRect(30, 220, 461, 210))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.layoutWidget1 = QtWidgets.QWidget(self) #
        self.layoutWidget1.setGeometry(QtCore.QRect(270, 20, 221, 192))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_4.addWidget(self.lineEdit_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.layoutWidget2 = QtWidgets.QWidget(self) #
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 20, 183, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setChecked(True) #Default
        self.verticalLayout.addWidget(self.radioButton_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget2)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_5.addWidget(self.radioButton)
        self.listWidget = QtWidgets.QListWidget(self) #
        self.listWidget.setGeometry(QtCore.QRect(30, 610, 461, 161))
        self.listWidget.setObjectName("listWidget")
        self.layoutWidget3 = QtWidgets.QWidget(self) #
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 520, 461, 64))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color: green")
        self.verticalLayout_6.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color: red")
        self.verticalLayout_6.addWidget(self.label_6)
        self.widget = QtWidgets.QWidget(self) #
        self.widget.setGeometry(QtCore.QRect(30, 440, 461, 64))
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_7 = QtWidgets.QLabel("") #self.widget
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)

        self.retranslateUi(self) #
        QtCore.QMetaObject.connectSlotsByName(self) #
        
        self.accounts = [] #empty list
        self.bankaccounttype = "Saving" #Default (saving)
        
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.selected = None
        
        self.connectMethods()
        
        self.Timer = QtCore.QTimer(self)
        self.Timer.timeout.connect(self.refreshInfo)
        self.Timer.start(1000)
        
    def connectMethods(self):       
        self.radioButton_2.toggled.connect(self.accountTypeSelection_Saving)
        self.radioButton.toggled.connect(self.accountTypeSelection_Youth)
        self.pushButton_2.clicked.connect(self.depositButton)
        self.pushButton_3.clicked.connect(self.withdrawButton)
        self.pushButton.clicked.connect(self.creataccount)      
        self.listWidget.itemSelectionChanged.connect(self.selection_changed)

    def retranslateUi(self, hiho):
        _translate = QtCore.QCoreApplication.translate
        hiho.setWindowTitle(_translate("Dialog", "Bankaccount KRP"))
        self.label_2.setText(_translate("Dialog", "Type in your name:"))
        self.label_3.setText(_translate("Dialog", "Type in your age:"))
        self.pushButton.setText(_translate("Dialog", "Create Account"))
        self.pushButton_2.setText(_translate("Dialog", "Deposit"))
        self.pushButton_3.setText(_translate("Dialog", "Withdraw"))
        self.label.setText(_translate("Dialog", "Choose Account:"))
        self.radioButton_2.setText(_translate("Dialog", "SavingAccount"))
        self.radioButton.setText(_translate("Dialog", "YouthAccount"))
        self.label_4.setText(_translate("Dialog", "Information:"))
        
    def selection_changed(self):
        item = self.listWidget.currentItem()
        print("Current selection: {0}".format(item.text()))
        for bankAccount in self.accounts:
            if bankAccount.user == item.text():
                self.selected = bankAccount
    
    def fill_account_list(self):
        for account in self.accounts:
            self.listWidget.addItem(account.user)
            
    def creataccount(self):
        self.name = self.getNameInput()
        self.age = self.getAgeInput()
        
        if self.bankaccounttype == "Saving":
            self.newAddSaving = SavingAccount(self.name, self.age)
            self.listWidget.addItem(self.newAddSaving.user)
            self.accounts.append(self.newAddSaving)
            print("Saving")
        
        if self.bankaccounttype == "Youth":
            self.newAddYouth = YouthAccount(self.name, self.age)
            self.listWidget.addItem(self.newAddYouth.user)
            self.accounts.append(self.newAddYouth)
            print("Youth")

    def accountTypeSelection_Saving(self):
        self.bankaccounttype = "Saving"
            
    def accountTypeSelection_Youth(self):
        self.bankaccounttype = "Youth"
        
    def getDepositInput(self):
        self.deposit_2 = float(self.lineEdit_3.text()) #take deposit(float/int) from userinput
        return(self.deposit_2)
    
    def getWithdrawInput(self):
        self.withdraw_2 = float(self.lineEdit_4.text()) #take withdraw(float/int) from userinput
        return(self.withdraw_2)
    
    def getNameInput(self):
        self.name = str(self.lineEdit.text()) #take name(string) from userinput
        return(self.name)
    
    def getAgeInput(self):
        self.age = int(self.lineEdit_2.text()) #take age(int) from userinput
        return(self.age)
    
    def depositButton(self): #call method deposit from bankaccountclass
        self.selected.deposit(self.getDepositInput())
        self.label_5.setText(str("Deposit: ") + str(self.getDepositInput()) + str( " CHF"))
        self.label_7.setText(self.selected.info())
#        self.label_5.setText(self.deposit()) # doesnt work
        
    def withdrawButton(self): #call withdraw method from bankaccountclass
        self.selected.withdraw(self.getWithdrawInput())
        self.label_6.setText(str("Withdraw: ") + str(self.getWithdrawInput()) + str( " CHF"))
        self.label_7.setText(self.selected.info())
        
    def refreshInfo(self):
        if self.selected != None:
            self.selected.calcinterest()
            self.label_7.setText(self.selected.info())



app = QtWidgets.QApplication([])
hiho = Bankgui()
hiho.show()
app.exec_()

