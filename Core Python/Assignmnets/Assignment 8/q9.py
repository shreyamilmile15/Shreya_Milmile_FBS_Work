#Write a program to check if entered number is a palindrome or not.

def palindrome(n):
    temp = n
    rev_num = 0
    while(n>0):
        d = n%10
        rev_num = rev_num * 10 + d
        n //= 10
    if rev_num == temp:
        return True
    else:
        return False
n = int(input('enter number:'))
res = palindrome(n)
print(f'{n} is palindrome.')