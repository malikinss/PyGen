'''
TODO:
    We will assume that the PIN code is correct if it meets the following
    conditions:
        - consists of 4, 5 or 6 characters
        - consists only of digits (0-9)
        - does not contain spaces

    Implement the is_valid() function, which takes one argument:
        string — an arbitrary string

    The function should return True if the string is a valid PIN, or False
    otherwise.

NOTE:
    If an empty string is passed to the function, the function must return
    False.
'''


def is_valid(string: str) -> bool:
    """
    Checks if the given string is a valid PIN code.

    A valid PIN code:
        - Consists of 4, 5, or 6 digits.
        - Contains only digits (0-9).
        - Does not contain spaces.

    Args:
        string (str): The string to be checked.

    Returns:
        bool: True if the string is a valid PIN, False otherwise.
    """
    flags = [
        len(string) in range(4, 7),  # Check if length is between 4 and 6
        string.isdigit(),            # Check if all characters are digits
        ' ' not in string            # Check if there are no spaces
    ]

    return all(flags)
