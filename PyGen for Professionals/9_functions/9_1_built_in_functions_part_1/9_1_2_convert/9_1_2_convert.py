"""
TODO:
    Implement a function convert() that takes one argument:
        number — an integer

    The function should return a tuple of three elements in the following
    order:
        - binary representation of number as a string without the 0b prefix
        - octal representation of number as a string without the 0o prefix
        - hexadecimal representation of number as an uppercase string without
        the 0x prefix

NOTE:
    The bin(), oct(), and hex() functions are useful in this problem.
"""
from typing import Tuple


def strip_prefix(number_str: str) -> str:
    """
    Remove the prefix from a string representation of a number.

    Args:
        number_str (str): String representation of a number with prefix.

    Returns:
        cleaned_str (str): String representation without prefix.
    """
    if number_str.startswith('-'):
        return '-' + number_str[3:]

    return number_str[2:]


def convert(number: int) -> Tuple[str, str, str]:
    """
    Convert an integer to its binary, octal, and hexadecimal representations.

    Args:
        number (int): The integer to be converted.

    Returns:
        Tuple[str, str, str]: A tuple containing the binary, octal, and
        hexadecimal
        representations of the number.
    """
    binary_str = strip_prefix(bin(number))
    octal_str = strip_prefix(oct(number))
    hexadecimal_str = strip_prefix(hex(number)).upper()

    return (binary_str, octal_str, hexadecimal_str)


print(convert(-24))
