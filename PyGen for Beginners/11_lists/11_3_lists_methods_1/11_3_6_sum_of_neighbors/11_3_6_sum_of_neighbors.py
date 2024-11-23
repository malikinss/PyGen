'''
TODO:
    The input to the program is a natural number n≥2, and then n integers.

    Write a program that creates a list from the specified numbers,
    consisting of the sums of neighboring numbers
    (0 and 1, 1 and 2, 2 and 3, etc.).
'''
from typing import List


def sum_of_neighbors(n: int, numbers: List[int]) -> List[int]:
    """
    This function takes a list of integers and returns a list of sums
    of neighboring numbers.

    Args:
    n (int): The number of integers in the list.
    numbers (List[int]): A list of n integers.

    Returns:
    List[int]: A list of sums of neighboring numbers.
    """
    return [numbers[i] + numbers[i + 1] for i in range(n - 1)]


# Input: The number of integers n
n = int(input())

# Read the list of numbers
numbers = [int(input()) for _ in range(n)]

# Call the function and print the result
result = sum_of_neighbors(n, numbers)
print(result)
