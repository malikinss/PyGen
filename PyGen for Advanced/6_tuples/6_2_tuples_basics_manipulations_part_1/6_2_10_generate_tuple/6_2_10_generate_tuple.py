'''
TODO:
    Using the concatenation (+) and tuple multiplication (*) operators,
    complete the code below so that it prints a tuple:
        (
            1, 2, 3,
            1, 2, 3,
            6, 6, 6,
            6, 6, 6,
            6, 6, 6,
            6, 7, 8,
            9, 10, 11,
            12, 13
        )
'''
from typing import Tuple


def generate_tuple() -> Tuple[int, ...]:
    """
    Generates and returns a tuple based on the specific concatenation
    and multiplication rules.

    The tuple is created by concatenating and multiplying predefined
    tuples according to the given instructions:
        - (1, 2, 3) * 2
        - (6,) * 6
        - (7, 8)
        - (9, 10, 11)
        - (12, 13)

    Returns:
    Tuple[int, ...]: The resulting tuple after concatenation
                     and multiplication.
    """
    numbers1 = (1, 2, 3)
    numbers2 = (6,)
    numbers3 = (7, 8, 9, 10, 11, 12, 13)

    # Concatenating and multiplying the tuples
    result = numbers1 * 2 + numbers2 * 6 + numbers3

    return result


# Generate and print the resulting tuple
print(generate_tuple())
