#6. Python Program to Take in a String and Replace Every Blank Space 
# with Hyphen

s = input('enter a string:')
new = ' '
for ch in s:
    if ch == ' ':
        new = new + '_'
    else:
        new = new + ch
print(new)
