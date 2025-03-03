'''
TODO:
    Implement the add_attrs decorator, which takes an arbitrary number of
    named arguments and sets them as attributes of the decorated function.

    The attribute name should be the argument name, and the attribute value
    should be the argument value.

    The decorator should also preserve the name and docstring of the decorated
    function.
NOTE:
    Remember the __dict__ function attribute.

    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


def add_attrs(**attributes) -> Callable:
    """
    Decorator to add attributes to a function.

    Args:
        **attributes (Any): Named arguments to be set as attributes.

    Returns:
        Callable[..., Any]: The decorated function with added attributes.
    """
    def decorator(func: Callable) -> Callable:
        """
        Decorator to set attributes to the function.

        Args:
            func (Callable[..., Any]): The function to be decorated.

        Returns:
            Callable[..., Any]: The decorated function with added attributes.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        # Set attributes to the function's __dict__
        for key, value in attributes.items():
            wrapper.__dict__[key] = value

        return wrapper

    return decorator
