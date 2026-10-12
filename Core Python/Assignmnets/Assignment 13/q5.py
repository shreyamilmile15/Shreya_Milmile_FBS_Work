# 5. Python Program to Sum All the Items in a Dictionary

d = {'a': 10, 'b': 20, 'c': 75, 'd': 50}
sum = 0
for value in d.values():
    sum = sum + value
print("Sum is", sum)