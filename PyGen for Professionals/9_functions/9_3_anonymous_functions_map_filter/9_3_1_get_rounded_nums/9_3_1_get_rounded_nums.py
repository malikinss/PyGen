'''
TODO:
    You have a list data containing arbitrary objects.

    Complete the code below so that it prints all the numbers (int and
    float) in the list, discarding the fractional part of the real numbers.

    The numbers must be in their original order, each on a separate line.

NOTE:
    The initial part of the answer looks like this:
        -16
        -202
        883
        ...

    It is convenient to use the map() and filter() functions in
    the problem.
'''
from typing import List, Union


def filter_numbers(data: List[Union[int, float, object]]) -> filter:
    """
    Filters out integers and floats from a list of arbitrary objects.

    Args:
        data (List): The list containing arbitrary objects.

    Returns:
        filter: A filter object containing only integers and floats.
    """
    return filter(lambda x: isinstance(x, (int, float)), data)


def get_rounded_nums(data: List[Union[int, float, object]]) -> List[int]:
    """
    Rounds down all the integers and floats in the list, converting them to
    integers.

    Args:
        data (List): The list containing arbitrary objects.

    Returns:
        List[int]: A list of integers with the fractional part removed.
    """
    numbers = filter_numbers(data)
    return [int(x) for x in numbers]  # Use list comprehension for simplicity


data = [
    'Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765,
    (3, 4), -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'],
    479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733,
    'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '',
    323.7720806756133, 'beegeek', -224, 431, 170.6353248658936,
    -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863,
    'zero', -113, 288, None, -708.3036176571618
]

print(*get_rounded_nums(data), sep='\n')
