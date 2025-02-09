'''
TODO:
    The program is given a line of text with the name of the text file as
    input.

    Write a program that displays the contents of this file, but with the
    replacement of all forbidden words with asterisks * (the number of
    asterisks is equal to the number of letters in the word).

    Forbidden words separated by a space character are stored in a text file
    forbidden_words.txt.

    It is guaranteed that all words in this file are written in lowercase.

NOTE:
    Your program should replace the forbidden words wherever they occur, even
    if they occur in the middle of another word.

    The program must replace forbidden words regardless of their case.

    For example, if the file forbidden_words.txt contains the forbidden word
    exam, then the words exam, Exam, ExaM, EXAM and the like should be
    replaced with ****.
'''
import re
from typing import List


def get_forbidden_words() -> List[str]:
    """
    Reads the list of forbidden words from the 'forbidden_words.txt' file.

    Returns:
        List[str]: A list of forbidden words from the file.
    """
    with open('forbidden_words.txt', 'rt', encoding='utf-8') as file:
        return file.read().split()


def mask_forbidden_words(text: str, words: List[str]) -> str:
    """
    Replaces all occurrences of forbidden words in the text with asterisks.

    Args:
        text (str): The input text.
        words (List[str]): A list of forbidden words.

    Returns:
        str: The text with forbidden words replaced by asterisks.
    """
    pattern = re.compile(
        r'(' + '|'.join(map(re.escape, words)) + r')', re.IGNORECASE
    )
    return pattern.sub(lambda m: '*' * len(m.group()), text)


def replace_forbidden_words_in_file() -> None:
    """
    Reads the input text file, replaces forbidden words with asterisks,
    and prints the processed lines.
    """
    forbidden_words: List[str] = get_forbidden_words()
    filename: str = input().strip()

    with open(filename, 'rt', encoding='utf-8') as file:
        for line in file:
            print(mask_forbidden_words(line.strip(), forbidden_words))


# Start execution
replace_forbidden_words_in_file()
