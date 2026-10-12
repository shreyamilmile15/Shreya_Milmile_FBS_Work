class Transport:
    def __init__(self, number, type, capacity):
        self.number = number
        self.type = type
        self.capacity = capacity

    def calFare(self):
        print(f"Fare of Transport depend upon Transport type.")

## Transport class ends here

class RoadTransport(Transport):
    def __init__(self, number, type, capacity, wheels):
        super().__init__(number, type, capacity)
        self.wheels = wheels

    def calFare(self, distance):
        print(f"Fare of Road Transport = {distance * 10}")

## RoadTransport class ends here

class AirTransport(Transport):
    def __init__(self, number, type, capacity, airline):
        super().__init__(number, type, capacity)
        self.airline = airline

    def calFare(self, distance):
        print(f"Fare of Air Transport = {distance * 50}")

## AirTransport class ends here

t1 = Transport(101, "Transport", 50)
r1 = RoadTransport(11, "Bus", 50, 6)
a1 = AirTransport(21, "Flight", 180, "IndiGo")

t1.calFare()
r1.calFare(100)
a1.calFare(100)