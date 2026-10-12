# 6. Python Program to Multiply All the Items in a Dictionary 
d = {'a': 2, 'b': 5,'c':3,'d':4}
multi = 1
for value in d.values():
    multi *= value
print('Multiplication is:',multi)