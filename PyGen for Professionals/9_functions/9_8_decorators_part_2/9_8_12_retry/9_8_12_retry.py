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
    def __init__(self, message: str):
        super().__init__(message)


def retry(times: int) -> Callable:
    """
    Decorator to retry a function call if an exception occurs.

    Args:
        times (int): Maximum number of retry attempts.

    Returns:
        Callable: Wrapped function that retries on failure.

    Raises:
        MaxRetriesException: If the function fails after the maximum number
        of retries.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed with exception: {e}")
                    if attempt == times:
                        raise MaxRetriesException(
                            f"Function failed after {times} retries."
                        ) from last_exception
            return None

        return wrapper

    return decorator
