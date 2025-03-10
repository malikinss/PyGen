'''
TODO:
    Implement the all_together() function using generator expressions that
    takes an arbitrary number of positional arguments, each of which is
    an iterable.

    The function should return a generator that produces each element of
    all the iterables passed in:
        first all the elements of the first iterable, then the second iterable,
        and so on.

NOTE:
    The iterable passed to the function is guaranteed not to be a set.
'''
from collections.abc import Iterable
from typing import Any, Generator


def all_together(*args: Iterable[Any]) -> Generator[Any, None, None]:
    """
    Returns a generator that produces elements from all iterables in order.

    Args:
        *args (Iterable[Any]): An arbitrary number of iterables.

    Returns:
        Generator[Any, None, None]: A generator yielding elements from
                                    all iterables sequentially.

    Example:
        list(
            all_together([1, 2], "abc", (10, 20))
        ) -> [1, 2, 'a', 'b', 'c', 10, 20]
    """
    return (element for iterable in args for element in iterable)
