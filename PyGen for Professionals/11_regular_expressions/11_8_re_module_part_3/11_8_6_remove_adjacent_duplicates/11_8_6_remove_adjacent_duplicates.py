'''
TODO:
    Write a program that replaces all repeated adjacent words with one word.

    The program is given a string containing words as input.

    The program must replace all repeated adjacent words in the input string
    with one word and output the result.

NOTE:
    The program must be case-sensitive, i.e., for example, the words python
    and Python are considered different.

    A word is a sequence of characters corresponding to \\w, surrounded by
    characters corresponding to \\W.
'''
import re


def remove_adjacent_duplicates(text: str) -> str:
    """
    Removes all repeated adjacent words in a string.

    Args:
        text (str): Input string containing words.

    Returns:
        str: String with adjacent duplicate words removed.

    Example:
        >>> remove_adjacent_duplicates("hello hello world")
        'hello world'
        >>> remove_adjacent_duplicates("Python Python is great")
        'Python is great'
        >>> remove_adjacent_duplicates("repeat repeat repeat")
        'repeat'
    """
    return re.sub(r'\b(\w+)(?:\W+\1\b)+', lambda match: match.group(1), text)


print(remove_adjacent_duplicates(input()))
