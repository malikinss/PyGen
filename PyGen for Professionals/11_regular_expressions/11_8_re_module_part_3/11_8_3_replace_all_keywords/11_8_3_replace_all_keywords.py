'''
TODO:
    There are keywords in Python that cannot be used to name variables,
    functions, and classes.

    You can use the kwlist attribute from the keyword module to get a list
    of all keywords.

    The code below:
        import keyword
        print(keyword.kwlist)

    outputs:
        [
            'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
            'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
            'except', 'finally', 'for', 'from', 'global', 'if', 'import',
            'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
            'return', 'try', 'while', 'with', 'yield'
        ]

    Write a program that takes a string of text and replaces all the keywords
    in it on <kw>.
'''
import re
import keyword


def replace_keyword(match: re.Match) -> str:
    """
    Replaces a Python keyword with <kw>, case-insensitive.

    Args:
        match (re.Match): A match object from the regex search.

    Returns:
        str: <kw> if the matched word is a Python keyword, otherwise the word
        itself.
    """
    word = match.group()
    if word.lower() in {kw.lower() for kw in keyword.kwlist}:
        return '<kw>'
    return word


def replace_all_keywords(string: str) -> str:
    """
    Replaces all Python keywords in the given string with the <kw> tag.

    Args:
        string (str): The input string containing words.

    Returns:
        str: The string with Python keywords replaced by <kw>.
    """
    return re.sub(r'\b[a-zA-Z_]+\b', replace_keyword, string)


print(replace_all_keywords(input()))
