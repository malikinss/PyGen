'''
TODO:
    Let's call a multiplication of a string by a number a record in the format
    n(string), where n is a non-negative integer, and string is a string that
    must be written n times.

    We will consider the expansion of a multiplication to be an expanded
    version of this record, for example, the string ti2(Be)3(Ge) after
    expanding all the multiplications in it will look like tiBeBeGeGeGe.

    Write a program that expands all the multiplications in the text and
    outputs the result.

    The program is given one input line containing lowercase Latin letters,
    numbers and brackets.

    The program must output a line in which all the multiplications are
    expanded taking into account the priority of the operations.

NOTE:
    It is guaranteed that the multiplication in the supplied line is always
    written correctly, that is, strictly in the format n(string).

    Records of the form 4(2), 3q, (fg)7 are incorrect.

    Let's consider the third test.
    Taking into account the priority of operations, we first expand the
    multiplication 2(a) and obtain the intermediate string bbbb10(aa)bbb, then
    expand the multiplication 10(aa) and obtain the final result as the string
    bbbbaaaaaaaaaaaaaaaaaaaabbb.

    The string in which all multiplications are expanded always contains only
    lowercase Latin letters.

    The maximum length of the resulting string does not exceed 450,000
    characters.
'''
import re


def unwrap(match: re.Match) -> str:
    """
    Expands a multiplication pattern in the format n(string) by repeating
    the string n times.

    Args:
        match (re.Match): A match object containing the multiplier and
        the string.

    Returns:
        str: The expanded string.
    """
    num = int(match.group(1))
    piece = match.group(2)
    return piece * num


def expand_multiplications(text: str) -> str:
    """
    Recursively expands all multiplication patterns in a given string.

    Args:
        text (str): The input string containing multiplication patterns.

    Returns:
        str: The fully expanded string.
    """
    # Continue expanding until no more patterns are found
    while re.search(r'\d+\(\w+\)', text):
        text = re.sub(r'(\d+)\((\w+)\)', unwrap, text)
    return text


print(expand_multiplications(input()))
