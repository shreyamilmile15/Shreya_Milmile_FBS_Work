#Q4. filter out palindrome number between n number.

def palindrome(n):
    temp = n
    rev_num = 0
    while(n>0):
        d = n%10
        rev_num = rev_num*10+d
        n = n//10 
    if (rev_num == temp):
        return True
    else:
        return False
n = int(input('enter n:'))
res = filter(palindrome,range(1,n+1))
print(list(res))