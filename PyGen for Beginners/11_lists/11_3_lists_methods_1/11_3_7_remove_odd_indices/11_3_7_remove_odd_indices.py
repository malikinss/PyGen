'''
TODO:
    The input to the program is a natural number n, and then n integers.

    Write a program that creates a list from the given numbers, then removes
    all elements at odd indices, and then prints the resulting list.
'''
from typing import List


def remove_odd_indices(n: int, numbers: List[int]) -> List[int]:
    """
    This function removes all elements at odd indices in the given list
    of integers.

    Args:
    n (int): The number of integers in the list.
    numbers (List[int]): A list of n integers.

    Returns:
    List[int]: A list with all elements at odd indices removed.
    """
    # Removing elements at odd indices
    return numbers[::2]


# Input: The number of integers n
n = int(input())

# Read the list of numbers
numbers = [int(input()) for _ in range(n)]

# Call the function and print the result
result = remove_odd_indices(n, numbers)
print(result)
