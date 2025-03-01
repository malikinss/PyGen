'''
TODO:
        You have a list of numbers, which contains integers.
        Complete the code below so that it prints the sum of the squares of
        all two-digit numbers in the list that are divisible by 9 without
        a remainder.

NOTE:
        Please note that the number itself must be divisible by 9, not
        its square.
        The map() and filter() functions are useful in this task.
'''
from typing import List


def get_two_digit_numbers_divisible_by_9(numbers: List[int]) -> List[int]:
    """
    Filters a list of numbers, returning only those that are two-digit and
    divisible by 9.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        List[int]: Filtered list of two-digit numbers divisible by 9.
    """
    return list(filter(lambda x: 9 < abs(x) < 100 and x % 9 == 0, numbers))


def sum_of_squares_of_filtered_numbers(numbers: List[int]) -> int:
    """
    Calculates the sum of squares of all two-digit numbers in the list that
    are divisible by 9.

    Args:
        numbers (List[int]): List of integers.

    Returns:
        int: Sum of squares of filtered numbers.
    """
    # Filter numbers that are two-digit and divisible by 9
    filtered_nums = get_two_digit_numbers_divisible_by_9(numbers)

    # Calculate the sum of squares of filtered numbers using map
    return sum(map(lambda x: x ** 2, filtered_nums))


numbers = [4754, -4895, -364, -4764, 4683, 1639, -43,
           228, -2701, -1503, 1223, 4340, -1296, 3939,
           -345, 623, -3275, 1003, 4367, -1739, 550,
           -1217, -1334, 1526, -4359, -3028, -4663, 3356,
           3887, 4297, -1982, 1013, 3299, 3556, -3324, 417,
           3531, -3134, 1782, 4439, 1652, -985, 4327, 1517,
           1225, -915, 2808, -3851, -1005, 3396, 2842, -3879,
           -3824, -3805, 1609, -4741, -3072, 3573, 4680, 588,
           -1430, 2378, -1095, -343, 4357, -2164, -3304, 4354,
           4926, -352, -1187, -3313, 2741, 4786, -2689, 741,
           4558, 1442, 62, -1099, -2201, -16, -3115, 1862,
           2384, 4072, -90, 204, 1158, -3134, -2512, 756, 4148,
           4370, 1756, 3609, -1148, -3909, 4123, -2906, 69, 96, 1111]

print(sum_of_squares_of_filtered_numbers(numbers))
