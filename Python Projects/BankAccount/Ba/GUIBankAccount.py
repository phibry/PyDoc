import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

class Client:    
    age = int()
    name = str()
    
    def __init__(self, name, age):
        self.age = age
        self.name = name
        
class Bank: 
    
    def __init__(self, client):
        self.amount = 0
        self.client = client
    
    def deposit(self, money):
        if self.amount + money > 100000:
            return "Account is full"
        
        else:
            self.amount = self.amount + money
            return self.amount
                         
    def withdraw(self, cash):
        if self.amount - cash < 0:
            self.amount -= cash * 1.02
        else:
            self.amount -= cash
        return self.amount
    
    def balance(self, zeit):
        time.sleep(zeit)
        self.amount = self.amount * (1 + interest_s)**(int(time.time() - starttime))
        return self.amount
    
def print_clients(clients):
    for k,v in clients.items():
        print(k)

def print_numberd_clients(clients):
    counter = 0
    client_list = []
    for k,v in clients.items():
        client_list.append(k)       
    
    print("For whom?")
    for i in client_list:
        print(counter, i)
        counter += 1 
    return client_list[int(input())]

def add_client(clients):
    
    new_client = Client(str(input("Name ")),int(input("Age ")))
    clients.update({new_client.name:new_client})
    return clients
    
def add_account(clients, accounts):
    
    selection = print_numberd_clients(clients)
    accounts.update({selection:Bank(clients[selection])})   
    return clients, accounts

def deposit_money(clients, accounts):
    selection = print_numberd_clients(clients)
    amount = int(input("How much money? "))
    accounts[selection].deposit_funds(amount)
    print("New Balance:",accounts[selection].get_balance())
    return clients, accounts
    
starttime = time.time()
zeit = 1    
interest_s = 0.01


class Ui_MainWindow(object):
    
    def __init__(self, client):
        QMainWindow.__init__(self, client)
        Bank.__init__(self, client)
        self.setupUi(self)
        self.clients = {}
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 815)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.view_clients = QtWidgets.QListWidget(self.centralwidget)
        self.view_clients.setGeometry(QtCore.QRect(10, 10, 221, 301))
        self.view_clients.setObjectName("view_clients")
        
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
        #self.listWidget_2.clicked.connect(self.list)
       
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
        
        self.set_behaviours()
        clients = (("Ken Geeler", 22),("Philipp Rieser", 25),("Remo Richter", 27))
        for i in clients:
            self.add_client(i[0], i[1])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PostFinance Asset Management"))
        self.pushButton.setText(_translate("MainWindow", "Deposit"))
        self.pushButton_2.setText(_translate("MainWindow", "Withdraw"))
        self.pushButton_3.setText(_translate("MainWindow", "Balance"))
        self.label.setText(_translate("MainWindow", "Transaction Log"))
        
    def set_behaviours(self):
        self.view_clients.clicked.connect(self.set_active_account)
        self.view_clients.clicked.connect(self.refresh_GUI)
        self.pushButton.clicked.connect(self.deposit)
        self.pushButton_2.clicked.connect(self.withdraw)
        
    def refresh_GUI(self):
        try:
            self.clients.get(self.active_account).apply_intrest()
            self.lab_amount.setText(str(self.clients.get(self.active_account).balance))
            #print(self.clients.get(str(self.active_account)))
        except Exception as e:
            print("error: ",e)
            
    def add_client(self, name, age):
        new_client = Client(name, age)
#        if age < 26:
#            self.clients.update({name:BA.YouthAccount(new_client)})
#        else:
#            self.clients.update({name:BA.SavingAccount(new_client)})
        self.clients.update({name: Bank(new_client)})
        self.refresh_client_view()
        self.add_log_entry("Der Kunde "+name+" wurde hinzugefügt")
        
    def deposit(self):
        money = int(self.lineEdit.text())
        self.amount = self.amount + money
        #self.amount = self.amount * (1 + interest_s)**(int(time.time() - starttime))
        #print(self.amount)
        self.lcdNumber.display(self.amount)
        
    def withdraw(self):
        cash = int(self.lineEdit_2.text())
        if self.amount - cash < 0:
            self.amount -= cash * 1.02
        else:
            self.amount -= cash
        #print(self.amount)
        self.lcdNumber.display(self.amount)
        
    def balance(self, zeit):
        self.amount = self.amount * (1 + interest_s)**(int(time.time() - starttime))
        print(self.amount)
        self.lcdNumber.display(self.amount)
        
    def set_active_account(self):
        self.active_account = self.view_clients.currentItem().text()
        self.first_select = True
        
if __name__ == "__main__": 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
app = QApplication(sys.argv)
screen = Ui_MainWindow()
screen.show()
sys.exit(app.exec_())