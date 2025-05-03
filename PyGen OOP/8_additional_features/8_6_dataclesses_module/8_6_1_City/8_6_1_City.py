'''
TODO:
    You have access to the City class, which describes a city.

    When creating an instance, the class takes three arguments in
    the following order:
        name — the name of the city (type str)
        population — the population of the city (type int)
        founded — the year the city was founded (type int)

    An instance of the City class has three attributes:
        name — the name of the city
        population — the population of the city
        founded — the year the city was founded

    Also, an instance of the City class has the following formal string
    representation:
        City(
            name='<name of the city>',
            population=<population of the city>,
            founded=<year of the city's foundation>
        )

    Finally, instances of the City class support the comparison operation with
    each other using the == and != operators.

    Two cities are considered equal if their names, populations, and years of
    foundation are the same.

    Implement the City class as a data class.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of the City class;
    it can be arbitrary.
'''
from dataclasses import dataclass


@dataclass
class City:
    """
    A data class representing a city with name, population, and founding year.
    """
    name: str
    population: int
    founded: int
