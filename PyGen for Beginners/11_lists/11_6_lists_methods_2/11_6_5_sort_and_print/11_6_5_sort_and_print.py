'''
TODO:
    The input to the program is a text string containing integers.

    A list of numbers is formed from this string.

    Write a program that sorts and prints the given list first in ascending
    order and then in descending order.
'''
from typing import List


def sort_and_print(numbers: List[int]) -> None:
    """
    Sorts a list of integers in ascending and descending order
    and prints the results.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        None
    """
    # Sort in ascending order
    ascending = sorted(numbers)
    print(*ascending)

    # Sort in descending order
    descending = sorted(numbers, reverse=True)
    print(*descending)


# Input: Read a string of integers, split, and convert to a list of integers
sequence = list(map(int, input().split()))

# Process and Output: Sort and print the sequence
sort_and_print(sequence)
