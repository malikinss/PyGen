'''
TODO:
    You have a list numbers that contains integers.

    Complete the code below with iter() and next() functions so that it prints
    the last element of the list.
'''
from typing import List


def print_last_element(any_list: List[int]) -> None:
    """
    Print the last element of the given list using iter() and next().

    Args:
        any_list (List[int]): The list from which the last element is to
        be printed.

    Returns:
        None

    Raises:
        ValueError: If the list is empty.
    """
    if not any_list:
        raise ValueError("The list is empty and has no last element.")

    print(next(iter(reversed(any_list))))


# Пример списка
numbers = [
    100, 70, 34, 45, 30, 83, 12, 83, -28, 49,
    -8, -2, 6, 62, 64, -22, -19, 61, 13, 5,
    80, -17, 7, 3, 21, 73, 88, -11, 16, -22
]

# Вызов функции
print_last_element(numbers)
