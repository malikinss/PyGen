'''
TODO:
    Write a function count_args() that takes an arbitrary number of arguments
    and returns the number of arguments passed to it.

NOTE:
    Note that the function should take an arbitrary number of arguments,
    not a list.
'''
from typing import Any


def count_args(*args: Any) -> int:
    """
    Returns the number of arguments passed to the function.

    Args:
        *args (Any): An arbitrary number of arguments.

    Returns:
        int: The count of arguments passed.
    """
    return len(args)
