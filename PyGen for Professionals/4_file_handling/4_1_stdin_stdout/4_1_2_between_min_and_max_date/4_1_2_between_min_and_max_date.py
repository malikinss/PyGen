'''
TODO:
    A sequence of dates is given. Write a program that prints the number of
    days between the maximum and minimum dates of a given sequence.

    An arbitrary number of lines are supplied as input to the program; each
    line contains a date in ISO format (YYYY-MM-DD).

    The program should output a single number - the number of days between the
    maximum and minimum dates of the entered sequence.
'''
import sys
from datetime import datetime, date
from typing import List

DATE_FORMAT = '%Y-%m-%d'


def parse_iso_date(date_string: str) -> date:
    """
    Parses a string in ISO date format (YYYY-MM-DD) into a datetime.date
    object.

    Args:
        date_string (str): The date string in ISO format.

    Returns:
        datetime.date: The parsed date object.

    Raises:
        ValueError: If the date string is not in the expected ISO format.
    """
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid date format')


def get_dates_from_input() -> List[date]:
    """
    Reads multiple lines of date strings from the standard input, strips any
    leading/trailing spaces, and converts them to datetime.date objects.

    Returns:
        List[datetime.date]: A list of date objects representing the input
                             dates.
    """
    # Get input lines and remove extra spaces
    dates = [line.strip() for line in sys.stdin.readlines()]
    # Convert strings to date objects
    return [parse_iso_date(date) for date in dates]


def calculate_difference_between_min_and_max_dates(dates: List[date]) -> int:
    """
    Calculates the number of days between the maximum and minimum dates in
    a list.

    Args:
        dates (List[datetime.date]): A list of date objects.

    Returns:
        int: The number of days between the earliest and latest date in
             the list.
    """
    return (max(dates) - min(dates)).days


# Get input dates
dates = get_dates_from_input()
# Output the difference in days
print(calculate_difference_between_min_and_max_dates(dates))
