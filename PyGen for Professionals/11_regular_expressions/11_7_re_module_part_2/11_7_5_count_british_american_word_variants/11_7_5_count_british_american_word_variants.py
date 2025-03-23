'''
TODO:
    In one of the previous tasks, we have already observed the difference in
    the spelling of British and American words.

    Another difference is that Britain has kept the use of the letter
    combination our in its words, while America has abandoned the letter u and
    uses only or.

    Write a program that determines how many times a word appears in a text,
    given its British-American spelling.

    The program receives a word written in the British variant on the first
    line, and a text on the next line.

    The program must determine how many times the entered word appears in the
    text, given its British-American spelling, and output the result.

NOTE:
    A word is considered to be a sequence of characters corresponding to \\w,
    surrounded by characters corresponding to \\W.

    It is guaranteed that the entered word consists of 4 or more letters.

    The program must ignore case. That is, for example, the words Python and
    python are considered the same.
'''
import re


def count_british_american_word_variants(text: str, word: str) -> int:
    """
    Counts the occurrences of a word in a text, considering both British and
    American spellings.

    The word is provided in the British variant (with 'our' in it).

    The program will count both the British and American spelling variants
    (with 'our' and 'or' at the end) in the text, ignoring case.

    Args:
        text (str): The input text in which to search for the word.
        word (str): The word in British spelling (with 'our') to count.

    Returns:
        int: The number of times the word (with both British and American
        spellings) appears in the text.
    """
    regex = rf'\b{word[:-3]}(ou?r)\b'

    return len(re.findall(regex, text, re.I))


word = input()
text = input()

print(count_british_american_word_variants(text, word))
