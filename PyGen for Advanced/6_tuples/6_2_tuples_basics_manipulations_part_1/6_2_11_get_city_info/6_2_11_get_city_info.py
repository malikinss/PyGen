'''
TODO:
    The city_name variable contains the name of the city (for example, Moscow),
    and the city_year variable contains the year of its foundation
    (for example, 1147).

    Fill in the missing line so that the city variable contains a tuple
    of the values of these two variables (first the name of the city,
    then the year of foundation).
'''
from typing import Tuple


def get_city_info() -> Tuple[str, int]:
    """
    Takes user input for the name of a city and its year of foundation,
    and returns a tuple containing both values.

    Returns:
    Tuple[str, int]: A tuple where the first element is the city name (str),
                     and the second element is the year of foundation (int).
    """
    city_name = input("Enter city name: ")
    city_year = int(input("Enter city foundation year: "))

    city = (city_name, city_year)

    return city


# Get city information and print the resulting tuple
print(get_city_info())
