'''
TODO:
    Implement a get_value() function that takes two arguments in the following
    order:
        - nested_dicts is a dictionary containing arbitrary objects or
        dictionaries as values, which in turn also contain arbitrary objects
        or dictionaries as values; nesting can be arbitrary
        - key is a hashable object

    The function must determine the value that corresponds to the key key in
    the nested_dicts dictionary or one of its nested dictionaries, and return
    the result.

NOTE:
    It is guaranteed that the key key is present in the nested_dicts
    dictionary or one of its nested dictionaries, and in a single copy.
'''
from typing import Dict, Hashable, Any


def get_value(
    nested_dict: Dict[Hashable, Any], key: Hashable
) -> Any:
    """
    Retrieve the value associated with the given key from a nested dictionary.

    Args:
        nested_dict (dict): A dictionary that may contain other dictionaries.
        key (Hashable): The key to search for in the nested dictionaries.

    Returns:
        Any: The value associated with the given key.
    """
    # Check if the key is directly in the current dictionary
    if key in nested_dict:
        return nested_dict[key]

    # Otherwise, recursively check all values that are dictionaries
    for value in nested_dict.values():
        if isinstance(value, dict):
            found_value = get_value(value, key)

            if found_value is not None:
                return found_value


# Example data
data = {
    'firstName': 'Тимур',
    'lastName': 'Гуев',
    'birthDate': {
        'day': 10,
        'month': 'October',
        'year': 1993
    },
    'address': {
        'streetAddress': 'Часовая 25, кв. 127',
        'city': {
            'region': 'Московская область',
            'type': 'город',
            'cityName': 'Москва'
        },
        'postalCode': '125315'
    }
}

print(get_value(data, 'cityName'))
