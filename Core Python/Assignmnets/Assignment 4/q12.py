# WAP to check amstrong number

n = int(input('enter the number: '))
temp = n
count = 0
while(temp>0):                    # this while loop is just to count the digits
    temp = temp // 10
    count += 1
print(count)

temp = n
sum = 0
while(temp>0):             
    d = temp % 10
    temp = temp // 10
    sum += (d**count)
if (sum == n):
    print(f'{n} is amstrong number.')
else:
    print(f'{n} is not amstrong number.')

