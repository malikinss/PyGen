'''
TODO:
    You have access to the Counter class, which describes a non-negative
    counter.

    When creating an instance, the class takes one argument:
        start — the initial value of the counter, by default equals 0

    An instance of the Counter class has one attribute:
        value — the current value of the counter

    The Counter class has two instance methods:
        inc() — a method that takes an integer as an argument and increments
                the counter by this number.
                If the number is not passed, the method increments the counter
                by one
        dec() — a method that takes an integer as an argument and decrements
                the counter by this number.
                If the number is not passed, the method decrements the counter
                by one.
                The counter value is considered equal to 0 if it becomes
                negative when decremented

    Implement the DoubledCounter class, a descendant of the Counter class,
    describing a non-negative counter whose value is incremented and
    decremented twice when the corresponding methods are called.

    The process of creating an instance of the DoubledCounter class must
    coincide with the process of creating an instance of the Counter class.

    An instance of the DoubledCounter class must have one attribute:
        value — the current value of the counter

    The DoubledCounter class must have two instance methods:
        inc() — a method that takes an integer as an argument and increments
                the counter by that number twice.
                If no number is passed, the method must increment the counter
                by two
        dec() — a method that takes an integer as an argument and decrements
                the counter by that number twice.
                If no number is passed, the method must decrement the counter
                by two.
                The counter is considered to be 0 if it becomes negative when
                decremented

NOTE:
    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of classes, it can
    be arbitrary.
'''


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

    def inc(self, num: int = 1) -> None:
        """
        Increment the counter by the specified number.

        Args:
            num: The number to increment by, defaults to 1.
        """
        self.value += num

    def dec(self, num: int = 1) -> None:
        """
        Decrement the counter by the specified number, ensuring non-negativity.

        Args:
            num: The number to decrement by, defaults to 1.
        """
        self.value = max(self.value - num, 0)


class DoubledCounter(Counter):
    """
    Class representing a non-negative counter with doubled increments and
    decrements.

    Inherits from Counter and doubles the effect of incrementing and
    decrementing operations.
    """

    def inc(self, num: int = 1) -> None:
        """
        Increment the counter by twice the specified number.

        Args:
            num: The number to increment by, defaults to 1 (resulting in +2).
        """
        super().inc(num * 2)

    def dec(self, num: int = 1) -> None:
        """
        Decrement the counter by twice the specified number,
        ensuring non-negativity.

        Args:
            num: The number to decrement by, defaults to 1 (resulting in -2).
        """
        super().dec(num * 2)
