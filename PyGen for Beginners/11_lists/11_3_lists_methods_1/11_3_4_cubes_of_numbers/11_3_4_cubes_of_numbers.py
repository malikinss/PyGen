'''
TODO:
    The input to the program is a natural number n, and then n integers.

    Write a program that creates a list of their cubes from the given numbers.
'''
from typing import List


def cubes_of_numbers(n: int, numbers: List[int]) -> List[int]:
    """
    This function takes a number n and a list of integers, and returns a list
    where each element is the cube of the corresponding element
    in the input list.

    Args:
    n (int): The number of elements in the input list.
    numbers (List[int]): The list of integers.

    Returns:
    List[int]: A list containing the cubes of the given numbers.
    """
    return [num ** 3 for num in numbers]


# Input: Number of elements
n = int(input())

# Input: List of integers
numbers = [int(input()) for _ in range(n)]

# Call the function and print the result
result = cubes_of_numbers(n, numbers)
print(result)
