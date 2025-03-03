'''
TODO:
    Dima decided to learn the English alphabet, and to speed up the learning
    process, he came up with an exercise: he takes a random English word and
    arranges all the letters in it in lexicographic order.

    Sometimes Dima takes words again, because he does not remember whether he
    took them before.

    Write a program that takes an arbitrary number of English words as input
    and arranges the letters in each in lexicographic order.

    An arbitrary number of English words are fed to the program as input, each
    on a separate line.

    The program must arrange all the letters in each entered word in
    lexicographic order and output the result.

    The words must be arranged in their original order, each on a
    separate line.

NOTE:
    Please note that the task has a time limit of one second.
'''
import sys
from typing import List
from functools import lru_cache


def read_input() -> List[str]:
    """
    Reads input from stdin and returns a list of stripped lines.

    Returns:
        List[str]: A list of input words.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def process_words(words: List[str]) -> None:
    """
    Sorts letters of each word in lexicographic order and prints the result.

    Args:
        words (List[str]): A list of words to process.
    """
    @lru_cache(maxsize=None)
    def learn_word(word: str) -> str:
        """
        Sorts the letters in a word in lexicographic order.

        Args:
            word (str): The word to be sorted.

        Returns:
            str: The word with letters sorted lexicographically.
        """
        return ''.join(sorted(word))

    for word in words:
        print(learn_word(word))


process_words(read_input())
