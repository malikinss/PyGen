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
from typing import List, Any, Tuple


def filter_objects_by_type(objects: List[Any],
                           typeinfo: Tuple[type, ...]) -> List[Any]:
    """
    Filters the given list of objects by the specified type or types.

    Args:
        objects (List[Any]): A list of arbitrary objects.
        typeinfo (Tuple[type, ...]): A tuple of types to filter by.

    Returns:
        List[Any]: A list of objects that match the given type or types.
    """
    return list(filter(lambda obj: isinstance(obj, typeinfo), objects))


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
    try:
        # If typeinfo is not a tuple, convert it to a tuple for consistency
        if not isinstance(typeinfo, Tuple):
            typeinfo = (typeinfo,)

        matching_objects = filter_objects_by_type(objects, typeinfo)

        return len(matching_objects)
    except TypeError as e:
        print(f"An error occurred: {e}")

        return 0


numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))  # 2

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))  # 4

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))  # 0
