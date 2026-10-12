class Transport:
    def __init__(self, number, type, capacity):
        self.number = number
        self.type = type
        self.capacity = capacity

    def getNumber(self):
        return self.number
    def setNumber(self, newnumber):
        self.number = newnumber

    def getType(self):
        return self.type
    def setType(self, newtype):
        self.type = newtype

    def getCapacity(self):
        return self.capacity
    def setCapacity(self, newcapacity):
        self.capacity = newcapacity

    def display(self):
        print(f"Number = {self.number}\tType = {self.type}\tCapacity = {self.capacity}")
        
t1 = Transport(101, "car", 5)
t2 = Transport(11,"Bus",50)
print(t1.getType())
t1.display()
t2.display()
t2.setCapacity(60)
t2.display()