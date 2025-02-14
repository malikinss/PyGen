'''
TODO:
    Complete the code below to add one week and 12 hours to the
    datetime(2021, 11, 4, 13, 6) object and output the result in the format:
        DD.MM.YYYY HH:MM:SS.
'''
from datetime import datetime, timedelta


def add_time_to_datetime(dt: datetime, weeks: int = 1, hours: int = 12) -> str:
    """
    Adds a specified number of weeks and hours to a given datetime object
    and returns the result as a formatted string.

    Args:
        dt (datetime): The original datetime object.
        weeks (int, optional): Number of weeks to add. Defaults to 1.
        hours (int, optional): Number of hours to add. Defaults to 12.

    Returns:
        str: The resulting datetime formatted as 'DD.MM.YYYY HH:MM:SS'.
    """
    updated_dt = dt + timedelta(weeks=weeks, hours=hours)
    return updated_dt.strftime('%d.%m.%Y %H:%M:%S')


dt = datetime(2021, 11, 4, 13, 6)
print(add_time_to_datetime(dt))  # Output: 11.11.2021 01:06:00
