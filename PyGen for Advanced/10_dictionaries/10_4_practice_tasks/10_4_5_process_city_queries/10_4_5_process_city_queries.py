"""
TODO:
    The program is given a list of countries and cities in each country
    as input.

    Then the names of the cities are given.

    Write a program that for each city outputs what country it is in.
"""
from typing import Dict


def build_cities_dict(num_records: int) -> Dict[str, str]:
    """
    Builds a dictionary mapping cities to their respective countries.

    Args:
        num_records (int): The number of countries and their cities to input.

    Returns:
        Dict[str, str]: A dictionary where each city is a key and its value
                        is the country it belongs to.
    """
    city_to_country = {}

    for _ in range(num_records):
        input_data = input("Enter a country followed by its cities: ").split()
        country = input_data[0]
        cities = input_data[1:]

        for city in cities:
            city_to_country[city] = country  # Map each city to its country

    return city_to_country


def find_country(city_to_country: Dict[str, str], city: str) -> str:
    """
    Finds the country for a given city.

    Args:
        city_to_country (Dict[str, str]): A dictionary mapping cities
                                          to countries.
        city (str): The city to find the country for.

    Returns:
        str: The name of the country the city belongs to.
    """
    return city_to_country[city]


def process_city_queries(
    city_to_country: Dict[str, str], num_queries: int
) -> None:
    """
    Processes city queries and prints the corresponding country for each city.

    Args:
        city_to_country (Dict[str, str]): A dictionary mapping cities
                                          to countries.
        num_queries (int): The number of cities to query.
    """
    for _ in range(num_queries):
        query_city = input("Enter the name of the city: ")
        print(find_country(city_to_country, query_city))


# Main execution
num_records = int(input("Enter the number of countries: "))
city_country_mapping = build_cities_dict(num_records)

num_queries = int(input("Enter the number of cities to query: "))
process_city_queries(city_country_mapping, num_queries)
