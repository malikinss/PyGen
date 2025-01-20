'''
TODO:
    The list tuples contains tuples of three numbers.

    Complete the above code using the generator to produce a dictionary result
    in which the key is the first element of each tuple and the value is
    a tuple of the remaining two elements.

NOTE:
    You do not need to print the contents of the dictionary result.
'''
from typing import List, Tuple, Dict


def generate_tuple_dict(
    tuples: List[Tuple[int, int, int]]
) -> Dict[int, Tuple[int, int]]:
    """
    This function generates a dictionary from a list of tuples where the first
    element of each tuple is used as the key, and the remaining two elements
    form the value as a tuple.

    Args:
        tuples (List[Tuple[int, int, int]]): A list of tuples, each containing
                                             three integers.

    Returns:
        Dict[int, Tuple[int, int]]: A dictionary where the key is the first
                                    element of the tuple, and the value is
                                    a tuple of the remaining two elements.
    """
    # Using a dictionary comprehension to generate the result dictionary
    return {element[0]: element[1:] for element in tuples}


# List of tuples containing three numbers
tuples = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),
    (10, 11, 12), (13, 14, 15), (16, 17, 18),
    (19, 20, 21), (22, 23, 24), (25, 26, 27),
    (28, 29, 30), (31, 32, 33), (34, 35, 36)
]

# Calling the function to generate the result dictionary
result = generate_tuple_dict(tuples)
