'''
TODO:
    The program is given two natural numbers a and b as input.

    Write a program using the built-in function all() to find all integers in
    the range [a;b] that are divisible by each digit they contain without
    a remainder.

NOTE:
    Numbers containing zeros are not interesting and do not need to be printed.
'''
from typing import List


def is_self_dividing(number: int) -> bool:
    """
    Checks if a number is divisible by each of its nonzero digits.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is self-dividing, False otherwise.
    """
    digits = [int(digit) for digit in str(number)]
    exclude_zero = 0 not in digits
    return exclude_zero and all(number % digit == 0 for digit in digits)


def find_self_dividing_numbers(a: int, b: int) -> List[int]:
    """
    Finds all self-dividing numbers in the range [a, b].

    Args:
        a (int): The start of the range (inclusive).
        b (int): The end of the range (inclusive).

    Returns:
        List[int]: A list of self-dividing numbers in the given range.
    """
    return [num for num in range(a, b + 1) if is_self_dividing(num)]


# Read input values
a, b = int(input()), int(input())

# Find and print self-dividing numbers
print(*find_self_dividing_numbers(a, b))
