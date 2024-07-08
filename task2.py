import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min < 1 or max > 1000:
            print('Input error: min value should be >= 1, and max value should be < 1000')
        else:
            numbers = random.sample(range(min, max), quantity)
            numbers.sort()

            print('Your lucky numbers: ', numbers)
    except ValueError:
        print('Min value larger than max value')
        
try:
    min = int(input('Enter min value: '))
    max = int(input('Enter max value: '))
    quantity = int(input('Enter quantity: '))
    get_numbers_ticket(min, max, quantity)  
except ValueError:
    print('Incorrect input: Values should be type of integer')

