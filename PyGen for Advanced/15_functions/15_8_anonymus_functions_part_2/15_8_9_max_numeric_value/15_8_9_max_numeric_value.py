'''
TODO:
    The mixed_list contains integer and string values.

    Write a program that uses the built-in max() function to find and print
    the largest numeric value in the given list.

NOTE:
    To solve this problem, use an anonymous function and the optional key
    argument of the max() function.

    Note that you cannot compare numbers and strings.
'''
from typing import List, Any


def is_num(data: Any) -> bool:
    """
    Checks if the provided data is an instance of int or float.

    Args:
        data (Any): The data to check.

    Returns:
        bool: True if data is an int or float, False otherwise.
    """
    return isinstance(data, (int, float))


def max_numeric_value(mixed_list: List[Any]) -> int:
    """
    Finds and returns the largest numeric value from a mixed list of numbers
    and strings.

    The function uses an anonymous function (lambda) as the key for max() to
    filter out non-numeric values.

    Args:
        mixed_list (List[Any]): The list containing both numeric (int/float)
                                and string values.

    Returns:
        int: The largest numeric value found in the list.
    """
    return max(mixed_list, key=lambda x: x if is_num(x) else float('-inf'))


mixed_list = [
    'tuesday', 'abroad', 'abuse', 'beside',
    'monday', 'abate', 'accessory', 'absorb',
    1384878, 'sunday', 'about', 454805,
    'saturday', 'abort', 2121919, 2552839,
    977970, 1772933, 1564063, 'abduct',
    901271, 2680434, 'bicycle', 'accelerate',
    1109147, 942908, 'berry', 433507,
    'bias', 'bestow', 1875665, 'besides',
    'bewilder', 1586517, 375290, 1503450,
    2713047, 'abnormal', 2286106, 242192,
    701049, 2866491, 'benevolent', 'bigot',
    'abuse', 'abrupt', 343772, 'able',
    2135748, 690280, 686008, 'beyond',
    2415643, 'aboard', 'bet', 859105,
    'accident', 2223166, 894187, 146564,
    1251748, 2851543, 1619426, 2263113,
    1618068, 'berth', 'abolish', 'beware',
    2618492, 1555062, 'access', 'absent',
    'abundant', 2950603, 'betray', 'beverage',
    'abide', 'abandon', 2284251, 'wednesday',
    2709698, 'thursday', 810387, 'friday',
    2576799, 2213552, 1599022, 'accept',
    'abuse', 'abound', 1352953, 'bid',
    1805326, 1499197, 2241159, 605320, 2347441
]

# Find and print the largest numeric value in mixed_list.
print(max_numeric_value(mixed_list))
