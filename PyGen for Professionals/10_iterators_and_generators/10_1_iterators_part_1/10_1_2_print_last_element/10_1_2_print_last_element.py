'''
TODO:
    You have a list numbers that contains integers.

    Complete the code below with iter() and next() functions so that it prints
    the last element of the list.
'''
from typing import List


numbers = [100, 70, 34, 45, 30,
           83, 12, 83, -28, 49,
           -8, -2, 6, 62, 64,
           -22, -19, 61, 13, 5,
           80, -17, 7, 3, 21,
           73, 88, -11, 16, -22]


def print_last_element(any_list: List[int]) -> None:
    """
    Print the last element of the given list.

    Args:
        any_list (list[int]): The list from which the last element is to be
        printed.

    Returns:
        None
    """
    if not any_list:
        raise ValueError("The list is empty and has no last element.")

    # Create an iterator for the list
    iterator = iter(any_list)

    # Iterate through the list to reach the last element
    for _ in range(len(any_list) - 1):
        next(iterator)

    # Print the last element
    print(next(iterator))


# Test the function
print_last_element(numbers)
