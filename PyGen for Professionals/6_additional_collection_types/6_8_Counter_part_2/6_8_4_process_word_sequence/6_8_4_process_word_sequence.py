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
from collections import Counter
from typing import List, Counter as CounterType


def get_words_sequence() -> List[str]:
    """
    Receives input from the user, splits it into words, and converts them to
    lowercase.

    Returns:
        List[str]: A list of words in lowercase.
    """
    input_sequence = input().split()
    return [element.lower() for element in input_sequence]


def get_word_lengths(sequence: List[str]) -> CounterType[int]:
    """
    Gets the lengths of words in the sequence and counts their occurrences.

    Args:
        sequence (List[str]): A list of words.

    Returns:
        CounterType[int]: A counter with word lengths as keys and their counts
        as values.
    """
    lengths = [len(element) for element in sequence]
    return Counter(lengths)


def sort_counter_by_count(counter: CounterType[int]) -> CounterType[int]:
    """
    Sorts the counter by the count of its values.

    Args:
        counter (CounterType[int]): A counter to sort.

    Returns:
        CounterType[int]: A sorted counter by the count of values.
    """
    sorted_dict = dict(sorted(counter.items(), key=lambda item: item[1]))
    return Counter(sorted_dict)


def display_result(data: CounterType[int]) -> None:
    """
    Displays the result of word length grouping and counting.

    Args:
        data (CounterType[int]): A counter with word lengths and their counts.
    """
    data = sort_counter_by_count(data)
    for key, value in data.items():
        print(f'Words of length {key}: {value}')


def process_word_sequence() -> None:
    """
    Processes the sequence of words to group by length and display the result.
    """
    sequence = get_words_sequence()
    word_lengths_counter = get_word_lengths(sequence)
    display_result(word_lengths_counter)


if __name__ == "__main__":
    process_word_sequence()
