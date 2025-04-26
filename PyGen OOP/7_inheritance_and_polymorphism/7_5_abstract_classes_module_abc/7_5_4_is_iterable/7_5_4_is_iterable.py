'''
TODO:
    Implement a function is_iterable() that takes one argument:
        obj — an arbitrary object

    The function should return True if obj is an iterable object, or False
    otherwise.

    Also implement a function is_iterator() that takes one argument:
        obj — an arbitrary object

    The function should return True if obj is an iterator, or False otherwise.
'''
from typing import Any
from collections.abc import Iterable, Iterator


def is_iterable(obj: Any) -> bool:
    """
    Check if an object is iterable.

    Args:
        obj: Any object to check.

    Returns:
        True if the object is iterable, False otherwise.
    """
    return isinstance(obj, Iterable)


def is_iterator(obj: Any) -> bool:
    """
    Check if an object is an iterator.

    Args:
        obj: Any object to check.

    Returns:
        True if the object is an iterator, False otherwise.
    """
    return isinstance(obj, Iterator)
