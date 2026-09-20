#Q3. filter out strong number between n number.


def strong(n):
    temp = n
    sum = 0
    while(n>0):
        d = n%10
        n = n//10
        fact = 1
        for i in range(1,d+1):
            fact *= i
        sum += fact
    if (sum == temp):
        return(True)
    else:
        return False
n = int(input('enter n:'))
res = filter(strong,range(1, n+1))
print(list(res))