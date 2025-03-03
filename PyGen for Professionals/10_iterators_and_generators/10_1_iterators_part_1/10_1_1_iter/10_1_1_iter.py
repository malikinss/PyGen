'''
TODO:
    You have a list numbers that contains integers.

    Complete the code below using the iter() and next() functions so that it
    prints the fourth element of the list.
'''
from typing import List


def get_nth_element(numbers: List[int], n: int) -> int:
    """
    Returns the n-th element (1-based index) from the list using iter() 
    nd next().

    Args:
        numbers (List[int]): List of integers.
        n (int): Index of the element to retrieve (1-based).

    Returns:
        int: The n-th element of the list.

    Raises:
        IndexError: If n is out of range.
    """
    if not (1 <= n <= len(numbers)):
        raise IndexError("Index out of range")

    num_iter = iter(numbers)
    for _ in range(n):
        result = next(num_iter)

    return result


numbers = [
    100, 70, 34, 45, 30, 83, 12, 83, -28, 49,
    -8, -2, 6, 62, 64, -22, -19, 61, 13, 5,
    80, -17, 7, 3, 21, 73, 88, -11, 16, -22
]

print(get_nth_element(numbers, 4))
