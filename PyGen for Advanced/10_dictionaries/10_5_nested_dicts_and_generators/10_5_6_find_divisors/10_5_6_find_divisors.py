'''
TODO:
    Complete the above code using the generator to obtain a dictionary result,
    where the key is the element of the list numbers, and the value is
    a sorted list of all its divisors, starting with 1, in ascending order.

NOTE:
    If the list numbers were numbers = [1, 6, 18], the result would be
    a dictionary:
        result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}

    You do not need to print the contents of the dictionary result.
'''
from typing import List, Dict


def find_divisors(numbers: List[int]) -> Dict[int, List[int]]:
    """
    This function receives a list of numbers and returns a dictionary where:
        - the key is each number,
        - the value is a sorted list of its divisors in ascending order
          (starting from 1).

    Args:
        numbers (List[int]): A list of integers to find divisors for.

    Returns:
        Dict[int, List[int]]: A dictionary with each number as the key and
                               its divisors as the value.
    """
    # Generate the divisors for each number in the list
    result = {
        key: [
            value for value in range(1, key + 1) if key % value == 0
        ]
        for key in numbers
    }

    return result


# Example list of numbers
numbers = [
    34, 10, 4, 6, 10,
    23, 90, 100, 21, 35,
    95, 1, 36, 38, 19,
    1, 6, 87, 1000, 13456, 360
]

# Calling the function and storing the result in 'result'
result = find_divisors(numbers)
