'''
TODO:
    Implement a take() function that takes two arguments in the following
    order:
        iterable — the iterable
        n — a natural number

    The function must return an iterator that generates a sequence of the
    first n elements of the iterable.

NOTE:
    The iterable elements in the iterator returned by the function must be in
    their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from itertools import islice
from typing import Iterable, Iterator


def take(iterable: Iterable, n: int) -> Iterator:
    """
    Return the first n elements of the iterable.

    Args:
        iterable (Iterable): An iterable to take elements from.
        n (int): The number of elements to take from the iterable.

    Returns:
        Iterator: An iterator generating the first n elements of the iterable.

    Example:
        >>> list(take([1, 2, 3, 4, 5], 3))
        [1, 2, 3]
    """
    yield from islice(iterable, n)
