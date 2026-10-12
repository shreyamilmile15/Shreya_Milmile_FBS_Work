#2. Write a program to find factorial of given number using recursion

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
n = int(input("enter the number:"))
print(f"Factorial of {n} is {fact(n)}")