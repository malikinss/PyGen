'''
TODO:
    Timur and Ruslan are playing a game of cities.

    They love this game and know many cities, especially Timur, but by
    the end of the game, due to their age, they forget which cities they
    have already named.

    Write a program that reads information about the game and tells
    the children that another city has been named again.
'''


def check_city_repetition(cities: list, new_city: str) -> str:
    """
    Checks if the new city has already been named in the game.

    Args:
        cities (list): A list of cities that have already been named.
        new_city (str): The name of the new city to check.

    Returns:
        str: "REPEAT" if the city was already named, otherwise "OK".
    """
    if new_city in cities:
        return "REPEAT"
    else:
        return "OK"


# Input the number of cities
cities_number = int(input())

# Input the cities named during the game
cities_set = [input().strip() for _ in range(cities_number)]

# Input the new city to check
new_city = input().strip()

# Check if the new city is a repeat and print the result
print(check_city_repetition(cities_set, new_city))
