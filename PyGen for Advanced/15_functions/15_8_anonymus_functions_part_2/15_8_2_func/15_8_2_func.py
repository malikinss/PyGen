'''
TODO:
    Write a function func using anonymous function syntax that takes a string
    argument and returns True if the argument begins and ends with the English
    letter a (case is not important), or False otherwise.
'''
from typing import Callable


def starts_with(word: str, letter: str) -> bool:
    """
    Checks if the string starts with the given letter (case-insensitive).

    Args:
        word (str): The string to check.
        letter (str): The letter to compare.

    Returns:
        bool: True if the string starts with the letter, False otherwise.
    """
    return word[0].lower() == letter.lower()


def ends_with(word: str, letter: str) -> bool:
    """
    Checks if the string ends with the given letter (case-insensitive).

    Args:
        word (str): The string to check.
        letter (str): The letter to compare.

    Returns:
        bool: True if the string ends with the letter, False otherwise.
    """
    return word[-1].lower() == letter.lower()


# Anonymous function that returns True if the input string starts and
# ends with 'a'
func: Callable = lambda x: starts_with(x, 'a') and ends_with(x, 'a')
