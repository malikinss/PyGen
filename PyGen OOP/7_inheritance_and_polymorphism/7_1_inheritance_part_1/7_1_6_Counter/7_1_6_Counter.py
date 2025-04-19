'''
TODO:
    Implement a Counter class that describes a non-negative counter.

    When instantiated, the class must accept one argument:
        start — the initial value of the counter, equals 0 by default

    An instance of the Counter class must have one attribute:
        value — the current value of the counter

    The Counter class must have two instance methods:
        inc() — a method that takes an integer as an argument and increments
                the counter by that number.
                If no number is passed, the method must increment the counter
                by one
        dec() — a method that takes an integer as an argument and decrements
                the counter by that number.
                If no number is passed, the method must decrement the counter
                by one.
                The counter value is considered to be 0 if it becomes negative
                when decremented

    Also implement a NonDecCounter class, a descendant of the Counter class,
    that describes a counter whose value can be incremented but not
    decremented.

    The process of creating an instance of the NonDecCounter class must
    coincide with the process of creating an instance of the Counter class.

    An instance of the NonDecCounter class must have one attribute:
        value — the current value of the counter

    The NonDecCounter class must have one instance method:
        dec() — an empty method.
                The method signature must match the signature of the dec()
                method of the Counter class

    Finally, implement the LimitedCounter class, a subclass of the Counter
    class, describing a counter whose value can only be incremented to
    a certain number.

    When creating an instance, the class must accept two arguments in
    the following order:
        start — the initial value of the counter, by default equals 0
        limit — the maximum possible value of the counter, by default equals 10

    An instance of the LimitedCounter class must have one attribute:
        value — the current value of the counter

    The LimitedCounter class must have one instance method:
        inc() — a method that takes an integer as an argument and increments
                the counter by that number.
                If no number is passed, the method must increment the counter
                by one.
                When increasing the counter value, the method must not exceed
                the set limit

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of classes,
    it can be arbitrary.
'''
from typing import Optional


class Counter:
    """
    Class representing a non-negative counter.

    This class manages a counter that can be incremented or decremented,
    ensuring the value remains non-negative.
    """

    def __init__(self, start: int = 0) -> None:
        """
        Initialize a Counter instance.

        Args:
            start: The initial value of the counter, defaults to 0.
        """
        self.value = start

    def inc(self, num: Optional[int] = None) -> None:
        """
        Increment the counter by the specified number.

        Args:
            num: The number to increment by, defaults to 1 if None.
        """
        if num is None:
            num = 1
        self.value += num

    def dec(self, num: Optional[int] = None) -> None:
        """
        Decrement the counter by the specified number, ensuring non-negativity.

        Args:
            num: The number to decrement by, defaults to 1 if None.
        """
        if num is None:
            num = 1
        self.value -= num
        if self.value < 0:
            self.value = 0


class NonDecCounter(Counter):
    """
    Class representing a counter that can only be incremented.

    Inherits from Counter and disables decrementing functionality.
    """

    def dec(self, num: Optional[int] = None) -> None:
        """
        Empty method to disable decrementing.

        Args:
            num: The number to decrement by (ignored), defaults to None.
        """
        pass


class LimitedCounter(Counter):
    """
    Class representing a counter with an upper limit.

    Inherits from Counter and restricts incrementing to a specified limit.
    """

    def __init__(self, start: int = 0, limit: int = 10) -> None:
        """
        Initialize a LimitedCounter instance.

        Args:
            start: The initial value of the counter, defaults to 0.
            limit: The maximum value of the counter, defaults to 10.
        """
        self.value = start
        self.limit = limit

    def inc(self, num: Optional[int] = None) -> None:
        """
        Increment the counter by the specified number, respecting the limit.

        Args:
            num: The number to increment by, defaults to 1 if None.
        """
        if num is None:
            num = 1
        new_value = self.value + num
        if new_value <= self.limit:
            self.value = new_value
        else:
            self.value = self.limit
