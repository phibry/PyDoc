# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:46:20 2018

@author: Phili
"""
import time
import datetime
from abc import ABCMeta, abstractmethod
        
class BankAccount():
    def __init__(self, name, age):
        self.balance = 0
        self.user = name
        self.age = age
        self.timefirst = datetime.datetime.now().replace(microsecond=0)
        self.timedelta = 0
        self.current = False
        
    def openacc(self, name):
        self.user = name
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
    
    def info(self):
        return str("User: ") + str(self.user) + str("  Age: ") + str(self.age) + str("  Balance: ") + str(self.balance) + str(" CHF")
        
class SavingAccount(BankAccount):
    def __init__(self, name, age):
        BankAccount.__init__(self, name, age)
        self.interest_last = 0
        self.interest = 1.01
        
    def interest(self, interest):
        self.__interest = interest/100 + 1 #q (EZB)
        
    def calcinterest(self):
        self.__interestx__();
        
    def __interestx__(self):
        self.timedelta = (datetime.datetime.now().replace(microsecond=0)) - self.timefirst #calculate the time difference since opening
        self.interest_n = int(self.timedelta.total_seconds()) - self.interest_last #calculate n "years" since last billing
        self.interest_last = int(self.timedelta.total_seconds()) #save date
        self.balance = self.balance*1.00001**(self.interest_n) #write new bank balance
        
    def deposit(self, amount):
        self.__interestx__() #Only pay interest, because then the balance changes
        super(SavingAccount, self).deposit(amount) #call method BankAccount -> deposit
        
    def withdraw(self, amount):
        self.__interestx__() #Only pay interest, because then the balance changes
        super(SavingAccount, self).withdraw(amount) #call method BankAccount -> withdraw
        if self.balance < 0:
            self.balance -= 0.02*amount #2% fee, if balance < 0
            
class YouthAccount(BankAccount):
    def __init__(self, name, age):
        BankAccount.__init__(self, name, age)
        self.interest_last = 0
        self.interest = 1.05
        
    def interest(self, interest):
        self.__interest = interest/100 + 1 #q (EZB)
        
    def calcinterest(self):
        self.__interestx__();
        
    def __interestx__(self):
        self.timedelta = (datetime.datetime.now().replace(microsecond=0)) - self.timefirst #calculate the time difference since opening
        self.interest_n = int(self.timedelta.total_seconds()) - self.interest_last #calculate n "years" since last billing
        self.interest_last = int(self.timedelta.total_seconds()) #save date
        self.balance = self.balance*1.01**(self.interest_n) #write new bank balance
        
    def deposit(self, amount):
        self.__interestx__() #Only pay interest, because then the balance changes
        super(YouthAccount, self).deposit(amount) #call method BankAccount -> deposit
        
    def withdraw(self, amount):
        self.__interestx__() #Only pay interest, because then the balance changes
        super(YouthAccount, self).withdraw(amount) #call method BankAccount -> withdraw