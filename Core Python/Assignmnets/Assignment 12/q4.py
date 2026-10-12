# 4. Python Program to Form a New String where the First Character and 
# the Last Character have been Exchanged 

s = input('Enter a string:')
if len(s) <=1:
    print(s)
else:
    new = s[-1] + s[1:-1] + s[0]
    print(new)
