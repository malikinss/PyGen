'''
TODO:
    Implement a generator function years_days() that takes one argument:
        year — a natural number

    The function should return a generator that produces a sequence of all
    dates (type date) in the year year.

NOTE:
    Let's take the year 2022 as an example.

    January of this year has 31 days, February has 28, March has 31, and so on.

    Then the generator obtained by calling years_days(2022) should first
    produce all dates from January 1 to January 31, then from
    February 1 to February 28, and so on until December 31.
'''
from datetime import date, timedelta
from typing import Generator


def years_days(year: int) -> Generator[date, None, None]:
    """
    Generates all the dates in the specified year.

    Args:
        year (int): A natural number representing the year.

    Yields:
        date: All dates in the given year, starting from January 1st
        to December 31st.
    """
    current_date = date(year, 1, 1)
    end_date = date(year, 12, 31)

    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)
