class ElectronicDevice:
    def __init__(self,Brand,Model,Price):
        self.Brand = Brand
        self.Model = Model
        self.Price = Price

    def getBrand (self):
        return self.Brand
    def setBrand (self,Brand):
        self.Brand = Brand

    def getModel (self):
        return self.Model
    def setModel (self,Model):
        self.Model = Model

    def getPrice (self):
        return self.Price
    def setPrice (self,Price):
        self.Price = Price        

    def display(self):
        print(f"Brand = {self.Brand}\tModel = {self.Model}\tPrice = {self.Price}")
## class ElectronicDevice END here..........

class Laptop(ElectronicDevice):
    def __init__(self,Brand,Model,Price,Processor):
        super().__init__(Brand,Model,Price)
        self.Processor = Processor

    def getProcessor(self):
        return self.Processor
    def setProcessor(self,Processor):
        self.Processor

    def display(self):
        print(f"Processor = {self.Processor}\t")
        super().display()
## class Laptop ends here.......

class Mobile(ElectronicDevice):
    def __init__(self,Brand,Model,Price,SimCount):
        super().__init__(Brand,Model,Price)
        self.SimCount = SimCount
    
    def getSimCount(self):
        return self.SimCount
    def setSimCount(self,SimCount):
        self.SimCount
    
    def display(self):
        print(f"SimCount = {self.SimCount}\t")
        super().display()

e1 = ElectronicDevice("LG","LG Gram 14",40000)
l1 = Laptop("Asus","Vivobook",75000,"Ryzen 7")
m1 = Mobile("Iphone","15",45000,1)

e1.display()
l1.display()
m1.display()