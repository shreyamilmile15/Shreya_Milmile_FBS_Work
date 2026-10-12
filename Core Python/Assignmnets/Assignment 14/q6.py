# 6. Write a Python program to find the two numbers whose product is 
# maximum among all the pairs in a given list of numbers. Use the 
# Python set.

li = [10, 20, 5, 40, 30]
s = set(li)
max = None
num1 = 0
num2 = 0
for x in s:
    for y in s:
        if x!= y:
            product = x * y
            if max is None or product > max:
                    max = product
                    num1 = x
                    num2 = y
print("Numbers:", num1, num2)
print("Maximum product:", max)