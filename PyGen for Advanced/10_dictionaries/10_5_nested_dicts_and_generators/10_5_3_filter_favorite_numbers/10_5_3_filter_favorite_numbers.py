'''
TODO:
    Complete the above code using the generator to produce a result dictionary
    consisting of all elements of the favorite_numbers dictionary whose values
    are two-digit numbers.

NOTE:
    You do not need to print the contents of the result dictionary.
'''
from typing import Dict


def is_two_digit(value: int) -> bool:
    """
    This function checks whether the given number is a two-digit number
    (between 10 and 99 inclusive).

    Args:
        value (int): The number to check.

    Returns:
        bool: True if the value is a two-digit number, False otherwise.
    """
    return 10 <= value <= 99


def filter_favorite_numbers(numbers: Dict[str, int]) -> Dict[str, int]:
    """
    This function filters the numbers dictionary and returns a new dictionary
    containing only the key-value pairs where the value is a two-digit number
    (between 10 and 99 inclusive).

    Args:
        numbers (Dict[str, int]): A dictionary with names as keys and
                                           favorite numbers as values.

    Returns:
        Dict[str, int]: A dictionary containing only key-value pairs where
                        the value is a two-digit number.
    """
    # Using a generator expression inside a dictionary comprehension
    # to filter the numbers
    result = {k: val for k, val in numbers.items() if is_two_digit(val)}

    return result


# Sample dictionary of favorite numbers
favorite_numbers = {
    'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123,
    'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36,
    'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89,
    'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777,
    'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404,
    'olga': 271, 'anna': 55, 'madlen': 876
}

# Calling the function and storing the result in 'result'
result = filter_favorite_numbers(favorite_numbers)
