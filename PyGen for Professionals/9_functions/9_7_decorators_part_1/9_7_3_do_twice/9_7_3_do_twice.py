'''
TODO:
    Implement a do_twice decorator that calls the decorated function twice.

NOTE:
    Remember that the decorator must not consume the return value of the
    decorated function, and must be able to decorate functions with an
    arbitrary number of positional and named arguments.
'''
from typing import Callable, Any


def do_twice(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that calls the decorated function twice.

    Args:
        func (Callable[..., Any]): The function to be called twice.

    Returns:
        Callable[..., Any]: The wrapper function that calls `func` twice.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function that calls the original function twice.

        Args:
            *args (Any): Positional arguments for the original function.
            **kwargs (Any): Named arguments for the original function.

        Returns:
            Any: The return value of the original function from the second
            call.
        """
        # Call the function twice
        func(*args, **kwargs)  # First call, result is not used
        return func(*args, **kwargs)  # Second call, result is returned

    return wrapper
