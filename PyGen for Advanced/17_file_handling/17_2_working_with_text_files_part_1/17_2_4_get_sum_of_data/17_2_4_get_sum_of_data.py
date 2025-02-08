'''
TODO:
    You have access to a text file numbers.txt consisting of two lines,
    each of which contains an integer.

    Write a program that displays the sum of these numbers.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''


def get_data_from_file(file_name):
    """
    Reads the content of the file and returns the lines as a list of integers.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - list: List of integers from the file.
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        # Convert each line to an integer and return the list
        return [int(line.strip()) for line in file.readlines()]


def get_sum_of_data(data):
    """
    Returns the sum of the given list of integers.

    Parameters:
    - data (list): A list of integers.

    Returns:
    - int: The sum of the integers.
    """
    return sum(data)


# Read the file and get the integers
data = get_data_from_file('numbers.txt')

# Print the sum of the numbers
print(get_sum_of_data(data))
