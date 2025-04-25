'''
TODO:
    Implement a 'BirthdayDict' class, a subclass of 'UserDict', that describes
    a dictionary with birthday information, where the keys are names and
    the values are birthday dates.

    The process of creating an instance of the 'BirthdayDict' class must
    coincide with the process of creating an instance of the 'UserDict' class.

    When adding a new key: value pair to an instance of the 'BirthdayDict'
    class, a check must be performed to see if there is a pair in this
    instance that has the same value as the pair being added.

    And if such a pair exists, the text must be displayed:
        Hey, <key of the pair being added>, you're not the only one
        celebrating a birthday on this day!

    Similar behavior must be observed when changing the value by key.

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of
    the 'BirthdayDict' class, it can be arbitrary.
'''
from collections import UserDict
from typing import Any


class BirthdayDict(UserDict):
    """
    Dictionary storing names and birthdays with duplicate value notifications.

    Inherits from UserDict, printing a message when a duplicate birthday
    is added.
    """

    _MSG = "Hey, {}, you aren't the only one celebrating a bday on this day!"

    def _check_value(self, key: Any, value: Any) -> None:
        """
        Check if value exists for another key and print message if found.

        Args:
            key: Key being added or updated.
            value: Birthday value to check.
        """
        if any(k != key and v == value for k, v in self.data.items()):
            print(self._MSG.format(key))

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize with dictionary-like arguments, checking for duplicate
        birthdays.

        Args:
            *args: Positional arguments
                   (e.g., dict or iterable of key-value pairs).
            **kwargs: Keyword arguments as key-value pairs.
        """
        super().__init__(*args, **kwargs)
        for k, v in self.data.items():
            self._check_value(k, v)

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Set key-value pair, checking for duplicate birthdays.

        Args:
            key: Name to set.
            value: Birthday value to set.
        """
        self._check_value(key, value)
        self.data[key] = value

    def update(self, *args: Any, **kwargs: Any) -> None:
        """
        Update dictionary, checking for duplicate birthdays.

        Args:
            *args: Positional arguments
                   (e.g., dict or iterable of key-value pairs).
            **kwargs: Keyword arguments as key-value pairs.
        """
        temp = dict(*args, **kwargs)
        for k, v in temp.items():
            self._check_value(k, v)
        super().update(*args, **kwargs)
