'''
TODO:
    A sequence of words is given.

    Write a program that outputs the most frequently occurring word in
    this sequence.

    If there are several such words, the program should output the one
    that is greater in the lexicographic comparison.

    The program is given a sequence of words separated by a space.

    The program should determine the most frequently occurring word in the
    input string and output it in lowercase.

    If there are several such words, the program should output the one
    that is greater in the lexicographic comparison, also in lowercase.

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


def get_most_frequent_word(sequence: List[str]) -> str:
    """
    Determines the most frequently occurring word in a sequence.
    If there are multiple, returns the lexicographically greatest one.

    Args:
        sequence (List[str]): A list of words.

    Returns:
        str: The most frequent word in lowercase, or the lexicographically
        greatest one if multiple have the same frequency.
    """
    word_counts = Counter(sequence)
    most_frequent_words = word_counts.most_common()

    # The first element will be the most frequent word with the highest count.
    max_count = most_frequent_words[0][1]
    # Filter the list to only include words with the max count and return
    # the lexicographically largest one.
    return max(
        word for word, count in most_frequent_words if count == max_count
    )


if __name__ == "__main__":
    sequence = get_words_sequence()
    print(get_most_frequent_word(sequence))
