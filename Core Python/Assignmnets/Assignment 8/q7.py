#Write a program to find sum of digits of a number.

def sum_of_digit(n):
    sum = 0
    while (n>0):
        d = n%10
        sum = sum + d
        n = n//10
    return sum
n = int(input('enter number:'))
res = sum_of_digit(n)
print(res)