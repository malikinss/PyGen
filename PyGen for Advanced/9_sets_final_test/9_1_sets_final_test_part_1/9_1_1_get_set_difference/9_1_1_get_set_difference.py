'''
TODO:
    Fill the set1 with contents so that the program prints {'p'}.
'''
from typing import Set


def get_set_difference(set1: Set, set2: Set) -> Set:
    """
    Returns the difference between two sets, i.e., the elements that are
    in set1 but not in set2.

    Args:
        set1 (Set): The first set from which the difference will be calculated.
        set2 (Set): The second set that will be subtracted from set1.

    Returns:
        Set: The set of elements that are in set1 but not in set2.
    """
    return set1 - set2


# original sets
set1 = {'p', 'a'}
set2 = {'a', 't', 'f'}

# Get and print the difference between set1 and set2
print(get_set_difference(set1, set2))
