'''
TODO:
    Implement a Time class that represents the time on a digital clock.

    When instantiated, the class must take two arguments in the following
    order:
        - hours — the number of hours; every 24 hours must be converted
                  to 0 hours
        - minutes — the number of minutes; every 60 minutes should be
                    converted to 1 hour

    An instance of the Time class should have the following informal string
    representation:
        <number of hours in HH format>:<number of minutes in MM format>

    Also, instances of the Time class should support the operation of addition
    between themselves using the + and += operators:
        - the result of addition using the + operator should be a new instance
          of the Time class, the number of hours of which is equal to the sum
          of the hours of the original instances of the Time class, the number
          of minutes is equal to the sum of the minutes of the original
          instances of the Time class
        - the result of addition using the += operator should be a left
          instance of the Time class, the number of hours of which is
          increased by the number of hours of the right instance of the Time
          class, the number of minutes is increased by the number of minutes
          of the right instance of the Time class

NOTE:
    If the object with which the arithmetic operation is performed is
    incorrect, the method implementing this operation should return
    the NotImplemented constant.

    There are no restrictions regarding the implementation of the Time class,
    it can be arbitrary.
'''
from typing import Union


def get_total_minutes(obj: 'Time') -> int:
    """
    Calculate total minutes from a Time instance.

    Args:
        obj (Time): Time instance to convert to minutes.

    Returns:
        int: Total number of minutes (hours * 60 + minutes).
    """
    return obj.hours * 60 + obj.minutes


class Time:
    """
    A class representing time on a digital clock.
    """
    def __init__(self, hours: int, minutes: int) -> None:
        """
        Initialize Time with hours and minutes, normalizing to 24-hour format.

        Args:
            hours (int): Number of hours (every 24 hours converts to 0).
            minutes (int): Number of minutes (every 60 minutes converts
                           to 1 hour).
        """
        total_minutes = (hours * 60 + minutes)
        self.hours = (total_minutes // 60) % 24
        self.minutes = total_minutes % 60

    def __str__(self) -> str:
        """
        Informal string representation of the Time.

        Returns:
            str: Time in 'HH:MM' format with leading zeros.
        """
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __add__(self, other: 'Time') -> Union['Time', NotImplemented]:
        """
        Add two Time instances.

        Args:
            other (Time): Another Time instance to add.

        Returns:
            Time: New instance with summed and normalized time.
            NotImplemented: If other is not a Time instance.
        """
        if isinstance(other, Time):
            total_minutes = (
                get_total_minutes(self) + get_total_minutes(other)
            )
            return Time(total_minutes // 60, total_minutes % 60)
        return NotImplemented

    def __iadd__(self, other: 'Time') -> Union['Time', NotImplemented]:
        """
        In-place addition of another Time instance.

        Args:
            other (Time): Another Time instance to add.

        Returns:
            Time: Self with updated and normalized time.
            NotImplemented: If other is not a Time instance.
        """
        if isinstance(other, Time):
            total_minutes = (
                get_total_minutes(self) + get_total_minutes(other)
            )
            self.hours = (total_minutes // 60) % 24
            self.minutes = total_minutes % 60
            return self
        return NotImplemented
