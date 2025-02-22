'''
TODO:
    Consider the following dictionary:
        {'a': [1, 2], 'b': [3, 1], 'c': [2]}

    Let's "flip" it, representing keys as values, and values as keys:
        {1: ['a', 'b'], 2: ['a', 'c'], 3: ['b']}

    Implement a flip_dict() function that takes one argument:
        dict_of_lists is a dictionary where the key is a number or string,
        and the value is a list of numbers or strings

    The function should return a new dictionary (of type defaultdict with
    type list as the default value), which is a "reversed" dictionary
    dict_of_lists.

NOTE:
    The keys in the dictionary returned by the function, as well as the
    elements in the lists, must be in their original order.
'''
from collections import defaultdict
from typing import Dict, List, DefaultDict, Hashable


def flip_dict(
    dict_of_lists: Dict[Hashable, List[Hashable]]
) -> DefaultDict[Hashable, List[Hashable]]:
    """
    Flips the dictionary by inverting keys and values.

    Args:
        dict_of_lists (Dict[Hashable, List[Hashable]]): A dictionary where
        keys are hashable elements (strings or numbers) and values are lists
        of hashable elements.

    Returns:
        DefaultDict[Hashable, List[Hashable]]: A new dictionary with inverted
        keys and values.
    """
    result_dict = defaultdict(list)

    for key, values in dict_of_lists.items():
        for value in values:
            result_dict[value].append(key)

    return result_dict


if __name__ == '__main__':
    original_dict: Dict = {'a': [1, 2], 'b': [3, 1], 'c': [2]}
    flipped_dict = flip_dict(original_dict)
    print(dict(flipped_dict))
