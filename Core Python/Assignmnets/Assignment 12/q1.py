#1. Python Program to Replace all Occurrences of ‘a’ with $ in a String 

str = input('Enter a string:')
new = ''
for i in str:
    if i == 'a':
        new = new + '$'
    else:
        new = new + i
print(new)
