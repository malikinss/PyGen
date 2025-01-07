'''
TODO:
    The program is given two lines of text containing numbers as input.

    Write a program that determines the number of numbers that are in both
    the first line and the second line.
'''
from typing import List


def count_common_numbers(sequence_1: List[str], sequence_2: List[str]) -> int:
    """
    Determines the number of numbers that are present in both input sequences.

    Args:
        sequence_1 (List[str]): List of numbers from the first input line.
        sequence_2 (List[str]): List of numbers from the second input line.

    Returns:
        int: The number of common numbers between the two sequences.
    """
    set_1 = set(sequence_1)
    set_2 = set(sequence_2)

    common_numbers = set_1 & set_2
    return len(common_numbers)


# Main execution
sequence_1 = input().split()
sequence_2 = input().split()

result = count_common_numbers(sequence_1, sequence_2)
print(result)
