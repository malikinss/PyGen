'''
TODO:
    Implement the UpperPrint class.

    The class must not accept any arguments when instantiated.

    The UpperPrint class instance must be a context manager that, within
    the with block, allows all write operations to the standard output stream
    sys.stdout to be performed in uppercase.

NOTE:
    Visual examples of using the UpperPrint class are demonstrated in the test
    data.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    The UpperPrint class must satisfy the context manager protocol,
    i.e. have __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
import sys
from typing import Any, Callable


class UpperPrint:
    """
    A context manager that converts all sys.stdout writes to uppercase within
    a with block.
    """

    def __init__(self) -> None:
        """
        Initialize the UpperPrint context manager.
        """
        self.original_write: Callable[[str, Any], None] = None

    def _upper_write(self, text: str, *args: Any, **kwargs: Any) -> None:
        """
        Write text in uppercase using the original stdout write method.

        Args:
            text: The text to write.
            *args: Additional positional arguments for the write method.
            **kwargs: Additional keyword arguments for the write method.
        """
        self.original_write(str(text).upper(), *args, **kwargs)

    def __enter__(self) -> None:
        """
        Replace sys.stdout.write with the uppercase write method.

        Returns:
            None: No value is returned for use in the with block.
        """
        self.original_write = sys.stdout.write
        sys.stdout.write = self._upper_write
        return None

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """
        Restore the original sys.stdout.write method.

        Args:
            *args: Exception details (exc_type, exc_value, traceback).
            **kwargs: Additional keyword arguments (not used).
        """
        sys.stdout.write = self.original_write
