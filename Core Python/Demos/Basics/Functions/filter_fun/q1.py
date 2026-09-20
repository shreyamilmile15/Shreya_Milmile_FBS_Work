#Q1. filter out perfect number between n number.

def perfect(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum == n
n = int(input('enter value of n:'))
res = filter(perfect,range(1,n+1))
print(list(res))
        