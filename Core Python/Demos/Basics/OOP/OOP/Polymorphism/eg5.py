class Animal:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getAge(self):
        return self.age
    def setAge(self, newage):
        self.age = newage

    def getFood(self):
        return self.food
    def setFood(self, newfood):
        self.food = newfood

    def eatFood(self):
        print(f"{self.name} eats {self.food}")

#### class Animal ends here......

class Mammal(Animal):
    def __init__(self, name, age, food, fur):
        super().__init__(name, age, food)
        self.fur = fur

    def getFur(self):
        return self.fur
    def setFur(self, newfur):
        self.fur = newfur

    def eatFood(self):
        print(f"Mammal {self.name} eats {self.food}")

#### class Mammal ends here......

class Bird(Animal):
    def __init__(self, name, age, food, wings):
        super().__init__(name, age, food)
        self.wings = wings

    def getWings(self):
        return self.wings
    def setWings(self, newwings):
        self.wings = newwings

    def eatFood(self):
        print(f"Bird {self.name} eats {self.food}")

a1 = Animal("Animal", 5, "Food")
m1 = Mammal("Lion", 8, "Meat", "Thick Fur")
b1 = Bird("Parrot", 3, "Seeds", 2)

a1.eatFood()
m1.eatFood()
b1.eatFood()