'''
TODO:
    Write a function, is_num(), using anonymous function syntax that takes
    a string argument and returns True if the argument passed is a number
    (integer or float), or False otherwise.
'''
from typing import Callable


def is_valid_number(number: str) -> bool:
    """
    Checks if the string is a valid number (integer or float).

    Args:
        number (str): The string to check.

    Returns:
        bool: True if the string represents a valid number, False otherwise.
    """
    return number.replace('.', '', 1).replace("-", '').isdigit()


is_num: Callable[[str], bool] = lambda number: (
    "-" not in number[1:] and is_valid_number(number)
)
