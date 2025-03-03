'''
TODO:
    Implement the cyclic_shift() function using type annotations that takes
    two arguments in the following order:
        numbers — a list of integers or floats
        step — an integer

    The function should modify the passed list, cyclically shifting the list
    elements by step steps, and return None.

    If step is a positive number, the shift is to the right;
    if it is negative, the shift is to the left.

NOTE:
    Use the built-in types (list, tuple, ...), not the types from
    the typing module.
    Also use the | notation, not the Union type from the typing module.
'''
from collections import deque


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    """
    Cyclically shifts elements in the list by the specified number of steps.

    Args:
        numbers (list[int | float]): List of numbers to be shifted.
        step (int): Number of steps to shift the list.
        Positive values shift right, negative values shift left.

    Returns:
        None: The list is modified in place.
    """
    # Create a deque from the list to utilize the rotate function
    rotated_deque = deque(numbers)

    # Perform cyclic rotation
    rotated_deque.rotate(step)

    # Modify the original list in place
    numbers[:] = list(rotated_deque)
