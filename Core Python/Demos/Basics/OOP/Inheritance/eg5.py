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

    def display(self):
        print(f"Name = {self.name}\tAge = {self.age}\tFood = {self.food}")

## Animal class ends here

class Mammal(Animal):
    def __init__(self, name, age, food, fur):
        super().__init__(name, age, food)
        self.fur = fur

    def getFur(self):
        return self.fur
    def setFur(self, newfur):
        self.fur = newfur

    def display(self):
        print(f"Fur = {self.fur}\t")
        super().display()

## Mammal class ends here

class Bird(Animal):
    def __init__(self, name, age, food, wings):
        super().__init__(name, age, food)
        self.wings = wings

    def getWings(self):
        return self.wings
    def setWings(self, newwings):
        self.wings = newwings

    def display(self):
        print(f"Wings = {self.wings}\t")
        super().display()
## Bird class ends here

a1 = Animal("Animal", 5, "Food")
m1 = Mammal("Lion", 8, "Meat", "Thick Fur")
b1 = Bird("Parrot", 3, "Seeds", 2)

a1.display()
m1.display()
b1.display()