li = [10, 20, 30, 40, 50, 60, 70]
sum = 0

# method 1: Iterating values
#for ele in li:
#    sum += ele

# Method 2: Using indexing
for ind in range(0, len(li)):     #len(li) will give length of list
    sum += li[ind]

print(sum)

