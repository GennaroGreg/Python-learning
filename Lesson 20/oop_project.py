from bank_accounts import *

Greg = BankAccount(1000, "Greg's Account")
Percy = BankAccount(250, "Percy's Account")

Greg.getBalance()
Percy.getBalance()

Greg.deposit(500)
Percy.deposit(10000)

Greg.withdraw(10000)
Greg.withdraw(50)

Greg.transfer(10000, "Percy's Account")
Percy.transfer(5000, Greg)

Cody = InterestRewardsAcct(1000, "Cody's Account")
Cody.getBalance()
Cody.deposit(100)
Cody.transfer(100, Percy)

Emma = SavingsAccout(1000, "Emma's Account")
Emma.getBalance()
Emma.deposit(100)
Emma.transfer(1000, Percy)