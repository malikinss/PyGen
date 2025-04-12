'''
TODO:
    Implement the RomanNumeral class, which describes a number in the Roman
    numeral system.

    When instantiated, the class must accept one argument:
        number — a number in the Roman numeral system. For example, IV

    An instance of the RomanNumeral class must have the following informal
    string representation:
        <number in the Roman numeral system>

    In addition, an instance of the RomanNumeral class must support casting to
    the int type, which, when cast to, must yield an integer in the decimal
    numeral system to which it corresponds.

    Also, instances of the RomanNumeral class must support all comparison
    operations between themselves using the operators ==, !=, >, <, >=, <=.

    Finally, RomanNumeral class instances must support addition and
    subtraction operations between themselves using the + and - operators,
    respectively:
        - the result of addition must be a new RomanNumeral class instance
          representing the sum of the original
        - the result of subtraction must be a new RomanNumeral class instance
          representing the difference of the original

NOTE:
    It is guaranteed that the strictly smaller Roman number is always
    subtracted from the Roman numeral.

    You can read more about the Roman numeral system at the link.

    Do not forget that it is the NotImplemented constant that is recommended
    to be returned in methods implementing arithmetic operations or comparison
    operations, if these operations are not defined for objects of any type.

    There are no restrictions regarding the implementation of the RomanNumeral
    class, it can be arbitrary.
'''
from typing import Union


class RomanNumeral:
    """
    A class representing a number in the Roman numeral system.

    Attributes:
        number (str): The Roman numeral string (e.g., 'IV').
    """

    _NUMS = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    def __init__(self, number: str) -> None:
        """
        Initialize with a Roman numeral string.

        Args:
            number (str): A string representing a Roman numeral (e.g., 'IV').
        """
        self.number = number

    def __str__(self) -> str:
        """
        Return the Roman numeral string.

        Returns:
            str: The Roman numeral string.
        """
        return self.number

    def __int__(self) -> int:
        """
        Convert to decimal integer.

        Returns:
            int: The decimal equivalent of the Roman numeral.
        """
        result = 0
        i = 0
        while i < len(self.number):
            if i + 1 < len(self.number):
                two_chars = self.number[i:i+2]
                if two_chars in self._NUMS:
                    result += self._NUMS[two_chars]
                    i += 2
                    continue
            result += self._NUMS[self.number[i]]
            i += 1
        return result

    @classmethod
    def _to_roman(cls, num: int) -> str:
        """
        Convert integer to Roman numeral string.

        Args:
            num (int): The integer to convert.

        Returns:
            str: The Roman numeral string.
        """
        result = ''
        for roman, value in cls._NUMS.items():
            while num >= value:
                result += roman
                num -= value
        return result

    def __eq__(
        self, other: 'RomanNumeral'
    ) -> Union[bool, type(NotImplemented)]:
        """
        Check if equal to another Roman numeral.

        Args:
            other (RomanNumeral): Another RomanNumeral instance.

        Returns:
            bool or NotImplemented: True if equal, False otherwise,
                                    or NotImplemented if invalid type.
        """
        if isinstance(other, RomanNumeral):
            return int(self) == int(other)
        return NotImplemented

    def __ne__(
        self, other: 'RomanNumeral'
    ) -> Union[bool, type(NotImplemented)]:
        """
        Check if not equal to another Roman numeral.

        Args:
            other (RomanNumeral): Another RomanNumeral instance.

        Returns:
            bool or NotImplemented: True if not equal, False otherwise,
                                    or NotImplemented if invalid type.
        """
        if isinstance(other, RomanNumeral):
            return int(self) != int(other)
        return NotImplemented

    def __gt__(
        self, other: 'RomanNumeral'
    ) -> Union[bool, type(NotImplemented)]:
        """
        Check if greater than another Roman numeral.

        Args:
            other (RomanNumeral): Another RomanNumeral instance.

        Returns:
            bool or NotImplemented: True if greater, False otherwise,
                                    or NotImplemented if invalid type.
        """
        if isinstance(other, RomanNumeral):
            return int(self) > int(other)
        return NotImplemented

    def __ge__(
        self, other: 'RomanNumeral'
    ) -> Union[bool, type(NotImplemented)]:
        """
        Check if greater than or equal to another Roman numeral.

        Args:
            other (RomanNumeral): Another RomanNumeral instance.

        Returns:
            bool or NotImplemented: True if greater or equal, False otherwise,
                                    or NotImplemented if invalid type.
        """
        if isinstance(other, RomanNumeral):
            return int(self) >= int(other)
        return NotImplemented

    def __lt__(
        self, other: 'RomanNumeral'
    ) -> Union[bool, type(NotImplemented)]:
        """
        Check if less than another Roman numeral.

        Args:
            other (RomanNumeral): Another RomanNumeral instance.

        Returns:
            bool or NotImplemented: True if less, False otherwise,
                                    or NotImplemented if invalid type.
        """
        if isinstance(other, RomanNumeral):
            return int(self) < int(other)
        return NotImplemented

    def __le__(
        self, other: 'RomanNumeral'
    ) -> Union[bool, type(NotImplemented)]:
        """
        Check if less than or equal to another Roman numeral.

        Args:
            other (RomanNumeral): Another RomanNumeral instance.

        Returns:
            bool or NotImplemented: True if less or equal, False otherwise,
                                    or NotImplemented if invalid type.
        """
        if isinstance(other, RomanNumeral):
            return int(self) <= int(other)
        return NotImplemented

    def __add__(
        self, other: 'RomanNumeral'
    ) -> Union['RomanNumeral', type(NotImplemented)]:
        """
        Add another Roman numeral.

        Args:
            other (RomanNumeral): Another RomanNumeral instance.

        Returns:
            RomanNumeral or NotImplemented: A new RomanNumeral instance with
                                            the sum, or NotImplemented
                                            if invalid type.
        """
        if isinstance(other, RomanNumeral):
            result = int(self) + int(other)
            return RomanNumeral(self._to_roman(result))
        return NotImplemented

    def __sub__(
        self, other: 'RomanNumeral'
    ) -> Union['RomanNumeral', type(NotImplemented)]:
        """
        Subtract another Roman numeral.

        Args:
            other (RomanNumeral): Another RomanNumeral instance.

        Returns:
            RomanNumeral or NotImplemented: A new RomanNumeral instance with
                                            the difference, or NotImplemented
                                            if invalid type.
        """
        if isinstance(other, RomanNumeral):
            result = int(self) - int(other)
            return RomanNumeral(self._to_roman(result))
        return NotImplemented
