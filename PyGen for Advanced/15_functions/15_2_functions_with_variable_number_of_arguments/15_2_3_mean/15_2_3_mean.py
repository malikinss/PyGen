'''
TODO:
    Write a function mean() that takes an arbitrary number of arguments and
    returns the arithmetic mean of the numeric (int or float) arguments passed
    to it.

NOTE:
    Note that the function should take an arbitrary number of arguments,
    not a list.

    The function should ignore arguments of all types except int or float.
'''
from typing import Any


def mean(*args: Any) -> float:
    """
    Returns the arithmetic mean of the numeric (int or float) arguments passed
    to it.

    Non-numeric arguments are ignored.

    Args:
        *args (Any): An arbitrary number of arguments.

    Returns:
        float: The arithmetic mean of numeric arguments, or 0.0 if no numeric
               arguments were passed.
    """
    total: float = 0.0
    count: int = 0

    for element in args:
        if isinstance(element, (int, float)):
            total += element
            count += 1

    if count == 0:
        return 0.0

    return total / count
