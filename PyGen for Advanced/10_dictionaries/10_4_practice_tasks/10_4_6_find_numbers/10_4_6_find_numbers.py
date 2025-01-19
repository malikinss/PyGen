"""
TODO:
    Timur wrote down the phone numbers of all his friends to automate
    the search for the desired number.

    Each of Timur's friends may have one or more phone numbers.

    Write a program that will help Timur find all the numbers of
    a certain friend.

NOTE:
    Output the phone numbers of one person in one line separated by a space
    in the order in which they were specified in the input data.

    The number of lines in the answer must be equal to the number m.

    A phone number is several digits written in a row, and a name can consist
    of letters of the Russian or English alphabet.

    The entries are not repeated.
"""
from typing import Dict, List


def build_phonebook(num_entries: int) -> Dict[str, List[str]]:
    """
    Builds a phonebook from the input data.

    Args:
        num_entries (int): The number of phone-number-to-name pairs to input.

    Returns:
        Dict[str, List[str]]: A dictionary where the keys are names and
                              the values are lists of phone numbers.
    """
    phonebook: Dict = {}

    for _ in range(num_entries):
        phone, name = input("Enter phone and name: ").lower().split()
        phonebook.setdefault(name, []).append(phone)

    return phonebook


def find_numbers(phonebook: Dict[str, List[str]], num_queries: int) -> None:
    """
    Finds and prints the phone numbers of friends based on the queries.

    Args:
        phonebook (Dict[str, List[str]]): A dictionary mapping names to phone
                                          numbers.
        num_queries (int): The number of queries to process.
    """
    for _ in range(num_queries):
        query_name = input("Enter the name to search: ").lower()
        print(*phonebook.get(query_name, ['Not Found']))


# Phonebook creating
num_entries = int(input("Enter the number of phonebook entries: "))
phonebook = build_phonebook(num_entries)

# Search numbers by queries
num_queries = int(input("Enter the number of queries: "))
find_numbers(phonebook, num_queries)
