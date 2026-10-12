#7. Python Program to Find the Intersection of Two Lists.
li = [10,20,30,40,50]
li2 = [20,30,40,60,70]
intersection = []
for i in li:
    if i in li2:
        intersection.append(i)
print('Intersection:',intersection)