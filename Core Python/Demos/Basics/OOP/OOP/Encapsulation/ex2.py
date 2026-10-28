class Vehicle:
    def __init__(self,number,model,price):
        self.number = number
        self.model = model
        self.price = price

    def getNumber(self):
        return self.number
    def setNumber (self, newnumber):
        self.number = newnumber

    def getModel(self):
        return self.model
    def setModel (self, newmodel):
        self.number = newmodel

    def getPrice(self):
        return self.price
    def setPrice (self, newprice):
        self.price = newprice

    def display(self):
        print(f"Number = {self.number}\tModel= {self.model}\tPrice={self.price}")       

v1 = Vehicle("MH34AB1234", "Swift", 800000)
print(v1.getModel())
v1.display()
v1.setPrice(850000)
v1.display()