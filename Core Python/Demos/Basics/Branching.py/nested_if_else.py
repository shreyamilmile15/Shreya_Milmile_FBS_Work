gender = input('enter gender(M/F):')
age = int(input('enter age:'))
if(gender == ' F'):
    if(age >= 18):
        print("girl is eligible for marriage")
    else:
        print('not eligible')
else:
    if(age >= 21):
        print('Boy is eligible for marriage.')
    else:
        print('not eligible')
