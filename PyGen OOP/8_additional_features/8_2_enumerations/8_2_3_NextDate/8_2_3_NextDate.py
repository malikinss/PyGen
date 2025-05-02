'''
TODO:
    Implement a Weekday class that defines an enumeration with days of
    the week.

    The enumeration must have seven members:
        MONDAY — member with value 0
        TUESDAY — member with value 1
        WEDNESDAY — member with value 2
        THURSDAY — member with value 3
        FRIDAY — member with value 4
        SATURDAY — member with value 5
        SUNDAY — member with value 6

    Also implement a NextDate class that allows you to determine the next
    closest date that corresponds to a specified day of the week: for example,
    the date of the next Tuesday or the date of the next Friday.

    When instantiated, the class must accept three arguments in the following
    order:
        today — the current date, represented by an instance of the date class.
                Relative to this date, the next closest date corresponding
                to some day of the week should be determined
        weekday — the day of the week represented by the Weekday enumeration
                  element
        considering_today — a boolean value, defaults to False

    The considering_today parameter should determine whether the date today
    is taken into account when determining the date corresponding to the day
    of the week weekday.

    If the parameter is True, the date today should be taken into account,
    if False, it should not be taken into account.

    For example, if the day of the week of the date today is weekday and
    the considering_today parameter is True, then the date to be found
    corresponding to the day of the week weekday will be today itself.

    The NextDate class must have two instance methods:
        date() — a method that returns the next closest (relative to today)
                 date corresponding to the weekday, as an instance of the date
                 class
        days_until() — a method that returns the number of days until the next
                       closest (relative to today) date corresponding to
                       the weekday

NOTE:
    No additional data validation is required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding the implementations of the classes,
    they can be arbitrary.
'''
from enum import Enum
from datetime import date, timedelta


class Weekday(Enum):
    """
    Days of the week.
    """
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    """
    Next date for a specific weekday.
    """
    def __init__(
        self,
        today: date,
        weekday: Weekday,
        considering_today: bool = False
    ) -> None:
        """
        Init with current date and target weekday.

        Args:
            today: Current date.
            weekday: Target weekday.
            considering_today: Consider today if it matches weekday.
        """
        self.today = today
        self.weekday = weekday
        self.consider_today = considering_today

    def date(self) -> date:
        """
        Get next date for weekday.

        Returns:
            date: Next date matching weekday.
        """
        return self.today + timedelta(days=self.days_until())

    def days_until(self) -> int:
        """
        Get days until next weekday.

        Returns:
            int: Days until next matching weekday.
        """
        today_weekday = self.today.weekday()
        days = (self.weekday.value - today_weekday) % 7
        if days == 0 and not self.consider_today:
            return 7
        return days
