'''
TODO:
    A text file is available to you "lines.txt" , which contains lines of text.

    Write a program that outputs all the longest strings from a file without
    changing their order.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
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


def get_longest_lines(data: list[str]) -> list[str]:
    """
    Filters out the longest strings from a list of lines.

    Parameters:
    - data (list[str]): The list of lines to be checked.

    Returns:
    - list[str]: A list of the longest strings.
    """
    max_len = len(max(data, key=len))  # Find the maximum length of the lines
    return [line for line in data if len(line) == max_len]


# Read data from file
data = get_data_from_file('lines.txt')

# Output longest lines without changing their order
print(*get_longest_lines(data), sep='\n')
