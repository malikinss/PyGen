'''
TODO:
    Complete the given code so that it prints the arithmetic mean of
    the elements of the numbers set.
'''
from typing import Set


def calculate_arithmetic_mean(numbers: Set[int]) -> float:
    """
    Calculates and returns the arithmetic mean of the elements in
    the given set.

    Args:
    numbers (Set[int]): A set of integers.

    Returns:
    float: The arithmetic mean of the elements in the set.
    """
    return sum(numbers) / len(numbers)


numbers = {
    20, 6, 8, 18,
    18, 2, 4, 6,
    8, 10, 12, 14,
    16, 18, 20, 12,
    8, 8, 10, 4,
    2, 2, 2, 16, 20
}
print(calculate_arithmetic_mean(numbers))
