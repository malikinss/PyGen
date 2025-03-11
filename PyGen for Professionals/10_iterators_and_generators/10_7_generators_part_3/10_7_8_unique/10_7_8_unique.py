'''
TODO:
    Implement a generator function that takes one argument:
        iterable — the iterable

    The function must return a generator that produces a sequence of elements
    of the iterable object, without duplicates.

NOTE:
    The elements of the iterable object in the generator returned by the
    function must be in their original order.

    The iterable object passed to the function is guaranteed not to be a set.
'''
from typing import Iterable, Generator


def unique(iterable: Iterable) -> Generator:
    """
    Generate unique elements from an iterable, maintaining the original order.

    This function iterates over the given iterable and yields only unique
    elements while maintaining their original order.

    Each element is yielded only once.

    Args:
        iterable (Iterable): The input iterable (e.g., list, string, etc.)

    Yields:
        The unique elements from the iterable.
    """
    seen = set()  # A set to track seen elements
    for value in iterable:
        if value not in seen:
            seen.add(value)
            yield value
