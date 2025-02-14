'''
TODO:
    Implement a function num_of_sundays() that takes one argument as input:
        year — natural number, year

    The function should return the number of Sundays in the year year.
'''
from datetime import date, timedelta


def num_of_sundays(year: int) -> int:
    """
    Calculate the number of Sundays in a given year.

    Args:
        year (int): The year to count Sundays for.

    Returns:
        int: The number of Sundays in the given year.
    """
    first_day = date(year, 1, 1)
    first_sunday = first_day + timedelta(days=(6 - first_day.weekday()) % 7)
    last_day = date(year, 12, 31)

    return (last_day - first_sunday).days // 7 + 1


# Example usage
print(num_of_sundays(2024))
