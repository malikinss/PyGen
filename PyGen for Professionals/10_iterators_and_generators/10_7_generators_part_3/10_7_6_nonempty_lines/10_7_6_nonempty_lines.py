'''
TODO:
    Implement a generator function nonempty_lines() that takes one argument:
    file — the name of a text file, for example, data.txt

    The function should return a generator that produces a sequence of all
    non-empty lines in file with the line break \n removed.

    If a line contains more than 25 characters, it is replaced with
    an ellipsis ....

NOTE:
    When opening a file, use explicit UTF-8 encoding.
'''
from typing import Generator


def nonempty_lines(file: str) -> Generator[str, None, None]:
    """
    Generate non-empty lines from a text file, with long lines replaced
    by ellipsis.

    This function processes each line of the file and strips trailing
    whitespace characters.
    If a line has more than 25 characters, it is replaced with an
    ellipsis ('...').

    Args:
        file (str): The path to the text file.

    Yields:
        str: A non-empty line from the file, with long lines replaced
        by ellipsis.
    """
    with open(file, 'r', encoding='utf-8') as file_handle:
        for line in file_handle:
            stripped_line = line.rstrip('\n').strip()
            if stripped_line:
                yield stripped_line if len(stripped_line) <= 25 else '...'
