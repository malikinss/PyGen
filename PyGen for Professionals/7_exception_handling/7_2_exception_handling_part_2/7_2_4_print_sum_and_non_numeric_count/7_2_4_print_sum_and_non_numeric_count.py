"""
TODO:
    The program is given an unspecified number of lines of input, each
    containing an arbitrary value.

    Write a program using the try-except construct that prints the sum of all
    the numbers entered, and then the number of non-numeric values entered.

    The program should print the sum of all the numbers entered (int and float
    types), and then on the next line, the number of non-numeric values
    entered.

NOTE:
    If no numbers were entered, the sum is 0.
"""
import sys
from typing import List, Tuple


def read_input() -> List[str]:
    """
    Reads multiple lines of input from stdin, strips leading/trailing
    whitespace, and returns the lines as a list of strings.

    Returns:
        List[str]: A list of input lines with leading and trailing whitespace
        removed.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def split_to_numbers_and_non_numbers(
    data: List[str]
) -> Tuple[List[float], List[str]]:
    """
    Processes a list of input strings, separating them into numeric values and
    non-numeric values.

    Args:
        data (List[str]): A list of strings representing input data.

    Returns:
        Tuple[List[float], List[str]]: A tuple where the first element
        is a list of numeric values (converted to float) and the second
        element is a list of non-numeric values.
    """
    numbers = []
    non_numbers = []

    for item in data:
        try:
            number = float(item)
            numbers.append(number)
        except ValueError:
            non_numbers.append(item)

    return numbers, non_numbers


def print_sum_and_non_numeric_count(
    numbers: List[float], non_numbers: List[str]
) -> None:
    """
    Prints the sum of all numeric values and the count of non-numeric entries.

    Args:
        numbers (List[float]): A list of numeric values (int or float).
        non_numbers (List[str]): A list of non-numeric values encountered
        in the input.
    """
    total_sum = sum(numbers)

    if total_sum == int(total_sum):
        total_sum = int(total_sum)

    print(total_sum)
    print(len(non_numbers))


# Read input data
input_data = read_input()

# Split data into numbers and non-numbers
numbers, non_numbers = split_to_numbers_and_non_numbers(input_data)

# Print the formatted sum of numbers and count of non-numeric values
print_sum_and_non_numeric_count(numbers, non_numbers)
