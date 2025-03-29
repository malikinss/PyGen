'''
TODO:
    Implement the @jsonify decorator, which transforms the return value of the
    decorated function into a JSON string.

    The decorator should also preserve the name and docstring of the decorated
    function.

NOTE:
    The return value of the function is guaranteed to be of a type supported
    by the JSON format.
'''
import json
from functools import wraps
from typing import Any, Callable


def jsonify(func: Callable) -> Callable:
    """
    Decorator that transforms the return value of the decorated function into
    a JSON string.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: A wrapper function that returns the JSON string
        representation of the function's return value.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        return json.dumps(func(*args, **kwargs))

    return wrapper
