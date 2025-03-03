'''
TODO:
    Implement a get_min_max() function that takes one argument:
        iterable — an iterable whose elements are comparable

    The function should return a tuple whose first element is the minimum
    element of the iterable, and whose second element is the maximum element
    of the iterable.

    If the iterable is empty, the function should return None.
'''
from typing import Any, Tuple, Optional, Iterator


def get_min_max(iterable: Iterator[Any]) -> Optional[Tuple[Any, Any]]:
    """
    Returns the minimum and maximum elements of the iterable.

    Args:
        iterable (Iterator[Any]): An iterator or iterable of elements that are
        comparable.

    Returns:
        Optional[Tuple[Any, Any]]: A tuple containing the minimum and maximum
        elements of the iterable,
        or None if the iterable is empty.
    """
    try:
        iterator = iter(iterable)
        min_element = max_element = next(iterator)
    except StopIteration:
        return None

    for element in iterator:
        if element > max_element:
            max_element = element
        if element < min_element:
            min_element = element

    return (min_element, max_element)
