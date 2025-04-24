'''
TODO:
    Implement a ModularTuple class, a tuple subclass that describes a tuple
    whose elements are automatically divided by a given number with
    a remainder when created.

    When instantiated, the class must accept two arguments in the following
    order:
        iterable — an iterable defining the initial set of elements of
                   the ModularTuple instance.
                   If not passed, the initial set of elements is considered
                   empty
        size — an integer that divides the elements of the created
               ModularTuple instance with a remainder, defaulting to 100

NOTE:
    An instance of the ModularTuple class must not depend on the iterable from
    which it was created.

    In other words, if the original iterable changes, the instance of
    the ModularTuple class must not change.

    No additional data validation is required.

    The implemented class is guaranteed to be used only with valid data.

    There are no restrictions regarding the implementation of the ModularTuple
    class, it can be arbitrary.
'''
from collections.abc import Iterable
from typing import Any


class ModularTuple(tuple):
    """
    Class representing a tuple with elements divided by a number with
    remainder.

    Inherits from tuple, with elements computed as remainders when divided
    by size.
    """

    def __new__(
        cls, iterable: Iterable[Any] = (), size: int = 100
    ) -> 'ModularTuple':
        """
        Create a new ModularTuple with elements divided by size with remainder.

        Args:
            iterable: An iterable defining the initial elements.
                      Defaults to an empty tuple.
            size: The number to divide elements by, defaults to 100.

        Returns:
            ModularTuple: A new tuple with elements as remainders (x % size).
        """
        new_iterable = tuple(x % size for x in iterable)
        return super().__new__(cls, new_iterable)
