'''
TODO:
    We will consider a common fraction to be a sequence of one or more digits,
    followed by a forward slash /, and then a sequence of one or more digits,
    at least one of which is different from zero (the denominator cannot be
    zero).

    A sequence representing a common fraction may begin with an optional
    hyphen character -.

    Implement the is_fraction() function that takes one argument:
        - string — a string containing an arbitrary set of characters

    The function must return True if the string is a common fraction, or False
    otherwise.
'''
import re


def is_fraction(string: str) -> bool:
    """
    Checks if the given string represents a common fraction.

    A common fraction consists of one or more digits, followed by a forward
    slash '/', and then one or more digits, with at least one digit in the
    denominator being non-zero.

    The fraction may optionally start with a negative sign.

    Example:
        '1000/00001' -> True
        '-1000/00001' -> True
        '5/0' -> False (denominator cannot be zero)

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string represents a valid common fraction,
        False otherwise.
    """
    if not string or '/' not in string:
        return False

    numerator = r'(0|\d+)'
    denominator = r'0*[1-9]\d*'

    regex = fr'^-?{numerator}/{denominator}$'

    return bool(re.fullmatch(regex, string))
