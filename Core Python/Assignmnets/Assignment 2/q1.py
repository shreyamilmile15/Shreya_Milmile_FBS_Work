hh = int(input("Enter hours: "))
min = int(input("Enter minutes: "))
sec = int(input("Enter seconds: "))

total = (hh * 60 * 60) + (min * 60) + sec

print("Time in seconds =", total)