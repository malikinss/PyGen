'''
TODO:
    Using a for loop and the built-in max() function, complete the code below
    so that it prints the maximum element among all the elements of
    the nested lists of list1.
'''
from typing import List


def find_max_nested_list(list1: List[List[int]]) -> int:
    """
    Finds the maximum element among all elements in nested lists.

    Args:
        list1 (List[List[int]]): A list of nested lists containing integers.

    Returns:
        int: The maximum element in the nested lists.
    """
    maximum = -1

    for li in list1:
        current_max = max(li)
        if current_max > maximum:
            maximum = current_max

    return maximum


# Example usage
list1 = [
    [1, 7, 8],
    [9, 7, 102],
    [6, 106, 105],
    [100, 99, 98, 103],
    [1, 2, 3]
]

print(find_max_nested_list(list1))
