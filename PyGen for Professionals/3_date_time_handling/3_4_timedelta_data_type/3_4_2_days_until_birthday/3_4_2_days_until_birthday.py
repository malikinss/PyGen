'''
TODO:
    Complete the code below to print the number of days (integer) between
    the dates today and birthday.
'''
from datetime import date


def days_between_dates(start_date: date, end_date: date) -> int:
    """
    Calculates the absolute difference in days between two dates.

    Args:
        start_date (date): The first date.
        end_date (date): The second date.

    Returns:
        int: The number of days between the two dates.
    """
    return abs((start_date - end_date).days)


# Example usage
today = date(2000, 1, 1)
birthday = date(2075, 1, 1)
print(days_between_dates(today, birthday))  # Output: 336
