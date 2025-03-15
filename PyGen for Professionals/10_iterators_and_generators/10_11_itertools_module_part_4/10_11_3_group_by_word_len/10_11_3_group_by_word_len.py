'''
TODO:
    Write a program that groups words by their length.

    The program receives a sequence of words separated by a space.

    Each word is written in lowercase Latin letters.

    The program must group the input words by their length and output the
    resulting groups.

    The length must be specified for each group, and then the words of the
    corresponding length must be listed, separated by commas.

    The groups must be arranged in order of increasing length, each on
    a separate line, the words in the groups must be in alphabetical order,
    in the following format:
        <length> -> <word>, <word>, ...
'''
from itertools import groupby
from typing import List


def print_result(length: int, words: List[str]) -> None:
    """
    Prints the word length and corresponding words in a formatted way.

    Args:
        length (int): The length of the words in the group.
        words (List[str]): The list of words that have the same length.

    Returns:
        None
    """
    print(f'{length} -> {", ".join(words)}')


def group_by_word_len(words: List[str]) -> None:
    """
    Groups words by their length, sorts the words alphabetically within each
    group, and prints the groups in increasing order of length.

    Args:
        words (List[str]): A list of words (in lowercase Latin letters) to be
        grouped.

    Returns:
        None
    """
    words.sort(key=len)
    grouped = groupby(words, key=len)

    for length, group in grouped:
        print_result(length, sorted(group))


words = input().split()
group_by_word_len(words)
