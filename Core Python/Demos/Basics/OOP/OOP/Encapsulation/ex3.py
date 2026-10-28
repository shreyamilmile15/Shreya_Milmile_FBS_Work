class BankAccount:
    def __init__(self,acc_no,name,balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def getAcc_no(self):
        return self.acc_no
    def setAcc_no(self, newacc_no):
        self.acc_no = newacc_no

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getBalance(self):
        return self.balance
    def setBalance(self, newbalance):
        self.balance = newbalance

    def display(self):
        print(f"Account No.= {self.acc_no}\tName = {self.name}\tBalance = {self.balance}")

b1 = BankAccount(101, "Rajesh", 50000)
print(b1.getName())
b1.display()
b1.setBalance(60000)
b1.display()