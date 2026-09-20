# check no. is prime or not

#num = int(input('enter the number: '))
#for i in range(2,num):
 #   if(num%i==0):
  #      print(f'{num} is not prime number.')
   #     break
#else:
 #   print(f'{num} is prime number.')



# WAP to print prime number between 1 to n
n = int(input('enter the number: '))    
for num in range(2,n):              # for loop: to generate the number
    for i in range(2, num):         # for loop: to check the prime number
        if(num % i == 0):
            break
    else:
            print(num, end=" ")
    
    

# WAP to print first n prime number