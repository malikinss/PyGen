'''
TODO:
    Implement a square decorator that raises the return value of the decorated
    function to the power of two.

    The decorator must also preserve the name and docstring of
    the decorated function.

NOTE:
    The return value of the decorated function is guaranteed to be an object
    of type int or float.

    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps


def square(func: callable) -> callable:
    """
    Decorator that squares the return value of the decorated function.

    Args:
        func (callable): The function to decorate.

    Returns:
        callable: A new function that returns the square of the
        original function's return value.
    """
    @wraps(func)
    def squared_result_wrapper(*args, **kwargs) -> int | float:
        result = func(*args, **kwargs)
        return result ** 2
    return squared_result_wrapper
