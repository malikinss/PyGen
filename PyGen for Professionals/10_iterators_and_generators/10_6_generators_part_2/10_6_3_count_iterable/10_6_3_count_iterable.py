'''
TODO:
    Implement the count_iterable() function using generator expressions that
    takes one argument:
        - iterable — the iterable

    The function must return a single number — the number of elements in
    the iterable.

NOTE:
    The iterable passed to the function is guaranteed to be finite.
'''
from collections.abc import Iterable
from typing import Any


def count_iterable(iterable: Iterable[Any]) -> int:
    """
    Counts the number of elements in a given iterable.

    Args:
        iterable (Iterable[Any]): The iterable to count elements from.

    Returns:
        int: The number of elements in the iterable.

    Example:
        count_iterable([1, 2, 3, 4]) -> 4
        count_iterable("hello") -> 5
    """
    return sum(1 for _ in iterable)
