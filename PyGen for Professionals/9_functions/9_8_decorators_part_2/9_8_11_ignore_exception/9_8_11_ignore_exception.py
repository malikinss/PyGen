'''
TODO:
    Implement an ignore_exception decorator that takes an arbitrary number of
    positional arguments — exception types — and outputs the text:
        Exception <exception type> is handled -  if an exception of one of the
        passed types was raised during the execution of the decorated function.

    If the raised exception does not belong to any of the passed types, it
    should be raised again.

    The decorator should also preserve the name and docstring of the decorated
    function.
NOTE:
    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any, Type


def ignore_exception(*exceptions: Type[BaseException]) -> Callable:
    """
    Decorator to handle specified exceptions during function execution.

    Args:
        *exceptions (Type[BaseException]): Exception types to be handled.

    Returns:
        Callable: Wrapped function with exception handling.
    """
    def decorator(func: Callable) -> Callable:
        """
        Inner decorator function.

        Args:
            func (Callable): Function to be decorated.

        Returns:
            Callable: Wrapped function with exception handling.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                print(f'Exception {type(e).__name__} is handled')
            except Exception as e:  # Reraise any other unexpected exceptions
                raise e

        return wrapper

    return decorator
