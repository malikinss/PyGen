'''
TODO:
    Anagrams are words that consist of the same letters.

    For example:
        adapter — petard
        address — seredochka
        alphabet — bazooka
        aistenok — osetinka

    Implement the group_anagrams() function, which takes one argument:
        words — a list of words

    The function should group words from the words list that are anagrams into
    tuples and return a list of the resulting tuples.

NOTE:
    The order of the tuples in the list returned by the function, as well as
    the order of the elements in these tuples, is not important.
'''
from itertools import groupby
from typing import List, Tuple


def group_anagrams(
    words: List[str]
) -> List[Tuple[str, ...]]:
    """
    Groups words that are anagrams into tuples.

    Args:
        words (List[str]): A list of words to be grouped.

    Returns:
        List[Tuple[str, ...]]: A list of tuples, each containing words that
        are anagrams.
    """
    words.sort(key=sorted)
    grouped = groupby(words, key=sorted)

    return [tuple(group) for _, group in grouped]
