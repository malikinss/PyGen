'''
TODO:
    Different countries often use different date formats.

    Let's look at some of them:
        country code    date format
            ru          DD.MM.YYYY
            us          MM-DD-YYYY
            ca          YYYY-MM-DD
            br          DD/MM/YYYY
            fr          DD.MM.YYYY
            pt          DD-MM-YYYY

    Implement the DateFormatter class, instances of which allow you to convert
    dates to the format of a specific country from the table above.

    When creating an instance, the class must accept one argument:
        country_code — country code

    An instance of the DateFormatter class must be a callable object
    and accept one argument:
        d — date (date type)

    An instance of the DateFormatter class must return a string with
    the date d in the format of the country with the country_code code.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the DateFormatter class, it can be arbitrary.
'''
from datetime import date


class DateFormatter:
    """
    A class for formatting dates according to a specific country's format.
    """

    _FORMATS = {
        'ru': '%d.%m.%Y',  # DD.MM.YYYY
        'us': '%m-%d-%Y',  # MM-DD-YYYY
        'ca': '%Y-%m-%d',  # YYYY-MM-DD
        'br': '%d/%m/%Y',  # DD/MM/YYYY
        'fr': '%d.%m.%Y',  # DD.MM.YYYY
        'pt': '%d-%m-%Y',  # DD-MM-YYYY
    }

    def __init__(self, country_code: str) -> None:
        """
        Initialize DateFormatter with a country code.

        Args:
            country_code (str): Country code determining the date
                                format (e.g., 'ru', 'us').
        """
        self.country_code = country_code
        self._format = self._FORMATS[country_code]

    def __call__(self, d: date) -> str:
        """
        Format a date according to the country's format.

        Args:
            d (date): The date object to format.

        Returns:
            str: The formatted date string (e.g., '25.12.2023' for 'ru').
        """
        return d.strftime(self._format)
