'''
TODO:
    You have access to the titanic.csv file, which contains information
    about the passengers who were on board the Titanic.

    The first column contains a 1 if the passenger survived, and a 0 otherwise,
    the second column contains the full name of the passenger,
    the third column contains the gender
    the fourth column contains the age:
        survived;name;sex;age
        0;Mr. Owen Harris Braund;male;22
        1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
        ...

    Write a program that prints the names of the surviving passengers who
    were under 18 years old, each on a separate line.

    The names of all male passengers should be listed first, then the
    female ones, and the names in the male and female lists should be
    listed in their original order.
NOTE:
    The separator in the titanic.csv file is a semicolon, and quotation
    marks are not used.
'''
import csv
from typing import List, Dict, Callable

CSV_FILE_PATH = '4_2_9/tests/titanic.csv'


def read_csv(filename: str, delimiter: str = ';') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename (str): The path to the CSV file.
        delimiter (str): The delimiter used in the CSV file.

    Returns:
        List[Dict[str, str]]: The content of the CSV file as a list of
                              dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def is_survived(record: Dict[str, str]) -> bool:
    """
    Checks if a passenger survived.

    Args:
        record (Dict[str, str]): A dictionary representing a passenger record.

    Returns:
        bool: True if the passenger survived, False otherwise.
    """
    return int(record['survived']) == 1


def is_young(record: Dict[str, str]) -> bool:
    """
    Checks if a passenger is under 18 years old.

    Args:
        record (Dict[str, str]): A dictionary representing a passenger record.

    Returns:
        bool: True if the passenger is under 18 years old, False otherwise.
    """
    return float(record['age']) < 18


def is_male(record: Dict[str, str]) -> bool:
    """
    Checks if a passenger is male.

    Args:
        record (Dict[str, str]): A dictionary representing a passenger record.

    Returns:
        bool: True if the passenger is male, False otherwise.
    """
    return record['sex'] == 'male'


def is_female(record: Dict[str, str]) -> bool:
    """
    Checks if a passenger is female.

    Args:
        record (Dict[str, str]): A dictionary representing a passenger record.

    Returns:
        bool: True if the passenger is female, False otherwise.
    """
    return record['sex'] == 'female'


def print_names(passengers: List[Dict[str, str]], column: str) -> None:
    """
    Prints the values of a specific column for each passenger.

    Args:
        passengers (List[Dict[str, str]]): A list of dictionaries representing
                                           passenger records.
        column (str): The name of the column to print.

    Returns:
        None: This function prints the result and returns nothing.
    """
    for passenger in passengers:
        print(passenger[column])


def get_specific_sex_survivors_under_18(
    data: List[Dict[str, str]],
    sex_func: Callable[[Dict[str, str]], bool]
) -> filter:
    """
    Filters the data based on survival, age, and sex criteria.

    Args:
        data (List[Dict[str, str]]): A list of dictionaries representing
                                     passenger records.
        sex_func (Callable[[Dict[str, str]], bool]): A function to filter
                                                     passengers by sex.

    Returns:
        filter: A filtered iterator of passenger records satisfying
                the conditions.
    """
    return filter(
        lambda x: is_survived(x) and is_young(x) and sex_func(x), data
    )


# Read data from CSV file
data = read_csv(CSV_FILE_PATH, delimiter=';')

# Get and print male survivors under 18
male_survivors_under_18 = list(
    get_specific_sex_survivors_under_18(data, is_male)
)
print_names(male_survivors_under_18, 'name')

# Get and print female survivors under 18
female_survivors_under_18 = list(
    get_specific_sex_survivors_under_18(data, is_female)
)
print_names(female_survivors_under_18, 'name')
