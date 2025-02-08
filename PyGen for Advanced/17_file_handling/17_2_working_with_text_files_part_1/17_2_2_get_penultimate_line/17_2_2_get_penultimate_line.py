'''
TODO:
    The program is given a string with the name of a text file as input.

    Write a program that displays its penultimate line.

NOTE:
    The file is guaranteed to contain at least two lines.
'''


def get_penultimate_line(file_name: str) -> str:
    """
    Reads the penultimate line from a given file.

    Parameters:
    - file_name (str): The name of the file to read from.

    Returns:
    - str: The penultimate line of the file.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()

        # Return the penultimate line, stripped of trailing newline
        return lines[-2].strip()


# Example usage
file_name = input("Enter the file name: ")
print(get_penultimate_line(file_name))
