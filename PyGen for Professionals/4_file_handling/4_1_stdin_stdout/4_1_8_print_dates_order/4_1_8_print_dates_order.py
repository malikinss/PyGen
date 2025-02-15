'''
TODO:
    A sequence of dates is given.

    Write a program that determines the order in which dates appear in a given
    sequence.
'''
import sys
from datetime import datetime, date
from typing import List


def read_input() -> List[str]:
    """
    Reads input from stdin and returns a list of stripped lines.

    Returns:
        List[str]: A list of lines from input.
    """
    return [line.strip() for line in sys.stdin.readlines()]


def string_to_date(date_string: str) -> date:
    """
    Converts a date string in the format DD.MM.YYYY to a date object.

    Args:
        date_string (str): A string representing the date in DD.MM.YYYY format.

    Returns:
        date: A corresponding date object.
    """
    return datetime.strptime(date_string, '%d.%m.%Y').date()


def parse_dates(data: List[str]) -> List[date]:
    """
    Parses a list of date strings to a list of date objects.

    Args:
        data (List[str]): A list of date strings.

    Returns:
        List[date]: A list of date objects.
    """
    return [string_to_date(record) for record in data]


def check_order(dates: List[date]) -> str:
    """
    Determines if the dates are in strictly ascending, descending, or mixed
    order.

    Args:
        dates (List[date]): A list of date objects to check.

    Returns:
        str: "ASC" if strictly ascending, "DESC" if strictly descending,
             "MIX" otherwise.
    """
    if all(dates[i] < dates[i + 1] for i in range(len(dates) - 1)):
        return 'ASC'
    elif all(dates[i] > dates[i + 1] for i in range(len(dates) - 1)):
        return 'DESC'
    return 'MIX'


def print_dates_order(dates: List[date]) -> None:
    """
    Prints the order type of the given dates.

    Args:
        dates (List[date]): A list of date objects.
    """
    print(check_order(dates))


# Main execution
given_data = read_input()
given_dates = parse_dates(given_data)
print_dates_order(given_dates)
