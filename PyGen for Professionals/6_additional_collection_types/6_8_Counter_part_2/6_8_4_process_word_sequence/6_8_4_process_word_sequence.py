'''
TODO:
    A sequence of words is given.

    Write a program that groups words from this sequence by their length
    and determines the number of words in each resulting group.

    The program receives a sequence of words separated by a space as input.

    The program must group words from the input sequence by their length
    and determine the number of words in each resulting group.

    Each group is characterized by two numbers - the length of the words
    in this group and the number of words in this group.

    For example, for the group {is, to, hi, no} these are the numbers
    2 and 4.

    The program must output data about each group, arranging them in order
    of increasing number of words in them, each on a separate line, in the
    following format:
        Words of length <length of words in group>: <number of words in group>

NOTE:
    If two different groups have the same number of words, then the group
    whose word occurs earlier in the original sequence should come first.
'''
from collections import defaultdict
from typing import List


def get_words_sequence() -> List[str]:
    """
    Receives input from the user, splits it into words, and converts them to
    lowercase.

    Returns:
        List[str]: A list of words in lowercase.
    """
    input_sequence = input().split()
    return [element.lower() for element in input_sequence]


def group_words_by_length(sequence: List[str]) -> defaultdict:
    """
    Groups words by their length and counts the number of words in each group.

    Args:
        sequence (List[str]): A list of words.

    Returns:
        defaultdict: A dictionary where keys are word lengths and values are
        lists of words of those lengths.
    """
    grouped = defaultdict(list)
    for word in sequence:
        grouped[len(word)].append(word)

    return grouped


def display_result(grouped_data: defaultdict) -> None:
    """
    Displays the result of word length grouping and counting.

    Args:
        grouped_data (defaultdict): A dictionary with word lengths as keys and
                                    lists of words as values.
    """
    # Sort by the number of words in each group (ascending)
    sorted_groups = sorted(grouped_data.items(), key=lambda item: len(item[1]))

    for length, words in sorted_groups:
        print(f'Words of length {length}: {len(words)}')


def process_word_sequence() -> None:
    """
    Processes the sequence of words to group by length and display the result.
    """
    sequence = get_words_sequence()
    grouped_data = group_words_by_length(sequence)
    display_result(grouped_data)


if __name__ == "__main__":
    process_word_sequence()
