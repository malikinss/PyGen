'''
TODO:
    Complete the code below so that the number variable contains the number
    of elements in the countries tuple.
'''
from typing import Tuple


def count_elements_in_tuple(tup: Tuple[str, ...]) -> int:
    """
    Returns the number of elements in the provided tuple.

    Args:
    tup (Tuple[str, ...]): A tuple containing country names (strings).

    Returns:
    int: The number of elements in the tuple.
    """
    return len(tup)


# Tuple containing country names
countries: Tuple[str, ...] = (
    'Romania', 'Poland', 'Estonia',
    'Bulgaria', 'Slovakia', 'Slovenia',
    'Hungary'
)

# Count the number of elements in the countries tuple
number = count_elements_in_tuple(countries)

# Print the result
print(number)
