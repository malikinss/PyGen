'''
TODO:
    A block of code in Python is given.

    Write a program that deletes all lines in the given code that contain only
    comments.

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
    return [line for line in sys.stdin.readlines()]


def remove_comment_lines(code_snippet: List[str]) -> List[str]:
    """
    Removes all lines that contain only comments from the provided code
    snippet.

    Args:
        code_snippet (List[str]): The list of code lines.

    Returns:
        List[str]: The list of code lines excluding those that contain only
                   comments.
    """
    return [line for line in code_snippet if not line.lstrip().startswith('#')]


def display_code(code_snippet: List[str]) -> None:
    """
    Displays the code snippet.

    Args:
        code_snippet (List[str]): The list of code lines to display.
    """
    print(*code_snippet, sep='')


# Main execution
user_code = read_code_from_input()
updated_code = remove_comment_lines(user_code)
display_code(updated_code)
