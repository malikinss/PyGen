'''
TODO:
    Write a program that takes a string of text and a word as input and
    determines how many times the word appears as a subword in the input text.

    The program receives text on the first line, and a word on the second line.

    The program must determine how many times the word appears as a subword in
    the input text and output the result.

NOTE:
    A word is a sequence of characters corresponding to \\w, surrounded by
    characters corresponding to \\W.

    A subword is a sequence of characters corresponding to \\w, surrounded by
    characters corresponding to \\w.

    For example, is is a subword of optimist, and age is not a subword of
    ageless.

    The program must be case-sensitive.

    That is, for example, the words Python and python are considered different.
'''
import re


def count_inside(text: str, pattern: str) -> int:
    """
    Counts occurrences of a word as a subword inside other words in the text.

    Args:
        text (str): Input text.
        pattern (str): Word to search as a subword.

    Returns:
        int: Number of times the word appears as a subword.
    """
    regex = rf'(?<=\w){re.escape(pattern)}(?=\w)'
    return len(re.findall(regex, text))


text = input()
word = input()

print(count_inside(text, word))
