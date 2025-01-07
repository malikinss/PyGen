'''
TODO:
    Write a program to determine the total number of different words in
    a line of text.

NOTE:
    A word is a sequence of non-space characters in a row, words are separated
    by one or more spaces.

    Punctuation marks .,;:-?! are ignored.
'''
import string


def count_different_words(text: str) -> int:
    """
    Determines the total number of different words in a given line of text,
    ignoring punctuation and case.

    Args:
        text (str): The input line of text.

    Returns:
        int: The total number of different words.
    """
    punctuation = set(string.punctuation)  # Set of punctuation marks to remove
    words = text.lower().split()

    # Clean words by stripping punctuation marks
    cleaned_words = [
        word.strip(''.join(punctuation)) for word in words
    ]

    # Return the count of unique words
    return len(set(cleaned_words))


given_string = input()
print(count_different_words(given_string))
