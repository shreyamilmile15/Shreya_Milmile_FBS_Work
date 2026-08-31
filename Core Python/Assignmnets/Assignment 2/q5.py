CP = float(input("Enter cost price: "))
discount = float(input("Enter discount %: "))

discount_amt = CP * discount / 100
SP = CP - discount_amt
print('discount amount',discount_amt)

print("Selling Price =", SP)