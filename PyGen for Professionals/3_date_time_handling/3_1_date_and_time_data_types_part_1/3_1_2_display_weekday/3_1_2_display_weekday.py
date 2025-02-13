'''
TODO:
    Hurricane Andrew, which struck Florida on August 24, 1992, was one of the
    costliest and deadliest hurricanes in U.S. history.

    Complete the code below to print the day of the week (starting at 0) on
    which Hurricane Andrew made landfall in the United States.

'''
from datetime import date


def get_day_of_week_for_hurricane(year: int, month: int, day: int) -> int:
    """
    Given a date (year, month, day), returns the weekday as an integer
    (0 = Monday, 6 = Sunday).

    Args:
    - year (int): The year of the hurricane event.
    - month (int): The month of the hurricane event.
    - day (int): The day of the hurricane event.

    Returns:
    - int: The day of the week (0 = Monday, 6 = Sunday) for the given date.
    """
    hurricane_date = date(year, month, day)
    return hurricane_date.weekday()


hurricane_andrew_landfall = get_day_of_week_for_hurricane(1992, 8, 24)
print(hurricane_andrew_landfall)
