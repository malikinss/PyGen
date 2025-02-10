'''
TODO:
    You have access to the text file files.txt, which contains information
    about the files.

    Each line of the file contains three values, separated by a space
    character - the file name, its size (integer) and units of measurement:
        cant-help-myself.mp3 7 MB
        keep-yourself-alive.mp3 6 MB
        bones.mp3 5 MB
        ...

    Write a program that groups these files by extension, determining the
    total size of the files in each group, and displays the resulting groups
    of files, indicating the total size for each.

    Groups must be arranged in lexicographic order of extension names, files
    in groups - in lexicographic order of their names.

NOTE:
    For example, if the files.txt file looked like:

        input.txt 3000 B
        scratch.zip 300 MB
        output.txt 1 KB
        temp.txt 4 KB
        boy.bmp 2000 KB
        mario.bmp 1 MB
        data.zip 900 MB

    then the program should output:

        boy.bmp
        mario.bmp
        ----------
        Summary: 3 MB

        input.txt
        output.txt
        temp.txt
        ----------
        Summary: 8 KB

        data.zip
        scratch.zip
        ----------
        Summary: 1 GB

    where Summary is the total size of the group files.

    It is guaranteed that all file names contain the extension.

    The total size of the group's files is recorded in the largest
    (maximum possible) units of measurement, rounded to the nearest whole unit.

    In other words, you should first determine the total volume of all files
    in a group, say, in bytes, and then convert the resulting value into
    the largest (maximum possible) units of measurement.

    Convertion examples:
        1023 B -> 1023 B
        1300 B -> 1 KB
        1900 B -> 2 KB

    The values of units of measurement are the same as those accepted
    in computer science:
        1 KB = 1024 B
        1 MB = 1024 KB
        1 GB = 1024 MB
'''
from typing import List, Dict, Any

UNIT_CONVERSION = {
    'B': 1,
    'KB': 1024,
    'MB': 1024 * 1024,
    'GB': 1024 * 1024 * 1024
}
UNITS = ['B', 'KB', 'MB', 'GB']


def read_data_from_file(file_name: str) -> List[str]:
    """
    Reads the contents of the specified file and returns a list of lines.

    Args:
        file_name: The name of the file to read.

    Returns:
        A list of strings, each representing a line in the file.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as given_file:
            return [line.rstrip() for line in given_file.readlines()]
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return []


def parse_file_info(record: str) -> Dict[str, Any]:
    """
    Extracts file information (filename, extension, size, and unit) from
    a record string.

    Args:
        record: A string containing file information in the format
                "filename size unit".

    Returns:
        A dictionary containing the extracted file information.
    """
    filename, size_str, unit = record.split()
    filename_value, extension_value = filename.split('.')
    return {
        'filename': filename_value,
        'extension': extension_value,
        'size': int(size_str),
        'unit': unit
    }


def get_list_of_files_info(file_to_open: str) -> List[Dict[str, Any]]:
    """
    Reads a file and returns a list of file information dictionaries.

    Args:
        file_to_open: The name of the file to read.

    Returns:
        A list of dictionaries containing file information.
    """
    return [
        parse_file_info(record) for record in read_data_from_file(file_to_open)
    ]


def unique_values(files: List[Dict[str, Any]], key: str) -> List[str]:
    """
    Returns a sorted list of unique values for a specified key from a list
    of files.

    Args:
        files: A list of dictionaries containing file information.
        key: The key to extract unique values from.

    Returns:
        A sorted list of unique values.
    """
    return sorted({file[key] for file in files})


def filter_files_by_property(
    property_name: str, value: str, files: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Filters files by a specified property-value pair.

    Args:
        property_name: The property to filter by (e.g., 'extension', 'unit').
        value: The value to match for the specified property.
        files: A list of dictionaries containing file information.

    Returns:
        A list of files that match the specified property-value pair.
    """
    return list(filter(lambda file: file[property_name] == value, files))


def get_total_size_for_files_with_property(
    property_name: str, value: str, files: List[Dict[str, Any]]
) -> int:
    """
    Calculates the total size of files with the same property and value.

    Args:
        property_name: The property to filter by (e.g., 'extension', 'unit').
        value: The value to filter by (e.g., 'MP3', 'MB').
        files: A list of dictionaries containing file information.

    Returns:
        The total size in bytes for the filtered files.
    """
    filtered_files = filter_files_by_property(property_name, value, files)
    return sum(
        convert_to_bytes(file['size'], file['unit']) for file in filtered_files
    )


def convert_to_bytes(size: int, unit: str = 'B') -> int:
    """
    Converts a given size in a specific unit to bytes.

    Args:
        size: The size to convert.
        unit: The unit of the size (default is 'B').

    Returns:
        The size in bytes.
    """
    return size * UNIT_CONVERSION.get(unit, 1)


def convert_bytes_to_largest_unit(size_in_bytes: int) -> List[Any]:
    """
    Converts a given size in bytes to the largest possible unit.

    Args:
        size_in_bytes: The size in bytes to convert.

    Returns:
        A list containing the size and the largest unit.
    """
    for unit in reversed(UNITS):
        if size_in_bytes >= UNIT_CONVERSION[unit]:
            return [round(size_in_bytes / UNIT_CONVERSION[unit]), unit]
    return [size_in_bytes, 'B']


def print_result_form(filenames: List[str], size_unit_out: List[Any]) -> None:
    """
    Prints the filenames and their total size in the specified unit.

    Args:
        filenames: A list of filenames to print.
        size_unit_out: A list containing the total size and its corresponding
                       unit.
    """
    print(*filenames, sep='\n')
    print('-' * 10)
    print('Summary:', *size_unit_out)
    print()


def group_files_by_extension_and_calculate_total_sizes(
    files: List[Dict[str, Any]]
) -> None:
    """
    Groups files by extension, calculates their total size, and prints
    the result.

    Args:
        files: A list of dictionaries containing file information.
    """
    extensions = unique_values(files, 'extension')

    for extension in extensions:
        filenames = sorted(
            f"{file['filename']}.{extension}"
            for file in files if file['extension'] == extension
        )
        total_size_in_bytes = get_total_size_for_files_with_property(
            'extension', extension, files
        )
        size_unit_out = convert_bytes_to_largest_unit(total_size_in_bytes)
        print_result_form(filenames, size_unit_out)


# Example usage
file_to_open = "files.txt"
data = get_list_of_files_info(file_to_open)

group_files_by_extension_and_calculate_total_sizes(data)
