'''
TODO:
    A text file is available to you "nums.txt".

    The file can contain non-negative integers and anything else.

    Let's call a number a sequence of one or more digits in a row (the number
    is always non-negative).

    Write a program that calculates the sum of all the numbers written in
    the file.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''
import re


def get_data_from_file(file_name: str) -> list[str]:
    """
    Reads all lines from a file and returns them as a list of strings.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - list[str]: A list of strings, each representing a line from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        # Read and return all lines
        return given_file.readlines()


def extract_numbers_from_text(data: list[str]) -> list[int]:
    """
    Extracts all the numbers from the text data.

    Parameters:
    - data (list[str]): A list of strings representing the content of the file.

    Returns:
    - list[int]: A list of integers extracted from the text.
    """
    numbers: list = []

    # Iterate over each line and extract numbers using regex
    for row in data:
        # Find all sequences of digits in the row
        numbers.extend(map(int, re.findall(r'\d+', row)))

    return numbers


# Get data from the file
data = get_data_from_file('nums.txt')

# Output the sum of all numbers
print(sum(extract_numbers_from_text(data)))
