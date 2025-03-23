'''
TODO:
    An abbreviation is a word formed by shortening a word or phrase and read
    by the alphabetical name of the initial letters or by the initial sounds
    of the words included in it.

    Implement the abbreviate() function, which takes one argument:
        - phrase — phrase

    The function should create an uppercase abbreviation from the phrase
    phrase and return it.

NOTE:
    The abbreviation must contain both the initial letters of words and the
    initial letters of subwords that begin with a capital letter, for example,
    JavaScript Object Notation -> JSON.
'''
import re


def abbreviate(phrase: str) -> str:
    """
    Create an abbreviation from the given phrase by taking the first letter of
    each word or subword that starts with a capital letter and returns it
    in uppercase.

    Args:
        phrase (str): The input phrase from which to create an abbreviation.

    Returns:
        str: The uppercase abbreviation formed from the initial letters.
    """
    regex = r'\b[a-zA-Z]|[A-Z]'
    letters = re.findall(regex, phrase)

    return ''.join(letters).upper()
