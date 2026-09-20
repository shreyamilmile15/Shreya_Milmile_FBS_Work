# Write a program to find sum of digits using recursion.

def sum_of_digits(n):
    if n == 0:
        return 0
    d = n%10
    return(d +sum_of_digits(n//10))
n = int(input('enter the number:'))
res = sum_of_digits(n)
print(f'{res} is sum of digits in {n}')
