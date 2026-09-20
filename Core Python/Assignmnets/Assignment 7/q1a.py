for i in range(1,11):
    for j in range(1,11):
        if(i+j==6 and i-j==4):
            print('*', end= ' ')
        else:
            print('')
    print()