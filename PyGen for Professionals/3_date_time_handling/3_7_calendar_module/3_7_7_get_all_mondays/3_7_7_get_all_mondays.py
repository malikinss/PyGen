'''
TODO:
    Implement a function get_all_mondays() that takes one argument:
        year — natural number

    The function should return a list, sorted in ascending order, of all
    dates (type date) in the year year that fall on Monday.
'''
import calendar
from datetime import date


def get_all_weekdays_in_year(year: int, target_weekday: int) -> list:
    """
    Returns a list of all dates in the given year that fall on the specified
    weekday.

    Args:
        year (int): The year to check.
        target_weekday (int): The weekday to find (0 for Monday,
                              1 for Tuesday, etc.).

    Returns:
        list: A sorted list of all dates in the given year that fall on the
              target weekday.
    """
    weekdays = []

    # Iterate through all months
    for month in range(1, 13):
        # Get the number of days in the month
        _, num_days = calendar.monthrange(year, month)

        # Check every day in the month
        for day in range(1, num_days + 1):
            current_date = date(year, month, day)

            # 0 is Monday, 1 is Tuesday, etc.
            if current_date.weekday() == target_weekday:
                weekdays.append(current_date)

    return weekdays


def get_all_mondays(year: int) -> list:
    """
    Retrieves all the Mondays of the specified year.

    This function returns a sorted list of `date` objects that correspond to
    each Monday within the given year.

    Args:
        year (int): The year for which Mondays are to be retrieved.

    Returns:
        list: A list of `date` objects, each representing a Monday in the
              specified year, sorted in ascending order.
    """
    return get_all_weekdays_in_year(year, 0)


# Example usage
mondays = get_all_mondays(2021)
print(*mondays, sep='\n')
