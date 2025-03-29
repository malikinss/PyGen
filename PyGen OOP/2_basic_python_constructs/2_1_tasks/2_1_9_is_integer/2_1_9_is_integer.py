'''
TODO:
    An integer is a sequence of one or more digits, which may begin with an
    optional hyphen character -.

    Implement the is_integer() function that takes one argument:
        - string — a string containing an arbitrary set of characters

    The function should return True if the string is an integer,
    or False otherwise.
'''
import re


def is_integer(string: str) -> bool:
    """
    Checks if the provided string is a valid integer.

    A valid integer may begin with an optional hyphen and must be followed by
    one or more digits.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string represents an integer, False otherwise.
    """
    return bool(re.fullmatch(r'^-?\d+$', string))
