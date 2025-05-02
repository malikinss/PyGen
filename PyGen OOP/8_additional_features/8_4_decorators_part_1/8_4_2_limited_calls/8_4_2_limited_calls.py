'''
TODO:
    Implement a @limited_calls decorator class that takes one argument:
        n - an integer

    The decorator must allow the decorated function to be called n times.

    If the decorated function is called more than n times, a MaxCallsException
    must be thrown with the text:
        The allowed number of calls has been exceeded

NOTE:
    Remember that the decorator must not consume the return value of
    the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Any, Callable


class MaxCallsException(Exception):
    """
    Exception for exceeding call limit.
    """
    pass


class limited_calls:
    """
    Decorator to limit function calls.
    """
    def __init__(self, n: int) -> None:
        """
        Init decorator.

        Args:
            n: Maximum number of calls.
        """
        self.limit = n
        self.count = 0

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Wrap function to limit calls.

        Args:
            func: Function to decorate.

        Returns:
            Callable: Wrapped function.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if self.count >= self.limit:
                raise MaxCallsException(
                    "The allowed number of calls has been exceeded"
                )
            self.count += 1
            return func(*args, **kwargs)
        return wrapper
