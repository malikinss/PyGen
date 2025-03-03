'''
TODO:
    Implement a prefix decorator that takes two arguments in the following
    order:
        string — an arbitrary string
        to_the_end — a boolean value, defaulting to False

    The decorator must append the string to the return value of the decorated
    function.
    If to_the_end is True, the string is appended to the end; if False, it is
    appended to the beginning.

    The decorator must also preserve the name and docstring of the decorated
    function.
NOTE:
    The return value of the decorated function is guaranteed to be an object
    of type str.

    Remember that the decorator must not consume the return value of the
    decorated function, and must be able to decorate functions with an
    arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


def prefix(string: str, to_the_end: bool = False) -> Callable:
    """
    Decorator to add a prefix or suffix to the return value of a function.

    Args:
        string (str): The string to be added.
        to_the_end (bool): If True, the string is added to the end
        of the return value.
                           If False, it is added to the beginning.

    Returns:
        Callable: The decorated function with the added string.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            """
            Wrapper function that adds the string to the return value.

            Args:
                *args (Any): Positional arguments passed to the decorated
                function.
                **kwargs (Any): Keyword arguments passed to the decorated
                function.

            Returns:
                str: The modified return value of the decorated function.
            """
            result = func(*args, **kwargs)  # Call the original function
            if to_the_end:
                return f'{result}{string}'  # Append string to the end
            return f'{string}{result}'  # Prepend string to the beginning

        return wrapper

    return decorator
