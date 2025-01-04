'''
TODO:
    Using slices, extend the code below to print all elements of the countries
    tuple except the last two and the first three.
'''
from typing import Tuple


def get_elements_except_first_three_and_last_two(
    tup: Tuple[str, ...]
) -> Tuple[str, ...]:
    """
    Returns all elements of the tuple except the first three and the last two.

    Args:
    tup (Tuple[str, ...]): A tuple of country names (strings).

    Returns:
    Tuple[str, ...]: A tuple containing all elements except the first three
                     and last two.
    """
    return tup[3:-2]


# Tuple containing country names
countries: Tuple[str, ...] = (
    'Russia', 'Argentina',
    'Slovakia', 'Canada',
    'Slovenia', 'Italy',
    'Spain', 'Ukraine',
    'Chile', 'Cameroon'
)

# Get elements excluding the first three and last two
remaining_countries = get_elements_except_first_three_and_last_two(countries)

# Print the result
print(remaining_countries)
