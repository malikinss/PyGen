'''
TODO:
    Implement the WriteSpy class.

    When instantiated, the class must accept three arguments in the following
    order:
        file1 — a file object
        file2 — a file object
        to_close — a boolean value, defaults to False

    The WriteSpy class instance must be a context manager that performs
    a write operation to both file objects file1 and file2 at once.

    The to_close parameter must determine the state of the file objects file1
    and file2 after the with block is complete.

    If it is True, the context manager must close both file objects after
    the with block is complete; if it is False, it must leave them open.

    The WriteSpy class must have four instance methods:
        - write() — a method that takes text as an argument and writes it
                    to both file objects.
                    If at least one of the file objects is closed or not
                    writable, a ValueError exception should be raised with
                    the text:
                        The file is closed or not writable
        - close() — a method that immediately closes both file objects
        - writable() — a method that returns True if both file objects
                       are writable, or False otherwise
        - closed() — a method that returns True if both file objects
                     are closed, or False otherwise

NOTE:
    Visual examples of using the WriteSpy class are demonstrated in the test
    data.

    To check whether a file object is writable, use the writable() method.

    This method returns True if the file object is writable, or False
    otherwise.

    An attempt to apply the method to a closed file object will raise
    an exception.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    The WriteSpy class must satisfy the context manager protocol, that is,
    have the __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Any, IO


class WriteSpy:
    """
    A context manager that writes to two file objects simultaneously.
    """

    def __init__(
        self, file1: IO[str], file2: IO[str], to_close: bool = False
    ) -> None:
        """
        Initialize with two file objects and a flag to close them.

        Args:
            file1: First file object.
            file2: Second file object.
            to_close: Whether to close both files after the with block.
                      Defaults to False.
        """
        self._file1: IO[str] = file1
        self._file2: IO[str] = file2
        self._to_close: bool = to_close

    def __enter__(self) -> 'WriteSpy':
        """
        Enter the context manager.

        Returns:
            WriteSpy: The context manager instance for writing to both files.
        """
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """
        Exit the context manager, closing files if to_close is True.

        Args:
            *args: Exception details (exc_type, exc_value, traceback).
            **kwargs: Additional keyword arguments (not used).
        """
        if self._to_close:
            self.close()

    def write(self, text: str) -> None:
        """
        Write text to both file objects.

        Args:
            text: The text to write.

        Raises:
            ValueError: If at least one file is closed or not writable.
        """
        if not self.writable():
            raise ValueError("The file is closed or not writable")
        self._file1.write(text)
        self._file2.write(text)

    def close(self) -> None:
        """
        Close both file objects.
        """
        self._file1.close()
        self._file2.close()

    def writable(self) -> bool:
        """
        Check if both file objects are writable.

        Returns:
            bool: True if both files are writable, False otherwise.
        """
        try:
            return self._file1.writable() and self._file2.writable()
        except (ValueError, AttributeError):
            return False

    def closed(self) -> bool:
        """
        Check if both file objects are closed.

        Returns:
            bool: True if both files are closed, False otherwise.
        """
        return self._file1.closed and self._file2.closed
