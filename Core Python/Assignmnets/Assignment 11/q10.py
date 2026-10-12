#10. Write a program to print list after removing even numbers.

li = [5,10,15,20,22,43,50,11,77]
odd = []
for i in li:
    if i % 2 != 0:
        #odd = odd +[i]
        odd.append(i)
print(odd)
