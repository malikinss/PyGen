"""
TODO:
    You are given a dictionary consisting of pairs of synonymous words.

    There are no duplicate words in the dictionary.

    Write a program that determines a synonym for one given word.

NOTE:
    It is guaranteed that a synonym for the entered word exists in
    the dictionary.

    All words in the dictionary begin with a capital letter.
"""
from typing import Dict


def build_synonyms_dict(num_records: int) -> Dict[str, str]:
    """
    Builds a dictionary of synonyms from the input.

    Args:
        num_records (int): The number of synonym pairs to input.

    Returns:
        Dict[str, str]: A dictionary where each word is paired with
                        its synonym.
    """
    synonyms = {}
    for _ in range(num_records):
        word, synonym = input("Enter a word and its synonym: ").split()
        synonyms[word] = synonym
        synonyms[synonym] = word  # Ensures bidirectional mapping
    return synonyms


def find_synonym(synonyms: Dict[str, str], word: str) -> str:
    """
    Finds the synonym of a given word from the synonyms dictionary.

    Args:
        synonyms (Dict[str, str]): A dictionary of synonyms.
        word (str): The word to find the synonym for.

    Returns:
        str: The synonym of the given word.
    """
    return synonyms[word]


# Main execution
num_pairs = int(input("Enter the number of synonym pairs: "))
synonyms_dict = build_synonyms_dict(num_pairs)
query_word = input("Enter a word to find its synonym: ")
synonym = find_synonym(synonyms_dict, query_word)

print(synonym)
