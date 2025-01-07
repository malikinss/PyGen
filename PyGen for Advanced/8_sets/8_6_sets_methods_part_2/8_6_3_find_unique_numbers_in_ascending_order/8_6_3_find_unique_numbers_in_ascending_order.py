'''
TODO:
    The program is given two lines of text containing numbers as input.

    Write a program that outputs all the numbers in ascending order that
    are in the first line but not in the second.
'''
from typing import List


def find_unique_numbers_in_ascending_order(
    sequence_1: List[str], sequence_2: List[str]
) -> List[int]:
    """
    Returns all numbers that are in the first sequence but not in the second,
    in ascending order.

    Args:
        sequence_1 (List[str]): List of numbers from the first input line.
        sequence_2 (List[str]): List of numbers from the second input line.

    Returns:
        List[int]: List of unique numbers from the first sequence,
                    sorted in ascending order.
    """
    set_1 = set(map(int, sequence_1))
    set_2 = set(map(int, sequence_2))

    unique_numbers = sorted(set_1 - set_2)
    return unique_numbers


# Main execution
sequence_1 = input().split()
sequence_2 = input().split()

result = find_unique_numbers_in_ascending_order(sequence_1, sequence_2)
print(*result)
