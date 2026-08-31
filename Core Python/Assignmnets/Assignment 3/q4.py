a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

if (a + b > c and a + c > b and b + c > a):  # one side  should be big
    print('Triangle is valid')
else:
    print('Triangle is not valid')