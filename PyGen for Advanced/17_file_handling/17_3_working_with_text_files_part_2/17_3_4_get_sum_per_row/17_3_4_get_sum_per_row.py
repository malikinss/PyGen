'''
TODO:
    A text file is available to you "numbers.txt" , each line of which can
    contain one or more integers separated by one or more spaces.

    Write a program that calculates the sum of the numbers in each row and
    displays this amount on the screen (for each row, the sum of the numbers
    in this row is displayed)

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.
'''


def get_data_from_file(file_name: str) -> list[str]:
    """
    Reads all lines from a file and returns them as a list of strings.

    Parameters:
    - file_name (str): The name of the file to read.

    Returns:
    - list[str]: A list of strings, each representing a line from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        # Read all lines and strip trailing newlines
        return [line.rstrip() for line in given_file]


def get_sum_per_row(data: list[str]) -> list[int]:
    """
    Calculates the sum of numbers in each row.

    Parameters:
    - data (list[str]): A list of lines, each containing space-separated
                        numbers.

    Returns:
    - list[int]: A list of sums, one for each row.
    """
    return [sum(map(int, row.split())) for row in data]


# Read data from file
data = get_data_from_file('numbers.txt')

# Output the sums for each row
print(*get_sum_per_row(data), sep='\n')
