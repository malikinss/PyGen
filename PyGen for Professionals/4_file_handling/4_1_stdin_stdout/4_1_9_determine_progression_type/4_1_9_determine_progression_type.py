'''
TODO:
    Given a sequence of integers.

    Write a program that determines whether a given sequence is a progression,
    and if so, determines its type.

NOTE:
    It is guaranteed that the type of progression is uniquely determined.

    You can read more about arithmetic and geometric progressions here and
    here, respectively.
'''
import sys
from typing import List


def get_list_of_nums_from_input() -> List[int]:
    """
    Reads the input and returns a list of integers.

    Returns:
        List[int]: A list of integers from the input.
    """
    return [int(line.strip()) for line in sys.stdin.readlines()]


def is_arithmetic_progression(nums: List[int]) -> bool:
    """
    Checks if the given list of numbers forms an arithmetic progression.

    Args:
        nums (List[int]): A list of integers to check.

    Returns:
        bool: True if the list forms an arithmetic progression,
              False otherwise.
    """
    if len(nums) < 2:
        # A single number or empty list is trivially an arithmetic progression.
        return True

    difference = nums[1] - nums[0]
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] != difference:
            return False
    return True


def is_geometric_progression(nums: List[int]) -> bool:
    """
    Checks if the given list of numbers forms a geometric progression.

    Args:
        nums (List[int]): A list of integers to check.

    Returns:
        bool: True if the list forms a geometric progression, False otherwise.
    """
    if len(nums) < 2:
        # A single number or empty list is trivially a geometric progression.
        return True

    if nums[0] == 0:  # To avoid division by zero
        return False

    ratio = nums[1] / nums[0]
    for i in range(2, len(nums)):
        if nums[i] == 0 or nums[i] / nums[i - 1] != ratio:
            return False
    return True


def print_progressions(nums: List[int]) -> None:
    """
    Determines the type of progression (arithmetic, geometric, or none) in the
    given list of numbers.

    Args:
        nums (List[int]): A list of integers.
    """
    if is_arithmetic_progression(nums):
        print('Arithmetic progression')
    elif is_geometric_progression(nums):
        print('Geometric progression')
    else:
        print('Not a progression')


given_nums = get_list_of_nums_from_input()
print_progressions(given_nums)
