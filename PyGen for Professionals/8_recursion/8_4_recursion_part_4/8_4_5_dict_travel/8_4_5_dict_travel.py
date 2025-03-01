'''
TODO:
    Implement a dict_travel() function that takes one argument:
    - nested_dicts - is a dictionary containing numbers, strings,
    or dictionaries as values,
    which in turn also contain numbers, strings, or dictionaries as values;
    nesting can be arbitrary

    The function should print all key-value pairs of the nested_dicts
    dictionary, as well as the values of all its child dictionaries.

    When printing the values of child dictionaries, list the names of all
    keys, starting from the top level, separated by periods.

    For example, in the dictionary:
        {'name': 'Arthur', 'grades': {'math': 4, 'chemistry': 3}}
    the value 4 should be printed in the following format:
        grades.math: 4

    All key-value pairs should be in lexicographic order, each on a
    separate line.

NOTE:
    It is guaranteed that the keys in the dictionary passed to the function
    are strings containing only lowercase Latin letters.

    It is guaranteed that no key in the dictionary passed to the function is a
    sequence of other keys.

    In other words, the dictionary cannot have, for example, the following
    form:
        {'b.c': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
'''
from typing import List, Tuple


def dict_travel(nested_dicts: dict) -> None:
    """
    Traverse and print all key-value pairs from a nested dictionary in
    lexicographical order.

    Args:
        nested_dicts (dict): The nested dictionary containing numbers, strings,
        or other dictionaries as values.

    Returns:
        None: The function prints key-value pairs to the console.
    """

    def traverse_recursive(
        data: dict, current_prefix: str = ''
    ) -> List[Tuple[str, any]]:
        """
        Recursively traverse nested dictionaries and collect key-value pairs.

        Args:
            data (dict): The dictionary to traverse.
            current_prefix (str): The prefix representing the current path
            of keys.

        Returns:
            result (List[Tuple[str, any]]): A list of tuples containing key
            paths and their corresponding values.
        """
        result = []

        for key, value in sorted(data.items()):
            full_key = f"{current_prefix}{key}"

            if isinstance(value, dict):
                result.extend(traverse_recursive(value, f'{full_key}.'))
            else:
                result.append((full_key, value))

        return result

    result = traverse_recursive(nested_dicts)
    print_result(result)


def print_result(result: List[Tuple[str, any]]) -> None:
    """
    Print the result in key-value format.

    Args:
        result (List[Tuple[str, any]]): A list of tuples containing key paths
        and values.

    Returns:
        None: The function prints the result to the console.
    """
    for key, value in result:
        print(f'{key}: {value}')


# Test data
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)
