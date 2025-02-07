'''
TODO:
    Write a program that uses the built-in functions map() and filter() to:
        1) Remove all odd elements greater than 47 from the numbers list;
        2) Divides all even elements by 2 (integer division - //).

    The resulting numbers should be printed on one line, separated by a space
    character and preserving the original order.

NOTE:
    Use an anonymous function as a filtering criterion.
'''
from typing import List


def is_even(num: int) -> bool:
    """
    Checks if the given number is even.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is even, False otherwise.
    """
    return num % 2 == 0


def process_numbers(input_nums: List[int]) -> List[int]:
    """
    Processes the input list of numbers by performing the following steps:
      1) Filters out odd numbers greater than 47, i.e. keeps numbers that
         are either less than or equal to 47 or, if greater than 47, are even.
      2) Divides all even numbers by 2 using integer division; odd numbers
         remain unchanged.

    Args:
        input_numbers (List[int]): The list of integers to process.

    Returns:
        List[int]: The processed list of integers.
    """
    # Filter: Keep numbers <= 47 or numbers > 47 that are even
    filtered_numbers = list(
        filter(
            lambda num: num <= 47 or (num > 47 and is_even(num)), input_nums
        )
    )

    # Map: For even numbers perform integer division by 2;
    # leave odd numbers unchanged.
    result_numbers = list(
        map(lambda num: num // 2 if is_even(num) else num, filtered_numbers)
    )

    return result_numbers


# List of input numbers
input_numbers = [
    46, 61, 34, 17, 56,
    26, 93, 1, 3, 82,
    71, 37, 80, 27, 77,
    94, 34, 100, 36, 81,
    33, 81, 66, 83, 41,
    80, 80, 93, 40, 34,
    32, 16, 5, 16, 40,
    93, 36, 65, 8, 19,
    8, 75, 66, 21, 72,
    32, 41, 59, 35, 64,
    49, 78, 83, 27, 57,
    53, 43, 35, 48, 17,
    19, 40, 90, 57, 77,
    56, 80, 95, 90, 27,
    26, 6, 4, 23, 52,
    39, 63, 74, 15, 66,
    29, 88, 94, 37, 44,
    2, 38, 36, 32, 49,
    5, 33, 60, 94, 89,
    8, 36, 94, 46, 33
]

# Process the numbers and print the result on one line, separated by a space.
result_numbers = process_numbers(input_numbers)
print(*result_numbers)
