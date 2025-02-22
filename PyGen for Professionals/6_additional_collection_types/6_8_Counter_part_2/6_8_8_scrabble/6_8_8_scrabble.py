'''
TODO:
    Implement a scrabble() function that takes two arguments in the following
    order:
        symbols — a set of symbols
        word — a word

    The function should return True if the set of symbols can be used to form
    the word word, or False otherwise.

NOTE:
    The check takes into account the number of characters needed to form a
    word, and is not case-sensitive.
'''
from collections import Counter


def scrabble(symbols: str, word: str) -> bool:
    """
    Determines if the given word can be formed from the set of available
    symbols.

    Args:
        symbols (str): A string of available symbols.
        word (str): The word to form.

    Returns:
        bool: True if the word can be formed from the symbols, False otherwise.
    """
    return Counter(symbols.lower()) >= Counter(word.lower())


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
print(scrabble('begk', 'beegeek'))
