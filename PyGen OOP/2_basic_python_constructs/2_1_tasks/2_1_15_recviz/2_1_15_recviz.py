from functools import wraps
from typing import Any


def recviz(func: Any) -> Any:
    """
    A decorator that visualizes the execution of a function, including
    recursive calls.

    It prints the function call and its arguments in a human-readable format,
    followed by the result.

    Args:
        func (Any): The function to be decorated.

    Returns:
        Any: The result of the function call after execution.

    This decorator is able to handle an arbitrary number of positional and
    keyword arguments.

    It prints:
        - The function name and its arguments when a call is made (
            `-> function_name(arg1, arg2, ...)`
        )
        - The result when the function returns (
            `<- result`
        )
    """
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        """
        The wrapper function that logs function calls and their results.

        Args:
            *args (tuple): Positional arguments passed to the decorated
            function.
            **kwargs (dict): Keyword arguments passed to the decorated
            function.

        Returns:
            Any: The result returned by the decorated function.
        """
        cur_indent_size = wrapper.indent * 4
        cur_indent = ' ' * cur_indent_size

        args_str = ', '.join(repr(arg) for arg in args)
        kwargs_str = ', '.join(
            f"{key}={repr(value)}"
            for key, value in kwargs.items()
        )

        if args_str and kwargs_str:
            call_details = f'{func.__name__}({args_str}, {kwargs_str})'
        elif args_str:
            call_details = f'{func.__name__}({args_str})'
        elif kwargs_str:
            call_details = f'{func.__name__}({kwargs_str})'
        else:
            call_details = f'{func.__name__}()'

        print(f'{cur_indent}-> {call_details}')
        wrapper.indent += 1

        result = func(*args, **kwargs)

        print(f"{cur_indent}<- {repr(result)}")
        wrapper.indent -= 1

        return result

    wrapper.indent = 0
    return wrapper
