'''
TODO:
    A sequence of dates is given.

    Write a program that creates and displays a list whose elements are
    nonnegative integers—the number of days between two adjacent dates in
    the sequence.

NOTE:
    The dates in the sequence can be in any order, that is, it is not
    guaranteed that the next date is greater than the previous one.

    If the sequence consists of a single date, then the program should output
    an empty list.
'''
from datetime import datetime
from typing import List

DATE_FORMAT = '%d.%m.%Y'


def get_user_dates() -> List[datetime]:
    """
    Prompt the user to input dates and return a list of datetime objects.

    Returns:
        List[datetime]: A list of parsed datetime objects.
    """
    while True:
        user_input = input(
            "Enter dates (DD.MM.YYYY format), separated by spaces: "
        ).split()

        try:
            # Attempt to parse each date and return the list
            return [
                datetime.strptime(date_str, DATE_FORMAT)
                for date_str in user_input
            ]
        except ValueError:
            print("Invalid date format. Please use the format DD.MM.YYYY.")


def calculate_days_difference(dates: List[datetime]) -> List[int]:
    """
    Calculate the absolute differences in days between adjacent dates.

    Args:
        dates (List[datetime]): A list of datetime objects.

    Returns:
        List[int]: A list of non-negative differences in days.
    """
    if len(dates) < 2:
        return []

    # List comprehension to calculate the differences
    return [abs((dates[i] - dates[i + 1]).days) for i in range(len(dates) - 1)]


user_dates = get_user_dates()
days_diff = calculate_days_difference(user_dates)
print(days_diff)
