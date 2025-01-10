'''
TODO:
    Using a set generator, complete the code below to produce a set containing
    the unique words (in lowercase) of the string sentence.

    Print the result on a single line in alphabetical order, separating
    elements with a single space character.

NOTE:
    Note that punctuation marks do not apply to words.
'''
from typing import Set


def clean_word(word: str) -> str:
    """
    Cleans the word by removing punctuation and converting it to lowercase.

    Args:
        word (str): The word to clean.

    Returns:
        str: The cleaned word in lowercase.
    """
    return word.lower().strip(':,.!?();')


def get_unique_words(sentence: str) -> Set:
    """
    Extracts unique words from the sentence, cleaned and in lowercase.

    Args:
        sentence (str): The input sentence from which words are extracted.

    Returns:
        Set: A set of unique words in lowercase.
    """
    return {clean_word(word) for word in sentence.split()}


def print_sorted_words(words: Set) -> None:
    """
    Prints the sorted words in alphabetical order, space-separated.

    Args:
        words (set): A set of words to be printed in alphabetical order.
    """
    print(*sorted(words))


# Input sentence
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

# Get unique words and print them sorted
unique_words = get_unique_words(sentence)
print_sorted_words(unique_words)
