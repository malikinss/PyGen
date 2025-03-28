'''
TODO:
    When writing programs, we often leave comments or documentation lines
    for functions.

    Let's define three types of comments:
        - single-line comments - lines of code that begin with the pound
        sign #.

        Single-line comments can be at any nesting level.

        For example:
            # is a single-line comment
            def func(a, b):
                # is a single-line comment
                return a + b

        - comments that immediately follow a line of code.

        In other words, it is a line of code followed by 2 spaces, a pound
        sign #, a space, and the comment itself, for example:
            numbers = [1, 2, 3] # this is a comment

        - multiline comments are one or more lines of code that begin and end
        with three quotation marks """.

        Multiline comments can be at any level of nesting.

        For example:
            """this is a multiline comment"""
            def func(a, b):
                """this is a
                multiline
                comment"""
                return a + b

    Write a program that removes all comments from Python code.

    The program is given an arbitrary number of lines of Python code as input.

    The program must remove all comments from the input code according to the
    problem statement and output the result.
NOTE:
    It is guaranteed that a comment following a line of code is uniquely
    determined.

    In other words, the # symbol is not used in the lines of code themselves.

    Blank lines at the beginning and end of all Python code, as well as spaces
    at the end lines of code are not taken into account when comparing answers.

    In other words, the entries:
        def func(a, b):
        return a + b
        def func(a, b):
        return a + b
        def func(a, b):
        return a + b
    are considered the same.
'''
import re
import sys


def read_from_input() -> str:
    """
    Reads input from stdin.

    Returns:
        str: The input code as a string.
    """
    return sys.stdin.read()


def remove_comments(code: str) -> str:
    """
    Removes all types of comments from Python code:
        - Single-line comments starting with '#'
        - Inline comments after code (preceded by two spaces)
        - Multiline comments enclosed in triple double quotes

    Args:
        code (str): The input Python code as a string.

    Returns:
        str: The cleaned Python code without comments.
    """
    pattern = r'\n? *""".*?""".*?$||\n? *#.*?$'
    cleaned_code = re.sub(pattern, '', code, flags=re.M | re.S)

    return cleaned_code


print(remove_comments(read_from_input()))
