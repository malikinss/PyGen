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


def convert(number: int) -> Tuple[str, str, str]:
    """
    Convert an integer to its binary, octal, and hexadecimal representations.

    Args:
        number (int): The integer to be converted.

    Returns:
        Tuple[str, str, str]: A tuple containing the binary, octal, and
        hexadecimal representations of the number.
    """
    binary_str = bin(number)[2:]  # Remove '0b' prefix
    octal_str = oct(number)[2:]   # Remove '0o' prefix

    # Remove '0x' prefix and make uppercase
    hexadecimal_str = hex(number)[2:].upper()

    return (binary_str, octal_str, hexadecimal_str)


print(convert(-24))
