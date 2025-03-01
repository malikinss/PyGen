"""
TODO:
    Implement the is_greater() function that takes two arguments in the
    following order:
        - nested_lists is a list whose elements are lists of integers
        - number is an integer

    The function should return True if at least one nested list from the list
    nested_lists has a sum of all elements greater than number, or False
    otherwise.

NOTE:
    It is convenient to use the any() function in the problem.
"""
from typing import List


def is_greater(nested_lists: List[List[int]], number: int) -> bool:
    """
    Determine if any of the nested lists has a sum greater than a given number.

    Args:
        nested_lists (List[List[int]]): A list of lists containing integers.
        number (int): The number to compare the sum of the nested lists
        against.

    Returns:
        bool: True if at least one nested list's sum is greater than the given
        number, False otherwise.
    """
    return any(sum(nested_list) > number for nested_list in nested_lists)


# Test case where sum of one of the nested lists is greater than 10
data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
print(is_greater(data, 10))

# Test case where no nested list has a sum greater than 2
data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
print(is_greater(data, 2))

# Test case where sum of one of the nested lists is equal to 3
data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
print(is_greater(data, 3))
