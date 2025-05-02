'''
TODO:
    Implement a decorator class @ignore_exception that takes an arbitrary
    number of positional arguments — exception types — and outputs the text:
        Exception <exception type> handled

    if an exception of one of the passed types was thrown during the execution
    of the decorated function.

    If the thrown exception does not belong to any of the passed types,
    it must be thrown again.

NOTE:
    Remember that the decorator must not consume the return value of
    the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Any, Callable, Type


class ignore_exception:
    """
    Decorator to handle specified exceptions.
    """
    def __init__(self, *exceptions: Type[Exception]) -> None:
        """
        Init decorator.

        Args:
            *exceptions: Exception types to handle.
        """
        self.exceptions = exceptions

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Wrap function to handle exceptions.

        Args:
            func: Function to decorate.

        Returns:
            Callable: Wrapped function.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except self.exceptions as e:
                print(f"Exception {type(e).__name__} handled")
                return None
            except Exception as e:
                raise e
        return wrapper
