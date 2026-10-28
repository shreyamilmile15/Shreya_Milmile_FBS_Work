from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    @abstractmethod
    def calSal(self):
        pass

    def display(self):
        print(f"ID = {self.id}\tName = {self.name}\tSalary = {self.sal}")


class HR(Employee):
    def __init__(self, id, name, sal, commission):
        super().__init__(id, name, sal)
        self.commission = commission

    def calSal(self):
        print(f"Final Salary of HR: {self.sal + self.commission}")

    def display(self):
        print(f"Commission = {self.commission}")
        super().display()


class Developer(Employee):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def calSal(self):
        print(f"Final Salary of Developer: {self.sal + self.bonus}")

    def display(self):
        print(f"Bonus = {self.bonus}")
        super().display()


# Storing objects in a List
employees = [
    HR(103, "Sid", 40000, 5000),
    Developer(105, "Rohit", 50000, 7000)
]

for emp in employees:
    emp.display()
    emp.calSal()
    print()