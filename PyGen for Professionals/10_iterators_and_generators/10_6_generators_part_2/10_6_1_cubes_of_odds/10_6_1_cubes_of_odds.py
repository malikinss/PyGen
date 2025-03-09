'''
TODO:
    You can access the cubes_of_odds() generator function, which takes an
    iterable whose elements are integers as an argument and returns
    a generator that produces a sequence of odd numbers in the passed iterable
    raised to the third power.

    Rewrite this function using a generator expression to accomplish
    the same task.

NOTE:
    If the generator expression becomes large enough, it can be written over
    multiple lines.
'''
from typing import Iterable, Generator
"""
# original code

def cubes_of_odds(iterable):
    for number in iterable:
        if number % 2:
            yield number ** 3
"""


def cubes_of_odds(iterable: Iterable[int]) -> Generator[int, None, None]:
    """
    Returns a generator that yields the cubes of all odd numbers in the given
    iterable.

    Args:
        iterable (Iterable[int]): An iterable containing integers.

    Yields:
        int: The cube of each odd integer in the input iterable.

    Example:
        nums = [1, 2, 3, 4, 5]
        for num in cubes_of_odds(nums):
            print(num)
        # Output: 1, 27, 125
    """
    return (number**3 for number in iterable if number % 2)
