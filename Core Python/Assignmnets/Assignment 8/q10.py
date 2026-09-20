#Write a program to check if entered year is a leap year or not.

def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
year = int(input('enter year: '))
res = leap_year(year)
if res:
    print(f'{year} is leap year.')
else:
    print(f'{year} is not a leap year.')