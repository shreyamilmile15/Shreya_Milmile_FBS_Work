#3. Write a program to find the second largest element in the list.
li = [40,20,90,100,96,22,78]
max = li[0]
smax = 0
for i in range(1, len(li)):
    if max < li[i]:
        smax = max
        max = li[i]
    elif smax < li[i]:
        smax = li[i]
print('Maximum element:',max)
print('Second maximum element:',smax)