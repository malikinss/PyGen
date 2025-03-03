'''
TODO:
    Implement a returns_string decorator that checks that the return value of
    the decorated function is of type str. If the return value is of any other
    type, the decorator should raise a TypeError exception.

    The decorator should also preserve the name and docstring of the
    decorated function.

NOTE:
    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps


def returns_string(func: callable) -> callable:
    """
    Decorator that ensures the return value of the decorated function
    is a string.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function that checks its return type.

    Raises:
        TypeError: If the return value is not of type str.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Ensure the return value is a string
        if not isinstance(result, str):
            raise TypeError(
                f"Expected return type 'str', got {type(result).__name__}."
            )

        return result

    return wrapper
