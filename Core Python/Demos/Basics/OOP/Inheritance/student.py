class Student:
    stCount = 0
    def __init__(self,frn,name,bname):
        self.frn = frn
        self.name = name
        self.batch = bname
        Student.stCount += 1
    def display(self):
        print("FRN={self.frn}\tName={self.name}\tBatch={self.batch}\tStudent Count={Student.stCount}")

class PlacedStudent(Student):
    def __init__(self,frn,name,bname,cName):
        super().__init__(frn,name,bname)
        self.cName = cName
    def setCname(self,cName):
        self.cName = cName
    def getCName(self):
        return self.cName

    def display(self):
        print(f"Cname={self.Cname}")
        super().display()
s1 = Student(12,"Karan","April")
s2 = Student(1,"Payal","Jul/aug")
s3 = Student(52,"Sneha","Jul/aug")
s4 = PlacedStudent(22,"Kriti","Jul/aug","TCS")
s5 = PlacedStudent(34,"Gaurav","Jul/aug","Oracle")
print(Student.stCount)