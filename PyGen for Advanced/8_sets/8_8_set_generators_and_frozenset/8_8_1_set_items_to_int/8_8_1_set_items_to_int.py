'''
TODO:
    Using a set generator, complete the code below to produce a set containing
    the unique values of the items list.

    Print the result on one line, in sorted form, separating the elements
    with a single space character.

NOTE:
    Please note that some of the list elements are numbers and some
    are strings, and the strings must be treated as numbers.

    To print the set elements in sorted form, use the following code:
        print(*sorted(myset))
'''
from typing import List, Any, Set


def set_items_to_int(items: List[str | Any]) -> Set:
    """
    Converts the elements in the given list (numbers and strings) to integers,
    ensuring uniqueness by using a set.

    Args:
        items (List[str | Any]): The list of items containing numbers
                                 and string representations of numbers.

    Returns:
        Set: A set of unique integer values derived from the input list.
    """
    return {int(item) for item in items}


def print_sorted_set(values: Set) -> None:
    """
    Prints the elements of the given set in sorted order, separated by spaces.

    Args:
        values (Set): A set of values to be printed in sorted order.
    """
    print(*sorted(values))


items = [
    10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45,
    '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5
]
unique_items = set_items_to_int(items)
print_sorted_set(unique_items)
