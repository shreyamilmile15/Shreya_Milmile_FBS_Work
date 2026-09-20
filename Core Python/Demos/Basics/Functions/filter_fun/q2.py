#Q2. filter out prime number between n number.

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True
n = int(input('Enter n: '))
res = filter(prime, range(2, n + 1))
print(list(res))
        

