'''
TODO:
    Complete the code below so that it prints a list containing the average
    of the numbers in each nested tuple in the given tuple of tuples numbers.
'''
from typing import List, Tuple


def calculate_averages(numbers: Tuple[Tuple[int, ...], ...]) -> List[float]:
    """
    Calculates the average of numbers in each nested tuple in the given tuple
    of tuples.

    Args:
    numbers (tuple of tuples): A tuple containing nested tuples with
                               integer values.

    Returns:
    list: A list of averages of the numbers in each nested tuple.
    """
    result = []

    for element in numbers:
        average_value = sum(element) / len(element)
        result.append(average_value)

    return result


# Tuple of tuples containing numbers
numbers = (
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4),
    (90, 10)
)

# Calculate and print the averages
averages = calculate_averages(numbers)
print(averages)
