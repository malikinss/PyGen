'''
TODO:
    Implement a first_true() function that takes two arguments in the
    following order:
        iterable — the iterable
        predicate — the predicate function; if None, it behaves like bool()

    first_true() should return the first element of iterable for which
    predicate returns True.

    If there is no such element, first_true() should return None.

NOTE:
    A predicate is a function that returns True or False depending on the
    value passed as an argument.

    The iterable passed to the function is guaranteed not to be a set.
'''
from itertools import filterfalse
from typing import Iterable, Callable, TypeVar, Optional

T = TypeVar("T")


def first_true(
    iterable: Iterable[T],
    predicate: Callable[[T], bool] | None = None
) -> Optional[T]:
    """
    Returns the first element in the iterable for which the predicate function
    returns True.

    If no element satisfies the condition, returns None.

    Args:
        iterable (Iterable[T]): An iterable to search.
        predicate (Callable[[T], bool] | None): A function that returns True
        or False. If None, it behaves like bool().

    Returns:
        Optional[T]: The first element that satisfies the predicate, or None
        if not found.

    Example:
        >>> first_true([0, 0, 1, 2, 3], lambda x: x > 1)
        2
        >>> first_true([False, "", None, "hello"], None)
        'hello'
        >>> first_true([], lambda x: x > 0)
        None
    """
    predicate = predicate or bool
    return next(filterfalse(lambda x: not predicate(x), iterable), None)
