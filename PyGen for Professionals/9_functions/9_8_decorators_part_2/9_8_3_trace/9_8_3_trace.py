'''
TODO:
    Implement a trace decorator that prints debugging information about the
    decorated function during its execution, namely the function name, the
    arguments passed, and the return value in the following format:

    TRACE: call <function name>() with arguments: <tuple of positional
    arguments>, <dictionary of named arguments>

    TRACE: return value <function name>(): <return value>

    The decorator should also preserve the name and docstring of
    the decorated function.

NOTE:
    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


def trace(function: Callable) -> Callable:
    """
    Trace decorator that prints debugging information about the decorated
    function.

    Args:
        function (Callable): The function to be decorated.

    Returns:
        Callable: The decorated function.
    """
    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Trace function call with arguments and keyword arguments
        print(
            f'TRACE: call {function.__name__}()'
            f' with arguments: {args}, {kwargs}'
        )
        result = function(*args, **kwargs)
        # Trace the return value
        print(f'TRACE: return value {function.__name__}(): {repr(result)}')

        return result

    return wrapper
