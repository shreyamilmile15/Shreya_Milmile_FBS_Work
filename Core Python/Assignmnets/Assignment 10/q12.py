#12. Write a program to create three lists of numbers, their squares
#  and cubes.

li = [2, 3, 4, 5, 6, 7]
square = []
cube = []
for i in li:
    square = square + [i**2]
    cube = cube + [i**3]
print(f'{li} is list of number.')
print(f'{square} is square of list.')
print(f'{cube} is cube of list.')