'''
TODO:
    A pickle file containing a serialized dictionary or list is
    transmitted over a communication channel, and an integer
    — a checksum, which is calculated according to the following rule:
        1) for a dictionary — the sum of all integer keys (type int)
        2) for a list — the product of the minimum and maximum integer
            elements (type int)

    Write a program that calculates the checksum for an object contained
    in a pickle file and compares it with a given integer.

    The program receives the name of the pickle file containing the
    serialized dictionary or list in the first line, and an integer
    in the next line.

    The program should calculate the checksum for the object contained in
    the given pickle file, and if it matches the entered number,
    output the text:
        Checksums match

    if it does not match the entered number, output the text:
        Checksums do not match

NOTE:
    If the list (dictionary) does not contain integer elements (keys),
    then consider the checksum to be 0.
'''
import pickle
import sys
from typing import List, Dict, Any, Union


def deserialize_pickle_file(
    pickle_file_path: str
) -> Union[Dict[Any, Any], List[Any], None]:
    """
    Deserializes an object from the given pickle file.

    Args:
        pickle_file_path (str): Path to the pickle file.

    Returns:
        Union[Dict[Any, Any], List[Any], None]: The deserialized dictionary
        or list, or None if an error occurs.

    Raises:
        Exception: If deserialization fails.
    """
    try:
        with open(pickle_file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as error:
        print(f"Error loading pickle file: {error}", file=sys.stderr)
        return None


def extract_integer_elements(
    items: Union[List[Any], Dict[Any, Any]]
) -> List[int]:
    """
    Extracts all integer elements from a list or integer keys from
    a dictionary.

    Args:
        items (Union[List[Any], Dict[Any, Any]]): A list or dictionary
        containing various elements.

    Returns:
        List[int]: A list containing only integer elements (from a list)
        or integer keys (from a dictionary).
    """
    if isinstance(items, list):
        return [item for item in items if isinstance(item, int)]
    if isinstance(items, dict):
        return [key for key in items.keys() if isinstance(key, int)]
    return []


def calculate_checksum(
    data_structure: Union[Dict[Any, Any], List[Any]]
) -> int:
    """
    Calculates the checksum for the given data structure.

    Args:
        data_structure (Union[Dict[Any, Any], List[Any]]): The dictionary or
        list to process.

    Returns:
        int: The calculated checksum, or 0 if no valid integer elements
        are found.
    """
    integer_elements = extract_integer_elements(data_structure)

    if isinstance(data_structure, list) and integer_elements:
        return min(integer_elements) * max(integer_elements)
    if isinstance(data_structure, dict) and integer_elements:
        return sum(integer_elements)
    return 0


def compare_checksum(
    expected_checksum: int, calculated_checksum: int
) -> str:
    """
    Compares the expected checksum with the calculated checksum.

    Args:
        expected_checksum (int): The expected checksum value.
        calculated_checksum (int): The calculated checksum value.

    Returns:
        str: The result of the comparison.
    """
    if expected_checksum == calculated_checksum:
        return 'Checksums match'
    else:
        return 'Checksums do not match'


def process_pickle_checksum():
    """
    Reads input, processes the pickle file, and compares checksums.
    """
    try:
        pickle_file_path = input("Enter pickle file path: ").strip()
        expected_checksum = int(input("Enter expected checksum: ").strip())
    except ValueError:
        print("Invalid checksum input", file=sys.stderr)
        sys.exit(1)

    data_structure = deserialize_pickle_file(pickle_file_path)
    if data_structure is None:
        sys.exit(1)

    calculated_checksum = calculate_checksum(data_structure)
    print(compare_checksum(expected_checksum, calculated_checksum))
