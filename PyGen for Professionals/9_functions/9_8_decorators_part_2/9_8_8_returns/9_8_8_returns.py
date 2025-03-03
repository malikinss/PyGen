'''
TODO:
    Implement a returns decorator that takes one argument:
        datatype — the data type

    The decorator must check that the return value of the decorated function
    is of type datatype.

    If the return value is of any other type, the decorator must throw a
    TypeError exception.

    The decorator must also preserve the name and docstring of the decorated
    function.
NOTE:
    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


def returns(datatype) -> Callable:
    """
    Decorator to check the return type of the decorated function.

    Args:
        expected_type (type): The type that the return value of the function
        should have.

    Returns:
        Callable: A decorator that checks the return type.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            """
            Wrapper function that checks the return type of
            the decorated function.

            Args:
                *args (Any): Positional arguments to the decorated function.
                **kwargs (Any): Keyword arguments to the decorated function.

            Returns:
                Any: The return value of the decorated function.

            Raises:
                TypeError: If the return value is not of the expected type.
            """
            result = func(*args, **kwargs)

            if not isinstance(result, datatype):
                raise TypeError

            return result

        return wrapper

    return decorator
