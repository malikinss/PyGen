'''
TODO:
    Often, different countries use different date formats.
    Let's look at some of them:
        country code    | date format
        ru              | DD.MM.YYYY
        us              | MM-DD-YYYY
        ca              | YYYY-MM-DD
        br              | DD/MM/YYYY
        fr              | DD.MM.YYYY
        pt              | DD-MM-YYYY

    Implement the date_formatter() function that takes one argument:
    country_code — country code

    The date_formatter() function must return a function that takes
    a date (date type) as an argument and returns a string with this date
    in the format of the country with the country_code code.

NOTE:
    It is guaranteed that only those country codes listed in the table
    above are passed to the date_formatter() function.
'''
from typing import Callable
from datetime import date, datetime


def date_formatter(country_code: str) -> Callable[[date], str]:
    """
    Returns a function that formats a given date according to the date format
    of the specified country code.

    Args:
        country_code (str): The country code to determine the date format.

    Returns:
        format_date (Callable[[date], str]): Function that formats the date.
    """

    # Map of country codes to their respective date formats
    date_formats = {
        'ru': '%d.%m.%Y',
        'us': '%m-%d-%Y',
        'ca': '%Y-%m-%d',
        'br': '%d/%m/%Y',
        'fr': '%d.%m.%Y',
        'pt': '%d-%m-%Y'
    }

    # Validate the provided country code
    if country_code not in date_formats:
        raise ValueError(f"Unsupported country code: {country_code}")

    def format_date(given_date: date) -> str:
        """
        Formats the given date according to the country-specific format.

        Args:
            given_date (date): The date to format.

        Returns:
            str: The formatted date string.
        """
        return datetime.strftime(given_date, date_formats[country_code])

    return format_date


# Example usage
date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))  # Output: "25.01.2022"
