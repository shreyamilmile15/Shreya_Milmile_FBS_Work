#q2. Write a program to calculate area of circle

def area_of_circle(radius):
    area = 3.14 * radius**2
    return area
radius = int(input('enter the radius: '))
res = area_of_circle(radius)
print(f'{res} is area of circle.')