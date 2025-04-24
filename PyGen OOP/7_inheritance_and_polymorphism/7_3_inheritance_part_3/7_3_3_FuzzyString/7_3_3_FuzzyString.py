'''
TODO:
    Implement a FuzzyString class, a subclass of str, that describes a string
    that is case-insensitive for all comparisons (==, !=, >, <, >=, <=) and
    membership tests (in, not in).

    The process of creating an instance of the FuzzyString class must be
    the same as the process of creating an instance of the str class.

NOTE:
    If the object with which the comparison operation is performed is invalid,
    the method implementing this operation must return the NotImplemented
    constant.

    There are no restrictions regarding the implementation of the FuzzyString
    class, it can be arbitrary.
'''
from typing import Union, Any


class FuzzyString(str):
    """
    Class representing a case-insensitive string.

    Inherits from str and provides case-insensitive comparisons and membership
    tests.
    """

    def __eq__(
        self, other: Union[str, 'FuzzyString']
    ) -> Union[bool, Any]:
        """
        Check equality with another string case-insensitively.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the strings are equal case-insensitively,
                  False otherwise.
            NotImplementedType: If the other object is not a string
                                or FuzzyString.
        """
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        return self.lower() == other.lower()

    def __ne__(
        self, other: Union[str, 'FuzzyString']
    ) -> Union[bool, Any]:
        """
        Check inequality with another string case-insensitively.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the strings are not equal case-insensitively,
                  False otherwise.
            NotImplementedType: If the other object is not a string
                                or FuzzyString.
        """
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        return self.lower() != other.lower()

    def __gt__(
        self, other: Union[str, 'FuzzyString']
    ) -> Union[bool, Any]:
        """
        Check if the string is greater than another string
        case-insensitively.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the string is greater case-insensitively,
                  False otherwise.
            NotImplementedType: If the other object is not a string
                                or FuzzyString.
        """
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        return self.lower() > other.lower()

    def __lt__(
        self, other: Union[str, 'FuzzyString']
    ) -> Union[bool, Any]:
        """Check if the string is less than another string case-insensitively.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the string is less case-insensitively,
                  False otherwise.
            NotImplementedType: If the other object is not a string
                                or FuzzyString.
        """
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        return self.lower() < other.lower()

    def __ge__(
        self, other: Union[str, 'FuzzyString']
    ) -> Union[bool, Any]:
        """
        Check if the string is greater than or equal to another string
        case-insensitively.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the string is greater or equal case-insensitively,
                  False otherwise.
            NotImplementedType: If the other object is not a string
                                or FuzzyString.
        """
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        return self.lower() >= other.lower()

    def __le__(
        self, other: Union[str, 'FuzzyString']
    ) -> Union[bool, Any]:
        """
        Check if the string is less than or equal to another string
        case-insensitively.

        Args:
            other: The object to compare with.

        Returns:
            bool: True if the string is less or equal case-insensitively,
                  False otherwise.
            NotImplementedType: If the other object is not a string
                                or FuzzyString.
        """
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        return self.lower() <= other.lower()

    def __contains__(
        self, other: Union[str, 'FuzzyString']
    ) -> Union[bool, Any]:
        """
        Check if another string is a substring case-insensitively.

        Args:
            other: The substring to check for.

        Returns:
            bool: True if the substring is present case-insensitively,
                  False otherwise.
            NotImplementedType: If the other object is not a string
                                or FuzzyString.
        """
        if not isinstance(other, (str, FuzzyString)):
            return NotImplemented
        return other.lower() in self.lower()
