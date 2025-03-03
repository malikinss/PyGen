'''
TODO:
    Implement a numbers_sum() function that takes one argument:
        elems — a list of arbitrary objects

    The function should return the sum of the numbers (int and float types)
    in the elems list, ignoring any non-numeric objects.

    If there are no numbers in the elems list, the function should return
    the number 0.

    The function should also have the following docstring:
        Take a list and return the sum of its numbers (int, float),
        ignoring non-numeric objects.
        0 - if there are no numbers in the list.
'''
from typing import List, Any


def numbers_sum(elems: List[Any]) -> float:
    """
    Take a list and return the sum of its numbers (int, float),
    ignoring non-numeric objects.
    0 - if there are no numbers in the list.

    Args:
        elems (List[Any]): The list of arbitrary objects.

    Returns:
        float: The sum of numeric elements in the list or 0 if no numbers
        are found.
    """
    return sum(filter(lambda obj: isinstance(obj, (int, float)), elems))
