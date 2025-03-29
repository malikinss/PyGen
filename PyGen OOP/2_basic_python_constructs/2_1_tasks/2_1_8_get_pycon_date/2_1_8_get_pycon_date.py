'''
TODO:
    Every month, there is a Python meetup in San Diego, which takes place on
    the fourth Thursday of the month.

    Write a program that determines the day of the next Python meetup in
    San Diego.

    The program takes two natural numbers, representing the year and month,
    each on a separate line.

    The program should determine the day of the meetup in San Diego for
    the given year and month, and print the result in the format DD.MM.YYYY.

NOTE:
    It is guaranteed that the year and month supplied are always correct.
'''
from datetime import date, timedelta

DATE_FORMAT = '%d.%m.%Y'


def get_pycon_date() -> str:
    """
    Determines the date of the fourth Thursday of the given month and year.

    The function calculates the date of the fourth Thursday for the given
    month and year and returns it in the format DD.MM.YYYY.

    Args:
        None (the function will read input from stdin).

    Returns:
        str: The date of the fourth Thursday in the format DD.MM.YYYY.
    """
    year = int(input())
    month = int(input())

    start_date = date(year, month, 1)
    weekday_of_first = start_date.weekday()

    days_to_add = (3 - weekday_of_first + 7) % 7
    days_to_add += 21

    fourth_thursday = start_date + timedelta(days=days_to_add)

    return fourth_thursday.strftime(DATE_FORMAT)


print(get_pycon_date())
