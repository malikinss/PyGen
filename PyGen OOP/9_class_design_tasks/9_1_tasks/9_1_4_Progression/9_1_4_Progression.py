'''
TODO:
    Implement the ArithmeticProgression class to generate the terms of
    the arithmetic progression.

    When creating an instance of the ArithmeticProgression class, the first
    term of the sequence and the difference of the progression must be
    specified:
        progression = ArithmeticProgression(0, 1)
        for elem in progression:
        if elem > 10:
        break
        print(elem, end=' ') # 0 1 2 3 4 5 6 7 8 9 10

    Note that the arithmetic progression must be iterable and also infinite.

    Similarly, implement the GeometricProgression class to generate the terms
    of the geometric progression.

    When creating an instance of the GeometricProgression class, the first
    member of the sequence and the denominator of the progression must be
    specified:
        progression = GeometricProgression(1, 2)
        for elem in progression:
        if elem > 10:
        break
        print(elem, end=' ') # 1 2 4 8

    A geometric progression, like an arithmetic one, must be iterable and also
    infinite.
'''
from abc import ABC, abstractmethod
from typing import Self


class Progression(ABC):
    """
    Abstract base class for infinite progressions.
    """
    def __init__(self, start: float, step: float) -> None:
        """
        Initialize progression with start and step.

        Args:
            start: First term of the progression.
            step: Difference or ratio of the progression.
        """
        self.start = start
        self.step = step
        self.cur = start

    def __iter__(self) -> Self:
        """
        Return iterator object.
        """
        return self

    @abstractmethod
    def __next__(self) -> float:
        """
        Return next term of the progression.
        """
        pass


class ArithmeticProgression(Progression):
    """
    Class for infinite arithmetic progression.
    """
    def __next__(self) -> float:
        """
        Return next term and increment by step.
        """
        res = self.cur
        self.cur += self.step
        return res


class GeometricProgression(Progression):
    """
    Class for infinite geometric progression.
    """
    def __next__(self) -> float:
        """
        Return next term and multiply by step.
        """
        res = self.cur
        self.cur *= self.step
        return res
