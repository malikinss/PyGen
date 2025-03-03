'''
TODO:
    Implement a repeat decorator that takes one argument:
        times - a natural number

    The decorator must call the decorated function times times.

    The decorator must also preserve the name and docstring of
    the decorated function.
NOTE:
    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


def repeat(times: int) -> Callable:
    """
    Decorator that repeats the execution of the decorated function a specified
    number of times.

    Args:
        times (int): The number of times to repeat the function execution.

    Returns:
        decorator (Callable): The decorator function.
    """
    def decorator(func: Callable) -> Callable:
        """
        The actual decorator function that wraps the original function.

        Args:
            func (Callable): The function to be decorated.

        Returns:
            wrapper (Callable): The wrapped function with added repeat logic.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            The wrapper function that executes the original function multiple
            times.

            Args:
                *args (Any): Positional arguments for the original function.
                **kwargs (Any): Keyword arguments for the original function.

            Returns:
                result (Any): The return value of the last function execution.
            """
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
