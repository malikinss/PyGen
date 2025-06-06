'''
TODO:
    Implement a takes decorator that accepts an arbitrary number of positional
    arguments, each of which is a data type.

    The decorator must check that the arguments passed to the
    decorated function are of one of these types.

    If at least one argument is not of one of these types, the decorator must
    raise a TypeError exception.

    The decorator must also preserve the name and docstring of the decorated
    function.
NOTE:
    Remember that the decorator must not consume the return value of the
    decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


def takes(*types) -> Callable:
    """
    A decorator that checks the types of arguments passed to a function.

    Args:
        types (type): The types allowed for the function's arguments.

    Returns:
        Callable[[Callable], Callable]: The decorated function with
        type checking.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Combine positional and keyword arguments
            all_args = list(args) + list(kwargs.values())

            # Check each argument type
            for arg in all_args:
                if not isinstance(arg, types):
                    raise TypeError(f"Argument {arg} is not of type {types}")

            # Call the original function
            return func(*args, **kwargs)

        return wrapper

    return decorator
