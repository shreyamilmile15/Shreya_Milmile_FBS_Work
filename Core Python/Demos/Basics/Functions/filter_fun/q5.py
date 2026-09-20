#Q5. filter out armstrong number between n number.

def armstrong(n):
    temp = n
    count = 0
    while(temp>0):
        temp //=10
        count+=1
    temp = n
    sum = 0
    while(temp>0):
        d = temp%10
        temp//=10
        sum = sum+(d**count)
    if(sum == n):
        return True
    else:
        return False
n =  int(input('enter n:'))
res = filter(armstrong,range(1,n+1))
print(list(res))


