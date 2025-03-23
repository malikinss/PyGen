'''
TODO:
    American English and British English have several differences, one of
    which is in the spelling of words.

    For example, words written in American English and having the suffix ze
    are often written in the British English variant using the suffix se.

    Write a program that determines how many times a word appears in a text,
    given its British-American spelling.

    The program receives a word on the first line, which can be written in
    either the British or American variant, and the text on the next line.

    The program must determine how many times the entered word appears in the
    text, given its British-American spelling, and output the result.

NOTE:
    A word is considered to be a sequence of characters corresponding to \\w,
    surrounded by characters corresponding to \\W.

    The program must ignore case.

    That is, for example, the words Python and python are considered the same.
'''
import re


def count_word_variants(text: str, word: str) -> int:
    """
    Counts the occurrences of a word in a text, considering both British and
    American spellings.

    The word can be provided in either the British or American variant
    (with 'se' or 'ze' at the end), and the program will count all occurrences
    of both variants in the text, ignoring case.

    Args:
        text (str): The input text in which to search for the word.
        word (str): The word to count, which can be written in either the
        British or American spelling.

    Returns:
        int: The number of times the word (with both British and American
        spellings) appears in the text.
    """
    regex = rf'\b{word[:-2]}[zs]e\b'

    return len(re.findall(regex, text, re.I))


word = input()
text = input()

print(count_word_variants(text, word))
