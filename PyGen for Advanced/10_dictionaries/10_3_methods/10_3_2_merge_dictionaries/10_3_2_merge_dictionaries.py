"""
TODO:
    Complete the code below so that it combines the contents of the two
    dictionaries dict1 and dict2:
        - if the key is in both dictionaries, add it to the resulting
        dictionary with a value equal to the sum of the corresponding values
        from the first and second dictionaries;
        - if the key is in only one of the dictionaries, add it to the
        resulting dictionary with its current value.

    The resulting dictionary must be assigned to the variable result.

NOTE:
    There is no need to print the contents of the result dictionary.
"""
from typing import Dict


def merge_dictionaries(
    dict1: Dict[str, int], dict2: Dict[str, int]
) -> Dict[str, int]:
    """
    Merges two dictionaries based on the following rules:
    - If a key exists in both dictionaries, its value is the sum of the values
      from both dictionaries.
    - If a key exists in only one dictionary, it is added to the result with
      its current value.

    Args:
        dict1 (Dict[str, int]): The first dictionary.
        dict2 (Dict[str, int]): The second dictionary.

    Returns:
        Dict[str, int]: The resulting merged dictionary.
    """
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value

    return result


# Example usage
dict1 = {
    'a': 100, 'z': 333, 'b': 200,
    'c': 300, 'd': 45, 'e': 98,
    't': 76, 'q': 34, 'f': 90, 'm': 230
}
dict2 = {
    'a': 300, 'b': 200, 'd': 400,
    't': 777, 'c': 12, 'p': 123,
    'w': 111, 'z': 666
}

result = merge_dictionaries(dict1, dict2)
