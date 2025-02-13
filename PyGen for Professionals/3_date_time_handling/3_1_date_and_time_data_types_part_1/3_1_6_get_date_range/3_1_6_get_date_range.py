'''
TODO:
    Implement a function get_date_range() that takes two arguments in
    the following order:
        start — start date, date type
        end — end date, date type

    The get_date_range() function must return a list of dates (type date)
    from start to end inclusive.

    If start > end, the function should return an empty list.
'''
from datetime import date
from typing import List


def get_date_range(start: date, end: date) -> List[date]:
    """
    Returns a list of dates from the start date to the end date, inclusive.

    Args:
    - start (date): The start date.
    - end (date): The end date.

    Returns:
    - List[date]: A list of date objects from start to end inclusive.
      If start is greater than end, returns an empty list.
    """
    if start > end:
        return []

    start_data = start.toordinal()
    end_data = end.toordinal() + 1

    return [
        date.fromordinal(i) for i in range(start_data, end_data)
    ]


# Example usage
start_date = date(2020, 1, 1)
end_date = date(2020, 1, 5)

print(get_date_range(start_date, end_date))
# Output: [2020-01-01, 2020-01-02, 2020-01-03, 2020-01-04, 2020-01-05]
