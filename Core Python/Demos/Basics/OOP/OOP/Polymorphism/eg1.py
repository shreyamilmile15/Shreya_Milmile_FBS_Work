class Vehicle:
    def __init__(self,Vno,Brand,Speed):
        self.Vno = Vno
        self.Brand = Brand
        self.Speed = Speed

    def getVno (self):
        return self.Vno
    def setVno (self,Vno):
        self.Vno = Vno

    def getBrand(self):
        return self.Brand
    def setBrand(self,Brand):
        self.Brand = Brand

    def getSpeed(self):
        return self.Speed
    def setSpeed(self,Speed):
        self.Speed = Speed

    def calMileage(self):
        print("Vehicle milege is calculated based on vehicle type.")

    def display(self):
        print(f"Vno = {self.Vno}\tBrand = {self.Brand}\tSpeed = {self.Speed}")
## class vehicle end here..........

class Car(Vehicle):
    def __init__(self,Vno,Brand,Speed,Airbag):
        super().__init__(Vno,Brand,Speed)
        self.Airbag = Airbag

    def getAirbag (self):
        return self.Airbag
    def setAirbag (self,Airbag):
        self.Airbag = Airbag

    def calMileage(self):
        print(f"Car {self.Brand} mileage = 18 km/l")
    def display(self):
        print(f"Airbag = {self.Airbag}\t")
        super().display()

## class car ends here...........

class Bike(Vehicle):
    def __init__(self,Vno,Brand,Speed,Handle):
        super().__init__(Vno,Brand,Speed)
        self.Handle = Handle

    def getHandle (self):
        return self.Handle
    def setHandle (self,Handle):
        self.Handle = Handle

    def calMileage(self):
        print(f"Bike {self.Brand} mileage = 45 km/l")
        
    def display(self):
        print(f"Handle = {self.Handle}\t")
        super().display()

v1 = Vehicle(1234,"Honda",120)
c1 = Car(234,"Toyota",180,4)
b1 = Bike(456,"Pulsar",132,"Sport Handle")

v1.calMileage()
c1.calMileage()
b1.calMileage()