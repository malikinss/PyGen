'''
TODO:
    Implement the get_all_values() function that takes two arguments in
    the following order:
        - chainmap is a ChainMap whose elements are dictionaries
        - key is an arbitrary object

    The function must return a set whose elements are all the values for
    the key from all the dictionaries in the chainmap. If the key is not
    in the chainmap, the function must return an empty set.

NOTE:
    The ChainMap passed to the function is guaranteed to contain
    dictionaries with hashable values.
'''
from collections import ChainMap
from typing import Any, Set


def get_all_values(chainmap: ChainMap, key: Any) -> Set[Any]:
    """
    Returns a set of all values associated with the given key from all
    dictionaries in the ChainMap.

    Args:
        chainmap (ChainMap): A ChainMap containing multiple dictionaries.
        key (Any): The key to search for in the dictionaries.

    Returns:
        Set[Any]: A set of values corresponding to the key in the ChainMap.
                  Returns an empty set if the key is not found.
    """
    values = set()
    for element in chainmap.maps:
        if key in element:
            values.add(element[key])
    return values
