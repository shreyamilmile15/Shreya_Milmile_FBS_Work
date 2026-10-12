# 2. Python Program to Concatenate Two Dictionaries Into One 

d1 = {'Name':'ABC', 'Emp_id': 101}
d2 = {'Dept':'IT'}
d3 ={}
for key in d1:
    d3[key] = d1[key]
for key in d2:
    d3[key] = d2[key]
print(d3)