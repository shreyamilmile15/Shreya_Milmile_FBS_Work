num = int(input('Enter a 3 digit number: '))
original = num
a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10

reverse = a * 100 + b * 10 + c

if original == reverse:
    print('Number is palindrome')
else:
    print('Not palindrome')