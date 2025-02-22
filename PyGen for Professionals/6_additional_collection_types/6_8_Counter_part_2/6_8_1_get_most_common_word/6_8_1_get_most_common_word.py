'''
TODO:
    Given a sequence of words.
    Write a program that outputs the most frequently occurring word in
    this sequence.

    The program receives a sequence of words separated by a space.

    The program must determine the most frequently occurring word in the
    input sequence and output it in lowercase.

NOTE:
    It is guaranteed that the search word is unique.

    The program must ignore case.
    That is, for example, the words Python and python are considered the
    same.
'''
from collections import Counter
from typing import List


def get_words_sequence() -> List[str]:
    """
    Receives input from the user, splits it into words, and converts them to
    lowercase.

    Returns:
        List[str]: A list of words in lowercase.
    """
    input_sequence = input().split()

    return [element.lower() for element in input_sequence]


def get_most_common_word(sequence: List[str]) -> str:
    """
    Determines the most frequently occurring word in the given sequence.

    Args:
        sequence (List[str]): A list of words.

    Returns:
        str: The most frequently occurring word.
    """
    word_counts = Counter(sequence)
    most_common_word = word_counts.most_common(1)

    return most_common_word[0][0]


if __name__ == "__main__":
    sequence = get_words_sequence()
    print(get_most_common_word(sequence))
