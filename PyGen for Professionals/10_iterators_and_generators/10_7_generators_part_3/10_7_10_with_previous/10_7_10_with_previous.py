'''
TODO:
    Implement a generator function that takes one argument:
        iterable — the iterable

    The function must return a generator that produces a sequence of tuples,
    each containing the next element of the iterable and the element
    that preceded it:
        (<next element>, <previous element>)

    For the first element, the previous element is considered to be None.

NOTE:
    The elements of the iterable in the generator returned by the function
    must be in their original order.

    The iterable passed to the function is guaranteed not to be a set.
'''
from collections.abc import Iterable, Iterator
from typing import Any, Generator


def with_previous(
    iterable: Iterable[Any]
) -> Generator[tuple[Any, Any], None, None]:
    """
    Generates tuples containing each element of the iterable and its
    predecessor.

    Args:
        iterable (Iterable[Any]): An iterable containing elements of any type.

    Yields:
        Generator[tuple[Any, Any], None, None]: A generator that produces
        tuples where the first element is the current item from the iterable,
        and the second element is the previous item (None for the first
        element).

    Example:
        >>> list(with_previous([1, 2, 3]))
        [(1, None), (2, 1), (3, 2)]
    """
    iterator: Iterator[Any] = iter(iterable)
    prev: Any = None
    for el in iterator:
        yield el, prev
        prev = el
