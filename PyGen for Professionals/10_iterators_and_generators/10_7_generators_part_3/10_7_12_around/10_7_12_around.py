'''
TODO:
    Implement a generator function that takes one argument:
        iterable — the iterable

    The function must return a generator that produces a sequence of tuples,
    each containing the next element of the iterable, as well as the previous
    and next elements:
        (<previous element>, <next element>, <next element>)

    For the first element, the previous value is None, and for the last
    element, the next value is also None.

NOTE:
    The elements of the iterable in the generator returned by the function
    must be in their original order.

    It is guaranteed that the iterable passed to the function is not a set.
'''
from collections.abc import Iterable, Iterator
from typing import Any, Generator


def around(
    iterable: Iterable[Any]
) -> Generator[tuple[Any, Any, Any], None, None]:
    """
    Generates tuples containing each element of the iterable, its previous,
    and next elements.

    Args:
        iterable (Iterable[Any]): An iterable containing elements of any type.

    Yields:
        Generator[tuple[Any, Any, Any], None, None]: A generator that produces
        tuples where:
        - The first value is the previous element (None for the first item),
        - The second value is the current element,
        - The third value is the next element (None for the last item).

    Example:
        >>> list(around([1, 2, 3, 4]))
        [(None, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, None)]
    """
    iterator: Iterator[Any] = iter(iterable)

    prev: Any = None
    cur: Any = next(iterator, None)

    if cur is None:
        return

    next_: Any = next(iterator, None)

    while True:
        yield prev, cur, next_
        prev, cur = cur, next_
        next_ = next(iterator, None)

        if cur is None:
            break
