'''
TODO:
    Complete the code below to print the contents of the countries dictionary,
    arranging its elements in lexicographic key order, specifying , (a comma
    without a space) as the element separator, the string - (a space hyphen
    space) as the key-value pair separator, and three spaces as the
    indentation.

NOTE:
    The initial part of the response looks like this:
        {
        "Angola" - "Luanda",
        "Australia" - "Canberra",
        ...
'''
import json
from typing import Dict


def format_countries(countries: Dict) -> str:
    """
    Formats the countries dictionary into a JSON-like string with sorted keys,
    using a comma without a space as the separator and a key-value pair
    separator of " - " with three spaces indentation.

    Args:
        countries (Dict): The dictionary containing country names as keys and
                          their capitals as values.

    Returns:
        str: A formatted string displaying country-capital pairs.
    """
    return json.dumps(
        countries, indent=3, separators=(',', ' - '), sort_keys=True
    )


# Example usage
countries: Dict = {
    'Monaco': 'Monaco', 'Iceland': 'Reykjavik',
    'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
    'Mali': 'Bamako', 'Colombia': 'Bogota',
    'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
    'Cuba': 'Havana', 'France': 'Paris',
    'Gabon': 'Libreville', 'Liberia': 'Monrovia',
    'Angola': 'Luanda', 'India': 'New Delhi',
    'Canada': 'Ottawa', 'Australia': 'Canberra'
}

# Call the function and print the result
formatted_countries = format_countries(countries)
print(formatted_countries)
