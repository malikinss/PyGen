'''
TODO:
    Implement a max_pair() function that takes one argument:
        iterable — an iterable whose elements are numbers

    The function should return a single number — the maximum sum of two
    adjacent numbers of the iterable.

NOTE:
    Consider the list of numbers 1,8,2,4,3 from the first test.

    The following pairs of adjacent elements can be obtained from this
    sequence:
        1 and 8, 8 and 2, 2 and 4, 4 and 3.

    The second pair has the maximum sum — 10.

    It is guaranteed that the iterable passed to the function is not a set and
    also contains at least two elements.
'''
from itertools import pairwise, starmap
from typing import Iterable


def max_pair(iterable: Iterable[int]) -> int:
    """
    Find the maximum sum of two adjacent numbers in the iterable.

    Args:
        iterable (Iterable[int]): An iterable containing numbers.

    Returns:
        int: The maximum sum of two adjacent numbers in the iterable.

    Example:
        >>> max_pair([1, 8, 2, 4, 3])
        10
    """
    pair_sums = starmap(lambda a, b: a + b, pairwise(iterable))

    return max(pair_sums)
