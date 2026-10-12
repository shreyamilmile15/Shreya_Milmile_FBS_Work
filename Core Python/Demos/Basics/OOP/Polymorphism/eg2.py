class BankAccount:
    def __init__(self, AccNo, Name, Balance):
        self.AccNo = AccNo
        self.Name = Name
        self.Balance = Balance

    def getAccNo(self):
        return self.AccNo

    def setAccNo(self, AccNo):
        self.AccNo = AccNo

    def getName(self):
        return self.Name

    def setName(self, Name):
        self.Name = Name

    def getBalance(self):
        return self.Balance

    def setBalance(self, Balance):
        self.Balance = Balance

    def calBalance(self):
        print(f"Final Balance of Bank Account is {self.Balance}")

    def display(self):
        print(f"AccNo = {self.AccNo}\tName = {self.Name}\tBalance = {self.Balance}")

## BankAccount class ends here

class SavingAccount(BankAccount):
    def __init__(self, AccNo, Name, Balance, Interest):
        super().__init__(AccNo, Name, Balance)
        self.Interest = Interest

    def getInterest(self):
        return self.Interest

    def setInterest(self, Interest):
        self.Interest = Interest

    def calBalance(self):
        finalBalance = self.Balance + (self.Balance * self.Interest / 100)
        print(f"Final Balance of Saving Account is {finalBalance}")

    def display(self):
        print(f"Interest = {self.Interest}%")
        super().display()

## SavingAccount class ends here

class CurrentAccount(BankAccount):
    def __init__(self, AccNo, Name, Balance, Overdraft):
        super().__init__(AccNo, Name, Balance)
        self.Overdraft = Overdraft

    def getOverdraft(self):
        return self.Overdraft

    def setOverdraft(self, Overdraft):
        self.Overdraft = Overdraft

    def calBalance(self):
        finalBalance = self.Balance + self.Overdraft
        print(f"Final Balance of Current Account is {finalBalance}")

    def display(self):
        print(f"Overdraft = {self.Overdraft}")
        super().display()

## CurrentAccount class ends here

b1 = BankAccount(101, "Rahul", 50000)
s1 = SavingAccount(102, "Priya", 75000, 6.5)
c1 = CurrentAccount(103, "Amit", 100000, 25000)

b1.calBalance()
s1.calBalance()
c1.calBalance()