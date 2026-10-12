# 5. Python Program to Count the Number of Vowels in a String 

s = input('enter a string:')
count = 0
for ch in s:
    if ch =='a'or ch == 'e'or ch == 'i'or ch == 'o'or ch == 'u':
        count += 1
print('Number of vowels are',count)
