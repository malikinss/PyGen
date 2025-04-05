'''
TODO:
    Implement the HourClock class, which describes a clock with only an hour
    hand.

    When instantiating the class, it must accept one argument:
        - hours — the number of hours.

    If hours is not an integer in the range [1; 12], a ValueError exception
    must be raised with the text:
        Invalid time

    The HourClock class must have one property:
        - hours — a read-write property that returns the current number
                  of hours.

    When changing, the property must check that the new value is an integer in
    the range [1; 12], otherwise a ValueError exception must be raised with
    the text:
        Invalid time

NOTE:
    There are no restrictions regarding the implementation of the HourClock
    class, it can be arbitrary.
'''


class HourClock:
    """
    A class representing a clock with only an hour hand.

    Attributes:
        _hours (int): The current number of hours, stored internally.

    Properties:
        hours (int): A read-write property to get or set the number of hours,
                     must be an integer in the range [1; 12].
    """

    def __init__(self, hours: int) -> None:
        """
        Initialize the HourClock with a given number of hours.

        Args:
            hours (int): The number of hours, must be in [1; 12].

        Raises:
            ValueError: If hours is not an integer in [1; 12], with message
            'Invalid time'.
        """
        self._validate_hours(hours)
        self._hours: int = hours

    def _validate_hours(self, hours: int) -> None:
        """
        Validate that the hours value is an integer in the range [1; 12].

        Args:
            hours (int): The value to validate.

        Raises:
            ValueError: If hours is not an integer in [1; 12], with message
            'Invalid time'.
        """
        if not isinstance(hours, int) or not (1 <= hours <= 12):
            raise ValueError("Invalid time")

    def get_hours(self) -> int:
        """
        Get the current number of hours.

        Returns:
            int: The current hours value.
        """
        return self._hours

    def set_hours(self, hours: int) -> None:
        """
        Set a new number of hours.

        Args:
            hours (int): The new hours value, must be in [1; 12].

        Raises:
            ValueError: If hours is not an integer in [1; 12], with message
            'Invalid time'.
        """
        self._validate_hours(hours)
        self._hours = hours

    hours = property(get_hours, set_hours)
