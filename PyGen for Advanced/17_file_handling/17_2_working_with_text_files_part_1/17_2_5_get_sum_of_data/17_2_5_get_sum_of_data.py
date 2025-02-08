'''
TODO:
    The text file nums.txt is available to you.

    The file contains two integers; they can be separated by space and
    end-of-line characters.

    Write a program that displays the sum of these numbers.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''


def get_all_data_from_file(file_name):
    """
    Reads the content of the file and splits it into individual numbers.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - list: List of string representations of the numbers.
    """
    with open(file_name, 'r', encoding='utf-8') as given_file:
        # Splits on whitespace, including spaces and newlines
        content = given_file.read().split()

    return content


def get_sum_of_data(data):
    """
    Calculates the sum of the integers from the list.

    Parameters:
    - data (list): List of string representations of numbers.

    Returns:
    - int: The sum of the integers.
    """
    return sum(map(int, data))


# Read the data from the file
data = get_all_data_from_file('nums.txt')

# Print the sum of the numbers
print(get_sum_of_data(data))
