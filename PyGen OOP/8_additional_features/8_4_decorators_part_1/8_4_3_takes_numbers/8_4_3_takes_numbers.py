'''
TODO:
    Implement a @takes_numbers decorator class that checks that all arguments
    passed to the decorated function are of type int or float.

    If at least one argument is of any other type, a TypeError exception
    should be raised with the text:
        Arguments must be of type int or float

NOTE:
    Remember that the decorator must not consume the return value of
    the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import update_wrapper
from typing import Any, Callable


class takes_numbers:
    """
    Decorator to check numeric arguments.
    """
    def __init__(self, func: Callable[..., Any]) -> None:
        """
        Init decorator.

        Args:
            func: Function to decorate.
        """
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        Call function with type-checked args.

        Args:
            *args: Positional arguments.
            **kwds: Keyword arguments.

        Returns:
            Any: Function result.

        Raises:
            TypeError: If any argument is not int or float.
        """
        ERR_MSG = "Arguments must be of type int or float"
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(ERR_MSG)
        for value in kwds.values():
            if not isinstance(value, (int, float)):
                raise TypeError(ERR_MSG)
        return self.func(*args, **kwds)
