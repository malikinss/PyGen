'''
TODO:
    Implement a drop_while_negative() function that takes one argument:
        iterable — an iterable whose elements are integers

    The function must return an iterator that generates all the numbers in the
    iterable, starting with the first non-negative number.

NOTE:
    The iterable elements in the iterator returned by the function must be in
    their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from itertools import dropwhile
from typing import Iterable, Iterator


def drop_while_negative(iterable: Iterable[int]) -> Iterator[int]:
    """
    Skip all negative numbers and return an iterator starting from
    the first non-negative number.

    Args:
        iterable (Iterable[int]): An iterable of integers.

    Returns:
        Iterator[int]: An iterator that yields elements from the first
        non-negative number onward.

    Example:
        >>> list(drop_while_negative([-3, -2, -1, 0, 1, 2]))
        [0, 1, 2]
        >>> list(drop_while_negative([-5, -4, -3]))
        []
    """
    yield from dropwhile(lambda x: x < 0, iterable)
