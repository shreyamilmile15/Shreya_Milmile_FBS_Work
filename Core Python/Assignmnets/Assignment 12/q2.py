#2. Python Program to Remove the nth Index Character from a Non-Empty 
# String 

str = input('enter string:')
n = int(input('enter the index:'))
new = ''
for ch in range(len(str)):
    if ch != n:
        new = new + str[ch]

print(new)
