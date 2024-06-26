class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nTransaction declined! Account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nUnable to complete withdrawal: {error}")

    def transfer(self, amount, acctName):
        try:
            print("\n***** Transfer Initiated *****")
            self.viableTransaction(amount)
            self.withdraw(amount)
            acctName.deposit(amount)
            print("\n***** Transfer Completed *****")
        except BalanceException as error:
            print(f"Unable to complete transfer: {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (1.05 * amount)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAccout(InterestRewardsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nUnable to complete withdrawal: {error}")

    
        
