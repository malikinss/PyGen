'''
TODO:
    The program is given a string of text as input.

    Write a program that determines the number of different characters
    in the string.
'''


def count_unique_chars(text: str) -> int:
    """
    Determines the number of different (unique) characters in the given string.

    Args:
    text (str): Input string to evaluate.

    Returns:
    int: The number of unique characters in the string.
    """
    return len(set(text))


print(count_unique_chars(input()))
