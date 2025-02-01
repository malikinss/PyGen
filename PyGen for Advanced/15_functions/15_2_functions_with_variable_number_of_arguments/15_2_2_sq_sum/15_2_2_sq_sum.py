'''
TODO:
    Write a function sq_sum() that takes an arbitrary number of numeric
    arguments and returns the sum of their squares.

NOTE:
    Please note that the function should take an arbitrary number of arguments,
    not a list.
'''
from typing import Union


def sq_sum(*args: Union[int, float]) -> Union[int, float]:
    """
    Returns the sum of the squares of the given numeric arguments.

    Args:
        *args (Union[int, float]): An arbitrary number of numeric arguments.

    Returns:
        Union[int, float]: The sum of the squares of the arguments.
    """
    result: Union[int, float] = 0
    for element in args:
        result += element * element
    return result
