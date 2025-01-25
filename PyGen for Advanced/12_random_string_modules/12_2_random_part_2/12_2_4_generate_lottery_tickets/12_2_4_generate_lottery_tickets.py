'''
TODO:
    Write a program that uses the random module to generate 100 random lottery
    ticket numbers and print them, each on a separate line.

    Note that you must adhere to the following conditions:
        the number cannot start with zeros;
        the lottery ticket number must consist of 7 digits;
        all 100 lottery tickets must be different.
'''
import random


def generate_lottery_tickets(count: int = 100) -> set:
    """
    Generates a set of unique 7-digit random lottery ticket numbers.
    Each ticket number is between 1,000,000 and 9,999,999, inclusive.

    Args:
        count (int): The number of unique lottery tickets to generate
                     (default is 100).

    Returns:
        set: A set of unique lottery ticket numbers.
    """
    lottery_tickets: set = set()

    while len(lottery_tickets) < count:
        # Generates a 7-digit number
        ticket_number = random.randint(1000000, 9999999)
        lottery_tickets.add(ticket_number)

    return lottery_tickets


tickets = generate_lottery_tickets()
print(*tickets, sep='\n')
