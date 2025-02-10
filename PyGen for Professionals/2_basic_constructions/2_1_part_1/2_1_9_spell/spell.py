'''
TODO:
    Implement the spell() function, which takes an arbitrary number of
    positional arguments-words and returns a dictionary whose keys are the
    first letters of the words, and the values are the maximum word lengths
    for this letter.

NOTE:
    If no arguments are passed to the function, the function must return
    an empty dictionary.

    The function should ignore the case of words, while the resulting
    dictionary should contain exactly letters in lowercase.
'''
from typing import Dict


def spell(*args: str) -> Dict[str, int]:
    """
    Takes an arbitrary number of words and returns a dictionary where the keys
    are the first letters of the words (in lowercase), and the values are the
    maximum lengths of the words that start with that letter.

    Args:
        *args (str): A variable number of word arguments.

    Returns:
        Dict[str, int]: A dictionary where the keys are lowercase letters,
                        and the values are the maximum word lengths for that
                        letter.

    Notes:
        If no arguments are passed, the function returns an empty dictionary.
        The case of words is ignored when determining the first letter, but the
        resulting dictionary uses lowercase letters.
    """
    result: Dict = {}

    for word in args:
        first_letter = word[0].lower()
        cur_word_len = len(word)

        # Update the dictionary with the maximum word length for each letter
        if first_letter not in result or result[first_letter] < cur_word_len:
            result[first_letter] = cur_word_len

    return result
