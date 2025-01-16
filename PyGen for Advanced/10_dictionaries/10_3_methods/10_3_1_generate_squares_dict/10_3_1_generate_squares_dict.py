"""
TODO:
    Expand the code below so that the result variable stores a dictionary
    in which the keys are numbers from 1 to 15 (inclusive) and the values
    are the squares of the keys.

NOTE:
    You do not need to print the contents of the result dictionary.
"""
from typing import Dict


def generate_squares_dict(start: int, end: int) -> Dict[int, int]:
    """
    Generates a dictionary where keys are numbers in a specified range
    and values are the squares of those keys.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Returns:
        Dict[int, int]: A dictionary with numbers as keys and their squares
                        as values.
    """
    return {i: i ** 2 for i in range(start, end + 1)}


# Call the function for numbers 1 through 15
result = generate_squares_dict(1, 15)
