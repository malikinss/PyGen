'''
TODO:
    Write a program that outputs words consisting of two identical parts.

    The program is given an arbitrary number of words as input, each on
    a separate line.

    The program must output only those words from the input that consist of
    two identical syllables.

    The words must be arranged in their original order, each on a separate
    line.

NOTE:
    A word is any continuous sequence of one or more characters corresponding
    to \\w.
'''
import re
import sys
from typing import List


def read_code_from_input() -> List[str]:
    """
    Reads the phone number lines from the input.

    This function reads all input lines and strips any trailing
    whitespace characters from each line. It returns the input as a list of
    strings.

    Returns:
        List[str]: A list of phone number strings, each representing a phone
        number line.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def process_words(words: List[str]) -> None:
    """
    Processes each word and prints those consisting of two identical parts.

    A word consists of two identical parts if it can be split into two equal
    halves and both halves are the same.

    Args:
        words (List[str]): A list of words to check.

    Returns:
        None: Prints the words consisting of two identical parts.
    """
    regex = r'^(\w+)\1$'

    for word in words:
        if len(word) % 2 == 0 and re.fullmatch(regex, word):
            print(word)


process_words(read_code_from_input())
