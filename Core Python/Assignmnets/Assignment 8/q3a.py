#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n

def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum
n = int(input('enter n: '))
res = sum(n)
print('sum of series',res)