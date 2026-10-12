#7. Given two sets of numbers, write a Python program to find the missing 
# numbers in the second set as compared to the first and vice versa. 
# Use the Python set. 

s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}
missing_in_s2 = s1 - s2
missing_in_s1 = s2 - s1
print('Numbers missing in second set:', missing_in_s2)
print('Numbers missing in first set:', missing_in_s1)