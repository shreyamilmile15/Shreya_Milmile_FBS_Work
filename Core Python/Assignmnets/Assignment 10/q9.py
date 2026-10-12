# Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

li = [5,10,15,20,25,30,35,40,45,50]
even_li =[ ]
odd_li = [ ]
for i in li:
    if i % 2 == 0:
        even_li = even_li +[i]
    elif i %2 != 0:
        odd_li = odd_li + [i]
print(f'{even_li} is Even element list.')
print(f'{odd_li} is Odd element list.')
