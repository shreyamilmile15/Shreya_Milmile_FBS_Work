#WAP to print sum of series upto n.

n = int(input('enter the value: '))
i = 1
sum = 0
while (i<=n):
    sum = sum + i
    i +=1
    print('sum =', sum)        # print all sum step by step
#print('sum =', sum)           # print only final sum (write outside loop)
    