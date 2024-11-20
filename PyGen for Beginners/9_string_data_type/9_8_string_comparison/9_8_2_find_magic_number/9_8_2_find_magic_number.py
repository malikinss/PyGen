'''
TODO:
    In a certain set of words, Sam finds a "magic" number using
    the following algorithm:
        takes the "smallest" and "largest" strings, multiplies
        the Unicode codes of the last characters of these strings,
        and squares the resulting number.

    The result is the "magic" number.

    The program is given 4 words as input.

    Find the "magic" number in this set of words.
'''
from typing import Tuple


def find_min_max_words(words_num: int) -> Tuple[str, str]:
    """
    Finds the lexicographically smallest and largest words from
    a sequence of words.

    Parameters:
    - words_num (int): The number of words to process.

    Returns:
    - tuple: A tuple containing the smallest and largest words.
    """
    min_word = None
    max_word = None

    # Loop through the number of words
    for _ in range(words_num):
        # Read the next word and strip any surrounding whitespace
        row = input().strip()

        # Initialize min_word and max_word with the first word
        if min_word is None and max_word is None:
            min_word = row
            max_word = row
        else:
            # Update the lexicographically smallest and largest words
            min_word = min(min_word, row)
            max_word = max(max_word, row)

    return min_word, max_word


def find_magic_number() -> int:
    """
    Finds the "magic" number based on the smallest and largest words.

    The "magic" number is calculated as:
        (Unicode code of the last character of the smallest word * Unicode
        code of the last character of the largest word) ** 2.

    Returns:
    - int: The calculated "magic" number.
    """
    # Find the smallest and largest words
    min_word, max_word = find_min_max_words(4)

    # Calculate the "magic" number using the last character
    # of the min and max words
    magic_number = (ord(min_word[-1]) * ord(max_word[-1])) ** 2

    return magic_number


# Output the magic number
print(find_magic_number())
