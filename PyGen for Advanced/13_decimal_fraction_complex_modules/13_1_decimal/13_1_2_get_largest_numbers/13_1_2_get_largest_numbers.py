'''
TODO:
    Decimal numbers separated by a space are stored in the string variable s.

    Complete the code so that it prints the sum of all numbers on the first
    line, and the 5 largest numbers in descending order, separated by a space,
    on the second line.
'''
from decimal import Decimal
from typing import List


def get_largest_numbers(numbers: List[Decimal], count: int) -> List[Decimal]:
    """
    Get the largest numbers from a list of Decimal numbers.

    Args:
        numbers (List[Decimal]): A list of Decimal numbers.
        count (int): The number of largest numbers to return.

    Returns:
        List[Decimal]: A list of the largest numbers in descending order.
    """
    # Sort the numbers in descending order and return the first 'count' numbers
    return sorted(numbers, reverse=True)[:count]


def calculate_sum(numbers: List[Decimal]) -> Decimal:
    """
    Calculate the sum of all numbers in a list of Decimal numbers.

    Args:
        numbers (List[Decimal]): A list of Decimal numbers.

    Returns:
        Decimal: The sum of all numbers.
    """
    result: Decimal = sum(numbers)  # type: ignore
    return result


# Input string with Decimal numbers
decimal_string: str = (
    '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 '
    '9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 '
    '1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 '
    '5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
)

# Convert the string to a list of Decimal numbers
decimal_numbers: List[Decimal] = [
    Decimal(element) for element in decimal_string.split()
]

# Calculate and print the sum of all numbers
sum_total: Decimal = calculate_sum(decimal_numbers)
print(sum_total)

# Get and print the five largest numbers in descending order
largest_numbers: List[Decimal] = get_largest_numbers(decimal_numbers, 5)
print(*largest_numbers)
