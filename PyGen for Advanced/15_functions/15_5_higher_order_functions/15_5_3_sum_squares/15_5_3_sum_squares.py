'''
TODO:
    Write a program to calculate and print the sum of the squares of
    the elements of the numbers list.

NOTE:
    Try solving the problem in two ways: using the reduce() function and
    using the map() and sum() functions.
'''
from typing import Callable, List


def reduce(
    operation: Callable[[int, int], int], items: List[int], initial_value: int
) -> int:
    """
    Applies a binary function to the items in the list cumulatively to reduce
    it to a single value.

    Args:
        operation (function): A function that takes two arguments and returns
                              a single value.
        items (list): A list of elements to reduce.
        initial_value (int): The initial value for the reduction.

    Returns:
        int: The reduced value.
    """
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc


def sum_of_squares(x: int, y: int) -> int:
    """
    Returns the sum of the squares of two numbers.

    Args:
        x (int): The accumulated sum.
        y (int): The current number from the list.

    Returns:
        int: The new sum of squares.
    """
    return x + y ** 2


numbers = [
    97, 42, 9, 32, 3, 45, 31, 77, -1, 11,
    -2, 75, 5, 51, 34, 28, 46, 1, -8, 84,
    16, 51, 90, 56, 65, 90, 23, 35, 11,
    -10, 70, 90, 90, 12, 96, 58, -8, -4,
    91, 76, 94, 60, 72, 43, 4, -6, -5, 51,
    58, 60, 30, 38, 67, 62, 36, 72, 34, 82,
    62, -1, 60, 82, 87, 81, -7, 57, 26, 36,
    17, 43, 80, 40, 75, 94, 91, 64, 38, 72,
    29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82,
    1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73
]

# Using reduce to sum the squares of the elements
sum_squares_reduce = reduce(sum_of_squares, numbers, 0)
print(f"Sum of squares using reduce: {sum_squares_reduce}")

# Using map and sum to sum the squares of the elements
sum_squares_map_sum = sum(map(lambda x: x ** 2, numbers))
print(f"Sum of squares using map and sum: {sum_squares_map_sum}")
