'''
TODO:
    Implement a Month class that describes a month.

    When instantiated, the class must accept two arguments in the following
    order:
        year — year
        month — month ordinal number

    An instance of the Month class must have the following formal string
    representation:
        Month(<year>, <month ordinal number>)

    And the following informal string representation:
        <year>-<month ordinal number>

    Also, instances of the Month class must support all comparison operations
    using the operators ==, !=, >, <, >=, <=.

    Two Month objects are considered equal if their years and month ordinal
    numbers match.

    A Month object is considered greater than another Month object if its year
    is greater.

    If two Month objects have equal years, the one with the greater month
    is considered greater.

    Methods implementing comparison operations must be able to compare both
    two Month objects with each other, and a Month object with a tuple of two
    numbers representing the year and month.

NOTE:
    If the object being compared is invalid, the method implementing this
    operation must return the NotImplemented constant.

    There are no restrictions regarding the implementation of the Month class,
    it can be arbitrary.
'''
from functools import total_ordering


@total_ordering
class Month:
    """
    A class representing a month with a year and ordinal number.
    """

    def __init__(self, year: int, month: int) -> None:
        """
        Initialize a Month instance.

        Args:
            year (int): The year.
            month (int): The month ordinal number.
        """
        self.year = year
        self.month = month

    def __repr__(self) -> str:
        """
        Return a formal string representation of the month.

        Returns:
            str: The month in format 'Month(<year>, <month>)'.
        """
        return f"Month({self.year}, {self.month})"

    def __str__(self) -> str:
        """
        Return an informal string representation of the month.

        Returns:
            str: The month in format '<year>-<month>'.
        """
        return f"{self.year}-{self.month}"

    def __eq__(self, value: object) -> bool:
        """
        Compare the month with another month or tuple for equality.

        Args:
            value (object): The object to compare with (Month or tuple).

        Returns:
            bool: True if year and month match, False otherwise.
            NotImplemented: If the comparison is not supported.
        """
        if isinstance(value, Month):
            return self.year == value.year and self.month == value.month
        if isinstance(value, tuple) and len(value) == 2:
            return self.year == value[0] and self.month == value[1]
        return NotImplemented

    def __gt__(self, value: object) -> bool:
        """
        Compare the month with another month or tuple for greater-than.

        Args:
            value (object): The object to compare with (Month or tuple).

        Returns:
            bool: True if greater (by year, then month), False otherwise.
            NotImplemented: If the comparison is not supported.
        """
        if isinstance(value, Month):
            if self.year == value.year:
                return self.month > value.month
            return self.year > value.year
        if isinstance(value, tuple) and len(value) == 2:
            if self.year == value[0]:
                return self.month > value[1]
            return self.year > value[0]
        return NotImplemented
