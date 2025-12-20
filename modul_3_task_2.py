import random

def get_numbers_ticket(min, max, quantity):
    if min > max or quantity <= 0 or quantity > (max - min + 1):    
        return print("Invalid value entered")
    return sorted(random.sample(range(min, max), quantity))


print("Welcome to the lottery! ")
try:
    min = int(input("Enter minimum value: "))
    max = int(input("Enter maximum value: "))
    quantity = int(input("Enter the number of numbers from the pool: "))
    ticket = get_numbers_ticket(min, max, quantity)
    print(ticket)
except (ValueError, TypeError):
    print("You entered an invalid number, please try again! ")