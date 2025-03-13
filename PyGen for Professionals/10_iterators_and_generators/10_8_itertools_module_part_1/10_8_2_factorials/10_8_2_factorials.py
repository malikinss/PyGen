'''
TODO:
    Implement the factorials() function using the accumulate() function, which
    takes one argument:
        n - is a natural number

    The function should return an iterator that generates a sequence of n
    numbers, each of which is the factorial of the next natural number.
'''
from itertools import accumulate
from operator import mul
from collections.abc import Iterator


def factorials(n: int) -> Iterator[int]:
    """
    Generates a sequence of factorials from 1! to n!.

    Args:
        n (int): A natural number (n ≥ 1).

    Yields:
        Iterator[int]: Factorials of numbers from 1 to n.

    Example:
        >>> list(factorials(5))
        [1, 2, 6, 24, 120]
    """
    yield from accumulate(range(1, n + 1), mul)
