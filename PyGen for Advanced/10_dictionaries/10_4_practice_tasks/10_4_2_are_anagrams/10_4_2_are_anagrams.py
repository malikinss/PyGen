"""
TODO:
    An anagram is a word (phrase) formed by rearranging the letters that make
    up another word (or phrase).

    For example, the English words evil and live are anagrams.

    The program is given two words as input. Write a program that determines
    whether they are anagrams.
"""
from typing import Dict


def count_character_frequencies(word: str) -> Dict[str, int]:
    """
    Counts the frequency of each character in a given word.

    Args:
        word (str): The input word whose characters' frequencies
                    are to be counted.

    Returns:
        Dict[str, int]: A dictionary where keys are characters and values
                        are their frequencies.
    """
    frequency_dict: Dict = {}
    for char in word:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict


def are_anagrams(word1: str, word2: str) -> bool:
    """
    Determines whether two words are anagrams of each other.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        bool: True if the words are anagrams, False otherwise.
    """
    freq_word_1 = count_character_frequencies(word1)
    freq_word_2 = count_character_frequencies(word2)

    return freq_word_1 == freq_word_2


# Main execution
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if are_anagrams(word1, word2):
    print("YES")
else:
    print("NO")
