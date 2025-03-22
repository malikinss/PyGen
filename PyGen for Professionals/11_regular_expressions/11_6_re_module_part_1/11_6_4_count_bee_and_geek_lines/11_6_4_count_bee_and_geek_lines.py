'''
TODO:
    Write a program that determines:
        - the number of lines in which bee occurs as a substring at least twice
        - the number of lines in which geek occurs as a word at least once

    The program takes as input an arbitrary number of lines, each containing a
    set of arbitrary characters.

    The program should output two numbers:
        - the first is the number of lines in which bee occurs as a substring
          at least twice
        - the second is the number of lines in which geek occurs as a word at
          least once each on a separate line.

NOTE:
    A word is any continuous sequence of one or more characters matching \\w.

    A line can simultaneously satisfy both conditions.
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
    return [line.strip() for line in sys.stdin.readlines()]


def count_bee_and_geek_lines(lines: List[str]) -> None:
    """
    Counts how many lines contain:
    - 'bee' as a substring at least twice.
    - 'geek' as a whole word at least once.

    Args:
        lines (List[str]): A list of lines to check.

    Returns:
        None: Prints the counts for each condition.
    """
    # Regex to find 'bee' at least twice
    has_at_least_two_bee = r'(bee).*?\1'

    # Regex to find 'geek' as a whole word
    has_at_least_one_geek = r'\bgeek\b'

    # Count variables
    bees_count = 0
    geeks_count = 0

    for line in lines:
        if re.search(has_at_least_two_bee, line):
            bees_count += 1
        if re.search(has_at_least_one_geek, line):
            geeks_count += 1

    print(bees_count)
    print(geeks_count)


count_bee_and_geek_lines(read_lines_from_input())
