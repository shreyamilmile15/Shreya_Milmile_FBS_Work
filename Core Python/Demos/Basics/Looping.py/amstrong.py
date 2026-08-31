num = int(input('Enter the number: '))
temp = num
count = 0
while(temp>0):
    temp = temp//10
    count += 1
print(count)         # use to find the number of digits
temp = num
sum = 0
while(temp>0):
    d = temp % 10
    temp = temp // 10
    sum += (d**count)
if (sum == num):
    print(f'{num} is a Amstrong number.')
else:
    print(f'{num} is not a Amstrong number.')