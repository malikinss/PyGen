'''
TODO:
    Implement a pluck() function that takes three arguments in the following
    order:
        - data — a dictionary of arbitrary nesting
        - path — a string representing a key or a sequence of keys listed with
                 a dot .
        - default — an arbitrary object, the default value; has the value None
                    if not passed explicitly

    The function must return the value for the key path from the dictionary
    data.

    If path is a sequence of keys, for example, key1.key2, then the return
    value of the function must be the value for key2 from
    the dictionary data[key1].

    If the specified key or at least one key from the sequence of keys is not
    in the dictionary, the function must return the value default.
'''
from typing import Any


def pluck(data: dict, path: str, default: Any = None) -> Any:
    """
    Retrieves the value from a nested dictionary based on the specified path.

    The path is a sequence of keys separated by dots. If any key is missing in
    the dictionary, the function returns the specified default value.

    Args:
        data (dict): The dictionary to extract values from.
        path (str): A dot-separated string representing the key path.
        default (Any, optional): The default value to return if the key path
        doesn't exist. Defaults to None.

    Returns:
        Any: The value found at the specified path, or the default value if
        not found.
    """
    keys = path.split('.')

    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default

    return data
