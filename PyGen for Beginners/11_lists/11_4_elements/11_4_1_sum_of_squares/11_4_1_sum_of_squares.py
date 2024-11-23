'''
TODO:
    Modify the code above so that it prints the sum of the
    squares of the elements of the numbers list.
'''
from typing import List

# original code
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]


# fixed code
def sum_of_squares(numbers: List[int]) -> int:
    """
    Calculates the sum of the squares of the elements in the given list.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    int: The sum of the squares of the elements in the list.
    """
    return sum(i ** 2 for i in numbers)


# Input list
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

# Call the function and print the result
result = sum_of_squares(numbers)
print(result)
