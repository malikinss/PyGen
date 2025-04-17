'''
TODO:
    Implement the Greeter class.

    When instantiated, the class must accept one argument:
        name — user name

    An instance of the Greeter class must have one attribute:
        name — user name

    An instance of the Greeter class must be a context manager that greets
    the user named name before executing the with block and displays the text:
        Hello, <user name>!
    and also says goodbye to him after executing the with block and displays
    the text:
        See you there, <user name>!

NOTE:
    Visual examples of using the Greeter class are demonstrated in the test
    data.

    Additional data validation is not required.

    It is guaranteed that the implemented class is used only with correct data.

    The Greeter class must satisfy the context manager protocol, that is,
    have the __enter__() and __exit__() methods.

    The protocol implementation can be arbitrary.
'''
from typing import Any


class Greeter:
    """
    A context manager that greets and farewells a user in a with block.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the Greeter with a user name.

        Args:
            name: The name of the user.
        """
        self.name = name

    def __enter__(self) -> 'Greeter':
        """
        Print a greeting message when entering the context.

        Returns:
            Greeter: The context manager instance.
        """
        print(f'Hello, {self.name}!')
        return self

    def __exit__(self, *args: Any, **kwargs: Any) -> None:
        """
        Print a farewell message when exiting the context.

        Args:
            *args: Exception details (exc_type, exc_value, traceback).
            **kwargs: Additional keyword arguments (not used).
        """
        print(f'See you there, {self.name}!')
