'''
TODO:
    Implement a sum_of_digits() function that takes one argument:
        iterable — an iterable whose elements are natural numbers

    The function should return a single number — the sum of the digits of all
    the numbers present in the iterable.

NOTE:
    Consider the set of numbers 13,20,41,2,2,5 from the first test.

    The sum of the digits of all the numbers presented will be:
    1+3+2+0+4+1+2+2+5=20
'''
from itertools import chain
from typing import Iterable


def sum_of_digits(iterable: Iterable[int]) -> int:
    """
    Calculate the sum of all the digits of the numbers in the iterable.

    Args:
        iterable (Iterable[int]): An iterable containing natural numbers.

    Returns:
        int: The sum of all digits of all the numbers in the iterable.

    Example:
        >>> sum_of_digits([13, 20, 41, 2, 2, 5])
        20
    """
    return sum(map(int, chain(*map(str, iterable))))
