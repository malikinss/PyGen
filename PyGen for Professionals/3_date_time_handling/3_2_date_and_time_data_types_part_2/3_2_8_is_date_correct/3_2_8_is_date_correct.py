'''
TODO:
    Implement a function is_correct() that takes three arguments in
    the following order:
        day — natural number, day
        month — natural number, month
        year — natural number, year

    The function must return True if the date with day, month and year
    components is valid, or False otherwise.
'''
from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    """
    Checks if the given day, month, and year form a valid date.

    Args:
    day (int): The day of the month.
    month (int): The month of the year.
    year (int): The year.

    Returns:
    bool: True if the date is valid, False otherwise.
    """
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False
