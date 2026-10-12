#Write a program to create a duplicate of an existing list. 
# It should not point to same list.

li = [10,20,30,40,50]
li2 = []
for i in li:
    li2 = li2 + [i]
print('Original list:',li)
print('Duplicate list:',li2)

#li2[1] = 80
#print('Duplicate list after updation:',li2)  