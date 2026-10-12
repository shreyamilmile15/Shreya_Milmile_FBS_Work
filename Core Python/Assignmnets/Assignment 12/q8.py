#8. Python Program to Remove the Characters of Odd Index Values in a 
# String

s = input('Enter a string:')
new_str = ' '
for i in range(len(s)):
    if i % 2 == 0:
        new_str = new_str + s[i]
print('new string is',new_str)