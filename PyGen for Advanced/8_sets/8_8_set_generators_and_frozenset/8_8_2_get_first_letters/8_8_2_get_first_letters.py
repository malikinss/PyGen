'''
TODO:
    Using a set generator, complete the code below to produce a set containing
    the first letter of each word (in lowercase) in 'words'.

    Print the result on a single line in alphabetical order, separating
    elements with a single space character.
'''
from typing import Set


def get_first_letters(words: list) -> Set:
    """
    Extracts the first letter of each word in lowercase from the given list
    of words.

    Args:
        words (list): A list of words.

    Returns:
        Set: A set containing the first letter of each word in lowercase.
    """
    return {word[0].lower() for word in words}


def print_sorted_letters(letters: set) -> None:
    """
    Prints the sorted letters in alphabetical order, space-separated.

    Args:
        letters (set): A set of letters to be printed in alphabetical order.
    """
    print(*sorted(letters))


words = [
    'Plum', 'Grapefruit', 'apple', 'orange',
    'pomegranate', 'Cranberry', 'lime',
    'Lemon', 'grapes', 'persimmon', 'tangerine',
    'Watermelon', 'currant', 'Almond'
]

first_letters = get_first_letters(words)
print_sorted_letters(first_letters)
