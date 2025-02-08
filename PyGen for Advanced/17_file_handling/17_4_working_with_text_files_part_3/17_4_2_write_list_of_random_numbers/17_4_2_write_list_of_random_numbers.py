'''
TODO:
    Write a program that writes to a text file "random.txt" 25 random numbers
    in the range from 111 to 777 (inclusive), each with a new line.
NOTE:
    Assume that the executable program and the specified file are in the same
    folder.
'''
from random import sample
from typing import List


def write_data_to_file(file_name: str, data: List[str]) -> None:
    """
    Writes the given data to a file with the specified file name.

    Parameters:
    - file_name (str): The name of the file to write to.
    - data (List[str]): A list of strings to be written to the file.

    Returns:
    - None: This function doesn't return anything; it only writes data to
            a file.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data)


def get_list_of_random_numbers(
    range_start: int, range_end: int, quantity: int
) -> List[int]:
    """
    Generates a list of random numbers within a given range.

    Parameters:
    - range_start (int): The start of the range (inclusive).
    - range_end (int): The end of the range (exclusive).
    - quantity (int): The number of random numbers to generate.

    Returns:
    - List[int]: A list of random integers.
    """
    return sample(range(range_start, range_end + 1), quantity)


def convert_list_to_write_format(data: List[int]) -> List[str]:
    """
    Converts a list of integers into a list of strings, each followed by
    a newline character.

    Parameters:
    - data (List[int]): The list of integers to convert.

    Returns:
    - List[str]: A list of strings, each followed by a newline.
    """
    return [f"{x}\n" for x in data]


random_numbers = get_list_of_random_numbers(111, 777, quantity=25)
data_to_write = convert_list_to_write_format(random_numbers)
write_data_to_file('random.txt', data_to_write)
