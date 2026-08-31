#### using if else
#User_ID = input('Enter your User name: ')
#password = input('Enter your password: ')
#   print('User entered correct userid and password')
#else:
 #   print('It is wrong')


## using nested if else
User_ID = input('Enter your User name: ')
password = input('Enter your password: ')
if (User_ID=='abc'):
    if (password=='123'):
        print('Information is correct')
    else:
        print('Information is wrong')
else:
    print('Information is wrong')
