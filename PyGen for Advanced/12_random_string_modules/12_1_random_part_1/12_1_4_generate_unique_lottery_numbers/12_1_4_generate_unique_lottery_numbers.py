'''
TODO:
    The lottery ticket contains 7 numbers from 1 to 49 (inclusive).

    Write a program that uses the random module to generate 7 different random
    numbers for the lottery ticket.

    The program should output the numbers in ascending order on one line
    separated by one space.

NOTE:
    Make sure that the generated numbers do not contain duplicates.
'''
import random
from typing import List


def generate_unique_lottery_numbers(
    count: int, start: int, end: int
) -> List[int]:
    """
    Generates a specified number of unique random lottery numbers within
    a given range.

    Args:
        count (int): The number of unique numbers to generate.
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        List[int]: A list of unique random numbers sorted in ascending order.
    """
    lottery_numbers: set = set()

    # Continue generating until the set contains the desired count of numbers
    while len(lottery_numbers) < count:
        random_number = random.randint(start, end)
        lottery_numbers.add(random_number)

    return sorted(lottery_numbers)


def print_lottery_ticket() -> None:
    """
    Generates and prints a lottery ticket with 7 unique numbers in ascending
    order.

    Returns:
        None
    """
    lottery_numbers = generate_unique_lottery_numbers(7, 1, 49)
    print(*lottery_numbers)


# Generate and print the lottery ticket
print_lottery_ticket()
