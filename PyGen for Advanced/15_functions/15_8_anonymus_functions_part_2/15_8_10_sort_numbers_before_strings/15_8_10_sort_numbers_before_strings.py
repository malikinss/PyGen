'''
TODO:
    The mixed_list contains integer and string values.

    Write a program to sort it in non-decreasing order of element values,
    with numbers coming before strings.

    Output the elements of the sorted list on one line, separated by a space.

NOTE:
    To solve this problem, use an anonymous function and the optional key
    argument of the sorted() function.
'''
from typing import List, Any


def sort_numbers_before_strings(data: List[Any]) -> List[Any]:
    """
    Sorts a mixed list of numbers and strings, placing numbers first and
    sorting all elements in non-decreasing order.

    Args:
        data (List[Any]): A list containing integers and strings.

    Returns:
        List[Any]: A sorted list with numbers first, followed by strings.
    """
    return sorted(data, key=lambda x: (isinstance(x, str), x))


mixed_list = [
    'beside', 48, 'accelerate', 28, 'beware', 'absorb',
    'besides', 'berry', 15, 65, 'abate', 'thursday',
    76, 70, 94, 35, 36, 'berth',
    41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday',
    87, 'bigot', 41, 'abort', 13, 60,
    'friday', 26, 13, 'accident', 'access', 40,
    26, 20, 75, 13, 40, 67,
    12, 'abuse', 78, 10, 80, 'accessory',
    20, 'bewilder', 'benevolent', 'bet', 64, 38,
    65, 51, 95, 'abduct', 37, 98,
    99, 14, 'abandon', 'accept', 46, 'abide',
    'beyond', 19, 'about', 76, 26, 'abound',
    12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard',
    50, 89, 'tuesday', 66, 'bestow', 'absent',
    76, 46, 'betray', 47, 'able', 11
]

# Sorting and printing the result
print(*sort_numbers_before_strings(mixed_list))
