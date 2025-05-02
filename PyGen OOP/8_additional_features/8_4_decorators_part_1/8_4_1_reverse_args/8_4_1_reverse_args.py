'''
TODO:
    You have access to the @reverse_args decorator, which passes all
    positional arguments to the decorated function in reverse order.

    Implement the @reverse_args decorator as a decorator class.

NOTE:
    Remember that the decorator must not consume the return value of
    the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import update_wrapper
from typing import Any, Callable


class reverse_args:
    """
    Decorator to reverse positional arguments.
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
        Call decorated function with reversed args.

        Args:
            *args: Positional arguments.
            **kwds: Keyword arguments.

        Returns:
            Any: Function result.
        """
        return self.func(*args[::-1], **kwds)
