'''
TODO:
    Implement the Summator class, which describes an object that calculates
    the sum of natural numbers from 1 to n:
        1+2+3+...+n

    When creating an instance, the class should not take any arguments.

    The Summator class should have one instance method:
        total() — a method that takes an integer n as an argument and returns
                  the sum of integers from 1 to n inclusive

    In addition, implement the SquareSummator class, a subclass of
    the Summator class, which describes an object that calculates the sum of
    the squares of natural numbers from 1 to n:
        1^2+2^2+3^2+...+n^2

    The process of creating an instance of the SquareSummator class should
    coincide with the process of creating an instance of the Summator class.

    The SquareSummator class must have one instance method:
        total() — a method that takes an integer n as an argument and returns
                  the sum of the squares of integers from 1 to n inclusive

    Also implement the QubeSummator class, a descendant of the Summator class,
    describing an object that calculates the sum of the cubes of natural
    numbers from 1 to n:
        1^3+2^3+3^3+...+n^3

    The process of creating an instance of the QubeSummator class must
    coincide with the process of creating an instance of the Summator class.

    The QubeSummator class must have one instance method:
        total() — a method that takes an integer n as an argument and returns
                  the sum of the cubes of integers from 1 to n inclusive

    Finally, implement the CustomSummator class, a subclass of the Summator
    class, describing an object that calculates the sum of arbitrary powers of
    natural numbers from 1 to n:
        1^m+2^m+3^m+...+n^m

    When creating an instance, the class must take one argument:
        m — the power of numbers in the sequence

    The CustomSummator class must have one instance method:
        total() — a method that takes an integer n as an argument and returns
                  the sum of integers to the power m from 1 to n inclusive

NOTE:
    Try to implement the classes in such a way that the total() method is
    defined only in the Summator class.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    There are no restrictions regarding the implementation of classes; it can
    be arbitrary.
'''


class Summator:
    """
    Class representing a summator for natural numbers.

    Calculates the sum of numbers from 1 to n raised to a specific power.
    """

    def __init__(self) -> None:
        """
        Initialize a Summator instance.
        """
        self.power = 1

    def total(self, n: int) -> int:
        """
        Calculate the sum of numbers from 1 to n raised to the power attribute.

        Args:
            n: The upper bound of the range of numbers.

        Returns:
            int: The sum of numbers from 1 to n raised to self.power.
        """
        return sum(k ** self.power for k in range(1, n + 1))


class SquareSummator(Summator):
    """
    Class representing a summator for squares of natural numbers.

    Inherits from Summator and calculates the sum of squares from 1 to n.
    """

    def __init__(self) -> None:
        """Initialize a SquareSummator instance."""
        super().__init__()
        self.power = 2


class QubeSummator(Summator):
    """
    Class representing a summator for cubes of natural numbers.

    Inherits from Summator and calculates the sum of cubes from 1 to n.
    """

    def __init__(self) -> None:
        """Initialize a QubeSummator instance."""
        super().__init__()
        self.power = 3


class CustomSummator(Summator):
    """
    Class representing a summator for arbitrary powers of natural numbers.

    Inherits from Summator and calculates the sum of numbers raised to a given
    power.
    """

    def __init__(self, m: int) -> None:
        """Initialize a CustomSummator instance.

        Args:
            m: The power to which numbers are raised.
        """
        super().__init__()
        self.power = m
