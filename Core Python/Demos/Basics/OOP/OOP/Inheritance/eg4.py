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

## Transport class ends here

class RoadTransport(Transport):
    def __init__(self, number, type, capacity, wheels):
        super().__init__(number, type, capacity)
        self.wheels = wheels

    def getWheels(self):
        return self.wheels
    def setWheels(self, newwheels):
        self.wheels = newwheels

    def display(self):
        print(f"Wheels = {self.wheels}\t")
        super().display()

## RoadTransport class ends here

class AirTransport(Transport):
    def __init__(self, number, type, capacity, airline):
        super().__init__(number, type, capacity)
        self.airline = airline
    def getAirline(self):
        return self.airline
    
    def setAirline(self, newairline):
        self.airline = newairline
    def display(self):
        print(f"Airline = {self.airline}\t")
        super().display()

## AirTransport class ends here

t1 = Transport(101, "Transport", 50)
r1 = RoadTransport(11, "Bus", 50, 6)
a1 = AirTransport(21, "Flight", 180, "IndiGo")

t1.display()
r1.display()
a1.display()