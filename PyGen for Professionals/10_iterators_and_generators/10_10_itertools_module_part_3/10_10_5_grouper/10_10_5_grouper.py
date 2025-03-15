'''
TODO:
    Implement a grouper() function that takes two arguments in the following
    order:
        iterable — the iterable
        n — a natural number

    The function must return an iterator that generates a sequence whose
    elements are the adjacent elements of the iterable, grouped into n-element
    tuples.

    If an element does not have enough neighbors, the value None becomes its
    neighbors.

NOTE:
    The iterable elements in the iterator returned by the function must be in
    their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from itertools import zip_longest, repeat
from typing import Iterable, Iterator, Tuple, Optional


def grouper(
    iterable: Iterable, n: int
) -> Iterator[Tuple[Optional[int], ...]]:
    """
    Groups elements of an iterable into tuples of size `n`, filling missing
    values with None.

    Args:
        iterable (Iterable): The iterable to group.
        n (int): The size of each group.

    Returns:
        Iterator[Tuple[Optional[int], ...]]: An iterator yielding n-element
        tuples.

    Example:
        >>> list(grouper([1, 2, 3, 4, 5], 2))
        [(1, 2), (3, 4), (5, None)]

        >>> list(grouper([1, 2, 3, 4, 5], 3))
        [(1, 2, 3), (4, 5, None)]
    """
    return zip_longest(
        *repeat(iter(iterable), n), fillvalue=None
    )
