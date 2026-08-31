a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if (a + b + c == 180):                  # sum of angle of triangle is 180
    print("Triangle is valid")
else:
    print("Triangle is not valid")