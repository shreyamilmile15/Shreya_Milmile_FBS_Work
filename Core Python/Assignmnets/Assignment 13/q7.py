# 7. Python Program to Remove the Given Key from a Dictionary.

d = {'name': 'XYZ', 'age': 22, 'city': 'Pune'}
key = input("Enter key to remove: ")
if key in d:
    d.pop(key)
    print(d)
else:
    print("Key does not exist")