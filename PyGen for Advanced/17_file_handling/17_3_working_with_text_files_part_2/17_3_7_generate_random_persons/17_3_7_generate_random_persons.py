'''
TODO:
    Two text files are available to you "first_names.txt" and "last_names.txt",
    one with names, the other with surnames.

    Write a program that uses the random module to create 3 random pairs of
    first name + last name, and then outputs them, each on a separate line.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''
from random import choice


def get_data_from_file(file_name: str) -> list[str]:
    """
    Reads all lines from a file and returns them as a list of strings.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - list[str]: A list of strings, each representing a line from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as file:
        return [line.rstrip() for line in file]


def generate_random_person(
    first_names: list[str], last_names: list[str]
) -> str:
    """
    Generates a random full name by selecting a random first and last name.

    Parameters:
    - first_names (list[str]): A list of first names.
    - last_names (list[str]): A list of last names.

    Returns:
    - str: A randomly generated full name (first name + last name).
    """
    return f"{choice(first_names)} {choice(last_names)}"


def generate_random_persons(
    first_names: list[str], last_names: list[str], num_persons: int
) -> list[str]:
    """
    Generates a list of random full names.

    Parameters:
    - first_names (list[str]): A list of first names.
    - last_names (list[str]): A list of last names.
    - num_persons (int): The number of random names to generate.

    Returns:
    - list[str]: A list of randomly generated full names.
    """
    res = [
        generate_random_person(
            first_names, last_names
        ) for _ in range(num_persons)
    ]

    return res


# Main execution
first_names = get_data_from_file('first_names.txt')
last_names = get_data_from_file('last_names.txt')

# Generate 3 random full names
random_persons = generate_random_persons(first_names, last_names, 3)

# Output the generated names
print(*random_persons, sep='\n')
