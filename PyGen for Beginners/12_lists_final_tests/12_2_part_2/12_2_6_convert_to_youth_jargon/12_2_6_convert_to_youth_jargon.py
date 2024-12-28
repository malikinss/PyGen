'''
TODO:
    The input to the program is a string of text.
    Write a list expression program that converts each word of the input text
    into "youth jargon" according to the following rule:
        - the first letter of each word is removed and placed
        at the end of the word;
        - then the syllable "ki" is added to the end of the word.
'''


def convert_to_youth_jargon(text: str) -> list:
    """
    Converts each word in the given text to youth jargon by removing
    the first letter of the word, placing it at the end, and adding 'ki'.

    Args:
        text (str): The input string containing words to be converted.

    Returns:
        List[str]: A list of words transformed into youth jargon.
    """
    return [word[1:] + word[0] + "ki" for word in text.split()]


# Input string
given_string = input()

# Output the converted string
print(*convert_to_youth_jargon(given_string))
