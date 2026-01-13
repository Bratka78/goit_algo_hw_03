import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min > max or quantity <= 0 or quantity > (max - min + 1) or min <= 0 or max >= 1000:
            return []
        return sorted(random.sample(range(min, max), quantity))
    except (ValueError, TypeError):
        return []

print("Welcome to the lottery! ")
min = 1
max = 20
quantity = 10
ticket = get_numbers_ticket(min, max, quantity)

print(ticket)