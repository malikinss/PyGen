'''
TODO:
    You have a program that adds the remainder of 36 to each number in the
    numbers list to the remainders list.

    If the number is zero, it is ignored.

    Add a try-except construct to the code below to ensure that it runs
    without errors.
'''
from typing import List


def calculate_remainders(numbers: List[int]) -> List[int]:
    """
    Adds the remainder of 36 when divided by each number in the list to the
    remainders list.

    Ignores numbers that are zero.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list containing the remainders when 36 is divided by each
        non-zero number.
    """
    remainders = []

    for number in numbers:
        try:
            remainders.append(36 % number)
        except ZeroDivisionError:
            continue  # Ignore zero to avoid division by zero error

    return remainders


# Example usage
numbers = [
    6, 0, 36, 8, 2,
    36, 0, 12, 60,
    0, 45, 0, 3, 23
]

result = calculate_remainders(numbers)
print(result)
