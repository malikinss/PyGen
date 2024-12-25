'''
TODO:
    The input to the program is a string of text.

    Write a program that displays the character that appears most frequently
    on the screen.

NOTE:
    If there are several such characters, output the last character in order.

    It is necessary to distinguish between uppercase and lowercase letters,
    as well as letters of the Russian and English alphabets.
'''
from typing import Dict


def most_frequent_char(given_text: str) -> str:
    """
    Finds the character that appears most frequently in the string.
    If there are multiple characters with the same frequency,
    the last one is selected.

    Args:
        given_text (str): The input string.

    Returns:
        str: The character that appears most frequently.
    """
    # Create a dictionary to store the frequency of each character
    frequency: Dict = {}

    # Count the frequency of each character
    for char in given_text:
        frequency[char] = frequency.get(char, 0) + 1

    # Find the character with the maximum frequency,
    # considering the last one in order if tied
    most_common = given_text[0]
    max_count = frequency[most_common]

    for char in given_text:
        if frequency[char] >= max_count:
            most_common = char
            max_count = frequency[char]

    return most_common


# User input
given_text = input("Enter the text: ")

# Find and print the most frequent character
result = most_frequent_char(given_text)
print(result)
