#10. Write a program to remove all occurrences of a given element in the list.

li = [10,20,30,40,50,10,20,20]

ele = int(input('Enter element to remove:'))
new_li = []
for i in li:
    if i != ele:
        new_li = new_li + [i]
print("Original list is", li)
print("New list is", new_li)