'''
TODO:
    A list of employees of the organization is given, which indicates their
    last names, given names and dates of birth.

    Write a program that determines which date has the most employees born.

    The input to the program in the first line is a natural number n - the
    number of employees working in the organization.

    In the next n lines, data about each employee is entered: first name, last
    name and date of birth, separated by a space.

    Date of birth is indicated in the format DD.MM.YYYY.

    The program should output the date on which the largest number of
    employees celebrate their birthdays, in the format DD.MM.YYYY.

    If there are several such dates, the program should display them all in
    ascending order, each on a separate line, in the same format.
'''
from collections import Counter
from datetime import datetime, date
from typing import List


DATE_FORMAT = '%d.%m.%Y'


def parse_date(date_string: str) -> date:
    """
    Parses a date string into a date object.

    Args:
        date_string (str): The date string in the format 'DD.MM.YYYY'.

    Returns:
        date: Parsed date object.

    Raises:
        ValueError: If the format is incorrect.
    """
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError('Invalid date format. Please use DD.MM.YYYY')


def collect_birth_dates(num_employees: int) -> Counter:
    """
    Reads employee data and counts occurrences of each birth date.

    Args:
        num_employees (int): The number of employees.

    Returns:
        Counter: A dictionary-like object where keys are birth dates and
                 values are their occurrences.
    """
    birth_dates = [
        parse_date(input().split()[2]) for _ in range(num_employees)
    ]
    return Counter(birth_dates)


def get_most_common_birthdays(dates_count: Counter) -> List[date]:
    """
    Finds the most common birth dates.

    Args:
        dates_count (Counter): Counter object mapping birth dates
                               to occurrence count.

    Returns:
        List[date]: List of the most common birth dates, sorted
                             in ascending order.
    """
    max_occurrence = max(dates_count.values(), default=0)
    return sorted(
        date for date, count in dates_count.items() if count == max_occurrence
    )


def display_dates(dates: List[date]) -> None:
    """
    Prints a list of dates in the required format.

    Args:
        dates (List[date): List of dates to print.
    """
    for some_date in dates:
        print(some_date.strftime(DATE_FORMAT))


num_employees = int(input())
birth_date_counts = collect_birth_dates(num_employees)
most_common_birthdays = get_most_common_birthdays(birth_date_counts)
display_dates(most_common_birthdays)
