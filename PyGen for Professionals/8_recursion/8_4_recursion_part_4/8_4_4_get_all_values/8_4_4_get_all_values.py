'''
TODO:
    Implement a get_all_values() function that takes two arguments in the
    following order:
        - nested_dicts is a dictionary containing arbitrary objects or
        dictionaries as values, which in turn also contain arbitrary objects
        or dictionaries as values; nesting can be arbitrary
        - key is a hashable object

    The function should determine all values that correspond to the key key in
    the nested_dicts dictionary and all its nested dictionaries, and return
    them as a set.

    If the key is not in any dictionary, the function should return an
    empty set.
NOTE:
    It is guaranteed that all the searched values are hashable objects, i.e.
    they can be elements of the set.
'''
from typing import Dict, Hashable, Any, Set


def get_all_values(nested_dicts: Dict[str, Any],
                   key: Hashable) -> Set[Any]:
    """
    Retrieve all values associated with the given key from a nested dictionary.

    Args:
        nested_dicts (Dict[str, Any]): A dictionary that may contain other
        dictionaries.
        key (Hashable): The key to search for in the nested dictionaries.

    Returns:
        values (Set[Any]): A set of values associated with the given key.
    """
    values = set()

    # Check if the key exists at the current level and add it to the set
    if key in nested_dicts:
        values.add(nested_dicts[key])

    # Recursively search for the key in nested dictionaries
    for value in nested_dicts.values():
        if isinstance(value, dict):
            values.update(get_all_values(value, key))

    return values


my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'},
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))
