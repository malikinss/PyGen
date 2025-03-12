'''
TODO:
    Implement a generator function that takes one argument:
        iterable — the iterable

    The function must return a generator that produces a sequence of tuples,
    each containing the next element of the iterable, plus the next element:
        (<next element>, <next element>)

    For the last element, the next element is None.

NOTE:
    The elements of the iterable in the generator returned by the function
    must be in their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from collections.abc import Iterable, Iterator
from typing import Any, Generator


def pairwise(
    iterable: Iterable[Any]
) -> Generator[tuple[Any, Any], None, None]:
    """
    Generates tuples containing each element of the iterable and the
    next element.

    Args:
        iterable (Iterable[Any]): An iterable containing elements of any type.

    Yields:
        Generator[tuple[Any, Any], None, None]: A generator that produces
        tuples where the first element is the current item from the iterable,
        and the second element is the next item (None for the last element).

    Example:
        >>> list(pairwise([1, 2, 3]))
        [(1, 2), (2, 3), (3, None)]
    """
    iterator: Iterator[Any] = iter(iterable)
    prev: Any = next(iterator, None)

    if prev is None:
        return

    for cur in iterator:
        yield prev, cur
        prev = cur

    yield prev, None
