# Write a program to print Fibonacci series using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
n = int(input('enetr n:'))
res = fibonacci(n)
print(res)
