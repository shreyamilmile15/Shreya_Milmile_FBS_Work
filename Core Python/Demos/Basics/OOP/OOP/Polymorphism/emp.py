class Employee:          ### object class or cosmic super class
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
    
    def getId(self):
        return self.id
    def selfId(self,newid):
        self.id=newid

    def getName(self):
        return self.name
    def setName(self,newname):
        self.name=newname

    def getSal(self):
        return self.sal
    def setSal(self,newsal):
        self.sal=newsal

    def calSal (self):
        print(f"Final Salary of Employee is {self.sal}")

    def display(self):
        print(f"Id = {self.id}\tName = {self.name}\tSal={self.sal}")

## EMP Ends Here..............

class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com = com

    def getCom(self):
        return self.com
    def setCom(self,ncom):
        self.com = ncom

    def calSal (self):
        print(f"Final Salary of HR is {self.sal + self.com}")

    def display(self):
        print(f"Com = {self.com}\t")
        super().display()

## HR class ends here

class Developer(Employee):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.bonus = bonus

    def getbonus(self):
        return self.bonus
    def setbonus(self,nbonus):
        self.bonus = nbonus

    def calSal (self):
        print(f"Final Salary of Developer is {self.sal + self.bonus}")

    def display(self):
        print(f"Bonus = {self.bonus}\t")
        super().display()

e1 =Employee(10,'Sachine',12123)
h1 = Hr(18,'Virat',33456, 1200)
d1 = Developer (22, "Suraj", 30000, 5400)

e1.calSal()
h1.calSal()
d1.calSal()
