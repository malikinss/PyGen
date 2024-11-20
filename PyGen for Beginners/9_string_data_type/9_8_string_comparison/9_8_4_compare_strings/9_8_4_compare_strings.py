'''
TODO:
    The program is given 2 strings as input.

    You need to compare these strings character by character, not taking into
    account the case and ignoring all non-alphabetic characters.

    The program should output "YES" if the strings are equal as a result
    of such a check, or "NO" otherwise.
'''


def get_only_letters(text: str) -> str:
    """
    Extracts only alphabetic characters from the given text and converts them
    to lowercase.

    This function removes all non-alphabetic characters and returns
    a lowercase version of the remaining letters.

    Parameters:
    - text (str): The input string to process.

    Returns:
    - str: A string containing only lowercase alphabetic characters.
    """
    new_text = ''

    # Loop through each character and add it if it's alphabetic
    for symbol in text:
        if symbol.isalpha():
            new_text += symbol.lower()

    return new_text


def compare_letters_in_two_texts(text_1: str, text_2: str) -> None:
    """
    Compares two strings character by character after ignoring non-alphabetic
    characters and case sensitivity.

    If the processed strings are equal, it prints "YES", otherwise prints "NO".

    Parameters:
    - text_1 (str): The first string to compare.
    - text_2 (str): The second string to compare.
    """
    # Get only alphabetic characters and convert to lowercase for both strings
    processed_text_1 = get_only_letters(text_1)
    processed_text_2 = get_only_letters(text_2)

    # Compare the processed strings and print the result
    if processed_text_1 == processed_text_2:
        print("YES")
    else:
        print("NO")


# Read the two input strings
text_1 = input()
text_2 = input()

# Compare the strings
compare_letters_in_two_texts(text_1, text_2)
