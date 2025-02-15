'''
TODO:
    Write a program that determines the day of the week corresponding
    to a given date.

    The program input is a date in the YYYY-MM-DD format.

    The program should display the full name of the day of the week in English,
    which corresponds to the entered date.
'''
import calendar
from datetime import datetime

DATE_FORMAT = '%Y-%m-%d'


def convert_to_date(date_string):
    """
    Converts a string in the format 'YYYY-MM-DD' to a datetime.date object.

    Args:
        date_string (str): The date string in 'YYYY-MM-DD' format.

    Returns:
        datetime.date: The parsed date.

    Raises:
        ValueError: If the input string is not in the correct format.
    """
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")


def print_weekday(user_date):
    """
    Prints the full name of the weekday for a given date.

    Args:
        user_date (str): The date string in 'YYYY-MM-DD' format.
    """
    given_date = convert_to_date(user_date)
    print(calendar.day_name[given_date.weekday()])


print_weekday(input("Enter date (YYYY-MM-DD): "))
