'''
TODO:
    The variable florida_hurricane_dates stores a list of dates (type date) on
    which a hurricane occurred in Florida from 1950 to 2017.

    Complete the code below to print the earliest date in the
    florida_hurricane_dates list in three different formats:
        in ISO standard (YYYY-MM-DD)
        in a typical Russian style (DD.MM.YYYY)
        in typical American style (MM/DD/YYYY)

NOTE:
    Assume that the florida_hurricane_dates variable is declared and available
    to your program.

    Assume that the date type is already imported into the program.
'''
from datetime import date
from typing import List


def print_hurricane_first_date(florida_hurricane_dates: List[date]) -> None:
    """
    Prints the earliest hurricane date in three formats:
        - ISO standard (YYYY-MM-DD)
        - Russian style (DD.MM.YYYY)
        - American style (MM/DD/YYYY)

    Args:
        florida_hurricane_dates (List[date]): List of dates on which
        hurricanes occurred in Florida.
    """
    # assign the earliest date of the hurricane to the first_date variable
    first_date = min(florida_hurricane_dates)

    # convert the date to ISO and RU format
    iso = first_date.isoformat()
    ru = first_date.strftime('%d.%m.%Y')
    us = first_date.strftime('%m/%d/%Y')

    msg_template = 'Date of first hurricane in '
    print(f'{msg_template}ISO format: {iso}')
    print(f'{msg_template}RU format: {ru}')
    print(f'{msg_template}US format: {us}')


# Example usage
florida_hurricane_dates = [
    date(1992, 8, 24), date(2000, 7, 7), date(2010, 9, 28)
]

print_hurricane_first_date(florida_hurricane_dates)
