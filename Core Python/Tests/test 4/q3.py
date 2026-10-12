def pattern():
    print("*" * 22)
    spaces = 22
    for i in range(10):
        print(" " * spaces + "*")
        spaces = spaces - 2
    print("*" * 21 + " *")
pattern()