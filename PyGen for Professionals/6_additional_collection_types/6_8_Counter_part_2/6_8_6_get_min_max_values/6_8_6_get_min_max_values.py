'''
TODO:
    You have access to the variable data, which contains the Counter
    dictionary.

    Complete the code below to add two attributes to this dictionary:
        - min_values() is a function that returns a list of elements with
        the smallest value
        - max_values() is a function that returns a list of elements with
        the largest value

    Both functions must not take any arguments.

NOTE:
    We will consider a tuple (key, value) as a dictionary element.

    The dictionary elements in the lists returned by the functions must be
    in their original order.

    The functions data.min_values() and data.max_values() must take into
    account the contents of the dictionary.

    For example, if a new key-value pair is added to the data dictionary,
    then the key and value must also be present in the lists returned by
    the functions.

    The program must not output anything.
'''
from collections import Counter
from typing import Dict, List, Tuple


def filter_items_by_specific_value(
    given_dict: Dict[str, int],
    given_value: int
) -> List[Tuple[str, int]]:
    """
    Filters a dictionary to return items (key, value) that have a specific
    value.

    Args:
        given_dict (Dict[str, int]): The dictionary to filter.
        given_value (int): The value to filter by.

    Returns:
        List[Tuple[str, int]]: A list of (key, value) tuples where the value
        matches the specified value.
    """
    return [item for item in given_dict.items() if item[1] == given_value]


def get_max_values(self: Counter) -> List[Tuple[str, int]]:
    """
    Returns a list of elements (key, value) with the largest value in
    the Counter.

    This function finds the maximum value in the Counter and returns
    all (key, value) pairs that have this maximum value.

    The returned list preserves the original order.

    Returns:
        List[Tuple[str, int]]: A list of (key, value) tuples with the largest
                               value.
    """
    return filter_items_by_specific_value(self, max(self.values()))


def get_min_values(self: Counter) -> List[Tuple[str, int]]:
    """
    Returns a list of elements (key, value) with the smallest value in
    the Counter.

    This function finds the minimum value in the Counter and returns
    all (key, value) pairs that have this minimum value.

    The returned list preserves the original order.

    Returns:
        List[Tuple[str, int]]: A list of (key, value) tuples with the smallest
                               value.
    """
    return filter_items_by_specific_value(self, min(self.values()))


# Sample data for testing
data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjsk'
               'anvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

# Add the methods to the Counter class
Counter.max_values = get_max_values  # type: ignore
Counter.min_values = get_min_values  # type: ignore
