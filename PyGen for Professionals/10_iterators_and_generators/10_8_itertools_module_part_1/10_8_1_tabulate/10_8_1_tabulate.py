'''
TODO:
    Implement a tabulate() function that takes one argument:
        - func - is an arbitrary function

    The tabulate() function should return an iterator that generates an
    infinite sequence of return values of func , first with argument 1, then 2,
    then 3, and so on.
'''
from collections.abc import Iterator, Callable
import itertools


def tabulate(func: Callable[[int], any]) -> Iterator[any]:
    """
    Generates an infinite sequence of values produced by applying `func`
    to consecutive integers starting from 1.

    Args:
        func (Callable[[int], any]): A function that takes an integer and
        returns any value.

    Yields:
        Iterator[any]: An infinite sequence of function outputs.

    Example:
        >>> gen = tabulate(lambda x: x**2)
        >>> next(gen)
        1
        >>> next(gen)
        4
        >>> next(gen)
        9
    """
    yield from map(func, itertools.count(1))
