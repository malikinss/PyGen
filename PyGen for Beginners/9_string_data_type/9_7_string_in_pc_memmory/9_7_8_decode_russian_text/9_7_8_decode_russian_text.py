'''
TODO:
    After a recent crash in the operating system from the company "Oursoft",
    Guido's computer encoding went wrong.

    Now all the letters of the Russian alphabet are displayed incorrectly:
        [u-<symbol number in the Unicode table>]

    Guido has not yet learned to read symbols in this format, so he asks you
    to write a program that will "decode" all the texts on the computer
    for him.

    The program receives a string of text as input.

    Decode the text by replacing all the [u-<symbol number in the Unicode>]
    constructions with the corresponding letters of the Russian alphabet,
    and output it.

NOTE:
    We will assume that the letter Ё is not in the Russian alphabet. 🤫
'''


def decode_russian_text(encoded_text: str) -> str:
    """
    Decodes a string with Russian letters represented as
    [u-<symbol number in Unicode>].
    Replaces each encoded Unicode number with the corresponding Russian letter.

    Parameters:
    - encoded_text (str): The input string containing encoded Russian letters.

    Returns:
    - str: The decoded text with Russian letters restored.
    """
    decoded_text = ""
    i = 0
    while i < len(encoded_text):
        # Check for the start of an encoded character
        if encoded_text[i:i+3] == "[u-":
            # Find the closing bracket and extract the Unicode number
            j = i + 3
            unicode_number = ""
            while j < len(encoded_text) and encoded_text[j] != "]":
                unicode_number += encoded_text[j]
                j += 1
            # Convert the Unicode number to the corresponding character
            if unicode_number.isdigit():
                decoded_text += chr(int(unicode_number))
            # Move the index to the character after the closing bracket
            i = j + 1
        else:
            # If not part of an encoded character, add to the result as-is
            decoded_text += encoded_text[i]
            i += 1
    return decoded_text


# Input: the encoded text
encoded_text = input()

# Decode the text
decoded_text = decode_russian_text(encoded_text)

# Output the decoded text
print(decoded_text)
