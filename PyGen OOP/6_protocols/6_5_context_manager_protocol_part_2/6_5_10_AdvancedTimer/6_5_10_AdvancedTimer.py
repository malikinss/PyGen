'''
TODO:
    Implement the AdvancedTimer class.

    The class must not take any arguments when instantiated.

    The AdvancedTimer class instance must be a reusable context manager that
    measures the execution time of the code inside each with block.

    The AdvancedTimer class instance must also have four attributes:
        - last_run — a number representing the execution time of the code
                     inside the last with block
        - runs — a list of numbers, each of which represents the execution
                 time of some code inside the with block.
                 The first element of the list must represent the execution
                 time of the code inside the first with block, the second
                 element — the execution time of the code inside the second
                 with block, and so on
        - min — a number representing the minimum execution time of the code
                inside the with block among all measurements
        - max — a number representing the maximum execution time of the code
                inside the with block among all measurements

    If the AdvancedTimer class instance has never been used to measure
    the execution speed of any code block, the values of the last_run, min,
    and max attributes must be None.

NOTE:
    Visual examples of the use of the AdvancedTimer class are demonstrated in
    the test data.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The AdvancedTimer class must comply with the context manager protocol,
    i.e. have the __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Optional, Type
from time import perf_counter
from types import TracebackType


class AdvancedTimer:
    """
    A reusable context manager that measures execution time of code in with
    blocks.
    """

    def __init__(self) -> None:
        """
        Initialize the timer with no prior measurements.
        """
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None
        self.start = None

    def __enter__(self) -> 'AdvancedTimer':
        """
        Start timing and return the timer instance.

        Returns:
            AdvancedTimer: The timer instance for accessing timing attributes.
        """
        self.start = perf_counter()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> None:
        """
        Stop timing, update measurements, and compute min/max.

        Args:
            exc_type: Type of the exception, or None if no exception occurred.
            exc_value: The exception instance, or None.
            traceback: The traceback object, or None.
        """
        self.last_run = perf_counter() - self.start
        self.runs.append(self.last_run)
        if self.runs:
            self.min = min(self.runs)
            self.max = max(self.runs)
