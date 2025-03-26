'''
TODO:
    Implement a normalize_whitespace() function that takes one argument:
        string — an arbitrary string

    The function should replace all multiple spaces in the string with
    a single space and return the result.
'''
import re


def normalize_whitespace(string: str) -> str:
    """
    Normalize the whitespace in a string by replacing all sequences of
    whitespace characters (spaces, tabs, newlines) with a single space.

    Leading and trailing whitespace characters are also removed.

    Args:
        string (str): The input string to normalize.

    Returns:
        str: The normalized string with single spaces and no leading/trailing
        spaces.
    """
    return re.sub(r'\s+', ' ', string).strip()
