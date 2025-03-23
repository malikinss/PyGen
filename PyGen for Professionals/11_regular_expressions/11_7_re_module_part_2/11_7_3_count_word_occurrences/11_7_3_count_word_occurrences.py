'''
TODO:
    Write a program that takes a text string and a word as input and
    determines how many occurrences of the word are contained in the input
    text.

    The program receives text on the first line, and a word on the second line.

    The program must determine how many occurrences of the word are contained
    in the input text and output the result.

NOTE:
    A word is a sequence of characters corresponding to \\w, surrounded by
    characters corresponding to \\W.
'''
import re


def count_word_occurrences(text: str, word: str) -> int:
    """
    Counts the occurrences of a specific word in a given text.

    The word is considered as a whole word, meaning it is surrounded by
    non-word characters.

    Args:
        text (str): The input text in which to search for the word.
        word (str): The word to count occurrences of.

    Returns:
        int: The number of times the word appears in the text.
    """
    regex = rf'\b{re.escape(word)}\b'
    return len(re.findall(regex, text))


text = input()
word = input()

print(count_word_occurrences(text, word))
