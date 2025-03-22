'''
TODO:
    You have access to a set of popular publications from the social network
    Twitter, which may look like this:
        - I love BEEGEEK courses!
        - When is the OOP course? @timur_guev
        - BEEGEEK, thanks for the courses, you are the best! #python #BeeGeek
        etc.

    Write a program that determines how many publications contain the string
    beegeek.

    The program is given an arbitrary number of lines as input, each of which
    represents the next publication.

    The program must determine how many of the input lines contain the string
    beegeek in any case, and output the result.
'''
import re
import sys
from typing import List


def read_lines_from_input() -> List[str]:
    """
    Reads input lines from stdin.

    This function reads all input lines, strips trailing
    whitespace, and returns them as a list of strings.

    Returns:
        List[str]: A list of strings representing the input lines.
    """
    return [line for line in sys.stdin.readlines()]


def count_occurances(lines: List[str]) -> int:
    """
    Counts how many lines contain the string 'beegeek' in any case.

    Args:
        lines (List[str]): A list of strings (publications).

    Returns:
        int: The count of lines that contain the string 'beegeek'.
    """
    total = 0
    for line in lines:  # Fixed the missing colon here
        if re.search(r'beegeek', line, re.I):
            total += 1

    return total


print(count_occurances(read_lines_from_input()))
