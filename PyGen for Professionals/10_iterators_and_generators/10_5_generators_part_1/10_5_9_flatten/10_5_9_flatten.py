'''
TODO:
    Implement a generator function flatten() that takes one argument:
        nested_list — a list whose elements are either integers or lists whose
                      elements are either integers or lists; nesting may be
                      arbitrary

    The function should return a generator that produces all the numbers
    contained in nested_list, including all the numbers in all nested lists,
    and then raise a StopIteration exception.
'''
from typing import Union, Generator


def flatten(nested_list: list[Union[int, list]]) -> Generator[int, None, None]:
    """
    Flattens a nested list structure into a sequence of integers.

    This function recursively traverses a list whose elements may be integers
    or nested lists, and yields all integers found in the structure.

    Args:
        nested_list (list[Union[int, list]]): A list that contains either
        integers or nested lists of integers.

    Yields:
        int: Each integer found in the nested structure.

    Example:
        nested_list = [1, [2, 3, [4, 5]], 6]
        for num in flatten(nested_list):
            print(num)
        # Output: 1, 2, 3, 4, 5, 6
    """
    for element in nested_list:
        if isinstance(element, int):
            yield element
        elif isinstance(element, list):
            yield from flatten(element)
