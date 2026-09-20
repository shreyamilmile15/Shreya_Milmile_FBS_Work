year = int(input('enter year:'))
if year % 400 == 0:
    print('Leap year.')
elif year % 100 == 0:
    print('Not a leap year.')
elif year % 4 == 0:
    print('Leap Year.')
else:
    print('not a leap year')

