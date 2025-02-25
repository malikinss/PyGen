'''
TODO:
    Write a program using the try-except construct that takes the name of a
    text file as input and outputs its contents.

    If there is no file with this name in the program folder, the program
    should output the text:
        File not found

    The program receives the name of a text file as input.

    The program should output the contents of the file with the entered name
    or the corresponding text if there is no file with this name in the
    program folder.

NOTE:
    The name of the file being submitted already contains an extension.

    When opening a file, use an explicit UTF-8 encoding.
'''


def read_file(filename: str) -> None:
    """
    Reads and prints the contents of the specified file. If the file is
    not found, prints an error message.

    Args:
        filename (str): The name of the text file to read, including
        its extension.

    Returns:
        None: If the file exists, its content is printed. If the file is
        not found, an error message is printed.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file_handle:
            print(file_handle.read())
    except FileNotFoundError:
        print('File not found')


read_file(input())
