from bank_account import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(100)
Dave.withdraw(1000)
Dave.transfer(500, Sara)
Dave.transfer(5000, Sara)

Jim = InterestRewardAccount(5000, "Jim", 5)
Jim.getBalance()
Jim.addInterest()
Jim.getBalance()
Jim.transfer(1000, Dave)