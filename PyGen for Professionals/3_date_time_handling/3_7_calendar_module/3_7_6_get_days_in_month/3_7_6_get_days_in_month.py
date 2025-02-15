'''
TODO:
    Implement a function get_days_in_month() that takes two arguments in
    the following order:
        year — natural number
        month — full name of the month in English

    The function should return a list, sorted in ascending order, of all dates
    (type date) of the month month and year year.
'''
import calendar
from datetime import date


def get_month_number_by_name(month_name: str) -> int:
    """
    Returns the month number for a given month name.

    Args:
        month_name (str): The full name of the month in English.

    Returns:
        int: The month number (1 for January, 2 for February, etc.).

    Raises:
        ValueError: If the month name is invalid.
    """
    month_name = month_name.capitalize()

    # Skip the empty string at index 0
    month_list = list(calendar.month_name)[1:]
    if month_name not in month_list:
        raise ValueError(
            f"Invalid month name: '{month_name}'. Please enter a valid month."
        )

    return month_list.index(month_name) + 1  # Month numbers start from 1


def get_days_in_month(year: int, month: str) -> list:
    """
    Returns a sorted list of all dates in the given month and year.

    Args:
        year (int): The year of the dates.
        month (str): The full name of the month in English.

    Returns:
        list: A list of dates in the month.
    """
    month_num = get_month_number_by_name(month)
    _, num_days = calendar.monthrange(year, month_num)

    return [date(year, month_num, day) for day in range(1, num_days + 1)]


# Example usage
print(get_days_in_month(2021, 'December'))
