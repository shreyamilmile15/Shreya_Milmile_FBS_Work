# 3. Write a Python program to find all the unique words and count the 
# frequency of occurrence from a given list of strings. Use Python set 
# data type. 

li = ['Mango','Mango','pears','Apple','Banana']
unique = set(li)
for word in unique:
    count = 0
    for x in li:
        if word == x:
            count += 1
    print(word,":", count)