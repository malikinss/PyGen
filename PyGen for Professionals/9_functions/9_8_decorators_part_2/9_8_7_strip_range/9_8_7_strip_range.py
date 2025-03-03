'''
TODO:
    Implement a strip_range decorator that takes three arguments in
    the following order:
        start - a non-negative integer
        end - a non-negative integer
        char - a single character, which defaults to a period .

    The decorator must modify the return value of the decorated function by
    replacing all characters in the index range from start (inclusive) to end
    (exclusive) with the char character.

    The decorator must also preserve the name and docstring of the decorated
    function.
NOTE:
    The return value of the decorated function is guaranteed to be an object
    of type str.

    It is guaranteed that start < end.

    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


def strip_range(start: int, end: int, char: str = '.') -> Callable:
    """
    Decorator to replace characters in a specified range with
    a given character.

    Args:
        start (int): The start index (inclusive).
        end (int): The end index (exclusive).
        char (str): The character to replace the range with. Defaults to '.'.

    Returns:
        Callable: The decorated function with modified return value.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            original_str = func(*args, **kwargs)
            replacement_str = len(original_str[start:end]) * char

            return original_str[:start] + replacement_str + original_str[end:]

        return wrapper

    return decorator
