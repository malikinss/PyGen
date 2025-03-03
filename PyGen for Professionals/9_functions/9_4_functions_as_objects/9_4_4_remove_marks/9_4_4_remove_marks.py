'''
TODO:
    Implement a remove_marks() function that takes two arguments in the
    following order:
        text — an arbitrary string
        marks — a set of characters

    The function should return the text string, having previously removed
    from it all the characters listed in the marks string.

    Also, the remove_marks() function should have a count attribute, which
    represents the number of times the function has been called.
'''
from typing import Iterable


def remove_marks(text: str, marks: Iterable) -> str:
    """
    Remove specified characters from the text.

    Args:
        text (str): The input string from which characters will be removed.
        marks (Iterable): A collection (e.g., set, list) containing characters
                          to be removed.

    Returns:
        str: The modified string with specified characters removed.
    """
    # Initialize 'count' if it's not already present
    remove_marks.__dict__.setdefault('count', 0)

    # Remove each character in the 'marks' set from the 'text' string
    for mark in marks:
        text = text.replace(mark, '')

    # Increment the count of how many times the function has been called
    remove_marks.count += 1

    return text
