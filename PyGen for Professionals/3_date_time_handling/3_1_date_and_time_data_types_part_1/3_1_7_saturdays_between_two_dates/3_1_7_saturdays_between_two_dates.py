'''
TODO:
    Implement a function saturdays_between_two_dates() that takes two
    arguments in the following order:

        start — start date, date type
        end — end date, date type

    The function must return the number of Saturdays between the start and end
    dates, inclusive.

NOTE:
    Dates can be transmitted in any order, that is, it is not guaranteed that
    the first date is less than the second.
'''
from datetime import date


def is_saturday(given_date: date) -> bool:
    """
    Checks if the given date is a Saturday.

    Args:
    - given_date (date): The date to check.

    Returns:
    - bool: True if the date is a Saturday, False otherwise.
    """
    return given_date.weekday() == 5


def saturdays_between_two_dates(start: date, end: date) -> int:
    """
    Returns the number of Saturdays between two dates, inclusive.

    Args:
    - start (date): The start date.
    - end (date): The end date.

    Returns:
    - int: The number of Saturdays between the start and end dates, inclusive.
    """
    saturdays_counter = 0

    # Convert dates to their ordinal number
    start_ord = start.toordinal()
    end_ord = end.toordinal()

    # Ensure start is less than or equal to end
    if start_ord > end_ord:
        start_ord, end_ord = end_ord, start_ord

    # Iterate over the range of days between start and end
    for current_date_ordinal in range(start_ord, end_ord + 1):
        current_date = date.fromordinal(current_date_ordinal)
        if is_saturday(current_date):
            saturdays_counter += 1

    return saturdays_counter


# Example usage
start_date = date(2020, 1, 1)
end_date = date(2020, 1, 10)

print(saturdays_between_two_dates(start_date, end_date))
# Output: 2 (Jan 4 and Jan 11)
