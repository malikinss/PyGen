'''
TODO:
    Complete the code below so that the variable new_tuples contains a list
    of tuples based on the list tuples with the last element of each tuple
    replaced with the numeric value 100.
'''
from typing import List, Tuple


def replace_last_element_with_100(
    tuples: List[Tuple[int, ...]]
) -> List[Tuple[int, ...]]:
    """
    Replaces the last element of each tuple in the given list of tuples with
    the number 100.

    Args:
    tuples (List[Tuple[int, ...]]): A list of tuples containing integers.

    Returns:
    List[Tuple[int, ...]]: A list of tuples with the last element replaced
                            by 100.
    """
    new_tuples = []

    for element in tuples:
        # Convert tuple to list to modify it
        element = list(element)   # type: ignore

        # Replace the last element with 100
        element[-1] = 100         # type: ignore
        element = tuple(element)  # Convert back to tuple

        new_tuples.append(element)

    return new_tuples


# Example input
tuples = [
    (10, 20, 40),
    (40, 50, 60),
    (70, 80, 90),
    (10, 90),
    (1, 2, 3, 4),
    (5, 6, 10, 2, 1, 77)
]

# Calling the function and printing the result
print(replace_last_element_with_100(tuples))
