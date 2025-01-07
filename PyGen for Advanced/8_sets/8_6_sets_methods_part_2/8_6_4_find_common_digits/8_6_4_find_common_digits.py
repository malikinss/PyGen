'''
TODO:
    The program is given a natural number n as input, and then n different
    natural numbers, each on a separate line.

    Write a program that outputs all common digits in ascending order for
    all the input numbers.
'''
from typing import List


def find_common_digits(numbers: List[str]) -> List[int]:
    """
    Returns the common digits found in all the input numbers, sorted
    in ascending order.

    Args:
        numbers (List[str]): List of numbers as strings.

    Returns:
        List[int]: List of common digits in ascending order.
    """
    common_digits = set(numbers[0])

    for number in numbers[1:]:
        common_digits.intersection_update(number)

    return sorted(map(int, common_digits))


n = int(input())
numbers = [input() for _ in range(n)]

result = find_common_digits(numbers)
print(*result)
