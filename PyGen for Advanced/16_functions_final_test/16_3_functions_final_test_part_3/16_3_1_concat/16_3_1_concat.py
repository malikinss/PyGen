'''
TODO:
    Write a function concat() that takes a variable number of arguments and
    concatenates them into a single string using a separator (sep).

    If the separator is not specified, a space serves as the separator.

NOTE:
    Please note that the concat() function should take a variable number of
    arguments, not a list.
'''
from typing import Any


def concat(*args: Any, sep: str = ' ') -> str:
    """
    Concatenates the given arguments into a single string using a separator.

    Parameters:
    - *args (Any): A variable number of arguments that will be concatenated.
    - sep (str, optional): A string to be used as the separator.
                           Default is a space.

    Returns:
    - str: The concatenated string with the specified separator.

    Example:
    >>> concat('Hello', 'World')
    'Hello World'
    >>> concat('apple', 'orange', sep=', ')
    'apple, orange'
    """
    return sep.join([str(i) for i in args])
