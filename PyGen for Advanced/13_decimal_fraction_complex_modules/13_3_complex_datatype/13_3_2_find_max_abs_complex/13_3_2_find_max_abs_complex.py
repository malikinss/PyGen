'''
TODO:
    Complex numbers are stored in the numbers list.

    Complete the code so that it prints the complex number with the largest
    absolute value and the absolute value of the number on separate lines.

NOTE:
    The absolute value of a complex number can be calculated using
    the built-in abs() function.
'''
from typing import List, Tuple


def find_max_abs_complex(numbers: List[complex]) -> Tuple[complex, float]:
    """
    Finds the complex number with the maximum absolute value.

    Args:
        numbers (List[complex]): List of complex numbers.

    Returns:
        Tuple[complex, float]: Complex number with the largest absolute value
        and its absolute value.
    """
    max_complex = max(numbers, key=abs)
    return max_complex, abs(max_complex)


# List of complex numbers
numbers = [
    3 + 4j, 3 + 1j, -7 + 3j,
    4 + 8j, -8 + 10j, -3 + 2j,
    3 - 2j, -9 + 9j, -1 - 1j,
    -1 - 10j, -20 + 15j, -21 + 1j,
    1j, -3 + 8j, 4 - 6j,
    8 + 2j, 2 + 3j
]

# Get the complex number with the maximum absolute value
max_complex, max_abs_value = find_max_abs_complex(numbers)

# Print the results
print(max_complex)
print(max_abs_value)
