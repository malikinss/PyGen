'''
TODO:
    Complete the code below so that it prints the product of the elements
    of the numbers tuple.
'''
from typing import Tuple


def product_of_elements(numbers: Tuple[int, ...]) -> int:
    """
    Calculates the product of the elements in the given tuple of numbers.

    Args:
    numbers (Tuple[int, ...]): A tuple containing integers.

    Returns:
    int: The product of all integers in the tuple.
    """
    result = 1
    for element in numbers:
        result *= element  # Multiply each element to the result

    return result


# Example input
numbers = (
    2, 3, 5, 7,
    -11, 13, 17, 19,
    23, 29, 31, -6,
    41, 43, 47, 53,
    59, 61, -96, 71,
    1000, -1
)

# Calling the function and printing the result
print(product_of_elements(numbers))
