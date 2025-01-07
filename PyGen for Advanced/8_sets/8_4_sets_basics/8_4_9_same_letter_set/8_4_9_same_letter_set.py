'''
TODO:
    The program is given a string consisting of three words as input.

    Is it true that the same set of letters was used to write all three words?
'''
from typing import List


def same_letter_set(words: List[str]) -> str:
    """
    Determines if all words in the list consist of the same set of letters.

    Args:
    words (List[str]): A list of three words.

    Returns:
    str: "YES" if all words contain the same set of letters, otherwise "NO".
    """
    first_word_set = set(words[0])
    is_same_set = all(first_word_set == set(word) for word in words[1:])

    return "YES" if is_same_set else "NO"


# Read input and call the function
words = input().split()
print(same_letter_set(words))
