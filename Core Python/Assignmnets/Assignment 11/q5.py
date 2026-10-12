#5. Python Program to Sort a List According to the Length of the Elements 
# within the list.

li = ['Watermelo','Kiwi','Banana','Apple']
for i in range(len(li)):
    for j in range(i+1, len(li)):
        if len(li[i]) > len(li[j]):
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print(li)