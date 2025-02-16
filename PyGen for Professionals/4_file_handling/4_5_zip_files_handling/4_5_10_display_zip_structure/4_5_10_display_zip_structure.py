'''
TODO:
    You have access to the desktop.zip archive, which contains various
    folders and files.

    Write a program that outputs its file structure and the size
    of each file.

    The program should output the file structure of the desktop.zip
    archive and the size of each file in uncompressed form.

    Since the archive has its own folder hierarchy, each nesting level
    should be separated by two spaces.

NOTE:
    The file size is written in the largest units of measurement, rounded
    to whole numbers.

    The values of the units of measurement are the same as those
    accepted in computer science:
        1 KB = 1024 B
        1 MB = 1024 KB
        1 GB = 1024 MB
'''
from zipfile import ZipFile
import os


def get_indent(nesting_level: int) -> str:
    """
    Get the indent string based on the nesting level.

    Args:
        nesting_level (int): The level of nesting.

    Returns:
        str: The indent string.
    """
    return ' ' * 2 * nesting_level


def convert_size(num_bytes: int | float) -> str:
    """
    Convert the number of bytes to a human-readable format.

    Args:
        num_bytes (int): The size in bytes.

    Returns:
        str: The size in the largest appropriate units.
    """
    units = ["B", "KB", "MB", "GB"]
    i = 0

    while num_bytes >= 1024 and i < len(units) - 1:
        num_bytes /= 1024.0
        i += 1

    return f"{round(num_bytes)} {units[i]}"


def format_record_with_indent(name: str) -> str:
    """
    Format the record with the appropriate indentation.

    Args:
        name (str): The name of the file or folder.

    Returns:
        str: The formatted record with indentation.
    """
    nesting_level = name.count('/')
    indent = get_indent(nesting_level)
    name_component = name.split('/')[-1]  # Extract the last part of the path
    return f'{indent}{name_component}'


def display_zip_structure(file_path: str) -> None:
    """
    Display the structure of the zip file and the size of each file.

    Args:
        file_path (str): The path to the zip archive.
    """
    with ZipFile(file_path) as zip_file:
        files_info = zip_file.infolist()

        for file in files_info:
            name = file.filename
            is_folder = file.is_dir()
            record = format_record_with_indent(name)

            if is_folder:
                print(record)
            else:
                size = convert_size(file.file_size)
                print(f'{record} {size}')


# Path to the ZIP file
directory = './tests'
zip_file_name = 'test.zip'
zip_file_path = os.path.join(directory, zip_file_name)

# Display the structure
display_zip_structure(zip_file_path)
