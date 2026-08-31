#Write a program to print prime numbers between 1 to 100.

n = int(input('enter the number: '))    
count = 0

while (count<n):
    for i in range(2,n):
        if n % i == 0:
            break

    else:
        print(n, end=" ")
        count += 1

    n += 1
