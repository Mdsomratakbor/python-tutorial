class BalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f'\nAccount {self.name} created.\nBalance = ${ self.balance:.2f}')
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance: ${self.balance:.2f}")   

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit successful.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceError(f"\nSorry😔, account '{self.name}' has insufficient funds to withdraw ${amount:.2f}.\nBalance: ${self.balance:.2f}")
       
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdrawal successful.✅")
            self.getBalance()
        except BalanceError as e:
            print(f'\nWithdrawal interrupted: {e}❌')
            
    def transfer(self, amount, recipient):
        try:
            print('\n*****************')
            print('\nTransfer initiated...🚀')
            
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\nAccount '{self.name}' balance: ${self.balance:.2f}")
            recipient.deposit(amount)
            print(f"\nTransfer successful! ✅.")
            print("\n\n*****************")
        except BalanceError as e:
            print(f'\nTransfer interrupted: {e} ❌')       

class InterestRewardAccount(BankAccount):
    def __init__(self, initialAmount, accName, interestRate):
        super().__init__(initialAmount, accName)
        
        self.interestRate = interestRate
        print(f'Interest rate: {self.interestRate:.2f}%')
        
    def addInterest(self):
        self.balance += self.balance * self.interestRate / 100
        print(f"\nInterest added. New balance: ${self.balance:.2f}")
class SavingAccount(InterestRewardAccount):
    def __init__(self, initialAmount, accName, fee):
        self.fee = fee
        super().__init__(initialAmount, accName, 5)
        print(f'Fee: ${self.fee:.2f}')
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdrawal successful.✅")
            self.getBalance()
        except BalanceError as e:
            print(f'\nWithdrawal interrupted: {e}❌')
            
            