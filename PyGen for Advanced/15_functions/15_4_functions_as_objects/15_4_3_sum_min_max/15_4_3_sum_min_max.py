'''
TODO:
    Given a list numbers containing tuples of numbers.

    Write a program that sorts and prints the list numbers according to the
    sum of the minimum and maximum elements of the tuple.

NOTE:
    In this problem, we assume that the tuple (2,1,3) is less than the tuple
    (6,4,5), since 1+3<4+6.

    However, the tuple (1,2,9) is equal to the tuple (4,5,6), since 1+9 = 4+6.

    Use the optional argument key.
'''
from typing import List, Tuple


def sum_min_max(
    numbers: List[Tuple[int, int, int]]
) -> List[Tuple[int, int, int]]:
    """
    Sorts a list of tuples based on the sum of the minimum and maximum
    elements of each tuple.

    Args:
        numbers (List[Tuple[int, int, int]]): A list of tuples where each
                                              tuple contains integer values.

    Returns:
        List[Tuple[int, int, int]]: A sorted list of tuples based on the sum
                                    of their min and max values.
    """
    return sorted(numbers, key=lambda x: min(x) + max(x))


numbers: List[Tuple[int, int, int]] = [
    (10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3),
    (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34),
    (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)
]

# Sorting the numbers based on the sum of the min and max values of each tuple
sorted_numbers = sum_min_max(numbers)

print(sorted_numbers)
