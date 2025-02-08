'''
TODO:
    Write a function call() that takes an arbitrary function and arguments for
    it and makes a call to the passed function, returning its value.
'''
from typing import Callable, Any


def call(func: Callable[..., Any], *args: Any) -> Any:
    """
    Calls the passed function with the provided arguments and returns
    the result.

    Parameters:
    - func (Callable[..., Any]): The function to be called.
    - *args (Any): The arguments to be passed to the function.

    Returns:
    - Any: The result of calling the function with the provided arguments.
    """
    return func(*args)
