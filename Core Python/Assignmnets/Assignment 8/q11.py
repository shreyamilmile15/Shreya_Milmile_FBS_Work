# WAP to check if a given number is Armstrong number or not. For
#  each task create separate functions.

def armstrong(n):
    temp = n
    count = 0
    sum = 0
    while(n>0):
        count +=1
        n //= 10
    n = temp
    sum = 0
    while(n>0):
        d = n%10
        sum = sum + (d**count)
        n //= 10
    if sum == temp:
        return True
    else:
        return False
n = int(input('enter number:'))
res = armstrong(n)
print(res)