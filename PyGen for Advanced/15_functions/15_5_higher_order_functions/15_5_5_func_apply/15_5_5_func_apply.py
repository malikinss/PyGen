'''
TODO:
    Write a function func_apply() that takes a function and a list of values
    as input and returns a list in which each value is the result of applying
    the passed function to the passed list.
'''
from typing import Callable, List


def func_apply(action: Callable[[int], int], items: List[int]) -> List[int]:
    """
    Applies the given function to each item in the list and returns a new list.

    Args:
        action (Callable[[int], int]): The function to apply to each item.
        items (List[int]): The list of items to apply the function to.

    Returns:
        List[int]: A new list with the results of applying the function to
                   each item.
    """
    new_items = []
    for item in items:
        new_item = action(item)
        new_items.append(new_item)

    return new_items


# Example functions to apply
def add3(x: int) -> int:
    """
    Adds 3 to the given number.
    """
    return x + 3


def mul7(x: int) -> int:
    """
    Multiplies the given number by 7.
    """
    return x * 7


# Example usage
numbers = [1, 2, 3, 4, 5]

# Apply add3 to each number
result_add3 = func_apply(add3, numbers)
print("Add 3 to each number:", result_add3)

# Apply mul7 to each number
result_mul7 = func_apply(mul7, numbers)
print("Multiply each number by 7:", result_mul7)
