'''
TODO:
    Given a sequence of words.

    Write a program that outputs the least frequently occurring word in
    this sequence.

    If there are several such words, the program should output them all.

    The program is given a sequence of words separated by a space.

    The program should determine the least frequently occurring word in
    the input sequence and output it in lowercase.

    If there are several such words, the program should output them all in
    lexicographic order, in lowercase, separated by a comma and a space.

NOTE:
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


def get_least_frequent_words(sequence: List[str]) -> List[str]:
    """
    Determines the least frequently occurring words in a sequence.

    Args:
        sequence (List[str]): A list of words.

    Returns:
        List[str]: A list of the least frequently occurring words in
        lexicographic order.
    """
    word_counts = Counter(sequence)
    least_frequent_word_count = min(word_counts.values())
    least_frequent_words = [
        word for word, count in word_counts.items()
        if count == least_frequent_word_count
    ]

    return sorted(least_frequent_words)


if __name__ == "__main__":
    sequence = get_words_sequence()
    least_frequent_words = get_least_frequent_words(sequence)
    print(', '.join(least_frequent_words))
