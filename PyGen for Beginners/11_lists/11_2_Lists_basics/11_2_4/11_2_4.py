'''
TODO:
    Modify the code above so that it displays the sum
    of the minimum and maximum elements of the numbers list.
'''
from typing import List

# original code
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print()


# fixed code
def sum_min_max(numbers: List[float]):
    """
    Returns the sum of the minimum and maximum values in the given
    list of numbers.
    """
    return min(numbers) + max(numbers)


# List of numbers
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

# Call the function and print the result
print(sum_min_max(numbers))
