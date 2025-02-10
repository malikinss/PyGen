'''
TODO:
    Implement the get_biggest() function, which takes one argument:
        numbers — a list of non-negative integers

    The function should return the largest number that can be made up of
    numbers from the numbers list.

    If the numbers list is empty, the function should return the number -1.

NOTE:
    Let's consider the first test with a list of numbers [1, 2, 3], from which
    the following numbers can be made:
        123, 132, 213, 231, 312, 321

    The largest of the presented is 321.
'''
from typing import List


def get_numbers_as_str_list(numbers: List[int]) -> List[str]:
    """
    Converts a list of numbers to a list of strings.

    Args:
        numbers (List[int]): A list of non-negative integers.

    Returns:
        List[str]: A list of numbers converted to strings.
    """
    return [str(number) for number in numbers]


def compare_elements(element1: str, element2: str) -> bool:
    """
    Compares two elements based on their concatenation.

    Args:
        element1 (str): The first string.
        element2 (str): The second string.

    Returns:
        bool: True if concatenating element1 before element2 is greater than
              element2 before element1, otherwise False.
    """
    return element1 + element2 > element2 + element1


def find_max_index(
    numbers_as_str: List[str], start_index: int, end_index: int
) -> int:
    """
    Finds the index of the maximum element within the given range.

    Args:
        numbers_as_str (List[str]): A list of numbers as strings.
        start_index (int): The starting index of the range.
        end_index (int): The ending index of the range.

    Returns:
        int: The index of the maximum element in the range.
    """
    max_index = start_index

    for j in range(start_index + 1, end_index):
        if compare_elements(numbers_as_str[j], numbers_as_str[max_index]):
            max_index = j

    return max_index


def swap_elements(nums_as_str: List[str], idx1: int, idx2: int) -> None:
    """
    Swaps elements at the specified indices in the list.

    Args:
        nums_as_str (List[str]): A list of numbers as strings.
        idx1 (int): The first index to swap.
        idx2 (int): The second index to swap.
    """
    nums_as_str[idx1], nums_as_str[idx2] = nums_as_str[idx2], nums_as_str[idx1]


def sort_numbers_for_maximum_combination(numbers_as_str: List[str]) -> None:
    """
    Sorts the list of numbers in a way that ensures the maximum concatenation.

    Args:
        numbers_as_str (List[str]): A list of numbers as strings.
    """
    length = len(numbers_as_str)

    for i in range(length):
        max_index = find_max_index(numbers_as_str, i, length)
        swap_elements(numbers_as_str, i, max_index)


def get_biggest(numbers: List[int]) -> int:
    """
    Returns the largest number that can be formed by concatenating the numbers
    from the given list.

    Args:
        numbers (List[int]): A list of non-negative integers.

    Returns:
        int: The largest number that can be formed by concatenating the
             numbers.
             If the list is empty, returns -1.
    """
    if not numbers:
        return -1

    numbers_as_str = get_numbers_as_str_list(numbers)

    sort_numbers_for_maximum_combination(numbers_as_str)

    # Concatenate the sorted strings and convert the result to an integer
    return int(''.join(numbers_as_str))
