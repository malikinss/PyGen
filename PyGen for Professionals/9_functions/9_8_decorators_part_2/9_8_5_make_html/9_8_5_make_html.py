'''
TODO:
    A tag is a markup language element used to format text.

    For example, text enclosed between the start tag <small> and
    the end tag </small> is displayed at a smaller size than the main text,
    and text between the tags <big> and </big> is displayed at a larger size.

    Implement the make_html() decorator, which takes one argument:
    tag — an HTML tag, such as del

    The decorator must wrap the return value of the decorated function in
    an HTML tag.

    The decorator must also preserve the name and docstring of
    the decorated function.
NOTE:
    The return value of the decorated function is guaranteed to be an object
    of type str.

    Remember that the decorator must not consume the return value
    of the decorated function, and must be able to decorate functions with
    an arbitrary number of positional and named arguments.
'''
from functools import wraps
from typing import Callable, Any


def make_html(tag: str) -> Callable:
    """
    Decorator to wrap the result of a function in an HTML tag.

    Args:
        tag (str): The HTML tag to wrap the result with.

    Returns:
        Callable: The wrapped function.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            result = func(*args, **kwargs)
            return f'<{tag}>{result}</{tag}>'

        return wrapper

    return decorator
