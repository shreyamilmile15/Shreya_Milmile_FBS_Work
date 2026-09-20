# A farmer has a field which is half in circle share and rest rectangle. 
# He needs to do fencing for entire field using barbed wire 5 times.
#  Circular section has radius 20m and rectangle length is 50 m and breadth is 40m.
#  If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

l = 50
b = 40
r = 20
semicircle = 3.14*r
boundary = l + b +b + semicircle
total_wire = boundary * 5
cost = total_wire * 35
print('total wire req.:',total_wire,'m')
print('total cost:', cost, 'rs')