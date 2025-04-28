'''
TODO:
    Implement a USADate class that represents a date in the American format.

    When instantiated, the class must accept three arguments in the following
    order:
        year — year
        month — month
        day — day

    The USADate class must have two instance methods:
        format() — method that returns a string representing a date in
                   the MM-DD-YYYY format
        iso_format() — method that returns a string representing a date in
                       the YYYY-MM-DD format

    Also implement an ItalianDate class that represents a date in the Italian
    format, with a constructor that accepts three arguments:
        year — year
        month — month
        day — day

    The ItalianDate class must have two instance methods:
        format() — method that returns a string representing a date in
                   the DD/MM/YYYY format
        iso_format() — method that returns a string representing a date in
                       the YYYY-MM-DD format

NOTE:
    No additional validation of the data is required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding the implementation of classes, they
    can be arbitrary.
'''
from abc import ABC, abstractmethod
from datetime import date


class AnyDate(ABC):
    """
    Abstract base class for date representations.
    """

    def __init__(self, year: int, month: int, day: int) -> None:
        """
        Initialize with year, month, and day.

        Args:
            year: Year of the date.
            month: Month of the date.
            day: Day of the date.
        """
        self.date = date(year, month, day)

    @abstractmethod
    def format(self) -> str:
        """
        Return a formatted date string.

        Returns:
            str: Date in a specific format.
        """
        pass

    def iso_format(self) -> str:
        """
        Return the date in ISO format (YYYY-MM-DD).

        Returns:
            str: Date in YYYY-MM-DD format.
        """
        return self.date.isoformat()


class USADate(AnyDate):
    """
    Class for dates in American format (MM-DD-YYYY).
    """
    def format(self) -> str:
        """
        Return the date in MM-DD-YYYY format.

        Returns:
            str: Date in MM-DD-YYYY format.
        """
        return self.date.strftime("%m-%d-%Y")


class ItalianDate(AnyDate):
    """
    Class for dates in Italian format (DD/MM/YYYY).
    """
    def format(self) -> str:
        """
        Return the date in DD/MM/YYYY format.

        Returns:
            str: Date in DD/MM/YYYY format.
        """
        return self.date.strftime("%d/%m/%Y")
