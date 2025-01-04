'''
TODO:
    Using slices, complete the code below so that it prints all elements
    of the countries tuple except the last three.
'''
from typing import Tuple


def get_elements_except_last_three(tup: Tuple[str, ...]) -> Tuple[str, ...]:
    """
    Returns all elements of the tuple except the last three.

    Args:
    tup (Tuple[str, ...]): A tuple of country names (strings).

    Returns:
    Tuple[str, ...]: A tuple containing all elements of the input tuple except
                     the last three.
    """
    return tup[:-3]


# Tuple containing country names
countries: Tuple[str, ...] = (
    'Russia', 'Argentina',
    'Slovakia', 'Canada',
    'Slovenia', 'Italy',
    'Spain', 'Ukraine',
    'Chile', 'Cameroon'
)

# Get all countries except the last three
remaining_countries = get_elements_except_last_three(countries)

# Print the result
print(remaining_countries)
