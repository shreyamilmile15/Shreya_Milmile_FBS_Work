#15.  Python Program to find larger string without using built-in functions.
s1 = input('enter a string:')
s2 = input('enter a string:')
count1 = 0
count2 = 0
for ch in s1:
    count1 += 1
for ch in s2:
    count2 += 1
if count1 > count2:
    print(f'{s1} is largest string.')
elif count1 < count2:
    print(f'{s2} is largest string.')
else:
    print('both are equal.') 