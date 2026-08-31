n = int(input("Enter a three-digit number: "))
d1 = n % 10
n = n // 10
print(d1)
d2 = n % 10
n = n // 10
print(d2)
d3 = n % 10
print(d3)
reverse = d1 * 100 + d2 * 10 + d3

print("Reverse number =", reverse)