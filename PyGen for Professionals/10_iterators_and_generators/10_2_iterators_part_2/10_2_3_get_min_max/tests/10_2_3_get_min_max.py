'''
TODO:
    Implement a get_min_max() function that takes one argument:
        data — a list of arbitrary objects that are comparable to each other

    The function should return a tuple in which:
        - the first element is the index of the minimum element in
        the data list
        - the second is the index of the maximum element in the data list.

    If the data list is empty, the function should return None.

NOTE:
    If there are multiple minimum/maximum elements, the indices of the first
    element in order should be returned.
'''
from typing import List, Tuple, Optional, Any


def get_min_max(data: List[Any]) -> Optional[Tuple[int, int]]:
    """
    Returns the indices of the minimum and maximum elements in the list.

    Args:
        data (List[Any]): A list of arbitrary objects that are comparable to
        each other.

    Returns:
        Optional[Tuple[int, int]]: A tuple containing the index of the minimum
        element and the index of the maximum element.
        If the list is empty, returns None.
    """
    if not data:
        return None

    # Initialize min and max values and their indices
    min_index = 0
    max_index = 0

    # Iterate through the list to find min and max indices
    for i, item in enumerate(data):
        if item < data[min_index]:
            min_index = i

        if item > data[max_index]:
            max_index = i

    return (min_index, max_index)
