'''
TODO:
    Implement a Vector class whose instance represents a vector of arbitrary
    dimension.

    An instance of the Vector class must be created based on its own
    coordinates:
        a = Vector(1, 2, 3)
        b = Vector(3, 4, 5)
        c = Vector(5, 6, 7, 8)

    As an informal string representation, a vector must have its own
    coordinates enclosed in parentheses:
        print(a) # (1, 2, 3)
        print(b) # (3, 4, 5)
        print(c) # (5, 6, 7, 8)

    Vectors must support addition, subtraction, product, and normalization
    operations among themselves:
        print(a + b) # (4, 6, 8)
        print(a - b) # (-2, -2, -2)
        print(a * b) # 1*3 + 2*4 + 3*5 = 26
        print(c.norm())
        # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292

    as well as equality and inequality comparison operations:
        print(a == Vector(1, 2, 3)) # True
        print(a == Vector(4, 5, 6)) # False

    When attempting to perform any operation with vectors of different
    dimensions, a ValueError exception should be raised with the text:
        Vectors must have equal length
'''
from typing import Union, Callable
from operator import add, sub, mul
from math import sqrt


class Vector:
    """
    A class representing a vector of arbitrary dimension.
    """
    ERR_MSG = 'Vectors must have equal length'

    def __init__(self, *coords: float) -> None:
        """
        Initialize vector with coordinates.

        Args:
            *coords: Variable number of coordinates.
        """
        self.coords = list(coords)

    def __str__(self) -> str:
        """
        Return informal string representation: (x, y, z).
        """
        return f"({', '.join(str(x) for x in self.coords)})"

    def _same_length(self, other: 'Vector') -> bool:
        """
        Check if vectors have equal length.

        Args:
            other: Vector to compare length with.

        Returns:
            True if lengths are equal.

        Raises:
            ValueError: If vectors have different lengths.
        """
        if len(self.coords) != len(other.coords):
            raise ValueError(self.ERR_MSG)
        return True

    def _do_action(
        self,
        other: 'Vector',
        action: Callable[[float, float], float]
    ) -> Union['Vector', float]:
        """
        Apply action to vector coordinates.

        Args:
            other: Vector to operate with.
            action: Operation to apply (add, sub, mul).

        Returns:
            Vector for add/sub, float for mul.

        Raises:
            ValueError: If vectors have different lengths.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if self._same_length(other):
            tmp = map(
                lambda x, y: action(x, y),
                self.coords,
                other.coords
            )
            if action == mul:
                return sum(tmp)
            return Vector(*tmp)

    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Add two vectors element-wise.
        """
        return self._do_action(other, add)

    def __sub__(self, other: 'Vector') -> 'Vector':
        """
        Subtract two vectors element-wise.
        """
        return self._do_action(other, sub)

    def __mul__(self, other: 'Vector') -> float:
        """
        Compute dot product of two vectors.
        """
        return self._do_action(other, mul)

    def __eq__(self, other: object) -> bool:
        """
        Check if two vectors are equal.
        """
        if not isinstance(other, Vector):
            return NotImplemented
        if self._same_length(other):
            return self.coords == other.coords

    def norm(self) -> float:
        """
        Compute Euclidean norm of the vector.
        """
        return sqrt(self._do_action(self, mul))
