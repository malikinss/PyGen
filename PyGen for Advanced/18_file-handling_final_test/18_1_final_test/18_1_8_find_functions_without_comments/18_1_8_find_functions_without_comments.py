'''
TODO:
    When writing your own functions, it is recommended to describe the purpose
    of the function, its parameters and the return value in the comments.

    Programmers often postpone writing such comments until the last, and then
    completely forget about them.

    The input to the program is a string of text with the name of the text
    file in which the Python code is written.

    Write a program that displays the names of all functions for which there
    is no explanatory comment.

    Let's assume that any line starting with the word def and a space is the
    beginning of the function definition.

    The function contains a comment if the first character of the previous
    line is #.

NOTE:
    Consider that the executable program and the specified files are in the
    same folder.
'''
from typing import List


def read_lines_from_file(file_name: str) -> List[str]:
    """
    Reads the lines of a file and returns them as a list of strings.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A list containing each line of the file as a string.
    """
    with open(file_name, 'rt', encoding='utf-8') as given_file:
        return [line.rstrip() for line in given_file.readlines()]


def get_function_name(line: str) -> str:
    """
    Extracts the function name from a line that defines a function.

    Args:
        line (str): The line containing the function definition.

    Returns:
        str: The function name.
    """
    return line[4:line.index('(')].strip()


def is_def(given_string: str) -> bool:
    """
    Checks if a given line starts with a function definition.

    Args:
        given_string (str): The line to check.

    Returns:
        bool: True if the line starts with 'def ', False otherwise.
    """
    return given_string.strip().startswith('def ')


def functions_without_comments(given_code: List[str]) -> List[str]:
    """
    Identifies functions in the provided code that do not have comments
    before them.

    Args:
        given_code (list): A list of code lines to check.

    Returns:
        list: A list of function names without comments, or an empty list
              if all have comments.
    """
    output_list = []

    for line_number in range(1, len(given_code)):
        line = given_code[line_number]
        prev_line = given_code[line_number - 1]

        # Check if the current line is a function definition without
        # a preceding comment
        if is_def(line) and not prev_line.strip().startswith('# '):
            function_name = get_function_name(line)
            output_list.append(function_name)

    # Handle case where the first line is a function definition without comment
    if is_def(given_code[0]) and (not given_code[0].startswith('# ')):
        function_name = get_function_name(given_code[0])
        output_list.append(function_name)

    return output_list


def find_functions_without_comments(file_name: str) -> str:
    """
    Finds all function names in a Python file that don't have explanatory
    comments directly preceding them. A function has no comment if the line
    before it doesn't start with a '#' character.

    Args:
        file_name (str): The name of the Python file to check.

    Returns:
        str: A string containing either the function names missing comments
             or 'Best Programming Team' if all functions have comments.
    """
    # Read the content of the provided file
    given_code = read_lines_from_file(file_name)

    # Find functions without comments
    output_list = functions_without_comments(given_code)

    # Output the result
    if len(output_list) == 0:
        return 'Best Programming Team'
    else:
        return '\n'.join(output_list)


# Example of calling the function
file_name = input().strip()
result = find_functions_without_comments(file_name)
print(result)
