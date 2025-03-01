"""
TODO:
    Implement a non_negative_even() function that takes one argument:
        - numbers - is a non-empty list of numbers

    The function should return True if all numbers in the numbers list are
    even and non-negative, or False otherwise.

NOTE:
    It is convenient to use the all() function in the problem.
"""
from typing import List


def is_even(number: int) -> bool:
    """
    Check if a number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0


def is_non_negative(number: int) -> bool:
    """
    Check if a number is non-negative.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is non-negative, False otherwise.
    """
    return number >= 0


def non_negative_even(numbers: List[int]) -> bool:
    """
    Check if all numbers in a list are even and non-negative.

    Args:
        numbers (List[int]): A list of numbers to check.

    Returns:
        bool: True if all numbers are even and non-negative, False otherwise.
    """
    # Check if all numbers are both even and non-negative in one pass
    return all(is_even(number) and is_non_negative(number) for number in numbers)


# Example usage
print(non_negative_even([0, 2, 4, 8, 16]))
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
print(non_negative_even([0, 0, 0, 0, 0]))
