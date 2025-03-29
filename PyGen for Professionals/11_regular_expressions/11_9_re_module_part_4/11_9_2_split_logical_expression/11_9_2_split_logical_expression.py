'''
TODO:
    Given a logical expression consisting of variables and the operators |, &,
    'and' or 'or'.

    Write a program that splits the given string by the specified operators.

    The program receives a string containing a logical expression consisting
    of variables and the operators |, &, 'and' or 'or', with spaces between
    them.

    The program must split the input string by the specified logical operators,
    capturing surrounding spaces, and output all the values obtained during
    the splitting, separated by a comma and a space.
'''
import re


def split_logical_expression(expression: str) -> list[str]:
    """
    Splits a logical expression by logical operators ('and', 'or', '&', '|').

    Args:
        expression (str): Logical expression consisting of variables and
        operators.

    Returns:
        list[str]: List of elements obtained after splitting the expression.

    Example:
        >>> split_logical_expression("A and B or C & D | E")
        ['A', 'B', 'C', 'D', 'E']
    """
    LOGICAL_OPERATORS_PATTERN = r'\s*(?:[|&]|and|or)\s*'
    return re.split(LOGICAL_OPERATORS_PATTERN, expression)


expression = input().strip()
print(*split_logical_expression(expression), sep=', ')
