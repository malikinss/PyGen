'''
TODO:
    Complete the above code using the generator to produce a result dictionary
    consisting of all elements of the colors dictionary except those whose
    value is None.

NOTE:
    You do not need to print the contents of the dictionary result.
'''
from typing import Dict, Optional


def filter_colors(colors: Dict[str, Optional[str]]) -> Dict[str, str]:
    """
    This function takes a dictionary of colors with their corresponding names
    and returns a new dictionary consisting of all the key-value pairs where
    the value is not None.

    Args:
        colors (Dict[str, Optional[str]]): A dictionary where keys are color
                                           identifiers and values are color
                                           names (which could be None).

    Returns:
        Dict[str, str]: A dictionary containing only the key-value pairs where
                        the value is not None.
    """
    # Using a dictionary comprehension to filter out entries with value None
    result = {key: value for key, value in colors.items() if value is not None}

    return result


# Sample dictionary of colors
colors = {
    'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green',
    'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None,
    'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold',
    'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige',
    'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl',
    'c21': None, 'c22': 'Sand', 'c23': None
}

# Calling the function and storing the result in 'result'
result = filter_colors(colors)
