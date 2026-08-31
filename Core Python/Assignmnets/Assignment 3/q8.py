import random

User_ID = input('Enter your User name: ')
password = input('Enter your password: ')

if (User_ID =='abc' and password =='123'):
    num = random.randint(1000,9999)                  # it will generate 4 digit pin randomly
    print('enter the displayed 4 digit number:',num)
    entered_num = int(input('enter number generated: '))

    if (entered_num == num):
        print('Success')
    else:
        print('Failed')
else:
    print('Incorrect information')

