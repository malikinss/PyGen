'''
TODO:
    Implement the Suppress class.

    When instantiated, the class must accept an arbitrary number of positional
    arguments, each representing an exception type.

    An instance of the Suppress class must be a context manager that
    suppresses an exception if it is raised during the execution of the code
    inside the with block.

    The exception types that are suppressed must be those that were listed
    when the context manager was created.

    An instance of the Suppress class must also have one attribute:
        exception — the exception that was suppressed by the context manager.

    If the exception was not suppressed or the code was executed without
    exceptions, the attribute must be None

NOTE:
    Visual examples of using the Suppress class are demonstrated in the test
    data.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    The Suppress class must conform to the context manager protocol, that is,
    it must have __enter__() and __exit__() methods.

    The implementation of the protocol can be arbitrary.
'''
from typing import Optional, Type, Tuple
from types import TracebackType


class Suppress:
    """
    A context manager that suppresses specified exception types within a with
    block.
    """

    def __init__(self, *args: Type[BaseException]) -> None:
        """
        Initialize with exception types to suppress.

        Args:
            *args: Exception types to suppress.
        """
        self._exceptions: Tuple[Type[BaseException], ...] = args
        self.exception: Optional[BaseException] = None

    def __enter__(self) -> 'Suppress':
        """
        Enter the context manager.

        Returns:
            Suppress: The context manager instance for accessing the exception
                      attribute.
        """
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> bool:
        """
        Exit the context manager, suppressing specified exceptions.

        Args:
            exc_type: Type of the exception, or None if no exception occurred.
            exc_value: The exception instance, or None.
            traceback: The traceback object, or None.

        Returns:
            bool: True if the exception was suppressed, False otherwise.
        """
        if exc_type is not None:
            for allowed_type in self._exceptions:
                if issubclass(exc_type, allowed_type):
                    self.exception = exc_value
                    return True
        return False
