'''
TODO:
    Implement a function called is_rising() that takes one argument:
        iterable — an iterable whose elements are numbers

    The function should return True if the iterable's elements are strictly in
    ascending order, or False otherwise.

NOTE:
    It is guaranteed that the iterable passed to the function is not a set and
    contains at least two elements.
'''
from itertools import pairwise
from typing import Iterable


def is_rising(iterable: Iterable[int]) -> bool:
    """
    Check if the elements of the iterable are strictly in ascending order.

    Args:
        iterable (Iterable[int]): An iterable containing numbers.

    Returns:
        bool: True if the elements are in strictly ascending order,
        False otherwise.

    Example:
        >>> is_rising([1, 2, 3, 4])
        True
        >>> is_rising([1, 2, 2, 4])
        False
    """
    # Use pairwise from itertools to create pairs of consecutive elements
    return all(a < b for a, b in pairwise(iterable))
