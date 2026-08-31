'''for i in range(1,6):
    for j in range (1,5):
        print('*', end = ' ')
    print()

# print same value in row
for i in range(1,6):           #change in  row
    for j in range (1,5):      # change in column
        print(i, end = ' ')    # chnage in printing
        
    print()

#  print same value in column
for i in range(1,6):           #change in  row
    for j in range (1,5):      # change in column
        print(j, end = ' ')    # chnage in printing
        
    print()

'''

letters = "ABCDE"

for i in letters:
    for j in range(5):
        print(i, end=' ')
    print()