#1. Python Program to Put Even and Odd elements of a List into two Different 
# Lists.

li = [5,10,15,20,25,30,35,40,45,50]
even_ele = []
odd_ele = []
for i in li:
    if i % 2 == 0:
        even_ele = even_ele + [i]
    else:
        odd_ele = odd_ele + [i]
print('Even element:',even_ele)
print('Odd element:',odd_ele) 