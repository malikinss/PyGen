'''
TODO:
    A text file is available to you data.txt , which contains lines of text.

    Write a program that outputs all the lines of this file in reverse order:
        first the last one, then the penultimate one, etc.

NOTE:
    Assume that the executable program and the specified file are in
    the same folder.
'''


def reverse_lines(lines: list[str]) -> list[str]:
    """
    Reverses the order of the given list of lines.

    Parameters:
    - lines (list[str]): The list of lines to be reversed.

    Returns:
    - list[str]: The list of lines in reverse order.
    """
    return lines[::-1]


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


data = get_data_from_file('data.txt')

# Output lines in reverse order
print(*reverse_lines(data), sep='\n')
