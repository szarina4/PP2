class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.balance+=dep
        print('You added {} and current balance is :{}'.format(dep, self.balance))
    def withdraw(self, mon):
         
        if mon > self.balance:
            print('Too much request,  only {} in your account'.format(self.balance))
        else:
            self.balance-=mon
            print('Withdrawal was made,your current balance is {}'.format(self.balance))
        
    
a=Account("Vanis",50)
a.withdraw(5)
a.withdraw(100)
a.deposit(4)

