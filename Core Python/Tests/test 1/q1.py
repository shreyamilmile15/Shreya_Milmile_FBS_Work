l = int(input('Enter l:'))
b = int(input('Enter b:'))
r = b/2
area_rec = l* b
area_semicircle = 0.5 * 3.14* r * r
area = area_rec + area_semicircle

peri_rec = 2*(l+b)
peri_semicircle = 3.14 * r
peri = 2*l+b+3.14*r

print('Total area of fig.',area)
print('Total perimeter of fig.',peri)