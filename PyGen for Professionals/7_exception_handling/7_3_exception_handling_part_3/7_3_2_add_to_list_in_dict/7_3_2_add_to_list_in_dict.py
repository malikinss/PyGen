'''
TODO:
    Implement the add_to_list_in_dict() function using a try-except
    construct that takes three arguments in the following order:
        - data is a dictionary of lists, i.e. a dictionary whose
        value are lists
        - key is a hashable object
        - element is an arbitrary object

    The function should add an element object to the list at the key in
    the data dictionary.

    If the key is not in the data dictionary, the function should add it
    to the dictionary, assign it an empty list as its value, and add the
    element object to the list.

NOTE:
    The function should modify the dictionary passed and return None.

    Elements should be added to the end of the list.

    Submit a program to the testing system that contains only the required
    add_to_list_in_dict() function, but not the code that calls it.
'''
from typing import Any, Dict, Hashable


def add_to_list_in_dict(data: Dict[Hashable, list],
                        key: Hashable,
                        element: Any) -> None:
    """
    Adds an element to the list at the given key in the data dictionary.

    If the key does not exist in the dictionary, it initializes an empty list
    for that key before adding the element to the list.

    Parameters:
        data (Dict[Hashable, list]): The dictionary of lists.
        key (Hashable): The key where the element should be added.
        element (Any): The element to add to the list.

    Returns:
        None
    """
    try:
        _ = data[key]
    except KeyError:
        data.update({key: []})
    finally:
        data[key].append(element)

    return None
