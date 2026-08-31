correct_userid = 'abc'
correct_pass = '@123'

for i in range(3):
    userid = input('Enter User ID: ')
    password = input('Enter Password: ')

    if userid == correct_userid and password == correct_pass:
        print("Login Successful!")
        break
    else:
        print('Incorrect User ID or Password')

else:
    print('You have used all 3 attempts. Program terminated.')