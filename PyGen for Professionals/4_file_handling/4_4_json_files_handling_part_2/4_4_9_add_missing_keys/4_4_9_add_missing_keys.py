'''
TODO:
        You have access to the people.json file, which contains a list of
        JSON objects.
        Moreover, different objects can have a different number of keys:
            [
                {
                    "age": 33,
                    "country": "Lesotho",
                    "phone": "(927) 316-2249",
                    "family_status": "married",
                    "email": "neonatus@outlook.com"
                },
                {
                    "age": 25,
                    "country": "Guinea",
                    "name": "Dorey",
                    "children": "yes",
                    "email": "ismail@gmail.com",
                    "university": "Khalifa University",
                    "family_status": "married"
                },
                ...
            ]

        Write a program that adds all missing keys to each JSON object from
        this list, assigning null to these keys.
        A key is considered missing if it is present in some other object, but
        is not present in this one.
        The program should create a list of updated JSON objects and write it
        to the updated_people.json file.

NOTE:
        The JSON objects in the list created by the program should be in their
        original order.

        The order of the keys in the JSON objects is not important.

        For example, if the people.json file was:
            [
                {
                    "age": 33,
                    "country": "Lesotho"
                },
                {
                    "age": 25,
                    "country": "Guinea",
                    "name": "Dorey"
                }
            ]
        then the program should create a file updated_people.json with the
        following contents:
            [
                {
                    "age": 33,
                    "country": "Lesotho"
                    "name": null
                },
                {
                    "age": 25,
                    "country": "Guinea",
                    "name": "Dorey"
                }
            ]
'''
import json
from typing import Dict, List, Set


def read_json_file(file_path: str) -> List[Dict]:
    """
    Reads JSON data from a file and returns it as a list of dictionaries.

    Args:
        file_path (str): Path to the JSON file to read.

    Returns:
        List[Dict]: A list of dictionaries containing the JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(file_path, 'r', encoding='utf8') as file:
        return json.load(file)


def write_json_file(data: List[Dict], file_path: str) -> None:
    """
    Writes a list of dictionaries as JSON data to a file.

    Args:
        data (List[Dict]): List of dictionaries containing the data to write.
        file_path (str): Path to the output JSON file.

    Raises:
        IOError: If the file cannot be written.
    """
    with open(file_path, 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)


def get_all_existing_keys(data: List[Dict]) -> set:
    """
    Retrieves all unique keys present in any dictionary within the given list.

    Args:
        data (List[Dict]): List of dictionaries to extract keys from.

    Returns:
        set: A set containing all unique keys from the dictionaries.
    """
    all_keys: Set = set()

    # Update all_keys with the keys from each dictionary in the data list
    for obj in data:
        all_keys.update(obj.keys())

    return all_keys


def add_missing_keys(data: List[Dict]) -> List[Dict]:
    """
    Adds missing keys to each dictionary in the list, assigning `None` to
    the missing keys.

    Args:
        data (List[Dict]): List of dictionaries to update.

    Returns:
        List[Dict]: A new list of dictionaries where each dictionary has all
        the keys from the full set of keys in the original data.
    """
    # Retrieve all the unique keys from the entire data
    all_keys = get_all_existing_keys(data)

    # Iterate through each dictionary and add missing keys with None values
    for item in data:
        for key in all_keys:
            if key not in item:
                item[key] = None

    return data


def update_json_data(input_file_path: str, output_file_path: str) -> None:
    """
    Reads data from the input JSON file, adds missing keys to each dictionary,
    and writes the updated data to the output JSON file.

    Args:
        input_file_path (str): Path to the input JSON file.
        output_file_path (str): Path to the output JSON file.
    """
    # Read the original data from the JSON file
    data = read_json_file(input_file_path)

    # Add missing keys to each dictionary in the list
    result_data = add_missing_keys(data)

    # Write the updated data back to a new JSON file
    write_json_file(result_data, output_file_path)


input_file_path = 'people.json'
output_file_path = 'updated_people.json'
update_json_data(input_file_path, output_file_path)
