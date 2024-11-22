'''
TODO:
    The program is given a string of text as input.

    Write a program that removes all occurrences of the "@" symbol.
'''


def remove_at_symbol(text: str) -> str:
    """
    Removes all occurrences of the '@' symbol from the given text.

    Parameters:
    text (str): The input string.

    Returns:
    str: The modified string without '@' symbols.
    """
    return text.replace('@', '')


# Read input and call the function
print(remove_at_symbol(input()))
