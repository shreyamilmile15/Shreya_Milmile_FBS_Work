#WAP to print Fibonacci series upto n.

n = int(input('How many fibonacci number u want: '))
a = 1
b = 2

for i in range(n):
    c = a+b            # we want c multiple time
    print(c, end = " ")
    a = b
    b = c
