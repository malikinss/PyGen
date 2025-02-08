'''
TODO:
    The CSV file data.csv is available to you, containing information in
    csv format.

    Write the read_csv function to read data from this file.

    It should return a list of dictionaries, interpreting the first line as
    the names of the keys, and each subsequent line as the values of these
    keys.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''
from typing import List, Dict


def read_file(file_name: str) -> List[str]:
    """
    Reads the content of the file and returns it as a list of lines.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - List[str]: List of lines from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as file:
        return [line.rstrip() for line in file.readlines()]


def get_keys_from(data: List[str]) -> List[str]:
    """
    Extracts the header (keys) from the first line of the data.

    Parameters:
    - data (List[str]): The list of lines from the CSV file.

    Returns:
    - List[str]: A list of keys.
    """
    return data[0].split(',')


def get_rows_from(data: List[str]) -> List[str]:
    """
    Extracts all rows of data excluding the header.

    Parameters:
    - data (List[str]): The list of lines from the CSV file.

    Returns:
    - List[str]: A list of rows (strings) from the data.
    """
    return data[1:]


def build_csv_dict(keys: List[str], rows: List[str]) -> List[Dict[str, str]]:
    """
    Builds a list of dictionaries from keys and rows.

    Parameters:
    - keys (List[str]): The list of keys (from the header).
    - rows (List[str]): The list of data rows.

    Returns:
    - List[Dict[str, str]]: A list of dictionaries representing the CSV data.
    """
    csv_dict = []
    for row in rows:
        values = row.split(',')
        record = {keys[i]: values[i] for i in range(len(values))}
        csv_dict.append(record)

    return csv_dict


def read_csv(file_name: str) -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns a list of dictionaries where each dictionary
    represents a row with keys from the header and values from the row data.

    Parameters:
    - file_name (str): The name of the CSV file to read.

    Returns:
    - List[Dict[str, str]]: A list of dictionaries where each dictionary
                            represents a row in the CSV file.
    """

    data = read_file(file_name)
    if not data:
        return []

    keys = get_keys_from(data)
    rows = get_rows_from(data)
    csv_dict = build_csv_dict(keys, rows)

    return csv_dict


# Example usage
print(read_csv('data.csv'))
