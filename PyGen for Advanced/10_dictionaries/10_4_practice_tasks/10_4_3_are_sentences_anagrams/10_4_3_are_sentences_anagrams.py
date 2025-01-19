"""
TODO:
    The program is given two sentences as input. Write a program that
    determines whether they are anagrams or not.

    Your program should ignore the case of characters, punctuation marks,
    and spaces.

NOTE:
    In addition to words, the text may contain spaces and punctuation
    marks .,!?:;-.

    There are no other symbols in the text.
"""
from typing import Dict


def count_character_frequencies(text: str) -> Dict[str, int]:
    """
    Counts the frequency of each relevant character in a given text.

    Args:
        text (str): The input text whose characters' frequencies are to
                    be counted.

    Returns:
        Dict[str, int]: A dictionary where keys are characters and values are
                        their frequencies.
    """
    frequency_dict: Dict = {}

    for char in text:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1

    return frequency_dict


def clean_text(text: str) -> str:
    """
    Removes spaces, punctuation marks, and converts text to lowercase.

    Args:
        text (str): The input text to clean.

    Returns:
        str: A cleaned version of the input text containing only lowercase
             letters.
    """
    allowed_characters = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    return ''.join(char for char in text if char in allowed_characters)


def are_sentences_anagrams(sentence1: str, sentence2: str) -> bool:
    """
    Determines whether two sentences are anagrams of each other.

    Args:
        sentence1 (str): The first sentence.
        sentence2 (str): The second sentence.

    Returns:
        bool: True if the sentences are anagrams, False otherwise.
    """
    cleaned_sentence_1 = clean_text(sentence1)
    cleaned_sentence_2 = clean_text(sentence2)

    frequencies_sentence_1 = count_character_frequencies(cleaned_sentence_1)
    frequencies_sentence_2 = count_character_frequencies(cleaned_sentence_2)

    return frequencies_sentence_1 == frequencies_sentence_2


# Main execution
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

if are_sentences_anagrams(sentence1, sentence2):
    print("YES")
else:
    print("NO")
