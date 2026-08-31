feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

total_inches = feet * 12 + inches
cm = total_inches * 2.54
m = cm / 100

print("Distance in meter =", m)
print("Distance in centimeter =", cm)