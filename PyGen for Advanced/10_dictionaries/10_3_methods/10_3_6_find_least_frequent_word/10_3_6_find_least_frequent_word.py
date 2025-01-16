"""
TODO:
    The program is given a string of text as input.

    Write a program that outputs the word that occurs least frequently,
    regardless of case.

    If there are several such words, output the one that is the least
    lexicographically.

NOTE:
    The program should not be case sensitive, the words apple and Apple should
    be perceived as the same.

    A word is a sequence of letters.

    In addition to words, the text may contain spaces and punctuation
    marks .,!?:;-, which should be ignored.

    There are no other symbols in the text.
"""
from string import punctuation
from typing import Dict


def find_least_frequent_word(text: str) -> str:
    """
    Finds the word that occurs least frequently in the text, ignoring case
    and punctuation.
    If multiple words are equally rare, the lexicographically smallest one
    is returned.

    Args:
        text (str): Input string of text.

    Returns:
        str: The least frequent word in the text.
    """
    # Normalize and clean text
    cleaned_words = [
        word.strip(punctuation).lower()
        for word in text.split()
    ]

    # Count occurrences of each word
    word_count: Dict = {}
    for word in cleaned_words:
        word_count[word] = word_count.get(word, 0) + 1

    # Find the minimum frequency
    min_count = min(word_count.values())

    # Collect words with the minimum frequency
    rare_words = []
    for word, count in word_count.items():
        if count == min_count:
            rare_words.append(word)

    # Return the lexicographically smallest word
    return min(rare_words)


# Example usage
input_text = input("Enter text: ")
result = find_least_frequent_word(input_text)
print(result)
