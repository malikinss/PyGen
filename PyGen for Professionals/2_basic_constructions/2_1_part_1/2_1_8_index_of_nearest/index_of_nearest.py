'''
TODO:
    Implement the index_of_nearest() function, which takes two arguments in
    the following order:
        numbers — a list of integers
        number — an integer

    The function must find the number closest to the number in the numbers
    list and return its index.

    If the numbers list is empty, the function should return the number -1.

NOTE:
    If a list containing several numbers that are simultaneously closest to
    the desired number is passed to the function, the function must return the
    smallest of the indexes of the nearest numbers.
'''
from typing import List


def get_differences(numbers: List[int], number: int) -> List[int]:
    """
    Calculate the absolute differences between each element in the list and
    the given number.

    Args:
        numbers (List[int]): A list of integers to compare.
        number (int): The integer to compare against.

    Returns:
        List[int]: A list of absolute differences between each number in
                   'numbers' and 'number'.
    """
    diff_list = []

    for cur_number in numbers:
        difference = abs(cur_number - number)
        diff_list.append(difference)

    return diff_list


def index_of_nearest(numbers: List[int], number: int) -> int:
    """
    Find the index of the number closest to the given 'number' in the 'numbers'
    list.

    Args:
        numbers (List[int]): A list of integers to search through.
        number (int): The integer to find the closest number to.

    Returns:
        int: The index of the closest number. If the list is empty, returns -1.

    Note:
        If there are multiple closest numbers, the smallest index is returned.
    """
    if len(numbers) == 0:
        return -1

    diff_list = get_differences(numbers, number)
    min_difference = min(diff_list)
    result_index = diff_list.index(min_difference)

    return result_index
