# Account Class


class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print(
            f'Deposit Accepted: Deposited ${dep_amt} to the Account of {self.owner}')
        # return self.balance

    def withdraw(self, wd_amt):
        if wd_amt > self.balance:
            print('Funds Unavailable!')
            # return self.balance
        else:
            self.balance -= wd_amt
            print(
                f'Withdrawal Accepted: Withdrawn ${wd_amt} of the Account of {self.owner}')
            # return self.balance

    def __str__(self):
        return (f'Account owner:      {self.owner} \nAccount balance:    ${self.balance}')


acct1 = Account('Phili', 100)
print(acct1)
print('\n')

acct1.deposit(50)
print(acct1)
print('\n')

acct1.withdraw(100)
print(acct1)
print('\n')

acct1.withdraw(100)
print(acct1)
