'''
TODO:
    Write a program to calculate and output the sum of the squares of
    two-digit numbers from the list numbers that are divisible by 7 without
    a remainder.

NOTE:
    When solving the problem, use the filter(), map(), and sum() functions.

    The original two-digit number must be divisible by 7, not its square.

    Don't forget about negative two-digit numbers.
'''
from typing import List


def square(number: int) -> int:
    """
    Returns the square of the given number.

    Args:
        number (int): The number to square.

    Returns:
        int: The square of the number.
    """
    return number ** 2


def predicate(number: int) -> bool:
    """
    Checks if the number is a two-digit number divisible by 7.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is a two-digit number divisible by 7,
              else False.
    """
    condition_1 = (0 == number % 7)  # Check if divisible by 7
    # Check if it's a two-digit number (positive or negative)
    is_two_digit_number = (9 < abs(number) <= 99)
    return condition_1 and is_two_digit_number


def sum_of_squares_of_filtered_numbers(numbers: List[int]) -> int:
    """
    Calculates the sum of the squares of two-digit numbers divisible by 7.

    Args:
        numbers (List[int]): The list of numbers to filter and process.

    Returns:
        int: The sum of the squares of the filtered numbers.
    """
    # Use generator expression to filter, square, and sum the results
    return sum(square(number) for number in numbers if predicate(number))


# List of numbers to process
numbers = [
    77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61,
    298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99,
    270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205,
    183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260,
    -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258,
    196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5,
    187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9,
    23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211,
    5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274,
    73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10,
    236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63,
    263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172,
    216, 30, 15, 229, 205, 123, -105
]

# Calculate and print the sum of squares of the filtered numbers
print(sum_of_squares_of_filtered_numbers(numbers))
