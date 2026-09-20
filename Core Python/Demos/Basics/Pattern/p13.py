for i in range(1,6):
    for j in range(1,i+1-1):       #if we take i+1 then 1 extra column will print to remove that change in range is done.
        print(' ',end= ' ')
    for j in range(1,7-i):       # for decrement pattern
        print('*', end= ' ')
    print()