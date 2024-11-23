'''
TODO:
    Complete the above code using a list expression so that you get a new list
    containing the string lengths of the original list.
'''


def get_string_lengths(strings: list[str]) -> list[int]:
    """
    This function takes a list of strings and returns a list of integers,
    where each integer is the length of the corresponding string in
    the input list.

    Args:
    strings (list[str]): A list of strings.

    Returns:
    list[int]: A list of the lengths of the strings in the input list.
    """
    return [len(i) for i in strings]


# Example usage
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
            'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in',
            'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
            'return', 'while', 'yield']

lengths = get_string_lengths(keywords)
print(lengths)
