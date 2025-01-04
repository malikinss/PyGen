'''
TODO:
    Using tuple indexing, extend the code below so that the last variable
    contains the last element of the countries tuple.
'''
from typing import Tuple


def get_last_country(countries: Tuple[str, ...]) -> str:
    """
    Given a tuple of country names, this function returns the last country
    in the tuple.

    Args:
    countries (Tuple[str, ...]): A tuple containing country names as strings.

    Returns:
    str: The last country in the tuple.
    """
    return countries[-1]


# Tuple containing the names of countries
countries: Tuple[str, ...] = (
    'Russia', 'Argentina', 'Spain',
    'Slovakia', 'Canada', 'Slovenia', 'Italy'
)

# Using the function to get the last country
last_country = get_last_country(countries)

# Print the last country
print(last_country)
