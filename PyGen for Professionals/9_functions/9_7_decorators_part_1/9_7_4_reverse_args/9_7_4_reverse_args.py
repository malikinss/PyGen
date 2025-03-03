'''
TODO:
    Implement a reverse_args decorator that passes all positional arguments to
    the decorated function func in reverse order.

NOTE:
    Remember that the decorator must not consume the return value of the
    decorated function, and must be able to decorate functions with an
    arbitrary number of positional and named arguments.
'''
from typing import Callable, Any


def reverse_args(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that reverses the positional arguments of the decorated function.

    Args:
        func (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Any]: The wrapped function with reversed
        positional arguments.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function that reverses the positional arguments.

        Args:
            *args (Any): Positional arguments.
            **kwargs (Any): Keyword arguments.

        Returns:
            Any: The result of the decorated function call.
        """
        return func(*args[::-1], **kwargs)

    return wrapper
