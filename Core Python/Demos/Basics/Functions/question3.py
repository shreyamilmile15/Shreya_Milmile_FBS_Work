# WAP to check strong number
# Type 1

def strong():
    num = int(input('enter the number: '))
    temp = num
    sum = 0
    while (num>0):
        d = num % 10
        num //= 10
        fact = 1
        for i in range(1, d+1):
            fact *= i
        sum +=fact
    if(sum == temp):
        print(True)
    else:
        print(False) 
strong()

#Type 2
# with passing argument , without passing value

def strong(num):
    temp = num
    sum = 0
    while(num>0):
        d = num % 10
        num //=10
        fact = 1
        for i in range(1, d+1):
            fact *= i
        sum += fact
    if (sum == temp):
        print(True)
    else:
        print(False)
num = int(input('enter the number: '))
strong(num)

# type 3
# without giving parameter , with returning value

def strong():
    num = int(input('enter the number: '))
    temp = num
    sum = 0
    while(num>0):
        d = num % 10
        num //= 10
        fact = 1
        for i in range(1,d+1):
            fact *= i
        sum += fact
    if (sum == temp):
        return True
    else:
        return False

result = strong()
print(result)

# type 4
# with passing parameter, with returning value

def strong(num):
    temp = num
    sum = 0
    while(num>0):
        d = num% 10
        num //= 10
        fact = 1
        for i in range(1, d+1):
            fact*=i
        sum +=fact
    if (sum == temp):
        return True
    else:
        return False
num = int(input('enter the number: '))
result = strong(num)
print(result)