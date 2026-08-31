x = 5
y = 10
print(f'before swapping x:{x} , y:{y}.')
z=y
y=x
x=z
print(f'after swapping x:{x} , y:{y}.')

## Swapping without 3rd variable

x = 15
y = 3
print(f'before swapping x:{x} , y:{y}.')
x,y = y,x
print(f'after swapping x:{x} , y:{y}.')