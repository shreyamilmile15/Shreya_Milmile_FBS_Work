#Write a program to input electricity unit charges and calculate total electricity bill
#according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill



units = int(input('enter the units: '))
if (units <= 50):                           # for 1st 50 unit
    bill = units * 0.50
elif (units <= 150):                         # for next 100 unit
    bill = (units * 0.50) + ((units - 50)*0.75)
elif units <= 250:                            # for next 100 unit
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:                                         ##  above 250 unit
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharge = bill * 0.20
total_bill = bill + surcharge
print("Electricity Bill =", total_bill)