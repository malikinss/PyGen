'''
TODO:
    Geographic coordinates are a pair of numbers (x,y), where
        - x is the latitude
        - y is the longitude
    and -90°≤x≤90°, -180°≤y≤180°.

    Write a program that takes an arbitrary number of strings and determines
    which of them represent valid geographic coordinates.

    The program is given an arbitrary number of strings as input, each of
    which is a pair of numbers in the following format:
        (<x coordinate>, <y coordinate>)

    The program should output True for each string if it represents valid
    geographic coordinates, or False otherwise.
'''
import sys


def read_input() -> list[str]:
    """
    Reads input from stdin and returns a list of stripped lines.

    Returns:
        list[str]: A list of coordinate strings.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def is_valid_latitude(x: float) -> bool:
    """
    Checks if the latitude (x-coordinate) is within the valid range of
    geographic coordinates,
    which is between -90 and 90 degrees inclusive.

    Args:
        x (float): The latitude value to check.

    Returns:
        bool: True if the latitude is within the valid range, otherwise False.
    """
    return -90 <= x <= 90


def is_valid_longitude(y: float) -> bool:
    """
    Checks if the longitude (y-coordinate) is within the valid range of
    geographic coordinates,
    which is between -180 and 180 degrees inclusive.

    Args:
        y (float): The longitude value to check.

    Returns:
        bool: True if the longitude is within the valid range, otherwise False.
    """
    return -180 <= y <= 180


def is_coordinates(string: str) -> bool:
    """
    Checks if a given string represents valid geographic coordinates in the
    format (x, y), where x is the latitude and y is the longitude.

    The function checks if:
        - The string starts with '(' and ends with ')'.
        - The coordinates are valid floats.
        - The latitude (x) is in the range [-90, 90].
        - The longitude (y) is in the range [-180, 180].

    Args:
        string (str): The coordinate string to validate.

    Returns:
        bool: True if the string represents valid geographic coordinates,
        otherwise False.
    """
    string = string.strip()
    if string.startswith('(') and string.endswith(')'):
        try:
            x, y = map(float, string.strip('()').split(","))
            return is_valid_latitude(x) and is_valid_longitude(y)
        except ValueError:
            return False
    return False


def check_correctness_coordinates(data: list[str]) -> list[bool]:
    """
    Iterates through a list of coordinate strings and checks whether each
    string represents valid geographic coordinates.

    Args:
        data (list[str]): A list of strings, each representing a coordinate
        pair (x, y).

    Returns:
        list[bool]: A list of booleans where each value indicates whether the
        corresponding coordinate string is valid.
    """
    return list(map(is_coordinates, data))


if __name__ == "__main__":
    input_data = read_input()
    result = check_correctness_coordinates(input_data)
    print(*result, sep="\n")
