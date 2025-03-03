'''
TODO:
    Implement a function sort_priority() that takes two arguments in the
    following order:
        values - a list of numbers
        group - a list, tuple, or set of numbers

    The function should sort the list of numbers values in non-decreasing
    order, with the group of numbers in group being the first to
    come first.
'''
from typing import List, Iterable


def sort_priority(values: List[int], group: Iterable[int]) -> None:
    """
    Sorts the list of values, placing elements from the group at the beginning.

    Args:
        values (List[int]): The list of numbers to be sorted.
        group (Iterable[int]): The group of numbers to prioritize
        in the sorting.

    Returns:
        None: The function sorts the `values` list in place.
    """
    # Validate inputs
    if not isinstance(values, list):
        raise ValueError("`values` should be a list.")
    if not isinstance(group, (set, list, tuple)):
        raise ValueError("`group` should be a set, list, or tuple.")

    group_set = set(group)  # Convert group to set for faster lookup

    def priority_sort_key(value: int) -> tuple:
        """
        Key function for sorting. Elements in group come first.

        Args:
            value (int): The number to be sorted.

        Returns:
            tuple: A tuple where the first element is 0 if the value is
            in the group, otherwise 1. The second element is the value itself.
        """
        # Check if the value is in the group, and assign priority accordingly
        return (0, value) if value in group_set else (1, value)

    values.sort(key=priority_sort_key)
