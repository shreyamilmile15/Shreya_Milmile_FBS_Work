#WAP to print all numbers in a range divisible by a given number.

start = int(input('Enter starting num: '))
end = int(input('Enter ending num: '))
num = int(input('Enter the number by which you want to divide: '))
for i in range(start, end+1):
    if(i % num == 0):
        print(i)