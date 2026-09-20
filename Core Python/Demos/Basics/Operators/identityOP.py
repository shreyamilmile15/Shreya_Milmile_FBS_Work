# 1. is
x = 10
y = 10
z = 20
l1 = [10,20]
l2 = [10,20]
print(x is y)  # immutable - address r same
print(x is z)
print(l1 is l2) # mutable - address is diff.
print(id(x))    
print(id(y))
print(id(l1))
print(id(l2))

#2. is not
print(x is not z)