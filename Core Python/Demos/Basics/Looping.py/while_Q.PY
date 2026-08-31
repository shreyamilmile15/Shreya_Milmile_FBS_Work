num = 367
while(num>0):
    d = num % 10
    print(d)
    num = num//10


# input from user
num = int(input('enter the number:'))
while(num>0):
    d = num % 10  # gives remainder
    print(d)
    num = num//10  # gives quotient


## Sum of the digit
num = int(input('enter the number:'))
sum = 0
while(num>0):
    d = num % 10  # gives remainder
    #print(d)
    sum += d
    num = num//10
print(f'sum is {sum}')