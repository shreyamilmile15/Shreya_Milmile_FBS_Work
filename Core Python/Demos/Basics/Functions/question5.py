#q5. WAP to check perfect number
#type1: without passing parameter, without returning value
def perfect():
    num = int(input('Enter the number: '))
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(True)
    else:
        print(False)
perfect()

#type2: with passing parameter, without returning value
def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(True)
    else:
        print(False)
num = int(input('Enter the number: '))
perfect(num)

#type3: without passing parameter , with returning value
def perfect():
    num = int(input('Enter the number: '))
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
result = perfect()
print(result)


#Type4: with passing parameter , with returning value
def perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
num = int(input('Enter the number: '))
result = perfect(num)
print(result)