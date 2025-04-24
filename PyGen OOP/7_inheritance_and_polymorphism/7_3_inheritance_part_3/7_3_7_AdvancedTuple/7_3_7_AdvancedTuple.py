'''
TODO:
    Implement the AdvancedTuple class, a tuple inheritor that describes
    a tuple that can perform the addition operation (+, +=) not only with
    instances of the AdvancedTuple and tuple classes, but also with any
    iterable objects.

    The process of creating an instance of the AdvancedTuple class must
    coincide with the process of creating an instance of the tuple class.

NOTE:
    Regardless of how the addition is performed, using the + or += operator,
    the result of the operation must be a new instance of the AdvancedTuple
    class.

    There are no restrictions regarding the implementation of
    the AdvancedTuple class, it can be arbitrary.
'''
from collections.abc import Iterable


class AdvancedTuple(tuple):
    """
    Class representing a tuple that supports addition with any iterable.

    Inherits from tuple, allowing + and += operations with tuples,
    AdvancedTuples, and other iterable objects, returning a new AdvancedTuple.
    """

    def __add__(self, other: Iterable) -> 'AdvancedTuple':
        """
        Add an iterable to the tuple, returning a new AdvancedTuple.

        Args:
            other: An iterable object to concatenate with the tuple.

        Returns:
            AdvancedTuple: A new AdvancedTuple containing concatenated
                           elements.
            NotImplemented: If other is not iterable.
        """
        if not isinstance(other, Iterable):
            return NotImplemented
        return AdvancedTuple(tuple(self) + tuple(other))

    def __radd__(self, other: Iterable) -> 'AdvancedTuple':
        """
        Add the tuple to an iterable, returning a new AdvancedTuple.

        Args:
            other: An iterable object to concatenate before the tuple.

        Returns:
            AdvancedTuple: A new AdvancedTuple containing concatenated
                           elements.
            NotImplemented: If other is not iterable.
        """
        if not isinstance(other, Iterable):
            return NotImplemented
        return AdvancedTuple(tuple(other) + tuple(self))

    def __iadd__(self, other: Iterable) -> 'AdvancedTuple':
        """
        Add an iterable in-place, returning a new AdvancedTuple.

        Args:
            other: An iterable object to concatenate with the tuple.

        Returns:
            AdvancedTuple: A new AdvancedTuple containing concatenated
                           elements.
            NotImplemented: If other is not iterable.
        """
        if not isinstance(other, Iterable):
            return NotImplemented
        return AdvancedTuple(tuple(self) + tuple(other))
