'''
TODO:
    Implement an exception_decorator that returns:
        a tuple (value, 'The function completed without errors') if
        the decorated function completed without errors, where value
        is the return value of the decorated function

        a tuple (None, 'An error occurred while calling the function')
        if an error occurred while executing the decorated function

NOTE:
    Remember that the decorator must not consume the return value of the
    decorated function, and must be able to decorate functions with an
    arbitrary number of positional and named arguments.
'''
from typing import Callable, Any, Tuple


def exception_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator that wraps a function to handle exceptions.

    Args:
        func (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Tuple[Any, str]]: The wrapped function that returns
        a tuple containing the function's return value (or None in case of
        an error) and a status message.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Tuple[Any, str]:
        try:
            # Execute the function and return the result with a success message
            return func(*args, **kwargs), 'Функция выполнилась без ошибок'
        except Exception:
            return None, 'При вызове функции произошла ошибка'
    return wrapper
