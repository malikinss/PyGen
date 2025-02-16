'''
TODO:
        Implement the is_correct_json() function that takes one argument:
            string — an arbitrary string

        The function should return True if the string is JSON-formatted, or
        False otherwise.
'''
import json


def is_correct_json(json_string: str) -> bool:
    """
    Check if the provided string is in valid JSON format.

    Args:
        json_string (str): The string to be checked.

    Returns:
        bool: True if the string is JSON-formatted, False otherwise.
    """
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False
