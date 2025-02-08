'''
TODO:
    A text file is available to you "population.txt " with the names of
    countries and their populations separated by the tab character '\t'.

    Write a program that outputs all countries whose names begin with the
    letter 'G', whose population is more than 500,000 people, without changing
    their order.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''


def get_data_from_file(file_name: str) -> list[str]:
    """
    Reads all lines from the given file and returns them as a list of strings.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - list[str]: A list of strings, each representing a line from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as file:
        return [line.rstrip() for line in file]


def get_correct_data(data: list[str]) -> list[list[str]]:
    """
    Splits each line into two elements, where the first element is the country
    name and the second element is the population, and returns the resulting
    list of lists.

    Parameters:
    - data (list[str]): The data to split by tab characters.

    Returns:
    - list[list[str]]: A list of lists, each containing country name and
                       population.
    """
    return [line.split('\t') for line in data]


def filter_countries(data: list[list[str]]) -> list[str]:
    """
    Filters countries whose names start with 'G' and population is greater
    than 500,000.

    Parameters:
    - data (list[list[str]]): A list of countries and their populations.

    Returns:
    - list[str]: A list of country names that meet the criteria.
    """
    return [
        country for country, population in data
        if country.startswith('G') and int(population) > 500_000
    ]


# Main execution
data = get_data_from_file('population.txt')
correct_data = get_correct_data(data)
filtered_countries = filter_countries(correct_data)

print(*filtered_countries, sep='\n')
