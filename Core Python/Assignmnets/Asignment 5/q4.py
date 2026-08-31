#WAP to print Armstrong number within a given range

start = int(input('enter starting  number: '))
end = int(input('enter end number: '))

for num in range(start, end+1):
    temp = num
    count = 0
    while(temp>0):                    # this while loop is just to count the digits
        temp = temp // 10
        count += 1
    #print(count)
    #print('Number:', num, 'Count:', count)

    temp = num
    sum = 0
    while(temp>0):             
        d = temp % 10
        temp = temp // 10
        sum += (d**count)
    if (sum == num):
         print("Armstrong number:", num)
#else:
 #   print(f'{n} is not amstrong number.')