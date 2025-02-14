'''
TODO:
    Two dates are given - the left and right boundaries of the range,
    respectively.

    Write a program that, from this range, including boundaries, prints,
    starting from a date for which the sum of the day and month is odd, every
    third date, only if it is not Monday or Thursday.

    The program receives two dates as input in the format DD.MM.YYYY - the
    left and right boundaries of the range, respectively, each on a separate
    line.

    It is guaranteed that the first date is not greater than the second.

    The program must, from the specified range, including the ends, output,
    starting from a date for which the sum of the day and month is odd, every
    third date, only if it is not Monday or Thursday.

    Each date must be located on a separate line, in the format DD.MM.YYYY.

NOTE:
    If there are no dates that satisfy the condition, the program should not
    output anything.
'''
from datetime import datetime, timedelta, date
from typing import Optional

DATE_FORMAT = '%d.%m.%Y'


def parse_date(date_string: str) -> date:
    """
    Convert a date string into a date object.

    Args:
        date_string (str): Date in the format 'DD.MM.YYYY'.

    Returns:
        date: The parsed date object.

    Raises:
        ValueError: If the format is incorrect.
    """
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid date format. Please use DD.MM.YYYY')


def is_odd(number: int) -> bool:
    """
    Check if a number is odd.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return number % 2 != 0


def sum_of_day_and_month(given_date: date) -> int:
    """
    Calculate the sum of the day and month of a given date.

    Args:
        given_date (date): The date to process.

    Returns:
        int: The sum of the day and month.
    """
    return given_date.day + given_date.month


def find_first_valid_date(start_date: date, end_date: date) -> Optional[date]:
    """
    Find the first date in the range where the sum of the day and month is odd.

    Args:
        start_date (date): The start of the date range.
        end_date (date): The end of the date range.

    Returns:
        Optional[date]: The first valid date, or None if no such date exists.
    """
    current_date = start_date

    while current_date <= end_date:
        if is_odd(sum_of_day_and_month(current_date)):
            return current_date
        current_date += timedelta(days=1)

    return None


def is_valid_weekday(given_date: datetime) -> bool:
    """
    Check if the given date is neither Monday nor Thursday.

    Args:
        given_date (datetime): The date to check.

    Returns:
        bool: True if the date is not Monday or Thursday, False otherwise.
    """
    return given_date.weekday() not in (0, 3)


def display_valid_dates():
    """
    Read input dates, find the first valid date in the range, and print every
    third valid date that is not Monday or Thursday.
    """
    start_date = parse_date(input())
    end_date = parse_date(input())

    current_date = find_first_valid_date(start_date, end_date)

    while current_date and current_date <= end_date:
        if is_valid_weekday(current_date):
            print(current_date.strftime(DATE_FORMAT))
        current_date += timedelta(days=3)


display_valid_dates()
