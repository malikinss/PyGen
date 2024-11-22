'''
TODO:
    The program is given a string of text as input.

    Write a program that replaces all occurrences of the number 1 with
    the word "one".
'''


def replace_ones_with_word(text: str) -> str:
    """
    Replaces all occurrences of the digit '1' with the word 'one'
    in the given text.

    Parameters:
    text (str): The input string.

    Returns:
    str: The modified string with '1' replaced by 'one'.
    """
    return text.replace('1', 'one')


# Read input and call the function
print(replace_ones_with_word(input()))
