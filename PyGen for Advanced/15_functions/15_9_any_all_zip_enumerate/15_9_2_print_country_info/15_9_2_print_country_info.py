'''
TODO:
    Using parallel iteration over three lists countries, capitals and
    population, output country information in the format:
        <capital> is the capital of <country>, population equal <population>
        people.

        Moscow is the capital of Russia, population equal 145934462 people.
        Washington is the capital of USA, population equal 331002651 people.
        ...

    Output information for each country on a separate line.
'''
from typing import List


def print_country_info(
    countries: List[str], capitals: List[str], populations: List[int]
) -> None:
    """
    Prints information about countries, including their capitals and
    population.

    Args:
        countries (List[str]): List of country names.
        capitals (List[str]): List of capital cities corresponding to
                              the countries.
        populations (List[int]): List of populations corresponding to
                                 the countries.

    Returns:
        None
    """
    cap_of = 'is the capital of'
    pop_eq = 'population equal'
    ppl = 'people.'

    for country, capital, population in zip(countries, capitals, populations):
        info = f"{capital} {cap_of} {country}, {pop_eq} {population} {ppl}"
        print(info)


# Example data
countries = [
    'Russia', 'USA', 'UK', 'Germany', 'France', 'India'
]
capitals = [
    'Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi'
]
populations = [
    145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385
]

# Call the function
print_country_info(countries, capitals, populations)
