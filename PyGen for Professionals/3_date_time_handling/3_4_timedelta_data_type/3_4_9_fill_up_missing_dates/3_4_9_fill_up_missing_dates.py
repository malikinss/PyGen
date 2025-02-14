'''
TODO:
    Implement a function fill_up_missing_dates() that takes one argument as
    input:
        dates — list of string dates in DD.MM.YYYY format

    The function should return a list containing all the dates in the dates
    list, in ascending order, plus any missing dates in between.

NOTE:
    Let's look at the first test. The dates list contains the period from
    01.11.2021 to 07.11.2021
        dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
    missing dates 02.11.2021, 05.11.2021, 06.11.2021.
    Then the function call:
        fill_up_missing_dates(dates)
    should return a list:
        [
            '01.11.2021', '02.11.2021', '03.11.2021',
            '04.11.2021', '05.11.2021', '06.11.2021',
            '07.11.2021'
        ]

    The function should create and return a new list, and not modify
    the passed one.

'''
from datetime import datetime, timedelta
from typing import List

DATE_FORMAT = '%d.%m.%Y'


def convert_to_datetime(date_str: str) -> datetime:
    """
    Convert a string date to a datetime object.

    Args:
        date_str (str): Date string in DD.MM.YYYY format.

    Returns:
        datetime: Corresponding datetime object.
    """
    try:
        return datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        raise ValueError(
            "Invalid date format. Please use the format DD.MM.YYYY"
        )


def fill_up_missing_dates(dates: List[str]) -> List[str]:
    """
    Fill up missing dates between the given dates in the list and return them
    in ascending order.

    Args:
        dates (List[str]): List of date strings in DD.MM.YYYY format.

    Returns:
        List[str]: List of all dates including missing dates in ascending
                   order.
    """
    if not dates:
        return []

    # Convert all dates to datetime objects and sort
    sorted_dates = sorted(convert_to_datetime(date) for date in dates)

    # Create a list of dates between the min and max date
    start_date = sorted_dates[0]
    end_date = sorted_dates[-1]

    # Generate all dates in the range
    all_dates = [
        start_date + timedelta(days=i)
        for i in range((end_date - start_date).days + 1)
    ]

    # Convert datetime objects back to string and return the list
    return [date.strftime(DATE_FORMAT) for date in all_dates]


# Example usage
dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))
