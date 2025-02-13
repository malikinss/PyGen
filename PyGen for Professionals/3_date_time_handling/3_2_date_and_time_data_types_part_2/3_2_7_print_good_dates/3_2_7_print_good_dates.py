'''
TODO:
    A date is considered “interesting” if its year coincides with the user's
    year of birth, and the sum of the month number and day number is equal to
    his age.

    Implement a function print_good_dates() that takes one argument:
        dates — list of dates (date type)

    The function should display “interesting” dates in ascending order, each
    on a separate line, in the format month_name DD, YYYY, where month_name is
    the full name of the month in English.

NOTE:
    If an empty list or a list with no interesting dates is passed to the
    function, the function should not output anything.
'''
from datetime import date
from typing import List

USER_BIRTHYEAR: int = 1992
USER_AGE: int = 29


def format_dates(dates: List[date]) -> List[str]:
    """
    Formats a list of dates into the 'Month DD, YYYY' format.

    Args:
    dates (List[date]): A list of date objects.

    Returns:
    List[str]: A list of formatted date strings.
    """
    return [current_date.strftime('%B %d, %Y') for current_date in dates]


def is_interesting_date(d: date) -> bool:
    """
    Checks if a date is 'interesting' based on predefined criteria.

    A date is considered interesting if:
    - The year matches the user's birth year.
    - The sum of the month number and day number equals the user's age.

    Args:
    d (date): A date object.

    Returns:
    bool: True if the date is interesting, False otherwise.
    """
    return d.year == USER_BIRTHYEAR and (d.month + d.day) == USER_AGE


def find_interesting_dates(dates: List[date]) -> List[date]:
    """
    Finds all 'interesting' dates from a given list.

    A date is considered interesting if:
    - The year matches the user's birth year.
    - The sum of the month and day equals the user's age.

    Args:
    dates (List[date]): A list of date objects.

    Returns:
    List[date]: A sorted list of interesting date objects.
    """
    return sorted([
        current_date for current_date in dates
        if is_interesting_date(current_date)
    ])


def print_good_dates(dates: List[date]) -> None:
    """
    Prints interesting dates in 'Month DD, YYYY' format.

    Args:
    dates (List[date]): A list of date objects.
    """
    interesting_dates = find_interesting_dates(dates)

    if interesting_dates:
        print("\n".join(format_dates(interesting_dates)))
