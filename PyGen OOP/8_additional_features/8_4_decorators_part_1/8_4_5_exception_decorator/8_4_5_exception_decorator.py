'''
TODO:
    Implement a decorator class @exception_decorator that returns
        - a tuple (value, None) - if the decorated function completed its work
                                  without raising an exception, where value is
                                  the return value of the decorated function
        - a tuple (None, errortype) - if an exception was raised during
                                      the execution of the decorated function,
                                      where errortype is the type of
                                      the exception raised

NOTE:
    Remember that the decorator must not consume the return value of
    the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import update_wrapper
from typing import Any, Callable, Type, Tuple, Union


class exception_decorator:
    """
    Decorator to handle function exceptions.
    """
    def __init__(self, func: Callable[..., Any]) -> None:
        """
        Init decorator.

        Args:
            func: Function to decorate.
        """
        update_wrapper(self, func)
        self.func = func

    def __call__(
        self, *args: Any, **kwargs: Any
    ) -> Tuple[Any, Union[Type[Exception], None]]:
        """
        Call function and handle exceptions.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Returns:
            Tuple: (value, None) if no exception,
                   (None, errortype) if exception.
        """
        try:
            return self.func(*args, **kwargs), None
        except Exception as e:
            return None, type(e)
