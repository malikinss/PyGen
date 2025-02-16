'''
TODO:
        You have access to the playgrounds.csv file with information about
        Moscow sports grounds.

        the first column contains the type of ground;
        the second column contains the administrative district;
        the third column contains the name of the district;
        the fourth column contains the address:
            ObjectName; AdmArea; District; Address
            Park, green urban area "Lianozovsky Park of Culture and Leisure";
            North-Eastern Administrative District; Lianozovo District;
            Uglichskaya Street, Building 13
            ...

        Write a program that creates a JSON object, the key of which is the
        administrative district, and the value is a JSON object, in which, in
        turn, the key is the name of the district related to this
        administrative district, and the value is a list of addresses of all
        the playgrounds in this district.

        The program should write the resulting JSON object to
        the addresses.json file.

NOTE:
        The addresses in the lists must be in their original order.
        The delimiter in the playgrounds.csv file is a semicolon, and
        quotation marks are not used.
        The initial part of the addresses.json file looks like this:
            {
                "North-Eastern Administrative Okrug": {
                    "Lianozovo District": [
                        "Uglichskaya Street, Building 13",
                        "Altufevskoe Shosse, Building 147A"
                    ],
                    "Otradnoe District": [
                        "Altufevskoe Shosse, Building 20A",
                        "Yurlovsky Proezd, Building 8, Building 1",
                        "Yurlovsky Proezd, Building 8, Building 1"
                    ],
                    ...
                },
                ...
            }
'''
import json
import csv
from typing import Dict, List


def read_csv(filename: str, delimiter: str = ',') -> List[Dict[str, str]]:
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename: The path to the CSV file.
        delimiter: The delimiter used in the CSV file.

    Returns:
        The content of the CSV file as a list of dictionaries.
    """
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
        return [row for row in reader]


def write_json_file(data: Dict[str, List[str]], file_path: str) -> None:
    """
    Write JSON data to a file.

    Args:
        data (Dict[str, List[str]]): JSON data to be written.
        file_path (str): Path to the output JSON file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)


def create_administrative_area_dict(
    data: List[Dict[str, str]]
) -> Dict[str, Dict[str, List[str]]]:
    """
    Create a dictionary where keys are administrative areas and values
    are dictionaries
    with keys as districts and values as lists of addresses.

    Args:
        data (List[Dict[str, str]]): List of dictionaries containing
        data from CSV.

    Returns:
        Dict[str, Dict[str, List[str]]]: Dictionary with administrative
        areas as keys and dictionaries of districts as values.
    """
    addresses: Dict = {}

    for row in data:
        adm_area = row['AdmArea']
        district = row['District']
        address = row['Address']

        if adm_area not in addresses:
            addresses[adm_area] = {}

        if district not in addresses[adm_area]:
            addresses[adm_area][district] = []

        addresses[adm_area][district].append(address)

    return addresses


input_file_path = 'playgrounds.csv'
output_file_path = 'addresses.json'
data = read_csv(input_file_path, delimiter=';')
addresses: Dict = create_administrative_area_dict(data)
write_json_file(addresses, output_file_path)
