# 8. Write a Python program to find all the anagrams and group them 
# together from a given list of strings.

li = ["listen", "silent", "enlist", "rat", "tar", "art", "hello"]
groups = {}
for word in li:
    key = ''.join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
for value in groups.values():
    print(value)