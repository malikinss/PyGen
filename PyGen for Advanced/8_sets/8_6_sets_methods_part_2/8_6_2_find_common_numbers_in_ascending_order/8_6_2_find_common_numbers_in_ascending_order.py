'''
TODO:
    The program is given two lines of text containing numbers as input.

    Write a program that outputs all the numbers in ascending order that
    are in both the first line and the second line.
'''
from typing import List


def find_common_numbers_in_ascending_order(
    sequence_1: List[str], sequence_2: List[str]
) -> List[int]:
    """
    Returns all common numbers between two sequences in ascending order.

    Args:
        sequence_1 (List[str]): List of numbers from the first input line.
        sequence_2 (List[str]): List of numbers from the second input line.

    Returns:
        List[int]: List of common numbers in ascending order.
    """
    set_1 = set(map(int, sequence_1))
    set_2 = set(map(int, sequence_2))

    common_numbers = sorted(set_1 & set_2)
    return common_numbers


# Main execution
sequence_1 = input().split()
sequence_2 = input().split()

result = find_common_numbers_in_ascending_order(sequence_1, sequence_2)
print(*result)
