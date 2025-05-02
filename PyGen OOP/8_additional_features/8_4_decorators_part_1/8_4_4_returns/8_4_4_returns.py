'''
TODO:
    Implement a @returns decorator class that takes one argument:
        datatype — the data type

    The decorator must check that the return value of the decorated function
    is of type datatype.

    If the return value is of any other type, a TypeError exception must be
    raised.

NOTE:
    Remember that the decorator must not consume the return value of
    the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Any, Callable, Type


class returns:
    """
    Decorator to check return type.
    """
    def __init__(self, datatype: Type[Any]) -> None:
        """
        Init decorator.

        Args:
            datatype: Expected return type.
        """
        self.datatype = datatype

    def __call__(self, func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Wrap function to check return type.

        Args:
            func: Function to decorate.

        Returns:
            Callable: Wrapped function.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            if not isinstance(result, self.datatype):
                raise TypeError
            return result
        return wrapper
