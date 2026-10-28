class Employee:
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

    def display(self):
        print(f"Bonus = {self.bonus}\t")
        super().display()

e1 =Employee(10,'Sachine',121234)
h1 = Hr(18,'Virat',334567, 1200)
d1 = Developer (22, "Suraj", 30000, 5400)

e1.display()
h1.display()
d1.display()
