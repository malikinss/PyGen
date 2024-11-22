'''
TODO:
    The program is given a string of text as input.

    Write a program that removes all characters with indices multiple of 3,
    i.e. characters with indices 0, 3, 6, ....
'''


def remove_multiple_of_three(s: str) -> str:
    """
    Removes all characters from the input string whose indices
    are multiples of 3.

    Parameters:
    s (str): The input string.

    Returns:
    str: The modified string with specified characters removed.
    """
    # Using list comprehension to filter characters
    return ''.join([char for i, char in enumerate(s) if i % 3 != 0])


# Read input and call the function
s = input()
print(remove_multiple_of_three(s))
