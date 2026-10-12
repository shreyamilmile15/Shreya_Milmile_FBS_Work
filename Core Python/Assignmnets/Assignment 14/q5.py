#5. Write a Python program to find the longest common prefix of all 
# strings. Use the Python set. 

li = ['liquid','lion','light','lite']
prefix = ''
for i in range(len(li[0])):
    s = set()
    for word in li:
        if i < len(word):
            s.add(word[i])
    if len(s) == 1:
        prefix += li[0][i]
    else:
        break
print('Longest common prefix:',prefix)