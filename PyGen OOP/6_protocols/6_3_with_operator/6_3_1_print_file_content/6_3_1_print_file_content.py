'''
TODO:
    Implement the print_file_content() function that takes one argument:
        filename — the name of the text file

    The function should output the contents of the file named filename.

    If there is no file with this name in the program folder, the function
    should output the text:
        File not found

NOTE:
    The file name passed to the function already contains an extension.

    When opening the file, use an explicit UTF-8 encoding.
'''


def print_file_content(filename: str) -> None:
    """
    Print the contents of a text file.

    Args:
        filename: Name of the text file (including extension).

    Prints:
        The contents of the file, or 'File not found' if the file
        does not exist.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print('File not found')
