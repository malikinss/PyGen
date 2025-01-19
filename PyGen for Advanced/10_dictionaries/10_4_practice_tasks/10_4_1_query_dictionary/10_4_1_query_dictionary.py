"""
TODO:
    Programmers, as you already know, are constantly learning, and they use
    a very specific language when communicating with each other.

    To systematize your growing professional lexicon, we came up with
    this task.

    Write a program to create a small dictionary of slang programming
    expressions, so that it can then return values from this dictionary
    upon request.

NOTE:
    It is guaranteed that the word or phrase being defined does not contain
    a colon (':') followed by a space.
"""

from typing import Dict


def create_developer_dictionary(dictionary_size: int) -> Dict[str, str]:
    """
    Creates a dictionary of programming slang expressions.

    This function prompts the user to input a number of terms and their
    corresponding definitions, then stores them in a dictionary.

    Args:
        dictionary_size (int): The number of terms to be added to
                               the dictionary.

    Returns:
        Dict[str, str]: A dictionary where keys are terms (slang expressions)
                        and values are their definitions.
    """
    developer_dict = {}

    for _ in range(dictionary_size):
        user_input = input()
        term, definition = user_input.split(":", 1)
        term = term.strip().lower()
        definition = definition.strip()

        developer_dict[term] = definition

    return developer_dict


def query_dictionary(
    developer_dict: Dict[str, str], queries_count: int
) -> None:
    """
    Queries the developer dictionary for definitions.

    This function prompts the user to input terms, and for each term, it looks
    up the corresponding definition in the provided dictionary and prints
    the result.

    Args:
        developer_dict (Dict[str, str]): The dictionary containing slang terms
                                         and their definitions.
        queries_count (int): The number of terms the user wants to query.

    Returns:
        None: This function does not return a value, it only prints
              the results of queries.
    """
    for _ in range(queries_count):
        term = input().lower()
        definition = developer_dict.get(term, 'Not Found')

        print(definition)


# Main execution
dictionary_size = int(input())
developer_dict = create_developer_dictionary(dictionary_size)

queries_count = int(input())
query_dictionary(developer_dict, queries_count)
