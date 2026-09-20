num = int(input('How many fibonacci number you want: '))
a = -1              # out of the loop because we want -1 & +1  only one time
b = 1
for i in range(num):
    c = a+b            # we want c multiple time
    print(c, end = " ")
    a = b
    b = c