'''
TODO:
    Linearization is the process of transforming a list, which may contain
    several levels of nested lists, into a list containing all the same
    elements without any nesting.

    For example, the list:
        [1, [2, 3], [4, [5, 6, [7, 8, 9]]]
    after linearization will look like:
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Implement linear() using recursion that takes one argument:
        - nested_lists is a list whose elements are integers or lists whose
        elements are either integers or lists; nesting may be arbitrary

    The function should return a new list that is the linearized
    list nested_lists.
'''
from typing import List, Union


def linear(nested_lists: Union[int, List[Union[int, List]]]) -> List[int]:
    """
    Recursively linearize a nested list of integers.

    Args:
        nested_lists (Union[int, List[Union[int, List]]]): A list or an
        integer, where the list may contain other nested lists or integers.

    Returns:
        List[int]: A new list that is the linearized version of the input.
    """
    # Base case: If the element is an integer, return it inside a list
    if isinstance(nested_lists, int):
        return [nested_lists]

    # Recursive case: If the element is a list,
    # recursively linearize each element
    result = []
    for element in nested_lists:
        result.extend(linear(element))  # Flatten the current element

    return result


# Example usage:
my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))  # Output: [3, 4, 5, 6, 7, 8]
