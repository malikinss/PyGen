'''
TODO:
    Complete the code below to obtain a list containing only non-empty tuples
    in the original list tuples, without changing their order.
'''
from typing import List, Tuple


def filter_non_empty_tuples(tuples: List[Tuple]) -> List[Tuple]:
    """
    Filters out empty tuples from the given list of tuples and returns
    a list containing only non-empty tuples, preserving their order.

    Args:
    tuples (List[Tuple]): A list containing tuples to be filtered.

    Returns:
    List[Tuple]: A list of non-empty tuples.
    """
    non_empty_tuples = [element for element in tuples if element]

    return non_empty_tuples


# Example input
tuples = [
    (), (), ('',),
    ('a', 'b'), (), ('a', 'b', 'c'),
    (1,), (), (),
    ('d',), ('', ''), ()
]

# Calling the function and printing the result
print(filter_non_empty_tuples(tuples))
