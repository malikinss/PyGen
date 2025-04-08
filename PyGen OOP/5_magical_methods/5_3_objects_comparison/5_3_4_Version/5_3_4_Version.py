'''
TODO:
    Implement a Version class that describes a version of software.

    When instantiated, the class must accept one argument:
        version — a string of three integers separated by periods that
                  describe the software version.

    For example, 2.8.1. If one of the numbers is omitted, it is assumed to
    be zero.

    For example, version 2 is equivalent to version 2.0.0, and version 2.8
    is equivalent to version 2.8.0

    An instance of the Version class must have the following formal string
    representation:
        Version('<software version as three integers separated by periods>')

    And the following informal string representation:
        <software version as three integers separated by periods>

    Also, instances of the Version class must support all comparison
    operations between themselves using the ==, !=, >, <, >=, <= operators.

    Two Version objects are considered equal if all three numbers in their
    versions match.

    A Version object is considered greater than another Version object if
    the first number in its version is greater.

    Or if the second number in its version is greater, if the first numbers
    are the same.

    Or if the third number in its version is greater, if the first and second
    numbers are the same.

NOTE:
    If the object being compared is invalid, the method implementing
    the operation must return the NotImplemented constant.

    There are no restrictions on the implementation of the Version class,
    it can be arbitrary.
'''
from functools import total_ordering


@total_ordering
class Version:
    """
    A class representing a software version with three numbers."""

    def __init__(self, version: str) -> None:
        """
        Initialize a Version instance.

        Args:
            version (str): A string of three integers separated by periods
                           (e.g., '2.8.1').
                           Missing numbers are assumed to be zero.
        """
        parts = version.split('.')
        while len(parts) < 3:
            parts.append('0')
        self.numbers = tuple(int(part) for part in parts[:3])
        self.version_str = '.'.join(str(num) for num in self.numbers)

    def __repr__(self) -> str:
        """
        Return a formal string representation of the version.

        Returns:
            str: The version in format "Version('<x.y.z>')".
        """
        return f"Version('{self.version_str}')"

    def __str__(self) -> str:
        """
        Return an informal string representation of the version.

        Returns:
            str: The version as 'x.y.z'.
        """
        return self.version_str

    def __eq__(self, value: object) -> bool:
        """
        Compare the version with another version for equality.

        Args:
            value (object): The object to compare with
                            (expected to be Version).

        Returns:
            bool: True if all three numbers match, False otherwise.
            NotImplemented: If the comparison is not supported.
        """
        if isinstance(value, Version):
            return self.numbers == value.numbers
        return NotImplemented

    def __gt__(self, value: object) -> bool:
        """
        Compare the version with another version for greater-than.

        Args:
            value (object): The object to compare with
                            (expected to be Version).

        Returns:
            bool: True if greater (by first, then second, then third number),
                  False otherwise.
            NotImplemented: If the comparison is not supported.
        """
        if isinstance(value, Version):
            return self.numbers > value.numbers
        return NotImplemented
