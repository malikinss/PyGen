'''
TODO:
    In many museums, there is one day of the month when visiting the museum
    for all persons or certain categories of citizens occurs without charging
    a fee.

    For example, in the Hermitage it is the third Thursday of the month.

    Write a program that determines the dates of free days to visit the
    Hermitage in a given year.
'''
import calendar
from datetime import datetime, date

DATE_FORMAT = '%Y-%m-%d'
DATE_FORMAT_2 = '%d.%m.%Y'
ENG_MONTH_NAMES = list(calendar.month_name)


def parse_date(date_string: str) -> date:
    """
    Converts a string in the format 'YYYY-MM-DD' to a date object.

    Args:
        date_string (str): The date in 'YYYY-MM-DD' format.

    Returns:
        date: The corresponding datetime.date object.

    Raises:
        ValueError: If the input string is not in the correct format.
    """
    try:
        return datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        raise ValueError(
            'Invalid datetime format. Please use the format YYYY-MM-DD.'
        )


def get_number_of_month_by_name(month_name: str) -> int:
    """
    Retrieves the month number corresponding to the given month name.

    Args:
        month_name (str): The full name of the month (e.g., 'January').

    Returns:
        int: The number of the month (1 for January, 2 for February, etc.).
    """
    return ENG_MONTH_NAMES.index(month_name)


def get_number_of_days_in_month(year: int, month: int) -> int:
    """
    Returns the number of days in a specific month of a given year.

    Args:
        year (int): The year (e.g., 2021).
        month (int): The month number (1-12).

    Returns:
        int: The number of days in the month (e.g., 28, 30, or 31).
    """
    _, number_of_days = calendar.monthrange(year, month)
    return number_of_days


def get_days_in_month(year: int, month: int) -> list:
    """
    Generates a list of all dates in a specific month of a given year.

    Args:
        year (int): The year (e.g., 2021).
        month (int): The month number (1-12).

    Returns:
        list: A list of datetime.date objects representing each date in
              the month.
    """
    days_number = get_number_of_days_in_month(year, month)
    result_list = []

    for day_num in range(1, days_number + 1):
        combined_date = f"{year:04d}-{month:02d}-{day_num:02d}"
        cur_date = parse_date(combined_date)
        result_list.append(cur_date)

    return result_list


def filter_dates_by_weekday_in_month(
    year: int, month: int, target_weekday: int
) -> list:
    """
    Filters out all dates in a specific month of a year that match the target
    weekday.

    Args:
        year (int): The year (e.g., 2021).
        month (int): The month number (1-12).
        target_weekday (int): The target weekday (0 for Monday, 1 for Tuesday,
                              ..., 6 for Sunday).

    Returns:
        list: A list of datetime.date objects that fall on the target weekday.
    """
    result = []
    cur_month_dates = get_days_in_month(year, month)

    for cur_date in cur_month_dates:
        cur_date_weekday = calendar.weekday(
            cur_date.year, cur_date.month, cur_date.day
        )
        if cur_date_weekday == target_weekday:
            result.append(cur_date)

    return result


def get_third_thursday_per_month(year: int, month_name: str) -> date:
    """
    Returns the third Thursday of a specific month in a given year.

    Args:
        year (int): The year (e.g., 2021).
        month_name (str): The full name of the month (e.g., 'January').

    Returns:
        date: The date of the third Thursday of the month.

    Raises:
        IndexError: If the third Thursday does not exist in the month.
    """
    thursdays = filter_dates_by_weekday_in_month(
        year,
        get_number_of_month_by_name(month_name),
        calendar.THURSDAY
    )
    return thursdays[2]


def get_all_third_thursdays(year: int) -> list:
    """
    Retrieves the third Thursday of each month in a given year.

    Args:
        year (int): The year (e.g., 2021).

    Returns:
        list: A list of string representations of the third Thursdays in each
              month, formatted as 'DD.MM.YYYY'.
    """
    result = []

    for month_name in ENG_MONTH_NAMES:
        if month_name == '':
            continue

        try:
            third_thursday = get_third_thursday_per_month(year, month_name)
            result.append(third_thursday.strftime(DATE_FORMAT_2))
        except IndexError:
            continue

    return result


# Example usage
thursdays = get_all_third_thursdays(2021)
print(*thursdays, sep='\n')
