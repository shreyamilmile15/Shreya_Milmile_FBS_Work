#2. Write a program to find maximum and minimum element in a list.

li = [20,30,50,90,2,15]
max_ele = li[0]
min_ele = li[0]
for i in li:
    if max_ele < i:
        max_ele = i
    if min_ele > i:
        min_ele = i
print('Maximum element is:',max_ele)
print('Minimum element is:',min_ele)




