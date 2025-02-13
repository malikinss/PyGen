'''
TODO:
    Write a function that takes two dates as input and outputs the smaller one.

    The function receives two correct dates in ISO format (YYYY-MM-DD), each
    on a separate line.

    The function must select the smaller of the two entered dates and display
    it in DD-MM (YYYY) format.

'''
from datetime import date
from typing import List


def get_min_date(dates: List[date]) -> date:
    """
    Given a list of dates, returns the smallest (earliest) date.

    Args:
    dates: List of date objects to compare.

    Returns:
    The smallest date in the list.
    """
    return min(dates)


def input_dates(dates_number: int) -> List[date]:
    """
    Reads a specified number of dates in ISO format from user input.

    Args:
    dates_number: The number of dates to input.

    Returns:
    A list of date objects based on the input.
    """
    return [
        date.fromisoformat(input("Enter a date in YYYY-MM-DD format: "))
        for _ in range(dates_number)
    ]


def select_min_date(dates_number: int) -> None:
    """
    Receives two dates in ISO format, selects the smaller one, and prints it
    in DD-MM (YYYY) format.

    Args:
    dates_number: The number of dates to input.
    """
    given_dates = input_dates(dates_number)
    min_date = get_min_date(given_dates)
    print(min_date.strftime('%d-%m (%Y)'))


# Example usage
select_min_date(2)  # Call the function for two date inputs
