'''
TODO:
    Implement a MinStat class that describes an object that finds the minimum
    value among a given set of numbers.

    When instantiated, the class must accept one argument:
        iterable — an iterable that defines the initial set of numbers.
                   If not passed, the initial set is considered empty

    The MinStat class must have three instance methods:
        add() — a method that takes a number as an argument and adds it to
                the set
        result() — a method that returns the minimum number from the set.
                   If the set is empty, the method must return None
        clear() — a method that removes all numbers from the set

    Also implement a MaxStat class that describes an object that finds
    the maximum value among a given set of numbers.

    When instantiated, the class must accept one argument:
        iterable — an iterable that defines the initial set of numbers.
                   If not passed, the initial set is considered empty

    The MaxStat class must have three instance methods:
        add() — a method that takes a number as an argument and adds it to
                the set
        result() — a method that returns the maximum number in the set.
                   If the set is empty, the method must return None
        clear() — a method that removes all numbers from the set

    Finally, implement the AverageStat class, which describes an object that
    finds the average of a given set of numbers.

    When instantiated, the class must take one argument:
        iterable — an iterable that defines the initial set of numbers.
                   If not passed, the initial set is considered empty

    The AverageStat class must have three instance methods:
        add() — a method that takes a number as an argument and adds it to
                the set
        result() — a method that returns the average of the set of numbers.
                   If the set is empty, the method must return None
        clear() — a method that removes all numbers from the set

NOTE:
    No additional validation of the data is required.

    It is guaranteed that the implemented classes are used only with correct
    data.

    There are no restrictions regarding the implementation of classes,
    they can be arbitrary.
'''
from abc import ABC
from collections.abc import Iterable
from numbers import Number
from statistics import fmean


class Stat(ABC):
    """
    Abstract base class for statistical operations on a set of numbers.
    """

    def __init__(self, iterable: Iterable[Number] = ()) -> None:
        """
        Initialize with an optional iterable of numbers.

        Args:
            iterable: Initial set of numbers, defaults to empty.
        """
        self._numbers = list(iterable)

    def add(self, num: Number) -> None:
        """
        Add a number to the set.

        Args:
            num: Number to add.
        """
        self._numbers.append(num)

    def result(self, action) -> float | None:
        """
        Return the statistical result.

        Returns:
            float | None: Statistical value or None if the set is empty.
        """
        return action(self._numbers) if self._numbers else None

    def clear(self) -> None:
        """
        Remove all numbers from the set.
        """
        self._numbers.clear()


class MinStat(Stat):
    """
    Class to find the minimum value in a set of numbers.
    """

    def result(self) -> float | None:
        """
        Return the minimum number in the set.

        Returns:
            float | None: Minimum value or None if the set is empty.
        """
        return super().result(min)


class MaxStat(Stat):
    """
    Class to find the maximum value in a set of numbers.
    """

    def result(self) -> float | None:
        """
        Return the maximum number in the set.

        Returns:
            float | None: Maximum value or None if the set is empty.
        """
        return super().result(max)


class AverageStat(Stat):
    """
    Class to find the average value in a set of numbers.
    """

    def result(self) -> float | None:
        """
        Return the average of the numbers in the set.

        Returns:
            float | None: Average value or None if the set is empty.
        """
        return super().result(fmean)
