# Write a program to check whether a number is prime or not using recursion.

def prime(n,i):
    if i == 1:
        return True
    if n % i == 0:
        return False
    else:
        return prime(n,i-1)
n = int(input('enter the number:'))
if n <= 1:
    print('Not prime.')
elif prime(n, n//2):
    print('prime')
else:
    print('not prime')