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


def sandwich(original_func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that adds bread slices before and after the function call.

    Args:
        original_func (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Any]: The wrapped function that adds "bread slices"
        before and after the original function call.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Print top slice of bread
        print('---- Top slice of bread ----')

        # Call the original function with arguments
        result = original_func(*args, **kwargs)

        # Print bottom slice of bread
        print('---- Bottom slice of bread ----')

        # Return the result of the original function
        return result

    return wrapper
