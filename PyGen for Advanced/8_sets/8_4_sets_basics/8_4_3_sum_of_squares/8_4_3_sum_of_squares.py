'''
TODO:
    Complete the given code so that it prints the sum of the squares of the
    elements of the set numbers.
'''
from typing import Set


def sum_of_squares(numbers: Set[int]) -> int:
    """
    Calculates and returns the sum of the squares of the elements
    in the given set.

    Args:
    numbers (Set[int]): A set of integers.

    Returns:
    int: The sum of the squares of the elements in the set.
    """
    return sum(element * element for element in numbers)


numbers = {
    9089, -67, -32, 1, 78,
    23, -65, 99, 9089, 34,
    -32, 0, -67, 1, 11,
    111, 111, 1, 23
}
print(sum_of_squares(numbers))
