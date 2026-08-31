P = int(input('enter value of P:'))
R = int(input('enter value of R:'))
T = int(input('enter value of T:'))
Compound_Interest = P*(1+R/100)**T-P
print(f'Compound Interest is {Compound_Interest}.')