#11.  Python Program to replace every blank space with hyphen in a string. 
s = input('Enter a string:')
new = ' '
for ch in s:
    if ch == ' ':
        new += '-'
    else:
        new += ch
print(new)