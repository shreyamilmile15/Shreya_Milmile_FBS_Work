#9. Python Program to Calculate the Number of Words and the Number of 
# Characters Present in a String 

s = input('Enter a string: ')
char_count = 0
word_count = 0
for ch in s:
    char_count += 1
    if ch == ' ':
        word_count += 1
if char_count > 0:
    word_count+= 1

print('Number of characters is ', char_count)
print('Number of words is ', word_count)