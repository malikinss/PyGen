'''
TODO:
    Decimal numbers separated by spaces are stored in the string variable s.

    Complete the code below so that it prints the sum of the largest
    and smallest Decimal numbers.
'''
from decimal import Decimal
from typing import List


def sum_of_min_and_max(decimal_string: str) -> Decimal:
    """
    Calculate the sum of the smallest and largest Decimal numbers in a string.

    Args:
        decimal_string (str): A string containing Decimal numbers separated
                              by spaces.

    Returns:
        Decimal: The sum of the smallest and largest Decimal numbers.
    """
    # Convert the string to a list of Decimal numbers
    decimal_numbers: List[Decimal] = [
        Decimal(element) for element in decimal_string.split()
    ]

    # Find the minimum and maximum values
    min_number: Decimal = min(decimal_numbers)
    max_number: Decimal = max(decimal_numbers)

    # Return the sum of the smallest and largest numbers
    return min_number + max_number


# Input string with Decimal numbers
decimal_string: str = (
    '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 '
    '0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.23 1.22 1.02 '
    '7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 '
    '5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
)

# Calculate and print the result
result: Decimal = sum_of_min_and_max(decimal_string)
print(result)
