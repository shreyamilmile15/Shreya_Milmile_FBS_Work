#Q1. Write a program to calculate area of rectangle.

def area_of_rectangle(l,b):
    area = l*b
    return area
l = int(input('enter the length: '))
b = int(input('enter the breadth: '))
res = area_of_rectangle(l,b)
print(f'{res} is area of rectangle.')