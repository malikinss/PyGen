'''
TODO:
    Implement a function first_largest() that takes two arguments in the
    following order:
        iterable — an iterable whose elements are integers
        number — an arbitrary number

    The function should return the index of the first element of the iterable
    that is greater than number.

    If there are no such elements, the function should return the number -1.

NOTE:
    Consider the list of numbers 10,2,14,7,7,18,20 from the first test.

    The first number greater than 11 is 14, which has index 2.

    The iterable passed to the function is guaranteed not to be a set.
'''
from itertools import dropwhile
from typing import Iterable


def first_largest(iterable: Iterable[int], number: int) -> int:
    """
    Find the index of the first element in the iterable that is greater than
    the given number.

    Args:
        iterable (Iterable[int]): An iterable of integers.
        number (int): The number to compare the elements with.

    Returns:
        int: The index of the first element greater than the given number,
        or -1 if no such element is found.

    Example:
        >>> first_largest([10, 2, 14, 7, 7, 18, 20], 11)
        2
        >>> first_largest([1, 2, 3], 5)
        -1
    """
    dropped_iter = dropwhile(
        lambda x: x[1] <= number, enumerate(iterable)
    )

    first_largest_el = next(dropped_iter, None)

    if first_largest_el is None:
        return -1

    return first_largest_el[0]


iterator = iter([18, 21, 14, 72, 73, 18, 20])
print(first_largest(iterator, 10))
