n = int(input('Enter number of students: '))

total_percentage = 0

for i in range(1, n + 1):
    
    marks = 0
    
    print('Student', i)
    
    for j in range(1, 6):
        m = int(input('Enter marks: '))
        marks = marks + m
    
    percentage = marks / 5
    
    print('Percentage =', percentage)
    
    total_percentage = total_percentage + percentage

average = total_percentage / n

print('Average percentage =', average)