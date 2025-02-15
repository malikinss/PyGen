'''
TODO:
    When you try to run the program below, an error occurs.

    Find and fix it so that the program creates a file called writing_test.csv
    that has the following contents:
        first_col,second_col
        value1,value2
'''
import csv
from typing import List, Dict


def write_csv_file(
    filename: str,
    fieldnames: List[str],
    data: List[Dict[str, str]]
) -> None:
    """
    Writes data to a CSV file with the given fieldnames.

    Args:
        filename (str): The name of the CSV file to write.
        fieldnames (List[str]): A list of column names for the CSV file.
        data (List[Dict[str, str]]): A list of dictionaries representing rows
                                     of data.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


# Usage
write_csv_file(
    'writing_test.csv',
    ['first_col', 'second_col'],
    [{'first_col': 'value1', 'second_col': 'value2'}]
)
