#4.  Write a Python program that finds all pairs of elements in a list whose 
# sum is equal to a given value.

li = [2,4,3,5,7,8,9]
target = 11
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] + li[j] == target:
            print(li[i],li[j])