'''
TODO:
    Complete the code below so that the index variable contains the index
    of the 'Slovenia' element in the countries tuple.
'''
from typing import Tuple


def find_country_index(countries: Tuple[str, ...], country: str) -> int:
    """
    Returns the index of the specified country in the countries tuple.

    Args:
    countries (Tuple[str, ...]): A tuple containing country names as strings.
    country (str): The country to find in the tuple.

    Returns:
    int: The index of the country in the tuple.
    """
    return countries.index(country)


# Tuple containing country names
countries: Tuple[str, ...] = (
    'Russia', 'Argentina',
    'Spain', 'Slovakia',
    'Canada', 'Slovenia',
    'Italy'
)

# Find the index of 'Slovenia'
index = find_country_index(countries, 'Slovenia')

# Print the result
print(index)
