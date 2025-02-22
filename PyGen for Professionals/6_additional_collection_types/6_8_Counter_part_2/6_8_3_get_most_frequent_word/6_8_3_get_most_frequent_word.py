'''
TODO:
        A sequence of words is given.

        Write a program that outputs the most frequently occurring word in
        this sequence.

        If there are several such words, the program should output the one
        that is greater in the lexicographic comparison.

        The program is given a sequence of words separated by a space.

        The program should determine the most frequently occurring word in the
        input string and output it in lowercase.

        If there are several such words, the program should output the one
        that is greater in the lexicographic comparison, also in lowercase.

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


def get_most_frequent_word(sequence: List[str]) -> str:
    """
    Determines the most frequently occurring word in a sequence.

    Args:
        sequence (List[str]): A list of words.

    Returns:
        str: The most frequently occurring word in lowercase. If there are
             multiple such words, the lexicographically greatest one
             is returned.
    """
    word_counts = Counter(sequence)
    most_frequent_word_count = max(word_counts.values())
    most_frequent_words = filter_dict_by_value_equal_to(word_counts, most_frequent_word_count)

    return max(most_frequent_words)


if __name__ == "__main__":
    sequence = get_words_sequence()
    print(get_most_frequent_word(sequence))
