'''
TODO:
    Implement a function get_weekday() that takes one argument:
        number — an integer (from 1 to 7 inclusive)

    The function should return the full name of the day of the week in Russian
    that corresponds to the number, and:
        - If number is not an integer, the function should raise an exception:
            TypeError('The argument is not an integer')

        - If number is an integer but does not belong to the segment [1;7],
        the function should raise an exception:
            ValueError('The argument does not belong to the required range')
'''
from calendar import day_name
import locale

# Set locale for correct display of weekdays in Russian
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# Dictionary mapping numbers to weekday names
days = {i: d for i, d in enumerate(map(str.title, day_name), 1)}


def get_weekday(number) -> str:
    """
    Returns the full name of the weekday in Russian corresponding to the
    number (1 to 7).

    Args:
        number (int): An integer from 1 to 7 representing the day of the week.

    Returns:
        str: The full name of the weekday in Russian.

    Raises:
        TypeError: If the argument is not an integer.
        ValueError: If the argument is not within the range 1 to 7.
    """
    # Check if the argument is an integer
    if not isinstance(number, int):
        raise TypeError("The argument is not an integer")

    # Check if the number is within the range 1 to 7
    if number not in range(1, 8):
        raise ValueError(
            "The argument does not belong to the required range"
        )

    # Return the name of the weekday
    return days[number]
