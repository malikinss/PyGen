"""
TODO:
    Write a program that overrides the built-in print() function so that
    it prints all passed string arguments in uppercase.

NOTE:
    The sep and end values must also be converted to uppercase.
"""
original_print = print


def print(*args: tuple, **kwargs: dict) -> None:
    """
    Custom print function that prints all string arguments in uppercase.

    Args:
        *args (Any): Positional arguments to be printed.
        **kwargs (Any): Keyword arguments, including 'sep' and 'end'.

    Returns:
        None
    """
    # Convert all string arguments to uppercase
    args = tuple(arg.upper() if isinstance(arg, str) else arg for arg in args)

    # Update keyword arguments to make 'sep' and 'end' uppercase
    kwargs = {key: (value.upper() if isinstance(value, str) else value)
              for key, value in kwargs.items()}

    # Ensure default 'sep' and 'end' values if not provided
    kwargs.setdefault('sep', ' ')
    kwargs.setdefault('end', '\n')

    # Call the original print function
    original_print(*args, **kwargs)
