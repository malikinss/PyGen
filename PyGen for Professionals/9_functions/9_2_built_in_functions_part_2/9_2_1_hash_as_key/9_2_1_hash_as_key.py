'''
TODO:
        Implement a hash_as_key() function that takes one argument:
            objects — a list of objects to hash

        The function should return a dictionary whose key is the hash value of
        an object in the objects list, and whose value is the object itself.

        If some objects have the same hash value, they should be combined
        into a list.

NOTE:
        The elements in the dictionary returned by the function, as well as
        the objects in the list that have equal hash values, should be in
        their original order.
'''
from collections import defaultdict
from typing import List, Dict, Union


def hash_as_key(objects: List) -> Dict[int, Union[object, List[object]]]:
    """
    Converts a list of objects into a dictionary where the keys are
    hash values of objects.

    Args:
        objects (List): A list of objects to hash.

    Returns:
        Dict[int, Union[object, List[object]]]: A dictionary with hash values
        as keys and objects or lists of objects as values.
    """
    try:
        hashed_objects = defaultdict(list)

        for obj in objects:
            # Add objects to dictionary using their hash values as keys
            hashed_objects[hash(obj)].append(obj)

        # Convert single-element lists back to the object itself
        for key, value in hashed_objects.items():
            if len(value) == 1:
                hashed_objects[key] = value[0]

        return dict(hashed_objects)
    except TypeError as e:
        raise ValueError("Unhashable object found") from e


data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))
