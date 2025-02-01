'''
TODO:
    Write a program that uses the built-in functions filter(), map(), sorted(),
    and reduce() to output an alphabetical list of primary cities with
    a population greater than 10,000,000, in the format:
        Cities: Beijing, Buenos Aires, ...
'''
from functools import reduce
from typing import List


def is_primary_and_population_over_10m(city_record: List) -> bool:
    """
    Checks if the city record is 'primary' and has a population greater
    than 10 million.

    Args:
        city_record (List): A list containing city name, population, and type.

    Returns:
        bool: True if the city is 'primary' and its population is over
              10 million, False otherwise.
    """
    return city_record[2] == 'primary' and city_record[1] > 10000000


def process_cities(data: List[List]) -> str:
    """
    Filters the cities based on population and type, then outputs
    an alphabetical list of primary cities with a population greater
    than 10,000,000.

    Args:
        data (List[List]): A list of city records containing city name,
                           population, and type.

    Returns:
        str: A formatted string of city names.
    """
    # Filter cities with 'primary' type and population greater than 10,000,000
    primary_cities_more_ten_millions = list(
        filter(
            lambda city: is_primary_and_population_over_10m(city), data
        )
    )

    # Extract the city names and sort them alphabetically
    cities_name = sorted(
        map(lambda city: city[0], primary_cities_more_ten_millions)
    )

    # Reduce the list to a single string of cities separated by commas
    result = reduce(lambda city1, city2: city1 + ', ' + city2, cities_name)

    return result


# Data of cities with their population and type
data = [
    ['Tokyo', 35676000, 'primary'],
    ['New York', 19354922, 'nan'],
    ['Mexico City', 19028000, 'primary'],
    ['Mumbai', 18978000, 'admin'],
    ['Sao Paulo', 18845000, 'admin'],
    ['Delhi', 15926000, 'admin'],
    ['Shanghai', 14987000, 'admin'],
    ['Kolkata', 14787000, 'admin'],
    ['Los Angeles', 12815475, 'nan'],
    ['Dhaka', 12797394, 'primary'],
    ['Buenos Aires', 12795000, 'primary'],
    ['Karachi', 12130000, 'admin'],
    ['Cairo', 11893000, 'primary'],
    ['Rio de Janeiro', 11748000, 'admin'],
    ['Osaka', 11294000, 'admin'],
    ['Beijing', 11106000, 'primary'],
    ['Manila', 11100000, 'primary'],
    ['Moscow', 10452000, 'primary'],
    ['Istanbul', 10061000, 'admin'],
    ['Paris', 9904000, 'primary']
]

# Get the result
result = process_cities(data)
print(f'Cities: {result}')
