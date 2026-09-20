add = lambda num1,num2: num1+num2
print(add(10,20))

# area of rectangle
area = lambda l, b: l*b
print(area(8,4))

# calculate cube
cube = lambda n: n**3
print(cube(2))

# calculate square
square = lambda n : n**2
print(square(7))

# calculate simple interest
SI = lambda p, r ,t : (p*r*t)/100
print(SI(200000,2,3))

# reverse 3 digit number
rev = lambda n: ((n%10)*100 + ((n//10)%10)*10 + (n//100))
print(rev(123))