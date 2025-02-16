'''
TODO:
        You have access to the countries.json file, which contains a list of
        JSON objects with information about countries and the religions
        practiced in them:
            [
                {
                    "country": "Afghanistan",
                    "religion": "Islam"
                },
                {
                    "country": "Albania",
                    "religion": "Islam"
                },
                ...
            ]
        Each object from this list contains two attributes:
            country — country
            religion — religion practiced

        Write a program that creates a single JSON object that has the name of
        a religion as a key and a list of countries where this religion is
        practiced as a value.

        The program should write the resulting JSON object to
        the religion.json file.

NOTE:
        Countries in the lists must be in their original order.
        The initial part of the religion.json file looks like this:
            {
                "Islam":[
                    "Afghanistan",
                    "Albania",
                    "Algeria",
                    ...
                ],
                ...
            }
'''
import json
from typing import Dict, List


def read_json_file(file_path: str) -> List[Dict[str, str]]:
    """
    Read JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, str]]: List of dictionaries containing JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        raise


def write_json_file(data: Dict[str, List[str]], file_path: str) -> None:
    """
    Write JSON data to a file.

    Args:
        data (Dict[str, List[str]]): JSON data to be written.
        file_path (str): Path to the output JSON file.

    Raises:
        IOError: If the file cannot be written.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=3)
    except IOError:
        print(f"Error: Could not write to {file_path}.")
        raise


def extract_and_group_religions(
    data: List[Dict[str, str]]
) -> Dict[str, List[str]]:
    """
    Create a dictionary where keys are religions and values are lists of
    countries practicing that religion.

    Args:
        data (List[Dict[str, str]]): List of dictionaries containing country
        and religion data.

    Returns:
        Dict[str, List[str]]: Dictionary with religions as keys and lists of
        countries as values.
    """
    religions_dict: Dict = {}

    for item in data:
        religion = item.get('religion')
        country = item.get('country')

        if religion and country:
            if religion not in religions_dict:
                religions_dict[religion] = []
            religions_dict[religion].append(country)

    return religions_dict


def update_religion_data(input_file_path: str, output_file_path: str) -> None:
    """
    Reads data from the input JSON file, groups countries by religion,
    and writes the resulting JSON object to the output file.

    Args:
        input_file_path (str): Path to the input JSON file.
        output_file_path (str): Path to the output JSON file.
    """
    # Read the original data from the JSON file
    data = read_json_file(input_file_path)

    # Group countries by religion
    religions = extract_and_group_religions(data)

    # Write the resulting data to a new JSON file
    write_json_file(religions, output_file_path)


input_file_path = 'countries.json'
output_file_path = 'religion.json'
update_religion_data(input_file_path, output_file_path)
