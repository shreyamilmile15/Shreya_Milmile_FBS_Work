#Q1. WAP to check prime number
# type 1: without giving parameter, without returning value

def prime():
    num = int(input('enter the number: '))
    for i in range(2,num):
        if(num % i == 0):
            print(False)
        else:
            
            print(True)
prime()

#type2
# with passing parameter , without returning value

def prime(num):
    for i in range(2,num):
        if(num%i==0):
            print(False)
        else:
            print(True)
num = int(input('enter number: '))
prime(num)

#Type3
# Without passing parament, with returning value

def prime():
    num = int(input('enter the number: '))
    for i in range(2,num):
        if(num % i == 0):
            return False
        else:
            return True
result = prime()
print(result)

# Type 4
# with passing parameter , with returning value 

def prime(num):
    for i in range(2,num):
        if(num % i == 0):
            return False
            
            return True
num = int(input('enter the number: '))
result = prime(num)
print(result)