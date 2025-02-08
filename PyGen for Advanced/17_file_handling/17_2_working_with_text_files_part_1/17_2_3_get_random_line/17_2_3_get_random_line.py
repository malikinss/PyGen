'''
TODO:
    You have access to a text file "lines.txt" consisting of several lines.

    Write a program that prints a random line from this file to the screen.

NOTE:
    Assume that the executable program and the specified file are in the
    same folder.

    It is guaranteed that the file contains at least one line.
'''
import random


def get_data_from_file(file_name):
    """
    Reads the content of the file and returns the lines as a list.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - list: List of lines from the file.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]


def get_random_line(data):
    """
    Returns a random line from the provided data list.

    Parameters:
    - data (list): A list of strings (lines of the file).

    Returns:
    - str: A random line from the data.
    """
    return random.choice(data)  # Returns a random line from the list


# Read the file and get the lines
data = get_data_from_file('lines.txt')

# Print a random line
print(get_random_line(data))
