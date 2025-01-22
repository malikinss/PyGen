'''
TODO:
    Write a function merge() that merges dictionaries into a single dictionary.

    The function should take a list of dictionaries and return a dictionary,
    each key of which contains a set of unique values collected from all the
    dictionaries in the passed list.

NOTE:
    The following code:
        result = merge(
            [
                {'a': 1, 'b': 2}, {'b': 10, 'c': 100},
                {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}
            ]
        )
    creates a dictionary:
        result = {'a': {1, 5}, 'b': {2, 10, 17}, 'c': {50, 100}, 'd': {777}}

    You don't need to call merge(), you just need to implement it.

    Merge of empty dictionaries must be an empty dictionary.
'''


def merge(values: list[dict]) -> dict:
    """
    Merges a list of dictionaries into a single dictionary with unique values.

    Args:
        values (list[dict]): A list of dictionaries to merge.

    Returns:
        dict: A merged dictionary where each key has a set of unique values
              collected from all dictionaries in the list.
    """
    result: dict = {}

    for current_dict in values:
        for key, value in current_dict.items():
            result.setdefault(key, set()).add(value)

    return result
