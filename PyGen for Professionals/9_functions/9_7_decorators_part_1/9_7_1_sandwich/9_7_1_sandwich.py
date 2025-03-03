'''
TODO:
    Implement a sandwich decorator that prints the texts:
        ---- Top slice of bread ----
        ---- Bottom slice of bread ----
    before and after calling the decorated function, respectively.

NOTE:
    Remember that the decorator should not consume the return value of the
    decorated function, and should also be able to decorate functions with an
    arbitrary number of positional and named arguments.
'''
from typing import Callable, Any


def sandwich(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that adds bread slices before and after the function call.

    Args:
        func (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Any]: The wrapped function.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print('---- Top slice of bread ----')
        result = func(*args, **kwargs)
        print('---- Bottom slice of bread ----')
        return result

    return wrapper
