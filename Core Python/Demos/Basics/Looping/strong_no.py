## WAP to check strong number
n = int(input('Enter the number: '))
temp = n
sum = 0
while(temp>0):
    d = temp % 10
    temp = temp//10
    fact = 1
    for i in range(1, d+1):
        fact *= i
    sum += fact
if (sum == n):
    print(f'{n} is strong number')
else:
    print(f'{n} is not a strong number')