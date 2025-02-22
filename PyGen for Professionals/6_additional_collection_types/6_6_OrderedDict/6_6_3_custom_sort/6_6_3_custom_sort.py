'''
TODO:
    Implement a custom_sort() function that takes two arguments in the
    following order:
        ordered_dict — an OrderedDict dictionary
        by_values ​​— a boolean value, defaults to False

    The function should sort the ordered_dict dictionary:
        by keys if by_values is False
        by values if by_values is True

NOTE:
    The function should modify the dictionary passed in, not return a new
    one.

    The return value of the function should be None.

    The dictionary passed in to the function is guaranteed to be sortable,
    i.e. it does not contain keys of different types, nor values
    of different types.

    If two elements have equal values, then their original order should
    be preserved.
'''
from collections import OrderedDict


def custom_sort(
    ordered_dict: OrderedDict[str, int], by_values: bool = False
) -> None:
    """
    Sorts an OrderedDict in place.

    Args:
        ordered_dict (OrderedDict[str, int]): The OrderedDict to sort.
        by_values (bool): If True, sort by values; otherwise, sort by keys.

    Returns:
        None: The dictionary is sorted in place.
    """
    ordered_dict.clear()

    if by_values:
        ordered_dict.update(
            sorted(ordered_dict.items(), key=lambda item: item[1])
        )
    else:
        ordered_dict.update(
            sorted(ordered_dict.items(), key=lambda item: item[0])
        )


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)
print(data)
