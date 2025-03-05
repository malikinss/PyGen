'''
TODO:
    Implement a random_numbers() function that takes two arguments:
        left — integer
        right — integer

    The function should return an iterator that generates an infinite sequence
    of random integers in the range from left to right inclusive.

NOTE:
    It is guaranteed that left <= right.

    Submit a program to the testing system that contains only the required
    random_numbers() iterator, but not the code that calls it.
'''
from typing import Iterator
import random


def random_numbers(left: int, right: int) -> Iterator[int]:
    """
    Generates an infinite sequence of random integers within a specified range.

    Args:
        left (int): The lower bound (inclusive) of the range.
        right (int): The upper bound (inclusive) of the range.

    Returns:
        Iterator[int]: An iterator that generates random integers in the range
        [left, right] indefinitely.

    Example:
        # This will generate an infinite sequence of random numbers
        # between 1 and 10:
        rand_gen = random_numbers(1, 10)
        print(next(rand_gen))  # Output: a random number between 1 and 10
        print(next(rand_gen))  # Output: a different random number between
                               # 1 and 10
    """
    return iter(lambda: random.randint(left, right), None)
