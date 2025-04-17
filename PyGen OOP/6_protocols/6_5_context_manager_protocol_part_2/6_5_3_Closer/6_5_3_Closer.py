'''
TODO:
    Implement the Closer class.

    When instantiated, the class must accept one argument:
        obj — an arbitrary object

    The Closer class instance must be a context manager that closes the used
    obj object using the close() method after executing the code inside
    the with block.

    If the object does not support the close operation, the context manager
    must print:
    Unclosed object

NOTE:
    Visual examples of using the Closer class are demonstrated in the test
    data.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The Closer class must satisfy the context manager protocol, that is,
    have __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Any


class Closer:
    """
    A context manager that closes an object after the with block.
    """

    def __init__(self, obj: Any) -> None:
        """
        Initialize the Closer with an object.

        Args:
            obj: The object to be closed.
        """
        self.obj = obj

    def __enter__(self) -> Any:
        """
        Enter the context manager, returning the object.

        Returns:
            Any: The object passed to the Closer.
        """
        return self.obj

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """
        Exit the context manager, attempting to close the object.

        If the object does not have a close method, print 'Unclosed object'.

        Args:
            *args: Exception details (exc_type, exc_value, traceback).
            **kwargs: Additional keyword arguments (not used).
        """
        try:
            self.obj.close()
        except AttributeError:
            print('Unclosed object')
