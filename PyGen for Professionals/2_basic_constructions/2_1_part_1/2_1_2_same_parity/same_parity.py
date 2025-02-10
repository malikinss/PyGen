'''
TODO:
    Implement the same_parity() function, which takes a single argument:
        numbers — a list of integers

    The function should return a new list, the elements of which are numbers
    from the numbers list having the same parity as the first element of this
    list.

NOTE:
    The numbers in the list returned by the function must be in their original
    order.
'''
from typing import List


def same_parity(numbers: List[int]) -> List[int]:
    """
    Filters and returns a list of numbers from the input list that have
    the same parity as the first element.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers having the same parity as the first
                   element.
    """
    # Return a list with elements having the same parity as the first element
    return [x for x in numbers if x % 2 == numbers[0] % 2]
