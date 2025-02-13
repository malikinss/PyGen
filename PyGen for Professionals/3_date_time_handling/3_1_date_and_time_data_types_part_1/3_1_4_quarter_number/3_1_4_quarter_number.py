'''
TODO:
    You have access to a dates list containing dates.

    Complete the code below to print the year and quarter number of each date
    in the given list.

    The date components must be in their original order, each on a separate
    line, in the following format:
        <year>-Q<quarter number>
'''
from datetime import date


def get_quarter(month: int) -> str:
    """
    Get the quarter of the year for a given month.

    Args:
    - month (int): The month number (1 to 12).

    Returns:
    - str: The quarter of the year ('Q1', 'Q2', 'Q3', or 'Q4').
    """
    if month in [1, 2, 3]:
        return 'Q1'
    elif month in [4, 5, 6]:
        return 'Q2'
    elif month in [7, 8, 9]:
        return 'Q3'
    else:
        return 'Q4'


def print_year_and_quarter(dates: list):
    """
    Print the year and quarter for each date in the list.

    Args:
    - dates (list): A list of date objects.
    """
    for cur_date in dates:
        quarter = get_quarter(cur_date.month)
        print(f'{cur_date.year}-{quarter}')


# List of dates
dates = [
    date(2010, 9, 28), date(2017, 1, 13),
    date(2009, 12, 25), date(2010, 2, 27),
    date(2021, 10, 11), date(2020, 3, 13),
    date(2000, 7, 7), date(1999, 4, 14),
    date(1789, 11, 19), date(2013, 8, 21),
    date(1666, 6, 6), date(1968, 5, 26)
]

# Call the function to print the result
print_year_and_quarter(dates)
