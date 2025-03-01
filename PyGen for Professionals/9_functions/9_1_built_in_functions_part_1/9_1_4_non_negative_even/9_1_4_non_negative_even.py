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


def non_negative_even(numbers: List[int]) -> bool:
    """
    Check if all numbers in a list are even and non-negative.

    Args:
        numbers (List[int]): A list of numbers to check.

    Returns:
        bool: True if all numbers are even and non-negative, False otherwise.
    """
    # Check if all numbers are even and non-negative in one pass
    return all(number >= 0 and number % 2 == 0 for number in numbers)


# Example usage
print(non_negative_even([0, 2, 4, 8, 16]))  # True
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))  # False
print(non_negative_even([0, 0, 0, 0, 0]))  # True
