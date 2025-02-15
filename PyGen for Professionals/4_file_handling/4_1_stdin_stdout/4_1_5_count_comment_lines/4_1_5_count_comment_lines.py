'''
TODO:
    A block of code in Python is given.

    Write a program that determines the number of lines in a given code that
    contain only comments.

    If there is something else in the line besides the comment, then such
    a line does not need to be taken into account.
'''
import sys
from typing import List


def read_code_from_input() -> List[str]:
    """
    Reads the code lines from the input.

    Returns:
        List[str]: A list of strings where each string is a line of code.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def count_comment_lines(code_snippet: List[str]) -> int:
    """
    Counts the number of lines that contain only comments in the code snippet.

    Args:
        code_snippet (List[str]): The list of code lines.

    Returns:
        int: The number of lines containing only comments.
    """
    counter = 0

    for code_line in code_snippet:
        # Strip leading/trailing spaces and check if the line is only a comment
        if code_line.lstrip().startswith('#'):
            counter += 1

    return counter


print(count_comment_lines(read_code_from_input()))
