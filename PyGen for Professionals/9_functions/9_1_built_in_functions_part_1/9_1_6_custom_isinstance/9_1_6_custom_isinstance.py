"""
TODO:
    Implement a custom_isinstance() function that takes two arguments in the
    following order:
        - objects — a list of arbitrary objects
        - typeinfo — a data type or a tuple with types

    The function should return a single number — the number of objects from
    the objects list that belong to the typeinfo type or one of the types if a
    tuple was passed.

NOTE:
    It is convenient to use the isinstance() function in the task.
"""
from typing import List, Any


def custom_isinstance(objects: List[Any], typeinfo: Any) -> int:
    """
    Counts the number of objects in the list that match the given type or
    types.

    Args:
        objects (List[Any]): A list of arbitrary objects.
        typeinfo (Any): A type or a tuple of types to match against.

    Returns:
        int: The number of objects that match the given type or types.
    """
    # Ensure typeinfo is a tuple, even if a single type is passed
    if not isinstance(typeinfo, tuple):
        typeinfo = (typeinfo,)

    # Count the objects that match any of the types in typeinfo
    return sum(1 for obj in objects if isinstance(obj, typeinfo))


# Test cases
numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))  # Expected output: 2

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))  # Expected output: 4

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))  # Expected output: 0
