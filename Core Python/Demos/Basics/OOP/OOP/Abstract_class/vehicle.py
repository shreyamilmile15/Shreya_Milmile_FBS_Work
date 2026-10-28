from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, cNo, color):
        self.cno = cNo
        self.color = color

    def getCno(self):
        return self.cno

    def setCno(self, neno):
        self.setCno = neno

    def getColor(self):
        return self.color

    def setCol(self, nCol):
        self.color = nCol

    @abstractmethod
    def brake(self):
        pass

    def __str__(self):
        return f"The CNo: {self.cno} Color={self.color}"

class Car(Vehicle):
    def brake(self):
        print("This is the Brake of Car.")

c = Car(12, "White")
print(c)
c.brake()