'''
TODO:
    Implement the Reloopable class.

    When instantiated, the class must accept one argument:
        file — a file object open for reading

    An instance of the Reloopable class must be a context manager that allows
    iterating over the file object inside the with block.

    The context manager must also close the file object it uses after
    executing the code inside the with block.

NOTE:
    Visual examples of using the Reloopable class are demonstrated in the test
    data.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The Reloopable class must satisfy the context manager protocol, that is,
    have the __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import TextIO, Iterator, Any


class Reloopable:
    """
    A context manager that allows multiple iterations over a file and closes
    it.
    """

    def __init__(self, file: TextIO) -> None:
        """
        Initialize with a file object open for reading.

        Args:
            file: File object open for reading.
        """
        self.file = file

    def __enter__(self) -> 'Reloopable':
        """
        Enter the context manager, returning self for iteration.

        Returns:
            Reloopable: The context manager instance for iteration.
        """
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """
        Close the file.

        Args:
            *args: Exception details (exc_type, exc_value, traceback).
            **kwargs: Additional keyword arguments (not used).
        """
        self.file.close()

    def __iter__(self) -> Iterator[str]:
        """
        Return an iterator over the file lines, resetting to the start.

        Returns:
            Iterator[str]: Iterator over file lines.
        """
        self.file.seek(0)  # Reset file pointer to start
        return iter(self.file)
