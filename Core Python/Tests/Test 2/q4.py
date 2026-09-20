#Write a program to calculate the total cost of painting. The interior of building with four equal sized walls. 
l = int(input('enter length of wall:'))
h = int(input('enter height of wall:'))
rate = int(input('enter painting rate:'))
area = 4*l*h
cost = area * rate
print('total area', area,'sq. m')
print('total painting cost:',cost,'rs')