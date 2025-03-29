'''
TODO:
    Write a program that splits a string by period, comma, and semicolon
    characters.

    The program is given a string containing different values separated by
    period ".", comma "," or semicolon ";" characters, with spaces around them.

    The program should split the input string by period, comma, and semicolon
    characters, capturing surrounding spaces, and output all the values
    obtained during the splitting, separated by spaces.
'''
import re
from typing import List


def custom_split(string: str) -> List[str]:
    """
    Splits a string by period (.), comma (,), and semicolon (;),
    removing any surrounding spaces.

    Args:
        string (str): The input string to be split.

    Returns:
        List[str]: A list of substrings obtained after splitting.
    """
    return re.split(r'\s*[.,;]\s*', string)


print(*custom_split(input()))
