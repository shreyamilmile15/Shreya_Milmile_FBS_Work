n = int(input('enter no. of emp:' ))
total = 0
for i in range(1, n+1):
    basic_sal = int(input('enetr the amount:'))
    if basic_sal < 20000:
        da = basic_sal *10/100
        ta = basic_sal*12/100
        hra = basic_sal*20/100
    else:
        da = basic_sal *15/100
        ta = basic_sal*18/100
        hra = basic_sal*20/100
    salary = basic_sal + da+ ta+ hra
    print('total salary is',salary)
    total = total + salary
print('total salary of employee is',total)