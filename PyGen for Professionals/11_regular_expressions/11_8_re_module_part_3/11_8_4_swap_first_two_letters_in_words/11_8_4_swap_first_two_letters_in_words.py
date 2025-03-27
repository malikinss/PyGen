'''
TODO:
    Write a program that swaps the first two letters in every word of two or
    more letters.

    The program is given a string containing words as input.

    The program should swap the first two letters in every word of two or more
    letters in the input string and output the result.

NOTE:
    A word is a sequence of characters matching \\w surrounded by characters
    matching \\W.
'''
import re


def replace_first_two_letters(match: re.Match) -> str:
    """
    Swaps the first two letters of a word.

    Args:
        match (re.Match): A match object containing the word.

    Returns:
        str: The word with the first two letters swapped.
    """
    word = match.group()
    return f"{word[1]}{word[0]}{word[2:]}"


def swap_first_two_letters_in_words(text: str) -> str:
    """
    Swaps the first two letters in every word of 2 or more letters.

    Args:
        text (str): The input string containing words.

    Returns:
        str: The modified string with swapped letters.
    """
    return re.sub(r'\b\w{2,}\b', replace_first_two_letters, text)


# Read input and process the text
print(swap_first_two_letters_in_words(input()))
