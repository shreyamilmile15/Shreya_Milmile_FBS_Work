# Q2.check palindrome number
# type 1: without passing parameter, without returning value

def palindrome():

    num = int(input("Enter the number: "))
    temp = num
    rev_num = 0
    while(num > 0):
        d = num % 10
        rev_num = rev_num * 10 + d
        num = num // 10

    if(rev_num == temp):
        print(True)
    else:
        print(False)

palindrome()


# Type2
# with giving parameter, without returnong value

def palindrome(num):
    temp = num
    rev_num = 0
    while(num>0):
        d = num % 10
        rev_num = rev_num * 10 + d
        num = num // 10
    if(rev_num == temp):
        print(True)
    else:
        print(False)
num = int(input('enter the number: '))
palindrome(num)

#type3
#without giving parameter , with returning value
def palindrome():
    num = int(input('enter the number: '))
    temp = num
    rev_num = 0
    while(num>0):
        d = num % 10
        num = num // 10
        rev_num = rev_num *10 + d

    if(rev_num == temp ):
        return True
    else:
        return False

result = palindrome()
print(result)


# Type 4
#with giving parameter , with returning Value

def palindrome(num):
    temp = num
    rev_num = 0
    while(num>0):
        d = num% 10
        num //=10
        rev_num = rev_num*10 + d
    if(rev_num == temp):
        return True
    else:
        return False
num = int(input('enter the value: '))
result= palindrome(num)
print(result)
