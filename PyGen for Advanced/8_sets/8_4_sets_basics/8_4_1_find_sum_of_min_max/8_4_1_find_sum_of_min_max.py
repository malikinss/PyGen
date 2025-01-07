'''
TODO:
    Complete the given code so that it prints the sum of the minimum
    and maximum elements of the numbers set.
'''
from typing import Set


def find_sum_of_min_max(numbers: Set[float]) -> float:
    """
    Calculates and returns the sum of the minimum and maximum elements
    of the given set of numbers.

    Args:
    numbers (Set[float]): A set of floating-point numbers.

    Returns:
    float: The sum of the minimum and maximum elements in the set.
    """
    return min(numbers) + max(numbers)


numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
result = find_sum_of_min_max(numbers)

print(result)
