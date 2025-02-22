'''
TODO:
        Given a sequence of words.

        Write a program that outputs the least frequently occurring word in
        this sequence.

        If there are several such words, the program should output them all.

        The program is given a sequence of words separated by a space.

        The program should determine the least frequently occurring word in
        the input sequence and output it in lowercase.

        If there are several such words, the program should output them all in
        lexicographic order, in lowercase, separated by a comma and a space.

NOTE:
        The program must ignore case.
        That is, for example, the words Python and python are considered the
        same.
'''
from collections import Counter
from typing import List, Dict


def get_words_sequence() -> List[str]:
    """
    Receives input from the user, splits it into words, and converts them to
    lowercase.

    Returns:
        List[str]: A list of words in lowercase.
    """
    input_sequence = input().split()

    return [element.lower() for element in input_sequence]


def filter_dict_by_value_equal_to(given_dict: Dict[str, int],
                                  given_value: int) -> List[str]:
    """
    Filters a dictionary to return keys that have a specific value.

    Args:
        given_dict (Dict[str, int]): The dictionary to filter.
        given_value (int): The value to filter by.

    Returns:
        List[str]: A list of keys with the specified value.
    """
    return [key for key, value in given_dict.items() if value == given_value]


def get_least_frequent_words(sequence: List[str]) -> List[str]:
    """
    Determines the least frequently occurring words in a sequence.

    Args:
        sequence (List[str]): A list of words.

    Returns:
        List[str]: A list of the least frequently occurring words in
        lexicographic order.
    """
    word_counts = Counter(sequence)
    least_frequent_word_count = min(word_counts.values())
    least_frequent_words = filter_dict_by_value_equal_to(word_counts, least_frequent_word_count)

    return sorted(least_frequent_words)


def print_words(words: List[str]) -> None:
    """
    Prints a list of words separated by a comma and a space.

    Args:
        words (List[str]): A list of words to print.
    """
    print(*words, sep=', ')


if __name__ == "__main__":
    sequence = get_words_sequence()
    least_frequent_words = get_least_frequent_words(sequence)
    print_words(least_frequent_words)
