'''
TODO:
    Complete the code below so that it converts the string to a tuple of the
    string's characters and prints the result.
'''
from typing import Tuple


def string_to_tuple(data: str) -> Tuple:
    """
    Converts a string to a tuple of its characters.

    Args:
    data (str): The input string to be converted.

    Returns:
    Tuple: A tuple containing the characters of the string.
    """
    return tuple(data)


# Example input
data = 'Python для продвинутых!'

# Calling the function and printing the result
result = string_to_tuple(data)
print(result)
