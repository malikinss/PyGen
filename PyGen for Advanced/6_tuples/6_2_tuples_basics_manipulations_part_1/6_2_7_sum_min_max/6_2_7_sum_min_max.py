'''
TODO:
    Complete the code below so that it prints the sum of the minimum
    and maximum elements of the numbers tuple.
'''
from typing import Tuple


def sum_min_max(numbers: Tuple[float, ...]) -> float:
    """
    Returns the sum of the minimum and maximum elements from the given tuple.

    Args:
    numbers (Tuple[float, ...]): A tuple containing numerical values (floats).

    Returns:
    float: The sum of the minimum and maximum values in the tuple.
    """
    min_el = min(numbers)
    max_el = max(numbers)

    return min_el + max_el


# Tuple containing numerical values
numbers: Tuple[float, ...] = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)

# Calculate and print the sum of the minimum and maximum elements
result = sum_min_max(numbers)
print(result)
