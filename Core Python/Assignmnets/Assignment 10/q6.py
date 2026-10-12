# 6. Write a program to remove duplicates from the list.

li = [10,20,30,40,50,50,30]
new_li = []
for i in li:
    found = False
    for j in new_li:
        if i == j:
            found = True
            break

    if found == False:
        new_li = new_li + [i]
print(new_li)
