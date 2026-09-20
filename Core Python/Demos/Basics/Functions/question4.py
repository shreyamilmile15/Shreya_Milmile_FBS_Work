# WAP to check armstrong number

# type 1
# without passing parameter, without returnig value

def armstrong():
    num = int(input('enter the number: '))
    temp = num
    count = 0
    while(temp>0):
        temp = temp // 10
        count+= 1
    temp = num
    sum = 0
    while(temp>0):
        d = temp % 10
        temp = temp// 10
        sum = sum + (d**count)
    if(sum == num):
        print (True)
    else:
        print( False)
armstrong()


# type 2
# with passing parameters, without returning value

def armstrong(num):
    
    temp = num
    count=0
    while(temp>0):
        temp = temp // 10
        count +=1
    temp = num
    sum = 0
    while (temp>0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d**count)
    if(sum == num):
        print(True)
    else:
        print(False)
num = int(input('enter the number:'))
armstrong(num)

# type 3
# without passing parameter, with returning value

def armstrong():
    num = int(input('enter the number'))
    temp = num
    count= 0
    while(temp>0):
        temp //=10
        count +=1
    temp = num
    sum = 0
    while(temp>0):
        d = temp %10
        temp //=10
        sum = sum + (d**count)
    if(sum == num):
        return True
    else:
        return False
result = armstrong()
print(result)

# type 4
# with passing output, with returning value

def armstrong(num):
    temp = num
    count = 0
    while(temp>0):
        temp //=10
        count+=1
    temp = num
    sum = 0
    while(temp>0):
        d = temp%10
        temp//=10
        sum = sum+(d**count)
    if(sum == num):
        return True
    else:
        return False
num =  int(input('enter the number:'))
result = armstrong(num)
print(result)
