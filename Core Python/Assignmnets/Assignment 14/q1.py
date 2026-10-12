#1. Write a Python program to find elements in a given set that are not in 
# another set. 

s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 60, 70}
result = s1 - s2
print('Elements in s1 but not in s2:', result)