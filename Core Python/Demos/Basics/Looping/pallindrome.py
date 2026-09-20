n = int(input('Enter the number: '))
temp = n
rev_num = 0
while(temp>0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num*10 + d
if(rev_num == n):
    print('The number is pallindrome.')
else:
    print('The number is not pallindrome.')



    