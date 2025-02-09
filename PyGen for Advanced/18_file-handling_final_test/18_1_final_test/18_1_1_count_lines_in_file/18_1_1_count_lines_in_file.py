'''
TODO:
    The program is given a line of text with the name of the text file
    as input.

    Write a program to display the number of lines of this file.

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.
'''


def count_lines_in_file(file_name: str) -> int:
    """
    Counts the number of lines in the given file.

    Args:
        file_name (str): The name of the file.

    Returns:
        int: The number of lines in the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        return sum(1 for line in given_file)


# Get the file name from input and count the lines
file_name = input()
print(count_lines_in_file(file_name))
