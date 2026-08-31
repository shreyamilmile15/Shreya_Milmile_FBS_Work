# 1. pass: escape from unexpected intendation error
for i in range(1,10):
    pass

#2. break:  for terminating the loop
for i in range(1,10):
    if(i==5):
        break
    print(i)

#3. continue:  to stop particular iteration
for i in range(1,10):
    if(i==5):
        continue
    print(i)

#4. else: will execute when loop execute successfully
for i in range(1,10):
    if(i==5):
        #break        # it will break the loop d
        continue
    
    print(i)
else:
    print('Else block execute')