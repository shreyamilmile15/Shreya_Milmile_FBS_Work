basic = float(input("Enter basic salary: "))
DA = 10 / 100 * basic
TA = 12 / 100 * basic
HRA = 15 / 100 * basic
total = basic + DA + TA + HRA
print("DA",DA)
print("TA",TA)
print("HRA",HRA)
print("Total Salary =", total)