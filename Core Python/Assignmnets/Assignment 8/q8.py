#Write a program find reverse of a number.

def reverse(n):
    temp = n
    rev_num = 0
    while (n>0):
        d = n%10
        rev_num = rev_num * 10 + d
        n //= 10
    
    return rev_num
n = int(input('enter number:'))
res = reverse(n)
print(res)