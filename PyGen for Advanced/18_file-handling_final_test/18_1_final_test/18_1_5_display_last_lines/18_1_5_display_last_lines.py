'''
TODO:
    The program is given a line of text with the name of the text file as
    input.

    Write a program that displays the latest 10 lines of this file.

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.

    If the number of lines in the file is less than 10, it is necessary to
    print the entire contents of the file.
'''


def read_last_lines(file_name: str, num_lines: int = 10):
    """
    Reads the last `num_lines` lines from the specified file.

    Args:
        file_name (str): The name of the file to read.
        num_lines (int): The number of lines to read from the end of the file.

    Returns:
        list: A list of the last `num_lines` lines of the file.
    """
    try:
        with open(file_name, 'rt', encoding='utf-8') as given_file:
            return given_file.readlines()[-num_lines:]
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []


def display_last_lines(file_name: str):
    """
    Displays the last 10 lines of the specified file.

    This function calls `read_last_lines` to get the last lines of the file
    and prints them to the console, one line per line.

    If the file has fewer than 10 lines, it will display all the available
    lines.

    Args:
        file_name (str): The name of the file to read and display.

    Returns:
        None
    """
    last_lines = read_last_lines(file_name)

    if last_lines:
        print(*[line.rstrip() for line in last_lines], sep='\n')


# Input the file name and display the last 10 lines
file_name = input().strip()
display_last_lines(file_name)
