'''
TODO:
    Implement a get_min_max() function that takes one argument:
        dates — list of dates (date type)

    The function must return a tuple whose first element is the minimum date
    from the dates list, and the second element is the maximum date from the
    dates list.

    If the dates list is empty, the function should return an empty tuple.
'''
from typing import List, Tuple
from datetime import date


def get_min_max(dates: List[date]) -> Tuple[date, date]:
    """
    Returns the minimum and maximum dates from the given list of dates.

    Args:
    - dates (List[date]): A list of date objects.

    Returns:
    - Tuple[date, date]: A tuple where the first element is the earliest
      date, and the second element is the latest date. If the list is empty,
      returns an empty tuple.
    """
    result: tuple = ()

    if dates:
        result = min(dates), max(dates)

    return result


# Example usage
dates = [
    date(2021, 10, 11), date(2020, 3, 13),
    date(2000, 7, 7), date(1999, 4, 14),
    date(2013, 8, 21)
]

print(get_min_max(dates))  # Output: (1999-04-14, 2021-10-11)
