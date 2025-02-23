'''
TODO:
    Implement a deep_update() function that takes three arguments in the
    following order:
        chainmap — a ChainMap whose elements are dictionaries
        key — a hashable object
        value — an arbitrary object

    The function should update all values by key in all dictionaries in
    the chainmap to value.

    If key is not present in the chainmap, the function should add
    the key: value pair to the first dictionary.

NOTE:
    The function should update the ChainMap passed to it and return None.

    It is guaranteed that the ChainMap passed to the function contains at
    least one dictionary.
'''
from collections import ChainMap
from typing import Any, Hashable


def deep_update(chain_map: ChainMap, key: Hashable, value: Any) -> None:
    """
    Updates all occurrences of the given key in the dictionaries within the
    ChainMap to the specified value. If the key is not present, adds the
    key-value pair to the first dictionary in the ChainMap.

    Parameters:
        chain_map (ChainMap): A ChainMap containing dictionaries.
        key (Hashable): The key to update.
        value (Any): The value to set for the given key.
    """
    # Iterate over each dictionary in the ChainMap
    for element in chain_map.maps:
        if key in element:
            element[key] = value  # Update the value of the key
            break
    else:
        # If the key is not found, add it to the first dictionary
        chain_map.maps[0][key] = value
