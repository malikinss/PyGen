'''
TODO:
    You have access to the zoo.json file, which contains a list of JSON
    objects with data about the inhabitants of a certain zoo.

    The key in each object is the name of the animal, the value is their
    number in the zoo:
        [
            {
                "Axolotl": 11,
                "Poison Frog": 12,
                "Sonoran Toad": 6,
                "Tiger Salamander": 16
            },
            {
                "African Fish Eagle": 6,
                "Andean Condor": 8,
                "Black Vulture": 8,
                "Bufflehead Duck": 9,
                "Flamingo": 8,
                "Great Horned Owl": 16,
                "Hornbill": 1
            },
            ...
        ]

    Write a program that determines how many animals live in the zoo and
    prints the result.

NOTE:
    All keys in JSON objects are guaranteed to be distinct.
'''
import json
from typing import Dict, List
from collections import ChainMap


def read_json_file(file_path: str) -> List[Dict[str, str]]:
    """
    Read JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, str]]: List of dictionaries containing JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def count_total_animals(zoo_data: Dict[str, int]) -> int:
    """
    Count the total number of animals in the zoo.

    Args:
        zoo_data (Dict[str, int]): Dictionary containing animal names as keys
        and their counts as values.

    Returns:
        int: Total number of animals in the zoo.
    """
    return sum(zoo_data.values())


def print_animals_total(filename: str) -> None:
    """
    Read the zoo data from the JSON file, count the total number of animals,
    and print the result.

    Args:
        filename (str): Path to the JSON file.
    """
    data = ChainMap(*read_json_file(filename))

    print(count_total_animals(data))


print_animals_total('zoo.json')
