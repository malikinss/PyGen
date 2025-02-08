'''
TODO:
    The program is supplied with a natural number of n and n lines with file
    names.

    Write a program that creates a file output.txt and outputs the contents of
    all files to it without changing their order.

NOTE:
    Assume that the executable program and the specified file are in the same
    folder.
'''


def read_data_from_file(file_name: str) -> list:
    """
    Reads the content of a file and returns its lines without trailing newline
    characters.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        list: A list of lines from the file.
    """
    with open(file_name, 'rt', encoding='utf-8') as file:
        return [line.rstrip() for line in file.readlines()]


def write_data_to_file(file_name: str, data: list) -> None:
    """
    Writes a list of strings to a file.

    Args:
        file_name (str): The name of the file to write to.
        data (list): The list of strings to write to the file.
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(data)


def get_file_names(files_number: int) -> list:
    """
    Collects file names from the user.

    Args:
        files_number (int): The number of files to process.

    Returns:
        list: A list of file names.
    """
    return [input() for _ in range(files_number)]


def concat_files(files_number: int) -> list:
    """
    Concatenates the contents of multiple files.

    Args:
        files_number (int): The number of files to concatenate.

    Returns:
        list: A list of concatenated lines from all the files.
    """
    file_names = get_file_names(files_number)
    data_to_write = []

    for file_name in file_names:
        file_data = read_data_from_file(file_name)
        # Safely concatenate the data
        if file_data:
            data_to_write.extend(file_data)

    return data_to_write


# Main logic to read the number of files and process the contents
files_count = int(input())  # Get the number of files
result_data = concat_files(files_count)

write_data_to_file('output.txt', result_data)
