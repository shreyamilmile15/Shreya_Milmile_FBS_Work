#(b) 1! + 2! + 3! + ... + n!

def fact_sum(n):
    sum = 0
    fact = 1
    for i in range(1, n+1):
        sum = sum+1
        fact = fact * i
    return fact
n = int(input('enter n:'))
res = fact_sum(n)
print(res)