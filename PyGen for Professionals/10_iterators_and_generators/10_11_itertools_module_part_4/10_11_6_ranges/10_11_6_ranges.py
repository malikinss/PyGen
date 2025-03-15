'''
TODO:
    We will assume that a sequence of non-negative integers can be transformed
    into a segment if the difference between adjacent elements of this
    sequence is equal to one.

    For example, the numbers 3,4,5,6,7,8 can be transformed into the segment
    [3;8].

    The numbers 1,3,5,11,15,22 cannot be transformed into a segment.

    A single number is transformed into a segment in which both the right and
    left border is itself.

    For example, the number 1 can be transformed into the segment [1;1].

    Implement the ranges() function that takes one argument:
    numbers is a list of distinct natural numbers arranged in ascending order

    The function should transform numbers from the numbers list into segments,
    representing them as tuples, where the first element of the tuple is the
    left border of the segment, and the second element is the right border of
    the segment.

    The function should return the resulting tuples-segments as a list.

NOTE:
    The numbers in the list returned by the function must be in their original
    order.
'''
from itertools import groupby
from typing import List, Tuple


def ranges(numbers: List[int]) -> List[Tuple[int, int]]:
    """
    Converts a list of consecutive numbers into segment tuples.

    Args:
        numbers (List[int]): A sorted list of distinct natural numbers.

    Returns:
        List[Tuple[int, int]]: A list of tuples representing number segments.
    """
    if not numbers:
        return []

    def key_func(n, c=[-1]):
        c[0] += 1
        return n - c[0]

    grouped_list = [
        list(g)
        for _, g in groupby(numbers, key=key_func)
    ]

    return [
        (group[0], group[-1])
        for group in grouped_list
    ]


numbers = [1, 2, 3, 4, 7, 8, 10]
print(*ranges(numbers))
