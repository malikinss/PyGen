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


def recursive_sum(nested_list: List[Union[int, List]]) -> int:
    """
    Recursively calculates the sum of all integers in a nested list.

    Args:
        nested_list (list): A list that contains integers or other nested
        lists (which can also contain integers or nested lists).

    Returns:
        int: The sum of all integers in the nested list, or 0 if the list
        is empty.
    """
    total = 0

    # Traverse each element in the nested list
    for element in nested_list:
        if isinstance(element, int):
            total += element  # If element is an integer, add it to the total
        else:
            # If element is a list, recurse into it
            total += recursive_sum(element)

    return total
