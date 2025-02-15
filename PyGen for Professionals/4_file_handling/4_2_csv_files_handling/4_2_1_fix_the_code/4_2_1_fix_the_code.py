'''
TODO:
    You have access to the csv file grades.csv, which has the following
    contents:
        name;grade
        Timur;100
        Ruslan;97

    Below is a program that should open this file and output the contents of
    each line as a list.

    There is an error in the program, so it outputs:
        ['n']
        ['a']
        ['m']
        ['e']
        ['', '']
        ['g']
        ['r']
        ['a']
        ['d']
        ['e']
        []
        ['T']
        ...

    Find and correct it so that the program outputs the lines:
        ['name', 'grade']
        ['Timur', '100']
        ['Ruslan', '97']
'''
import csv
from typing import List


def read_csv_file(file_path: str) -> List[List[str]]:
    """
    Reads a CSV file with a semicolon delimiter and returns its contents as
    a list of lists.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        List[List[str]]: A list of rows, where each row is a list of strings.

    The CSV file is expected to have a semicolon as the delimiter.
    Empty rows are skipped.
    """
    with open(file_path, encoding='utf-8') as csv_file:
        rows = csv.reader(csv_file, delimiter=';')

        # Return only non-empty rows as a list of lists
        return [row for row in rows if row]


# Example usage
file_path = 'grades.csv'
print(read_csv_file(file_path))
