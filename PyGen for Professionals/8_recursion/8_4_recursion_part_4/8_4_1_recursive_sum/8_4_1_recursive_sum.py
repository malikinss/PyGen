'''
TODO:
    Implement recursive_sum() using recursion that takes one argument:
        - nested_lists - is a list whose elements are integers or lists whose
        elements are either integers or lists;
        nesting can be arbitrary

    The function should calculate the sum of all the numbers in all the lists
    and return the result.

    If nested_lists is empty, the function should return the number 0.
'''
from typing import List, Union


def recursive_sum(nested_list: Union[int, List[Union[int, List]]]) -> int:
    """
    Recursively calculates the sum of all integers in a nested list.

    Args:
        nested_list (int | list): A list containing integers or other nested
        lists.

    Returns:
        total (int): The sum of all integers in the nested list.
    """
    total = 0

    # If the current element is an integer, add it to the total
    if isinstance(nested_list, int):
        total += nested_list
    else:
        # If the current element is a list, recursively sum its elements
        # No need to check if the list is empty because if it is,
        # the 'for' loop will simply not execute and 'total' will remain 0.
        for element in nested_list:
            total += recursive_sum(element)

    return total
