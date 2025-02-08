'''
TODO:
    A text file is available to you "input.txt" consisting of several lines.

    Write a program to write the contents of this file to a file "output.txt"
    in the form of a numbered list, where each line is preceded by its number,
    character ")" and a space.

    The line numbering should start with "1".

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.
'''
from typing import List


def read_data_from_file(file_name: str) -> List[str]:
    """
    Reads the contents of a text file and returns a list of its lines without
    trailing newlines.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - List[str]: A list of strings representing the file's lines.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return [line.rstrip() for line in file]


def write_data_to_file(file_name: str, data: List[str]) -> None:
    """
    Writes a list of strings to a file.

    Parameters:
    - file_name (str): The name of the file to write to.
    - data (List[str]): A list of strings to be written.

    Returns:
    - None: This function does not return anything.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(f"{line}\n" for line in data)


def enumerate_data_rows(data: List[str]) -> List[str]:
    """
    Adds line numbering to a list of text lines, formatting each line as
    "N) text".

    Parameters:
    - data (List[str]): The list of text lines to enumerate.

    Returns:
    - List[str]: A new list of strings with line numbers.
    """
    return [f"{index}) {line}" for index, line in enumerate(data, start=1)]


data = read_data_from_file('input.txt')
enumerated_data = enumerate_data_rows(data)
write_data_to_file('output.txt', enumerated_data)
