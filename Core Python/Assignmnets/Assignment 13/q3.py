#3. Python Program to Check if a Given Key Exists in a Dictionary or Not 

d = {'Name':'ABC', 'Gender':'F', 'Age':30}
key = input('Enter key:')
if key in d:
    print('Key exist.')
else:
    print("Key doesn't exist")