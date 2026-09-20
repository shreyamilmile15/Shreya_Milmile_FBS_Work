area = int(input('Enter area of one wall: '))
interior_cost = int(input('Enter interior painting cost per wall: '))
exterior_cost = int(input('Enter exterior painting cost per wall: '))

interior_total = area * interior_cost
exterior_total = area * exterior_cost

total_cost = interior_total + exterior_total

print("Interior painting cost:", interior_total)
print("Exterior painting cost:", exterior_total)
print("Total painting cost:", total_cost)