#14.  Python Program to count the occurrences of ach word in a string. 
s = input('Enter a string:')
words = s.split()
for word in words:
    count = 0
    for w in words:
        if word == w:
            count += 1
    print(word,':',count)
 
