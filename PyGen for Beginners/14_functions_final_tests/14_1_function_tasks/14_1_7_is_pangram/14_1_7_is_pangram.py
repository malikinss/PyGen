'''
TODO:
    A pangram is a phrase containing all the letters of the alphabet.

    Typically, pangrams are used to present fonts so that all glyphs can be
    considered in one phrase.

    Write a function is_pangram(text) that takes a string of English text
    as an argument and returns True if the text is a pangram
    and False otherwise.

NOTE:
    It is guaranteed that the entered string contains only English letters
    and spaces.
'''


def is_pangram(text: str) -> bool:
    """
    Checks if the given text is a pangram.

    A pangram is a phrase that contains all the letters
    of the English alphabet.

    Args:
        text (str): The input text containing only English letters and spaces.

    Returns:
        bool: True if the text is a pangram, False otherwise.
    """
    # Convert text to lowercase to ensure case-insensitive comparison
    text = text.lower()

    # Check if each letter from 'a' to 'z' is present in the text
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in text:
            return False

    return True


# Input
text = input("Enter the text: ")

# Output
print(is_pangram(text))
