'''
TODO:
    Implement a function ncycles() that takes two arguments in the following
    order:
        iterable — an iterable
        times — a natural number

    The function must return an iterator that generates a sequence of elements
    of the iterable, looped times times.

NOTE:
    The iterable elements in the iterator returned by the function must be in
    their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from itertools import tee, chain
from typing import Iterable


def ncycles(iterable: Iterable[int], times: int):
    """
    Create an iterator that generates a sequence of elements of the iterable,
    repeated `times` times using `tee` and `chain`.

    Args:
        iterable (Iterable[int]): An iterable whose elements are to be
        repeated.
        times (int): The number of times to repeat the iterable.

    Returns:
        Iterator: An iterator that generates the repeated sequence.

    Example:
        >>> list(ncycles([1, 2, 3], 2))
        [1, 2, 3, 1, 2, 3]
    """
    return chain.from_iterable(tee(iterable, times))
