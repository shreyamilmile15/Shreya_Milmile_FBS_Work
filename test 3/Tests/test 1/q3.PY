# Write a program to accept distance in km and convert it into meters and centimeters both.

km = int(input('enter km:'))
m = km * 1000
cm = km * 100000
print('Distance in meter:',m)
print('Distance in centimeter:',cm)