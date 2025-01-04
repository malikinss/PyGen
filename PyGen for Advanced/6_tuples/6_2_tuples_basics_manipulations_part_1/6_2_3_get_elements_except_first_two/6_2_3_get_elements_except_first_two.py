'''
TODO:
    Using slices, extend the code below to print the elements of the countries
    tuple except the first two.

NOTE:
    The output should be the string (
        'Slovakia', 'Canada', 'Slovenia', 'Italy',
        'Spain', 'Ukraine', 'Chile', 'Cameroon'
    ).
'''
from typing import Tuple


def get_elements_except_first_two(tup: Tuple[str, ...]) -> Tuple[str, ...]:
    """
    Returns all elements of the tuple except the first two.

    Args:
    tup (Tuple[str, ...]): A tuple of country names (strings).

    Returns:
    Tuple[str, ...]: A tuple containing all elements of the input tuple except
                     the first two.
    """
    return tup[2:]


# Tuple containing country names
countries: Tuple[str, ...] = (
    'Russia', 'Argentina', 'Slovakia',
    'Canada', 'Slovenia', 'Italy',
    'Spain', 'Ukraine', 'Chile', 'Cameroon'
)

# Get all countries except the first two
remaining_countries = get_elements_except_first_two(countries)

# Print the result
print(remaining_countries)
