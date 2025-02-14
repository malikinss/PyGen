'''
TODO:
    The store's operating hours are given.

    Write a program that takes the current date and time as input and
    determines the number of minutes remaining until the store closes.

    The program input is the current date and time in the format:
        DD.MM.YYYY HH:MM

    The program should display the number of minutes remaining until the store
    closes, or the text “The store is closed” if it is closed.
'''

from datetime import datetime, time
from typing import Tuple, Optional

TIME_FORMAT = '%H:%M'
DATETIME_FORMAT = '%d.%m.%Y %H:%M'

OPERATING_HOURS = {
    'Monday': ('09:00', '21:00'),
    'Tuesday': ('09:00', '21:00'),
    'Wednesday': ('09:00', '21:00'),
    'Thursday': ('09:00', '21:00'),
    'Friday': ('09:00', '21:00'),
    'Saturday': ('10:00', '18:00'),
    'Sunday': ('10:00', '18:00')
}


def parse_datetime(datetime_string: str) -> datetime:
    """
    Parses a datetime string into a datetime object.

    Args:
        datetime_string (str): Date and time in the format 'DD.MM.YYYY HH:MM'.

    Returns:
        datetime: Parsed datetime object.

    Raises:
        ValueError: If the format is incorrect.
    """
    try:
        return datetime.strptime(datetime_string, DATETIME_FORMAT)
    except ValueError:
        raise ValueError(
            'Invalid datetime format. Please use DD.MM.YYYY HH:MM'
        )


def get_operating_hours(date_obj: datetime) -> Optional[Tuple[time, time]]:
    """
    Retrieves the store's operating hours for a given date.

    Args:
        date_obj (datetime): The date for which to get the operating hours.

    Returns:
        Optional[Tuple[time, time]]: A tuple with opening and closing times,
                                     or None if the store is closed.
    """
    weekday = date_obj.strftime('%A')
    if weekday not in OPERATING_HOURS:
        return None

    open_str, close_str = OPERATING_HOURS[weekday]
    return (
        datetime.strptime(open_str, TIME_FORMAT).time(),
        datetime.strptime(close_str, TIME_FORMAT).time()
    )


def minutes_until_closing(current_dt: datetime, closing_time: time) -> int:
    """
    Calculates the number of minutes until the store closes.

    Args:
        current_dt (datetime): The current date and time.
        closing_time (time): The store's closing time.

    Returns:
        int: Minutes remaining until the store closes.
    """
    closing_dt = datetime.combine(current_dt.date(), closing_time)
    return max(0, (closing_dt - current_dt).seconds // 60)


def display_minutes_until_closing(datetime_string: str) -> None:
    """
    Prints the minutes remaining until the store closes or a message if it's
    closed.

    Args:
        datetime_string (str): The input date and time string.
    """
    current_dt = parse_datetime(datetime_string)
    operating_hours = get_operating_hours(current_dt)

    if operating_hours is None:
        print('The store is closed')
        return

    opening_time, closing_time = operating_hours
    if opening_time <= current_dt.time() < closing_time:
        print(minutes_until_closing(current_dt, closing_time))
    else:
        print('The store is closed')


# Example usage:
datetime_string = input()
display_minutes_until_closing(datetime_string)
