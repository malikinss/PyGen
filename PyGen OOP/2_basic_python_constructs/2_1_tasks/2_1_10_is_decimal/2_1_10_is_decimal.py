'''
TODO:
    We will consider a real number to be a sequence of one or more digits that
    may begin with an optional hyphen character - and also contain one decimal
    point . at any position, except when the point is before the hyphen
    character.

    Implement the is_decimal() function that takes one argument:
        - string — a string containing an arbitrary set of characters

    The function should return True if the string is an integer or a real
    number, or False otherwise.
'''
import re


def is_decimal(string: str) -> bool:
    """
    Checks if the provided string represents a valid decimal number.

    A valid decimal number may:
        - Be an integer (e.g. "123", "-456").
        - Be a real number with an optional decimal point
        (e.g. "12.34", "-0.56").
        - Not have a decimal point before the hyphen.

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string represents a valid decimal number (integer or
        real), False otherwise.
    """
    if not string:
        return False

    regex_1 = r'\d+\.\d+'
    regex_2 = r'\d+\.'
    regex_3 = r'\.\d+'
    regex_4 = r'\d+'

    regex = fr'^-?({regex_1}|{regex_2}|{regex_3}|{regex_4})$'

    return bool(re.fullmatch(regex, string))
