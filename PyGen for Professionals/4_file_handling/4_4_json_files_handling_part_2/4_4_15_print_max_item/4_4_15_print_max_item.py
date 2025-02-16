'''
TODO:
        You you have access to the food_services.json file, which contains a
        list of JSON objects that represent data on catering establishments:
            [
                {
                    "Name": "SMETANA",
                    "IsNetObject": "no",
                    "OperatingCompany": "",
                    "TypeObject": "cafe",
                    "AdmArea": "North-Eastern Administrative Okrug",
                    "District": "Yaroslavl District",
                    "Address": "Moscow, Yegor Abakumov Street, Building 9",
                    "SeatsCount": 48
                },
                ...
            ]

        By "establishment" we mean one JSON object from this list.

        The establishment has the following attributes:
            Name — name
            IsNetObject — yes or no depending on whether the establishment
                          is a chain
            OperatingCompany — name of the chain
            TypeObject — type (cafe, canteen, restaurant, etc.)
            AdmArea — administrative zone
            District — district
            Address — full address
            SeatsCount — number of seats

        Write a program that:
            1) determines the district of Moscow in which the most
            establishments are located and outputs the name of this district
            and the number of establishments in it

            2) determines the chain with the largest number of establishments
            and outputs the name of this chain and the number of
            establishments in this chain

        The program should output the obtained values in the
        following format:
            <district>: <number of establishments>
            <name of the chain>: <number of establishments>

NOTE:
        It is guaranteed that the desired chain is unique.

        Example output:
            district Metrogorodok: 456
            French bakery SeDelice: 144
'''
import json
from typing import Dict, List, Callable


def read_json_file(file_path: str) -> List[Dict[str, str]]:
    """
    Read and parse JSON file with food services data.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, str]]: List of dictionaries containing food services
        data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def count_items(
    data: List[Dict[str, str]],
    key_extractor: Callable[[Dict[str, str]], str],
    filter_func: Callable[[Dict[str, str]], bool] = lambda x: True
) -> Dict[str, int]:
    """
    Count items based on extracted keys and optional filter.

    Args:
        data (List[Dict[str, str]]): List of food service records.
        key_extractor (Callable): Function to extract key from record.
        filter_func (Callable): Function to filter records.

    Returns:
        Dict[str, int]: Dictionary with counts for each key.
    """
    counts: Dict[str, int] = {}
    for item in filter(filter_func, data):
        key = key_extractor(item)
        counts[key] = counts.get(key, 0) + 1
    return counts


def print_most_frequent(counts: Dict[str, int]) -> None:
    """
    Print item with the highest count.

    Args:
        counts (Dict[str, int]): Dictionary with item counts.
    """
    if not counts:
        return

    most_frequent = max(counts.items(), key=lambda x: x[1])
    print(f'{most_frequent[0]}: {most_frequent[1]}')


def analyze_food_services(file_path: str) -> None:
    """
    Analyze food services data and print statistics.

    Args:
        file_path (str): Path to the JSON file with food services data.
    """
    # Read data
    food_services = read_json_file(file_path)

    # Count districts
    districts = count_items(
        food_services,
        key_extractor=lambda x: x['District']
    )

    # Count chains
    chains = count_items(
        food_services,
        key_extractor=lambda x: x['OperatingCompany'],
        filter_func=lambda x: x['IsNetObject'].lower() == 'да'
    )

    # Print results
    print_most_frequent(districts)
    print_most_frequent(chains)


analyze_food_services('food_services.json')
