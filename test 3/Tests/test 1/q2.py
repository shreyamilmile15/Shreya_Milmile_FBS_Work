#Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

P = int(input('enter P:'))
R = int(input('enter R:'))
T = int(input('enter T:'))

SI = (P*R*T)/100
print('Simple interest is:',SI)