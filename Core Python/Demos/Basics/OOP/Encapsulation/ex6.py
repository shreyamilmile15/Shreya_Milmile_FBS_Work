class Animal:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getType(self):
        return self.type
    def setType(self, newtype):
        self.type = newtype

    def getAge(self):
        return self.age
    def setAge(self, newage):
        self.age = newage

    def display(self):
        print(f"Name = {self.name}\tType = {self.type}\tAge = {self.age}")
        
a1 = Animal("Tommy", "Dog", 3)
print(a1.getName())
a1.display()
a1.setAge(4)
a1.display()