# Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list.

li = [10,20,30,40,50,10]
num = int(input('enter the number:'))
count = 0
for i in li:
    if i == num:
        count += 1
if count > 0:
    print('element is present.')
    print(f'{num} occurs {count} times.')
else:
    print('element is not present.')       