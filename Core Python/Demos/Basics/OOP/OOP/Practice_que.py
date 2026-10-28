#q1 add 2 no.
# a = int(input("Enter first integer: "))
# b = int(input("Enter second integer: "))
# sum = a + b
# print("Addition =", sum)

#Q2. add 2 string
# a = input("Enter first string: ")
# b = input("Enter second string: ")
# s = a + " " +b
# print("Addition of two string is", s)

#Q3. add 2 floating no.
# a = float(input("Enter the number:"))
# b = float(input("Enter the number:"))
# sum = a+b
# print("Addition is", sum)

#Q4. add 2 list
# a = [10, 20, 30]
# b = [40, 50, 60]
# add = a + b
# print("Addition of 2 list is ", add)

#Q5. add two times

class Time:
    def __init__(self,hr,min,sec):
        self.hr = hr
        self.min = min
        self.sec = sec
    def __str__(self):
        return f"{self.hr} : {self.min} : {self.sec}"
    def __add__(self,other):
        # thr = self.hr+other.hr
        # tmin = self.min+other.min
        # tsec = self.sec+other.sec
        # return Time(thr,tmin,tsec)
        
        tsec = self.sec + other.sec
        emin = tsec//60
        tsec = tsec % 60
        tmin = self.min + other.min + emin
        ehr = tmin//60
        tmin = tmin%60
        thr = self.hr+other.hr + ehr
        return Time(thr,tmin,tsec)
    
t1 = Time(12,33,55)
t2 = Time(6,30,56)
t3 = Time(1,1,1)
a = t1+t2+t3
print(a)