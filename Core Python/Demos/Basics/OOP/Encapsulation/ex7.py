class Student:    
    inname = "FBS"
    @staticmethod
    def setInName(niname):
        Student.inName = niname

    def __init__(self,frn,name,bname,inname):
        self.frn = frn
        self.name = name
        self.batch = bname
        self.inName = inname

    def getname (self):
        return self.name
    def setname (self,newname):
        self.name = newname

    def getfrn (self):
        return self.frn
    def setfrn(self,newfrn):
        self.name = newfrn

    def getbname (self):
        return self.bname
    def setbname (self,newbname):
        self.bname = newbname

    def getinname (self):
        return self.inname
    def setinname (self,newinname):
        selfinbname = newinname

    def display(self):
        print(f"FRN = {self.frn}\tName = {self.name}\tBatch = {self.batch}\tInName = {self.inName}")

s1 = Student(15,"Shreya","Februray","FBS")
s2 = Student(16,"Mrudula","August","FBS")
s3 = Student(29,"Sakshi","April","FBS")
s1.display()
s2.display()
s3.display()