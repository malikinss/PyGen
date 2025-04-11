'''
TODO:
    Implement the @CountCalls decorator, which counts the number of calls
    to the decorated function.

    The call counter must be accessible via the calls attribute.

NOTE:
    Remember that the decorator must not consume the return value of
    the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.

    Submit a program to the testing system containing only the required
    @CountCalls decorator, but not the code that calls it.
'''
from typing import Callable, Any


class CountCalls:
    """
    A decorator class that counts the number of calls to a function.
    """

    def __init__(self, func: Callable) -> None:
        """
        Initialize the decorator with the function to be decorated.

        Args:
            func (Callable): The function to decorate and count calls for.
        """
        self.calls = 0
        self.func = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Call the decorated function and increment the call counter.

        Args:
            *args: Positional arguments to pass to the decorated function.
            **kwargs: Keyword arguments to pass to the decorated function.

        Returns:
            Any: The return value of the decorated function.
        """
        self.calls += 1
        return self.func(*args, **kwargs)
