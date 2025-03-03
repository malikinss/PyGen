'''
TODO:
    Implement a retry decorator that takes one argument:
        times — a natural number

    The decorator should retry calling the decorated function if an error
    occurs during its execution.

    The decorator should call it until it exhausts the number of times, after
    which it should throw a MaxRetriesException.

    The decorator should also save the name and docstring of
    the decorated function.
NOTE:
    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


class MaxRetriesException(Exception):
    pass


def retry(times: int) -> Callable:
    """
    Decorator to retry a function call if an exception occurs.

    Args:
        max_retries (int): Maximum number of retry attempts.

    Returns:
        Callable: Wrapped function that retries on failure.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass

            raise MaxRetriesException

        return wrapper

    return decorator
