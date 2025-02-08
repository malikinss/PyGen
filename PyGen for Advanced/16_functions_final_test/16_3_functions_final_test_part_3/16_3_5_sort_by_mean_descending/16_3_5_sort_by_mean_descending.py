'''
TODO:
    Given a list numbers, consisting of tuples.

    Complete the missing part of the program so that the list sorted_numbers
    is sorted in descending order of the arithmetic mean of the elements of
    the tuples of the list numbers.
'''
from typing import List, Tuple


def sort_by_mean_descending(
    numbers: List[Tuple[int, ...]]
) -> List[Tuple[int, ...]]:
    """
    Sorts a list of tuples based on their arithmetic mean in descending order.

    Parameters:
    - numbers (List[Tuple[int, ...]]): The list of tuples containing integers.

    Returns:
    - List[Tuple[int, ...]]: The sorted list of tuples.
    """
    return sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)


# Example usage
numbers = [
    (10, -2, 3, 4),
    (-13, 56),
    (1, 9, 2),
    (-1, -9, -45, 32),
    (-1, 5, 1),
    (17, 0, 1),
    (0, 1),
    (3,),
    (39, 12),
    (11, -23),
    (10, -100, 21, 32),
    (3, -8),
    (1, 1)
]

sorted_numbers = sort_by_mean_descending(numbers)
print(sorted_numbers)
