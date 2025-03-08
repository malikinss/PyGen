'''
TODO:
    Implement an Xrange class that produces iterators whose constructor takes
    three arguments in the following order:
        - start is an integer or real number
        - end is an integer or real number
        - step is an integer or real number, defaulting to 1

    An Xrange iterator must generate a sequence of members of an arithmetic
    progression from start to end, including start and excluding end, with
    a step size of step, and then raise a StopIteration exception.
'''
from typing import Union


class Xrange:
    def __init__(
        self,
        start: Union[int, float],
        end: Union[int, float],
        step: Union[int, float] = 1
    ) -> None:
        """
        Initialize the Xrange iterator.

        Args:
            start (int | float): The starting value of the sequence.
            end (int | float): The end value (exclusive).
            step (int | float, optional): The step value (default is 1).
        """
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        """
        Return the iterator object.

        Returns:
            Xrange: The iterator object.
        """
        return self

    def __next__(self) -> Union[int, float]:
        """
        Return the next value in the arithmetic progression.

        Returns:
            int | float: The next value in the progression.

        Raises:
            StopIteration: If the end of the progression is reached.
        """
        if (
            self.step > 0 and self.current < self.end
        ) or (
            self.step < 0 and self.current > self.end
        ):
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration
