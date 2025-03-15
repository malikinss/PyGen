'''
TODO:
    Implement a take_nth() function that takes two arguments in the following
    order:
        iterable — an iterable
        n — a natural number

    The function should return the n-th element of the iterable.

    If the iterable contains fewer than n elements, the function should return
    None.

NOTE:
    The iterable passed to the function is guaranteed not to be a set.
'''
from itertools import islice
from typing import Iterable, Optional, Any


def take_nth(iterable: Iterable, n: int) -> Optional[Any]:
    """
    Return the n-th element of the iterable.

    Args:
        iterable (Iterable): An iterable to take the element from.
        n (int): The position of the element to return (1-based index).

    Returns:
        Optional[Any]: The n-th element of the iterable, or None if the
                        iterable contains fewer than n elements.

    Example:
        >>> take_nth([1, 2, 3, 4, 5], 3)
        3
        >>> take_nth([1, 2], 3)
        None
    """
    return next(islice(iterable, n-1, None), None)
