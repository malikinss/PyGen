'''
TODO:
    Write a program that takes a sequence of dates as input and outputs them
    in non-decreasing order.

    The input to the program is a natural number n, and then n correct dates
    in ISO format (YYYY-MM-DD), each on a separate line.

    The program should output the entered dates in non-descending order, each
    on a separate line, in the format DD/MM/YYYY.

NOTE:
    A sequence is called non-decreasing if each next member is not less than
    the previous one, for example:
        1,1,2,3,4,4,4,5,6,...

    Please note that this sequence is not increasing.
'''
from datetime import date
from typing import List


def input_dates(dates_number: int) -> List[date]:
    """
    Reads n dates in ISO format (YYYY-MM-DD) and returns them as a list.

    Args:
    dates_number: Number of dates to input.

    Returns:
    List[date]: A list of date objects.
    """
    return [
        date.fromisoformat(input("Enter a date (YYYY-MM-DD): "))
        for _ in range(dates_number)
    ]


def format_output_dates(dates: List[date]) -> List[str]:
    """
    Converts a list of dates into the DD/MM/YYYY format.

    Args:
    dates: A list of date objects.

    Returns:
    List[str]: A list of formatted date strings.
    """
    return [current_date.strftime('%d/%m/%Y') for current_date in dates]


def display_sorted_dates(dates_number: int) -> None:
    """
    Takes n dates from the user, sorts them in non-decreasing order,
    and prints them in the DD/MM/YYYY format.

    Args:
    dates_number: Number of dates to input.
    """
    given_dates = input_dates(dates_number)
    sorted_dates = sorted(given_dates)
    formatted_dates = format_output_dates(sorted_dates)

    print("\n".join(formatted_dates))


# Example function call
display_sorted_dates(3)
