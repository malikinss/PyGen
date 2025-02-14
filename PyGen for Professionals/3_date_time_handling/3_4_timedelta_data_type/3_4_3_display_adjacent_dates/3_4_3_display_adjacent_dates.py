'''
TODO:
    Write a program that takes a date as input and outputs the previous
    and next dates.
NOTE:
    It is guaranteed that the submitted date has a previous and a next date.
'''
from datetime import datetime, timedelta

DATE_FORMAT = "%d.%m.%Y"


def get_adjacent_dates(date_str: str) -> tuple[str, str]:
    """
    Returns the previous and next dates for the given date string.

    Args:
        date_str (str): A date string in the format "DD.MM.YYYY".

    Returns:
        tuple[str, str]: A tuple containing the previous and next dates in the
                         same format.
    """
    current_date = datetime.strptime(date_str, DATE_FORMAT)
    previous_date = current_date - timedelta(days=1)
    next_date = current_date + timedelta(days=1)

    return previous_date.strftime(DATE_FORMAT), next_date.strftime(DATE_FORMAT)


# Example usage
user_date = input("Please input date in format DD.MM.YYYY: ")
prev_date, next_date = get_adjacent_dates(user_date)
print(prev_date, next_date, sep="\n")
