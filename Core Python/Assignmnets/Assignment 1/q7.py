import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b*b - 4*a*c

r1 = (-b + 0.5**(d)) / (2*a)
r2 = (-b - 0.5**(d)) / (2*a)

print("Roots are:", r1, r2)