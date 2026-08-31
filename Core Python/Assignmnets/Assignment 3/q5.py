a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))
if (a==b and b==c):                   # all side are equal
    print('Triangle is Equilateral.')
elif (a==b or b==c or c==a):          # 2 side are equal
    print('Triangle is Isosceles.')
else:                                     
    print('Triangle is Scalene.')      # no side is equal