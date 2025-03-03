'''
TODO:
    Implement a takes_positive decorator that checks that all arguments passed
    to the decorated function are positive integers.

    If at least one argument does not satisfy this condition, the decorator
    should throw an exception:
        - TypeError if the argument is not an integer
        - ValueError if the argument is an integer but negative or
        equal to zero

NOTE:
    The priority of throwing exceptions when an argument does not satisfy both
    conditions, or when there are different arguments that do not satisfy
    different conditions:
        TypeError, then ValueError.

    Remember that the decorator must not consume the return value of the
    decorated function, and must be able to decorate functions with an
    arbitrary number of positional and named arguments.
'''
from typing import Callable, Any


def takes_positive(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that ensures all arguments passed to the decorated function
    are positive integers.

    Args:
        func (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Any]: The decorated function with argument validation.

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If any argument is an integer but is not positive.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Combine all positional and keyword arguments into one list
        all_arguments = [*args, *kwargs.values()]

        for arg in all_arguments:
            # Check if the argument is not an integer
            if not isinstance(arg, int):
                raise TypeError(f"Argument {arg} is not an integer")
            # Check if the integer argument is positive
            if arg <= 0:
                raise ValueError(f"Argument {arg} is not a positive integer")

        return func(*args, **kwargs)

    return wrapper
