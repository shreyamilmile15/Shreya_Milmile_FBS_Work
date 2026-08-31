m1 = int(input('Enter marks of subject 1: '))
m2 = int(input('Enter marks of subject 2: '))
m3 = int(input('Enter marks of subject 3: '))
m4 = int(input('Enter marks of subject 4: '))
m5 = int(input('Enter marks of subject 5: '))
total = (m1 + m2 + m3 + m4 + m5)
print('total',total)
percentage = total / 5
print('percentage',percentage)

if percentage >= 75:
    print('Distinction')
elif percentage >= 60:
    print('First Class')
elif percentage >= 50:
    print('Second Class')
else:
    print('Fail')