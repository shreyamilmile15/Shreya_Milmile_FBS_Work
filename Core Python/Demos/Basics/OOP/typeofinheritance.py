class Electrical:
    def display(Self):
        print("Electrical")

class Mechanical:
    def display (self):
        print("Mechanical")
class Mechatronix(Electrical,Mechanical):
    def display(self):
       print("Mechatronix")
m = Mechatronix()
m.display()
