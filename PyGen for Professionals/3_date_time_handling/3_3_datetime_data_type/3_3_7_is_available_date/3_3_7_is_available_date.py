'''
TODO:
    During the visit of the next guest, hotel staff have to check whether
    a particular date is available for booking a room.

    Implement a function is_available_date() that takes two arguments in
    the following order:
        - booked_dates - is a list of string dates that are not available
                         for booking.

        The list element is either a single date or a period (two dates
        separated by a hyphen).
        For example:
            ['04.11.2021', '05.11.2021-09.11.2021']

        - date_for_booking - a single string date or period (two dates
        separated by a hyphen) for which the guest wishes to book a room.
        For example:
            '01.11.2021' or '01.11.2021-04.11.2021'

    The is_available_date() function must return True if the date or period
    date_for_booking is fully available for booking.

    Otherwise the function must return False.

NOTE:
    It is guaranteed that in the period the left date is always less than the
    right one.

    In the period (two dates separated by a hyphen), boundary dates are
    included.
'''
from datetime import datetime, timedelta
from typing import List, Union


def convert_to_dt(given_date: str) -> datetime:
    """
    Converts a given date string (in DD.MM.YYYY format) to a datetime object.

    Args:
        given_date (str): A string representing a date in DD.MM.YYYY format.

    Returns:
        datetime: Corresponding datetime object.
    """
    return datetime.strptime(given_date, '%d.%m.%Y')


def split_date_range(date_range_str: str) -> List[datetime]:
    """
    Splits a date range string (in DD.MM.YYYY-DD.MM.YYYY format) into
    individual dates.

    Args:
        date_range_str (str): A date range string in the format:
                              'DD.MM.YYYY-DD.MM.YYYY'.

    Returns:
        List[datetime]: A list of datetime objects corresponding to each date
                        in the range.
    """
    start_date, end_date = map(convert_to_dt, date_range_str.split('-'))

    range_frame = (end_date - start_date).days + 1
    return [
        start_date + timedelta(days=i) for i in range(range_frame)
    ]


def get_range_dates_dt(dates: List[str]) -> List[datetime]:
    """
    Converts a list of date strings (single dates or ranges) into a list
    of datetime objects.

    A date range is expanded into individual dates.

    Args:
        dates (List[str]): A list of date strings in DD.MM.YYYY format or
                           ranges in DD.MM.YYYY-DD.MM.YYYY format.

    Returns:
        List[datetime]: A list of all datetime objects representing the dates.
    """
    all_dates = []

    for date_str in dates:
        if '-' in date_str:
            all_dates.extend(split_date_range(date_str))
        else:
            all_dates.append(convert_to_dt(date_str))

    return sorted(all_dates)


def is_available_date(
    booked_dates: Union[List[str], str],
    date_for_booking: Union[List[str], str]
) -> bool:
    """
    Checks if a given date or date range is available for booking based on
    a list of already booked dates.

    Args:
        booked_dates (Union[List[str], str]): A list of booked dates or
                                              a single date/range string.
        date_for_booking (Union[List[str], str]): A single date or a range to
                                                  check for availability.

    Returns:
        bool: True if the date or range is available, False otherwise.
    """
    # Convert single date/range to a list for consistency
    if isinstance(booked_dates, str):
        booked_dates = [booked_dates]
    if isinstance(date_for_booking, str):
        date_for_booking = [date_for_booking]

    # Get datetime objects for all booked dates and the requested date range
    booked_dates_dt = get_range_dates_dt(booked_dates)
    date_for_booking_dt = get_range_dates_dt(date_for_booking)

    # Check if any of the requested dates overlap with booked dates
    for booking_date in date_for_booking_dt:
        if booking_date in booked_dates_dt:
            return False  # If any date is already booked, return False

    return True  # If none of the dates are booked, return True


# Example usage
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '11.11.2021-15.11.2021'

# Expected output: True (if not overlapping)
print(is_available_date(dates, some_date))
