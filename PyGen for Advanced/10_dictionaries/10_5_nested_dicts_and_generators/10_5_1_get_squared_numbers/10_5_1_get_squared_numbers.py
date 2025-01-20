'''
TODO:
    Complete the above code using the generator to get a dictionary result in
    which the key is the position of the number in the numbers list
    (starting with 0) and the value is its square.

NOTE:
    You do not need to print the contents of the dictionary result.
'''
from typing import List, Dict


def get_squared_numbers(numbers: List[int]) -> Dict[int, int]:
    """
    This function takes a list of integers and returns a dictionary where:
        - The key is the position (index) of the number in the list
          (starting from 0).
        - The value is the square of the number.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        Dict[int, int]: A dictionary with indices as keys and the square
                        of numbers as values.
    """

    # Using a generator expression to create a dictionary with index
    # as key and square of number as value
    result = {index: num**2 for index, num in enumerate(numbers)}

    return result


# Sample list of numbers
numbers = [
    34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87
]

# Calling the function and storing the result in 'result'
result = get_squared_numbers(numbers)
