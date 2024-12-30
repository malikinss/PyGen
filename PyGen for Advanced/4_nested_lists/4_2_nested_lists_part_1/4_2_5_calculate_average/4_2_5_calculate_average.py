'''
TODO:
    Complete the code below so that it prints a single number - the sum of all
    the numbers in list1 divided by the total number of all numbers.
'''
from typing import List


def calculate_average(list1: List[List[int]]) -> float:
    """
    Calculates the average of all elements in a list of nested lists.

    Args:
        list1 (List[List[int]]): A list of nested lists containing integers.

    Returns:
        float: The average value of all integers in the nested lists.
    """
    total = 0
    counter = 0

    for li in list1:
        counter += len(li)
        total += sum(li)

    return total / counter if counter != 0 else 0.0


# Example usage
list1 = [
    [1, 7, 8],
    [9, 7, 102],
    [102, 106, 105],
    [100, 99, 98, 103],
    [1, 2, 3]
]

print(calculate_average(list1))
