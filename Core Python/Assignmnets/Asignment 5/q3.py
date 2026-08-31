P = int(input('Enter the number of passenger: '))
ticket_cost = int(input('Enter the price: '))
total_amt = 0
for i in range (1, P+1):
    age = int(input('Enter the age: '))
    
    if age < 12:
        amount = ticket_cost - (ticket_cost * 30 / 100)
        print('30% discount applied')

    elif age > 59:
        amount = ticket_cost - (ticket_cost * 50 / 100)
        print('50% discount applied')

    else:
        amount = ticket_cost
        print('No discount')

    print('Ticket amt =', amount)

    total_amt = total_amt + amount
print('Total amount for all passengers =', total_amt)