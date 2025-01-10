'''
TODO:
    Using a set generator, complete the code below to produce a set containing
    the unique words in the string sentence that are less than 4 characters
    long.

    Print the result on a single line (in lowercase) in alphabetical order,
    separating elements with a single space character.

NOTE:
    Note that punctuation marks do not apply to words.
'''
from typing import Set


def clean_word(word: str) -> str:
    """
    Removes punctuation from the word and returns it in lowercase.

    Args:
        word (str): The word to clean.

    Returns:
        str: The cleaned word in lowercase.
    """
    return word.strip(':,.!?();').lower()


def is_short(word: str) -> bool:
    """
    Checks if the cleaned word is shorter than 4 characters.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is shorter than 4 characters, otherwise False.
    """
    return len(clean_word(word)) < 4


def get_short_words(sentence: str) -> Set:
    """
    Generate a set of unique words from the sentence that are less than
    4 characters long.

    Args:
        sentence (str): The input sentence from which words are extracted.

    Returns:
        Set: A set of unique words less than 4 characters long.
    """
    # Use a set generator to extract and clean short words
    return {clean_word(word) for word in sentence.split() if is_short(word)}


def print_sorted_words(words: Set) -> None:
    """
    Prints the sorted words in alphabetical order, space-separated.

    Args:
        words (Set): A set of words to be printed in alphabetical order.
    """
    print(*sorted(words))


# Input sentence
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

# Extract short words and print them sorted
short_words = get_short_words(sentence)
print_sorted_words(short_words)
