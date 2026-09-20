#c. 1^1 + 2^2 + 3^3+ ...... n^n

def power_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**i
    return sum
n = int(input('enter n:'))
res = power_sum(n)
print(res)