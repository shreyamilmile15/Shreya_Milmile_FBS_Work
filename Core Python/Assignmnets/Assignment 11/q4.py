#4. Python Program to Find the Second Largest Number in a List Using Bubble 
#Sort 

li = [30, 50, 90, 70, 10, 20]
for i in range(len(li) - 1):
    for j in range(len(li) - 1 - i):
        if li[j] > li[j + 1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

print('Sorted list:', li)
print('Second largest:', li[-2])