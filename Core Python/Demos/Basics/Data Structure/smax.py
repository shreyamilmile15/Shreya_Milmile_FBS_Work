# find max, smax, tmax

li = [30,50,90,70,10,20]
max = li[0]
smax = 0
tmax = 0
for ind in range(1,len(li)):
    if li[ind]>max:
        smax = max
        tmax = smax
        max = li[ind]
    elif (li[i]>tmax):
        smax = li[ind]
    elif (li[i]>smax):
        tmax = li[ind]
print('Max',max)
print('Smax',smax)
print('tmax',tmax)
    