'''
TODO:
    Complete the code below so that it prints the sum of the minimum
    and maximum keys in the dictionary my_dict.
'''
from typing import Dict, Any

# Define a type alias for keys
number = int | float


def sum_min_max_keys(given_dict: Dict[number, Any]) -> number:
    """
    Calculate the sum of the minimum and maximum keys in the given dictionary.

    Args:
        given_dict (Dict[number, Any]): A dictionary with numeric keys.

    Returns:
        number: The sum of the smallest and largest keys.
    """
    return min(given_dict) + max(given_dict)


# Example dictionary
my_dict = {
    1.12: 'aa',
    67.9: 45,
    3.11: 'ccc',
    7.9: 'dd',
    9.2: 'ee',
    7.1: 'ff',
    0.12: 'qq',
    1.91: 'aa',
    10.12: [1, 2, 3],
    99.0: {9, 0, 1}
}

# Calculate and display the result
result = sum_min_max_keys(my_dict)
print(result)
