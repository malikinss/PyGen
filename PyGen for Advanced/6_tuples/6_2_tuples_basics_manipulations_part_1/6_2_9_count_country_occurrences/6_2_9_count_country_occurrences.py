'''
TODO:
    Complete the code below so that the variable number contains
    the number of occurrences of 'Spain' in the tuple countries.
'''
from typing import Tuple


def count_country_occurrences(countries: Tuple[str, ...], country: str) -> int:
    """
    Returns the number of occurrences of a specific country in the
    countries tuple.

    Args:
    countries (Tuple[str, ...]): A tuple containing country names as strings.
    country (str): The country to count in the tuple.

    Returns:
    int: The number of occurrences of the specified country.
    """
    return countries.count(country)


# Tuple containing country names
countries: Tuple[str, ...] = (
    'Russia', 'Argentina',
    'Spain', 'Slovakia',
    'Canada', 'Slovenia',
    'Italy', 'Spain',
    'Ukraine', 'Chile',
    'Spain', 'Cameroon'
)

# Count the number of occurrences of 'Spain'
number = count_country_occurrences(countries, 'Spain')

# Print the result
print(number)
