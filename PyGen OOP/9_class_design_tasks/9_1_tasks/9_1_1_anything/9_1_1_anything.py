'''
TODO:
    Implement a function anything() that returns an object such that
    the result of comparison with it using the operators ==, !=, >, <, >=,
    and <= is always True.
'''
from typing import Any


def anything() -> 'Anything':
    """
    Return an object where all comparisons yield True.
    """
    return Anything()


class Anything:
    """
    A class where all comparison operations return True.
    """
    def __eq__(self, other: Any) -> bool:
        """
        Return True for equality comparison.
        """
        return True

    def __ne__(self, other: Any) -> bool:
        """
        Return True for inequality comparison.
        """
        return True

    def __gt__(self, other: Any) -> bool:
        """
        Return True for greater-than comparison.
        """
        return True

    def __ge__(self, other: Any) -> bool:
        """
        Return True for greater-or-equal comparison.
        """
        return True

    def __lt__(self, other: Any) -> bool:
        """
        Return True for less-than comparison.
        """
        return True

    def __le__(self, other: Any) -> bool:
        """
        Return True for less-or-equal comparison.
        """
        return True
