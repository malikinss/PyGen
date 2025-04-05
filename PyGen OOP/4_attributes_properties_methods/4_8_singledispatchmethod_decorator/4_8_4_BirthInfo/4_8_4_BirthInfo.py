'''
TODO:
    Implement the BirthInfo class that describes data about a birth date.

    When instantiated, the class must accept one argument:
        - birth_date — the birth date, represented as one of the following:
            1. an instance of the date class
            2. a string with the date in ISO format
            3. a list or tuple of three integers: year, month, and day

    If the birth date is invalid or represented in some other format,
    a TypeError exception must be raised with the text:
        The argument of the passed type is not supported

    An instance of the BirthInfo class must have one attribute:
        - birth_date — the birth date as an instance of the date class

    The BirthInfo class must have one property:
        - age — a read-only property that returns the current age in years,
                that is, the number of full years that have passed since
                the date of birth to the current day

NOTE:
    Age in years must be calculated in the same way as a person's normal age,
    that is, on their birthday, their age increases by one year.

    The code below:
        birthinfo = BirthInfo(date(2023, 2, 26))
        print(birthinfo.age)

    on 2024-02-25 should print:
        0
    on 2024-02-26 should print:
        1
    on 2025-02-25 should print:
        1
    on 2025-02-26 should print:
        2

    To check that the age property returns the correct age, we use our own
    function current_age(), which calculates the age in years based on
    the date of birth and the current date.

    There are no restrictions regarding the implementation of
    the BirthInfo class, it can be arbitrary.
'''
from functools import singledispatchmethod
from datetime import date
from dateutil.relativedelta import relativedelta


class BirthInfo:
    """
    A class representing birth date information.
    """
    ERR_MSG = "The argument of the passed type is not supported"

    @singledispatchmethod
    def __init__(self, birth_date: object) -> None:
        """
        Initialize BirthInfo with a birth date.

        Args:
            birth_date (object): A date object, ISO string, or list/tuple of
                                 [year, month, day].

        Raises:
            TypeError: If the birth_date type is not supported or data
                       is invalid.
        """
        raise TypeError(self.ERR_MSG)

    @__init__.register
    def _from_date(self, birth_date: date) -> None:
        """
        Initialize with a date object.

        Args:
            birth_date (date): The birth date as a date object, e.g.,
                               date(2023, 2, 26).

        Sets:
            self.birth_date: The birth date as a date object.
        """
        self.birth_date = birth_date

    @__init__.register
    def _from_iso(self, birth_date: str) -> None:
        """
        Initialize with an ISO format string.

        Args:
            birth_date (str): The birth date in ISO format, e.g., '2023-02-26'.

        Sets:
            self.birth_date: The birth date as a date object.

        Raises:
            TypeError: If the string is not a valid ISO date.
        """
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except ValueError:
            raise TypeError(self.ERR_MSG)

    @__init__.register
    def _from_list_or_tuple(self, birth_date: list | tuple) -> None:
        """
        Initialize with a list or tuple of [year, month, day].

        Args:
            birth_date (list | tuple): A sequence of three integers, e.g.,
                                       [2023, 2, 26].

        Sets:
            self.birth_date: The birth date as a date object.

        Raises:
            TypeError: If the sequence is invalid (wrong length, non-integers,
                       or invalid date).
        """
        if not isinstance(birth_date, (list, tuple)) or len(birth_date) != 3:
            raise TypeError(self.ERR_MSG)
        if not all(isinstance(x, int) for x in birth_date):
            raise TypeError(self.ERR_MSG)
        try:
            self.birth_date = date(*birth_date)
        except ValueError:
            raise TypeError(self.ERR_MSG)

    @property
    def age(self) -> int:
        """
        Get the current age in years.

        Returns:
            int: The number of full years since the birth date.
        """
        return relativedelta(date.today(), self.birth_date).years
