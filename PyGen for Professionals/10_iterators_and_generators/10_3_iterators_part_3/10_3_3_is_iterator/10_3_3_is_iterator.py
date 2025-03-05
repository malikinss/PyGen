'''
TODO:
    Implement a function called is_iterator() that takes one argument:
        obj is an arbitrary object

    The function should return True if obj is an iterator, or False otherwise.
NOTE:
    Submit a program to the testing system that contains only the required
    is_iterator() function, but not the code that calls it.
'''
from typing import Any


def is_iterator(obj: Any) -> bool:
    """
    Check if the given object is an iterator.

    Args:
        obj (Any): The object to check.

    Returns:
        bool: True if the object is an iterator, otherwise False.
    """
    return hasattr(obj, '__next__')
