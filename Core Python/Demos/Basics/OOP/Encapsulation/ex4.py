class ElectronicDevice:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getBrand(self):
        return self.brand
    def setBrand(self, newbrand):
        self.brand = newbrand

    def getPrice(self):
        return self.price
    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Device = {self.name}\tBrand = {self.brand}\tPrice = {self.price}")
        
d1 = ElectronicDevice("Mobile", "Samsung", 25000)
d2 = ElectronicDevice("LED", "LG", 55000)
print(d1.getBrand())
d1.display()
d2.display()
d2.setPrice(60000)
d2.display()