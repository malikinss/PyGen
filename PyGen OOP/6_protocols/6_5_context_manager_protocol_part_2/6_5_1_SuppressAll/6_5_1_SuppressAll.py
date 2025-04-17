'''
TODO:
    The SuppressAll class had to be implemented.

    The class was not supposed to accept any arguments when instantiated.

    The SuppressAll class instance was supposed to be a context manager
    that suppresses any exception that is raised while executing code inside
    the with block.

    The programmer was in a hurry and solved the problem incorrectly.

    Complete the code below and implement the SuppressAll class correctly.

NOTE:
    Illustrative examples of using the SuppressAll class are demonstrated in
    the test data.

    No additional data validation is required.

    It is guaranteed that the implemented class is used only with correct data.

    The SuppressAll class must satisfy the context manager protocol, that is,
    have __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Any


class SuppressAll:
    """
    A context manager that suppresses all exceptions raised within its with
    block.
    """

    def __enter__(self) -> 'SuppressAll':
        """
        Enter the context manager.

        Returns:
            SuppressAll: The context manager instance.
        """
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> bool:
        """
        Exit the context manager, suppressing any exception.

        Args:
            *args: Exception details (exc_type, exc_value, traceback).
            **kwargs: Additional keyword arguments (not used).

        Returns:
            bool: True to suppress any exception.
        """
        return True
