'''
TODO:
    Write a program using a decorator that overrides the print() function so
    that it prints all text in uppercase.

    The program takes nothing as input.

    The program must decorate the print() function so that it prints all text
    in uppercase.

NOTE:
    The sep and end values must also be converted to uppercase.

    Remember that the decorator must not consume the return value of the
    decorated function, and must be able to decorate functions with an
    arbitrary number of positional and named arguments.
'''
from typing import Callable, Any


def upper_print(func: Callable[..., None]) -> Callable[..., None]:
    """
    Decorator that converts all text output to uppercase.

    Args:
        func (Callable[..., None]): The function to decorate.

    Returns:
        Callable[..., None]: The decorated function.
    """

    def wrapper(*args: Any, **kwargs: dict[str, Any]) -> None:
        def is_string(obj: Any) -> bool:
            """
            Check if the object is a string.

            Args:
                obj (Any): The object to check.

            Returns:
                bool: True if the object is a string, False otherwise.
            """
            return isinstance(obj, str)

        def convert_to_uppercase(value: Any) -> Any:
            """
            Convert the value to uppercase if it is a string.

            Args:
                value (Any): The value to convert.

            Returns:
                Any: The converted value if it was a string, otherwise the
                original value.
            """
            return value.upper() if is_string(value) else value

        # Convert arguments and specified keyword arguments to uppercase
        uppercased_args = tuple(convert_to_uppercase(arg) for arg in args)
        uppercased_kwargs = {
            key: convert_to_uppercase(value)
            for key, value in kwargs.items()
            if key in {'sep', 'end'}
        }

        # Call the original print function with the converted arguments
        return func(*uppercased_args, **uppercased_kwargs)

    return wrapper


# Decorate the built-in print function to convert all text to uppercase
print = upper_print(print)
