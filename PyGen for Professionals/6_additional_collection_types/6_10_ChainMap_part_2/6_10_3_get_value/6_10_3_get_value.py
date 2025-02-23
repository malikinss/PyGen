'''
TODO:
        Implement a get_value() function that takes three arguments in the
        following order:
            chainmap is a ChainMap object whose elements are dictionaries
            key is an arbitrary object
            from_left is a Boolean value, which defaults to True

        The function should return the value for the key from the chainmap,
        where:
            - If from_left is True, the key in the chainmap should be searched
            from the first dictionary to the last
            - If from_left is False, the key in the chainmap should be searched
            from the last dictionary to the first
            - If the key is not present in the chainmap, the function should
            return None.
'''
from collections import ChainMap
from typing import Any, Hashable


def get_value(chainmap: ChainMap,
              key: Hashable,
              from_left: bool = True) -> Any:
    """
    Retrieve the value for a key from a ChainMap object.

    Args:
        chainmap (ChainMap): The ChainMap object whose elements are
        dictionaries.
        key (Hashable): The key to look up in the ChainMap.
        from_left (bool):
            If True, search from the first dictionary to the last.
            If False, search from the last dictionary to the first.

    Returns:
        Any: The value associated with the key if found; otherwise, None.
    """
    result = None

    if key in chainmap:
        if not from_left:
            chainmap.maps.reverse()

        result = chainmap.get(key)

    return result
