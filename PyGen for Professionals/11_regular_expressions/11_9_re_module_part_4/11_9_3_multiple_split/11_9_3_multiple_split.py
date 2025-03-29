'''
TODO:
    Implement a multiple_split() function that takes two arguments:
        - string — a string
        - delimiters — a list of strings

    The function should split the string into substrings using the strings in
    the delimiters list as delimiters, and return the result as a list.

NOTE:
    In other words, the multiple_split() function should work similarly to the
    string split() method, except that delimiters may contain a set of
    delimiters rather than a single delimiter.
'''
import re


def multiple_split(string: str, delimiters: list[str]) -> list[str]:
    """
    Splits a string using multiple delimiters.

    Args:
        string (str): The input string.
        delimiters (list[str]): A list of delimiters.

    Returns:
        list[str]: List of substrings obtained after splitting.

    Example:
        >>> multiple_split(
            "apple, orange; banana and grape", [", ", "; ", " and "]
        )
        ['apple', 'orange', 'banana', 'grape']
    """
    if not delimiters:
        return [string]

    escaped_delimiters = map(re.escape, delimiters)
    pattern = "|".join(escaped_delimiters)

    return re.split(pattern, string)
