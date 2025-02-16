'''
TODO:
        you have access to the food_services.json file, which contains a list
        of JSON objects that represent data on catering establishments:
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

        Write a program that identifies all types of establishments and for
        each type finds the largest establishment of this type (has the
        largest number of seats).

        The program should output all types of establishments in lexicographic
        order, indicating for each the largest establishment and the number of
        seats in it.

        The establishment data should be placed each on a separate line, in
        the following format:
            <type of establishment>: <name of establishment>, <number of seats>

NOTE:
        The initial part of the answer looks like this:
            bar: Bar association PROFSOYUZ, 800
            buffet: DINING - KANTINACITY, 320
            snack bar: Burger FARSH, 74
            ...
'''
import json
from typing import Dict, List, Any


def read_json_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Read JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing JSON data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def should_replace_largest(
    current_largest: List[Any], establishment_size: int
) -> bool:
    """
    Determines if the current establishment should replace the largest one
    based on the number of seats.

    Args:
        current_largest (List[Any]): The current largest establishment's name
        and seats count.
        establishment_size (int): The size of the new establishment.

    Returns:
        bool: True if the current establishment should replace the largest one.
    """
    return current_largest is None or establishment_size > current_largest[1]


def group_establishments_by_type_and_find_largest(
    establishments: List[Dict[str, Any]]
) -> Dict[str, List[Any]]:
    """
    Groups establishments by type and finds the largest establishment
    of each type.

    Args:
        establishments (List[Dict[str, Any]]): List of dictionaries
        representing establishments.

    Returns:
        Dict[str, List[Any]]: Dictionary where keys are establishment types,
        and values are lists of the name and seat count of the largest
        establishment of that type.
    """
    result: Dict[str, List[Any]] = {}

    for establishment in establishments:
        establishment_type = establishment.get('TypeObject')
        establishment_name = establishment.get('Name')
        establishment_size = establishment.get('SeatsCount')

        # Skip if establishment_type is None or establishment_size is
        # not an integer
        if establishment_type is None or \
           not isinstance(establishment_size, int):
            continue

        # Check if the type is already in result
        if establishment_type not in result:
            result[establishment_type] = [
                establishment_name, establishment_size
            ]
        else:
            current_largest = result[establishment_type]
            # If current establishment is larger, update the result
            if should_replace_largest(current_largest, establishment_size):
                result[establishment_type] = [
                    establishment_name, establishment_size
                ]

    return result


def print_establishments_results(data: Dict[str, List[Any]]) -> None:
    """
    Outputs results in the required format.

    Args:
        data (Dict[str, List[Any]]): Dictionary with grouped establishments.
    """
    for establishment_type in sorted(data):
        establishment_name, establishment_size = data[establishment_type]
        print(
            f'{establishment_type}: {establishment_name}, {establishment_size}'
        )


# Main execution
establishments = read_json_data('food_services.json')
result = group_establishments_by_type_and_find_largest(establishments)
print_establishments_results(result)
